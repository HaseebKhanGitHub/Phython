# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:04:57 2023

@author: khanb
"""

# Subject interface
class RealSubject:
    def request(self):
        print("RealSubject: Handling request")

# Proxy class
class Proxy:
    def __init__(self):
        self.real_subject = None

    def request(self):
        # Creating the real subject only when needed
        if not self.real_subject:
            self.real_subject = RealSubject()
        self.real_subject.request()

# Client code
proxy = Proxy()
proxy.request()
