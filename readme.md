### 问题描述

食堂来用自选方式提供午餐，每个学生可能会花1分钟、2分钟、3分钟完点选餐。设定排队最多容纳100人。假设学生是随机出现的，选餐所花时间是随机的(1分钟，2分钟或3分钟)。那么

- 食堂平均每小时接待多少名学生？
- 每位学生平均花多少时间？
- 排队等待的人平均有多少人？

### 假设条件

- 食堂只有一个窗口
- 接待学生数量，按照打上饭计算，即弹出队列的人数
- 排队等待的人按照60分钟，每分钟记录队伍人数，60分钟每分钟人数加和，再除以60计算
- 时间以1分钟作为最小单位

### 程序设计

1. 学生类

   属性：
   
   select_time:选餐时间
   create_time:出生时间（被生成的时间节点）
   select_begin_time:打饭开始时间（用来判定被弹出队列）
   finish_time:死亡时间（打完饭被弹出队列，可为空） 
   index:编号（方便统计）

2. 学生生成器

    按照一个规则产生学生（通过一个参数调整产生的速度，产生条件为队列非空），给学生进行初始化并塞进队列

    属性：

    upper_amount:向上取整的产生
    lower_amount:向下取整的产生
    p:希望一分钟产生的人数（可以是小数）
    thre:随机数的判定阈值
    index:计数

    > 生成方法：初始化时通过p确定产生人数的上下界，用rand函数产生一个[0,1)的随机数，通过比thre大小判定产生多少人。

    方法：

    generate：产生学生，return stu_list[list]
    
3. 模拟器

    用于整个过程的模拟

    属性：
    
    time_step:用于计数，一个计数表示一分钟
    stu_queue:初始化队列长度100
    finish_stu_list:搜集打完饭的学生用于统计
    queue_stat_list:记录每分钟队列的长度（排队人数）

    方法具体见代码

​		

### 统计方法

#### 食堂平均每小时接待多少名学生？

```python
stu_num = len(simulator.finish_stu_list)
```

#### 每位学生平均花多少时间？

```python
time_cost_list = [item.finish_time-item.create_time for item in simulator.finish_stu_list]

sum(time_cost_list)/float(stu_num)
```

#### 排队等待的人平均有多少人？

```
sum(simulator.queue_stat_list)/float(simulator.max_step)
```

### 启动

运行simulator.py

**注意：由于有随机数因素，每次执行结果都会不同**