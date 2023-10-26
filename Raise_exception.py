# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 06:38:24 2023

@author: khanb
"""

def raised_exception(L1,L2):
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('fuction called with bad arg')
    return ratios

'''

    L1=[1,2,3,4]

    L2=[5,6,7,8]
    
    raised_exception(L1,L2)
    Out[12]: [0.2, 0.3333333333333333, 0.42857142857142855, 0.5]

    L3=[3,4,5]

    raised_exception(L1,L3)
    Traceback (most recent call last):

      File d:\github\python\raise_exception.py:12 in raised_exception
        ratios.append(L1[index]/float(L2[index]))

    IndexError: list index out of range
    
    L4=[3,4,5,0]

    raised_exception(L1,L4)
    Out[16]: [0.3333333333333333, 0.5, 0.6, nan]
    
'''