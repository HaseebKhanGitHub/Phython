# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:18:36 2024

@author: khanb
"""

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.month)
print(x.time())
print(x.day)
print(x.strftime("%A"))
