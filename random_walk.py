from random import choice
class Randomwalk():
    #创建一个随机漫步的类

    def __init__(self, num_points=5000):
        #初始化属性
        self.num_points = num_points
        #开始于坐标原点
        self.x_rules = [0]
        self.y_rules = [0]
    def fill_walk(self):
        #计算随机漫步的所有点

        #不断漫步，直到到达指定的长度
        while len(self.x_rules) < self.num_points:
            #决定前进方向以及距离
            x_dirction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_dirction * x_distance

            y_dirction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_dirction * y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的位置
            next_x = self.x_rules[-1] + x_step
            next_y = self.y_rules[-1] + y_step

            self.x_rules.append(next_x)
            self.y_rules.append(next_y)


