# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:44:44 2019

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,cross_val_score,cross_validate 
from sklearn.model_selection import ShuffleSplit, GroupShuffleSplit 
from sklearn.model_selection import KFold, GroupKFold
from random import shuffle

# In[0]
data = pd.read_csv('expr_all_zscore.csv', lineterminator='\n',index_col=0)
data1 = pd.read_csv('expr_all_cpm_log.csv', lineterminator='\n')
data1.index=data.index
data2 = pd.read_csv('expr_all_cpm.csv', lineterminator='\n',index_col=0)


#plt.boxplot(data.values[:,:-1])
#plt.show()

# In[1]
def lower_sample_data(data, size=28):

    #percent:多数类别下采样的数量相对于少数类别样本数量的比例
    
    df1 = data[data['class\r'] == "yes\r"]  # 将多数类别的样本放在data1
    df0 = data[data['class\r'] == "no\r"]  # 将少数类别的样本放在data0
    np.random.seed(10)
    index = np.random.randint(len(df1), size=size) 
    # 随机给定下采样取出样本的序号
    lower_data = df1.iloc[list(index)]  # 下采样
    return(pd.concat([lower_data, df0]))

# In[2]
under = lower_sample_data(data,28)
under1 = lower_sample_data(data1,28)
under2 = lower_sample_data(data2,28)

#plt.boxplot(under.values[:,:-1])
#plt.show()

# In[3]
train_x,test_x, train_y, test_y = train_test_split(x,y,test_size = 0.2,random_state = 0)

# In[4]
# 随机划分子集
ss = ShuffleSplit(n_splits=5, test_size=0.2,random_state=0)
for train_index, test_index  in ss.split(under):
    print("k折划分：%s %s" % (train_index.shape, test_index.shape))
    break
train = under.iloc[list(train_index)]
test = under.iloc[list(test_index)]

# In[5]
# 随机分组
x = under.iloc[:,:-1]
y = under.iloc[:,-1]
groups = list(map(int,list('1'*10 + '2'*10 + '3'*10 +'4'*10 +'5'*10)))
shuffle(groups)
gss = GroupShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
for train_index, test_index in gss.split(x,y, groups=groups):
    print("随机分割：%s %s" % (train_index, test_index))
    
# In[6]
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
# In[7]
# k折分组
groups1 = list(map(int,list('1'*10 + '2'*10 + '3'*10 +'4'*10 +'5'*10)))
gkf = GroupKFold(n_splits=5)  # 训练集和测试集属于不同的组
for train_index, test_index in gkf.split(x1, y1, groups=groups1):
    print("组 k-fold分割：%s %s" % (train_index, test_index))

# In[8]


