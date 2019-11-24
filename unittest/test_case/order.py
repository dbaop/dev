#!/usr/bin/python
# -*- encoding:utf8 -*-
import os

class loan():
    def __init__(self,number,cust_no):
        self.number = number
        self.cust_no = cust_no

    def loan(self):
        for i in range(0,self.number):
            for order in self.ordr_no:
                command = r"java -jar scheduler_run/lib/scheduler-1.0.jar -r {0}".format(ordr)
                os.system (command)
if __name__ == '__main__':
    number = 4
    ordr_no=['150000168543',
             '150000168544',
             '150000168545',
             '150000168546']
    loan(number,ordr_no).loan()

