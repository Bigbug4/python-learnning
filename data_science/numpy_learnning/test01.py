#/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

my_list = [92, 94, 88, 91, 87]
test_1 = np.array(my_list)
print(test_1)

test_2 = np.genfromtxt('test_2.csv', delimiter=',')
print(test_2)
test_2 = np.array([79, 100, 86, 93, 91])

test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed= test_3 +2
print(test_3_fixed)

total_grade = test_1 + test_2 + test_3_fixed
print(total_grade)

final_grade = total_grade / 3
print(final_grade)

jeremy_test_2 = test_2[3]
print('jeremy_test_2: %d' % jeremy_test_2)
manual_adwoa_test_1 =test_1[1:3]
print(manual_adwoa_test_1)

coin_toss = np.array([1, 0, 0, 1, 0])
coin_toss_again = np.array([[1, 0, 0, 1, 0],
							[0, 0, 1, 1, 1]])

print(coin_toss_again)

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 =student_scores[2,0]
print('tanya_test_3: %d' % tanya_test_3)
cody_test_scores =student_scores[:,4]
print(cody_test_scores)

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
cold = porridge[porridge < 60]
print(cold)
hot = porridge[porridge > 80]
print(hot)
just_right = porridge[(porridge > 60) & (porridge < 80)]
print(just_right)

