# -*- coding: utf-8 -*-

import copy

def solution(a=[9, 3, 9, 3, 9, 7, 9]):
    result = list()
    for i in range(len(a)):
        if a.count(a[i])%2 != 0:
            result.append(a[i])
    return result

if __name__=='__main__':
    pass
