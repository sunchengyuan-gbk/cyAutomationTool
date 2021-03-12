# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10 19:07
@Auth ： scy
@File ：test.py
"""

def sort(li):
    for i in range(len(li)-1,0,-1):
        for j in range(i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]

if __name__ == '__main__':
    # for i in range(5,0,-1):
    #     print(i)
    # print(a)
    arr = [1, 5, 4, 2, 3]
    sort(arr)
    print(arr)




