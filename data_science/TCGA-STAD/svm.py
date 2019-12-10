# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:44:44 2019

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, precision_score,recall_score
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split,cross_val_score,cross_validate 
from sklearn.model_selection import ShuffleSplit, GroupShuffleSplit 
from sklearn.model_selection import KFold, GroupKFold
from random import shuffle

# In[0]
data = pd.read_csv('expr_all_zscore.csv', lineterminator='\n',index_col=0)

#data1 = pd.read_csv('expr_all_cpm_log.csv', lineterminator='\n')
#data1.index=data.index
#data2 = pd.read_csv('expr_all_cpm.csv', lineterminator='\n',index_col=0)

#plt.boxplot(data.values[:,:-1])
#plt.show()

# In[1]
def lower_sample_data(data, size=28):

    #percent:多数类别下采样的数量相对于少数类别样本数量的比例
    
    df1 = data[data['class\r'] == "yes\r"]  # 将多数类别的样本放在data1
    df0 = data[data['class\r'] == "no\r"]  # 将少数类别的样本放在data0
    #np.random.seed(0)
    index = np.random.randint(len(df1), size=size) 
    # 随机给定下采样取出样本的序号
    lower_data = df1.iloc[list(index)]  # 下采样
    return(pd.concat([lower_data, df0]))

# In[2]
under = lower_sample_data(data,28)
under.loc[under['class\r'] == "yes\r",'class\r']  = 1
under.loc[under['class\r'] == "no\r",'class\r'] = 0
    
#under1 = lower_sample_data(data1,28)
#under2 = lower_sample_data(data2,28)

#plt.boxplot(under.values[:,:-1])
#plt.show()

# In[3]

k_range = range(1,6)
cv_scores = []		#用来放每个模型的结果值
#cv_scores1 = []	

for n in k_range:
    
    under = lower_sample_data(data,28)
    under.loc[under['class\r'] == "yes\r",'class\r']  = 1
    under.loc[under['class\r'] == "no\r",'class\r'] = 0
   
    x = under.iloc[:,:-1]
    y = under.iloc[:,-1]
    train_x,test_x, train_y, test_y = train_test_split(x,y,test_size = 0.2)

    # 训练模型
    print('Training cross_val_score ...')
    clf = SVC(kernel='linear', C=1,gamma=1) 

    scores = cross_val_score(clf,train_x,train_y,cv=5,scoring='accuracy')  #cv：选择每次测试折数  accuracy：评价指标是准确度,可以省略使用默认值，具体使用参考下面。
    #scores = cross_val_score(rf,x,y,cv=5,scoring='accuracy')
    cv_scores.append(scores.mean())
    print(scores.mean())
    
    '''
    # cross-validation 训练
    print('Training cross-validation ...')
    cv_results = cross_validate(rf,train_x,train_y, cv=5,return_train_score=False)
    # 输出cross_validation结果 
    print(cv_results['test_score'].mean())
    cv_scores1.append(cv_results['test_score'].mean())
    '''
    
print(cv_scores)
#print(cv_scores1)
print('Average Accuracy:', np.mean(cv_scores))
#print('Average Accuracy1:', np.mean(cv_scores1))   

plt.plot(k_range,cv_scores)
plt.ylim([0.0,1.05])
plt.xlabel('K')
plt.ylabel('Accuracy')		
plt.show()

# In[4]
# 随机划分子集
ss = ShuffleSplit(n_splits=5, test_size=0.2,random_state=0)
for train_index, test_index  in ss.split(under):
    print("k折划分：%s %s" % (train_index.shape, test_index.shape))
    break
train = under.iloc[list(train_index)]
test = under.iloc[list(test_index)]

# In[5]
# k折划分子集
under_sample = under.sample(frac=1)
x1 = under_sample.iloc[:,:-1]
y1 = under_sample.iloc[:,-1]
kf = KFold(n_splits=5)
for train_index, test_index in kf.split(under):
    print("k折划分：%s %s" % (train_index.shape, test_index.shape))
    break
train1 = under_sample.iloc[list(train_index)]
test1 = under_sample.iloc[list(test_index)]

# In[6]
# k折分组
groups1 = list(map(int,list('1'*10 + '2'*10 + '3'*10 +'4'*10 +'5'*10)))
gkf = GroupKFold(n_splits=5)  # 训练集和测试集属于不同的组
for train_index, test_index in gkf.split(x1, y1, groups=groups1):
    print("组 k-fold分割：%s %s" % (train_index, test_index))

# In[7]
# 随机分组
x = under.iloc[:,:-1]
y = under.iloc[:,-1]
groups = list(map(int,list('1'*10 + '2'*10 + '3'*10 +'4'*10 +'5'*10)))
shuffle(groups)
gss = GroupShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
predicted = pd.DataFrame()
probablity = pd.DataFrame()
actual = pd.DataFrame()
score = list()
precision = list()
recall = list()

for train_index, test_index in gss.split(x,y, groups=groups):
    print("随机分割：%s %s" % (train_index, test_index))
    train_x = x.iloc[list(train_index)]
    train_y = y.iloc[list(train_index)]
    test_x = x.iloc[list(test_index)]
    test_y = y.iloc[list(test_index)]
    # 训练模型
    print('Training...')
    clf = SVC(kernel='linear', C=1,gamma=1,probability=True) 
    clf= clf.fit(train_x.values, train_y.values)
    # 进行预测
    print('predicting...')
    clf_pre = clf.predict(test_x.values)
    clf_proba = clf.predict_proba(test_x.values)
    
    # 混淆矩阵
    table = confusion_matrix(test_y.values,clf_pre)
    print(table)
    
    # 预测评分
    clf_score = clf.score(test_x.values,test_y.values)
    score.append(clf_score)
    print('score: %s' % score)
    
    #召回率和正确率 
    clf_recall = recall_score(test_y.values,clf_pre)
    recall.append(clf_recall)
    print('recall: %s' % recall)
    
    clf_precision = precision_score(test_y.values,clf_pre)
    precision.append(clf_precision)
    print('precision: %s' % precision)
    
    # 预测结果 
    clf_pre = pd.DataFrame(clf_pre)
    clf_proba = pd.DataFrame(clf_proba)
    predicted = pd.concat([predicted, clf_pre],axis=0,sort=False)
    probablity = pd.concat([probablity, clf_proba],axis=0,sort=False)
    actual = pd.concat([actual, test_y],axis=0,sort=False)

actual.index = predicted.index
results = pd.concat([predicted, actual],axis=1,sort=False)
results.columns = list(['predicted','actual'])

cmatrix = confusion_matrix(predicted.values, actual.values) 

print("\n",cmatrix)
print('Score: %s' % np.mean(score))
print('Recall: %s' %  np.mean(recall))
print('Precision: %s' %  np.mean(precision))

fpr, tpr, _ = roc_curve(actual.values, probablity[1].values)
roc_auc = auc(fpr,tpr)
print('auc:',roc_auc)

plt.plot(fpr,tpr, label='ROC curve (area = %0.4f)' % roc_auc)
plt.plot([0,1],[0,1],'k--')
plt.xlim([-0.05,1.0])
plt.ylim([0.0,1.05])
plt.xlabel('1 - Specificity')
plt.ylabel('Sensitivity')
plt.legend(loc='lower right')
plt.show()