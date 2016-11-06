# -*- coding: utf-8 -*-

def solution(n=0):
    cnt = 0
    temp = n
    zero_list = list()
    while(temp):
        if temp % 2:
            zero_list.append(cnt)
            cnt = 0
        else:
            cnt += 1
        temp /= 2
    return max(zero_list)

if __name__=='__main__':
    pass
