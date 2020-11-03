from student import Student
from math import floor,ceil
from random import random


class StuGenerator():
    def __init__(self, p):
        '''
        p:希望一分钟产生的人数（可以是小数）
        '''
        self.upper_amount = ceil(p)
        self.lower_amount = floor(p)
        self.thre = p-floor(p)
        self.index = 1

    def generate(self,create_time):
        amount = self.lower_amount if random()>self.thre else self.upper_amount
        return_list = []
        for _ in range(amount):
            return_list.append(Student(self.gen_select_time(),create_time,self.index))
            self.index=self.index+1
        return return_list

    def gen_select_time(self):
        '''
        随机产生打饭时间
        '''
        r = random()
        if r<0.33:
            return 1
        elif r<0.66:
            return 2
        else:
            return 3
