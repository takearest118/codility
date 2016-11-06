# -*- coding: utf-8 -*-

def solution(a=[], k=0):
    return a[len(a)-k:] + a[:len(a)-k]

if __name__=='__main__':
    pass
