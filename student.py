class Student():

    def __init__(self, select_time, create_time,index):
        self.select_time = select_time #选餐时间
        self.create_time = create_time #出生时间（被生成的时间节点）
        self.index = index #打饭开始时间（用来判定被弹出队列）
        self.select_begin_time = None #打饭开始时间（用来判定被弹出队列）
        self.finish_time = None #死亡时间（打完饭被弹出队列，可为空） 

    def set_begin_time(self,begin_time):
        self.select_begin_time = begin_time

    def set_finish_time(self,finish_time):
        self.finish_time = finish_time
