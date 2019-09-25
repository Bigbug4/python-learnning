#!/usr/bin/env python3
# coding:utf-8

print('{学习}使我{快乐}'.format(学习='学习',快乐='痛苦'))

study = {'语言':'python','排名':'天下第一'}

print('{语言} 是 {排名}'.format(**study))

print("hello %s" % "world")

print('%o' % 100)

print('%.2f' % 100)

print('%x' % 100)

print('%.2e' % 100)

say_hi = "hello {0}"

print(say_hi.format("world"))

print('{0} @ {1}'.format('DH','nihaoa'))

print('{1} @ {0}'.format('DH','nihaoa'))

print('你好 {:^10}'.format('python'))

print('你好 {:<10}'.format('python'))

print('你好 {:>10}'.format('python'))

print('你好 {:@<10}'.format('python'))

print('你好 {:@>10}'.format('python'))


print('{:.2f}'.format(3.1415926))

print('{:.5f}'.format(3.1415926))

print('{:b}'.format(100))

print('{:o}'.format(100))

print('{:d}'.format(100))

print('{:x}'.format(100))

