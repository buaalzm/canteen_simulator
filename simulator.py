from stu_generator import StuGenerator
from queue import Queue


class Simulator():
    def __init__(self, p):
        self.stu_generator = StuGenerator(p)
        self.stu_queue = Queue(100-1) # 有一个正在打饭的不计入队列，所以减一
        self.time_step = 0
        self.max_step = 60
        self.finish_stu_list = []
        self.queue_stat_list = []
        self.cache = None # 正在打饭的人

    def push(self):
        '''
        每步执行，新到的学生加入队列
        '''
        for stu in self.stu_generator.generate(create_time=self.time_step):
            if not self.stu_queue.full():
                stu.set_begin_time(self.time_step)
                self.stu_queue.put(stu)

    def pop(self):
        '''
        每步执行，判断队列是否向前移动
        '''
        if self.cache is None:
            # 初始情况，无人打饭
            self.queue_move()
        else:
            # 有人打饭的情况
            if self.time_step-self.cache.select_begin_time>=self.cache.select_time: 
                # 实际选餐时间大于设定选餐时间，打完饭
                self.cache.set_finish_time(self.time_step)
                self.finish_stu_list.append(self.cache) # 打完的走人，记录结束时间
                self.queue_move()
    
    def queue_move(self):
        '''
        队伍前移
        '''
        if not self.stu_queue.empty():
            self.cache = self.stu_queue.get()
            self.cache.set_begin_time(self.time_step)

    def step(self):
        '''
        每步迭代，执行的任务
        '''
        self.push()
        self.pop()
        self.queue_stat_list.append(self.stu_queue.qsize())
        self.time_step = self.time_step+1

    def run(self):
        '''
        主循环
        '''
        while(self.time_step<=self.max_step):
            self.step()

if __name__ == "__main__":
    simulator = Simulator(p = 4) # 更改这里，p的值是每分钟来排队学生数量的期望
    simulator.run()
    print('模拟完成')
    stu_num = len(simulator.finish_stu_list)
    time_cost_list = [item.finish_time-item.create_time for item in simulator.finish_stu_list]
    stu_avg_time_cost = sum(time_cost_list)/float(stu_num)
    queue_avg_len = sum(simulator.queue_stat_list)/float(simulator.max_step)
    print('食堂平均每小时接待{}名学生'.format(stu_num))
    print('每位学生平均花{}分钟'.format(stu_avg_time_cost))
    print('排队等待的人平均有{}人'.format(queue_avg_len))
