import math

class stadium_billiard:
    def __init__(self, vx_initial, vy_initial, x_initial, y_initial, time_interval, total_time, alpha):
        self.vx = [vx_initial]
        self.vy = [vy_initial]
        self.x = [x_initial]
        self.y = [y_initial]
        self.t = [0]
        self.dt = time_interval
        self.alpha = alpha
        self.steps = int(total_time // time_interval) + 1
    def calculate(self):
        for i in range(self.steps):
            new_y = self.y[i] + self.vy[i] * self.dt
            new_x = self.x[i] + self.vx[i] * self.dt
            if new_y <= self.alpha and new_y >= -self.alpha:
                if new_x > 1 :
                    new_x = self.x[i] + self.vx[i] * self.dt / 100
                    new_y = self.y[i] + self.vy[i] * self.dt / 100
                    time_interval_revised = self.dt / 100
                    while new_x < 1:
                        new_x = new_x + self.vx[i] * self.dt / 100
                        new_y = new_y + self.vy[i] * self.dt / 100
                        time_interval_revised = time_interval_revised + self.dt / 100
                    v_vertical_in_x = self.vx[i]
                    v_vertical_in_y = 0
                    v_parallel_in_x = 0
                    v_parallel_in_y = self.vy[i]
                    v_vertical_out_x = -self.vx[i]
                    v_vertical_out_y = 0
                    v_parallel_out_x = 0
                    v_parallel_out_y = self.vy[i]
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(v_vertical_out_x + v_parallel_out_x)
                    self.vy.append(v_vertical_out_y + v_parallel_out_y)
                    self.t.append(self.t[i] + time_interval_revised)
                elif new_x < -1:
                    new_x = self.x[i] + self.vx[i] * self.dt / 100
                    new_y = self.y[i] + self.vy[i] * self.dt / 100
                    time_interval_revised = self.dt / 100
                    while new_x > -1:
                        new_x = new_x + self.vx[i] * self.dt / 100
                        new_y = new_y + self.vy[i] * self.dt / 100
                        time_interval_revised = time_interval_revised + self.dt / 100
                    v_vertical_in_x = self.vx[i]
                    v_vertical_in_y = 0
                    v_parallel_in_x = 0
                    v_parallel_in_y = self.vy[i]
                    v_vertical_out_x = -self.vx[i]
                    v_vertical_out_y = 0
                    v_parallel_out_x = 0
                    v_parallel_out_y = self.vy[i]
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(v_vertical_out_x + v_parallel_out_x)
                    self.vy.append(v_vertical_out_y + v_parallel_out_y)
                    self.t.append(self.t[i] + time_interval_revised)
                else:
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(self.vx[i])
                    self.vy.append(self.vy[i])
                    self.t.append(self.t[i] + self.dt)
            elif new_y > self.alpha:
                if (new_x ** 2 + (new_y - self.alpha) ** 2) > 1:
                    new_x = self.x[i] + self.vx[i] * self.dt / 100
                    new_y = self.y[i] + self.vy[i] * self.dt / 100
                    time_interval_revised = self.dt / 100
                    while (new_x) ** 2 + (new_y - self.alpha) ** 2 < 1:
                        new_x = new_x + self.vx[i] * self.dt / 100
                        new_y = new_y + self.vy[i] * self.dt / 100
                        time_interval_revised = time_interval_revised + self.dt / 100
                    r = math.sqrt((new_x) ** 2 + (new_y - self.alpha) ** 2)
                    dot_product = self.vx[i] * (-new_x / r) + self.vy[i] * (self.alpha - new_y) / r
                    v_vertical_in_x = dot_product * (-new_x) / r
                    v_vertical_in_y = dot_product * (self.alpha - new_y) / r
                    v_parallel_in_x = self.vx[i] - v_vertical_in_x
                    v_parallel_in_y = self.vy[i] - v_vertical_in_y
                    v_vertical_out_x = -v_vertical_in_x
                    v_vertical_out_y = -v_vertical_in_y
                    v_parallel_out_x = v_parallel_in_x
                    v_parallel_out_y = v_parallel_in_y
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(v_vertical_out_x + v_parallel_out_x)
                    self.vy.append(v_vertical_out_y + v_parallel_out_y)
                    self.t.append(self.t[i] + time_interval_revised)
                else:
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(self.vx[i])
                    self.vy.append(self.vy[i])
                    self.t.append(self.t[i] + self.dt)
            elif new_y < -self.alpha:
                if (new_x ** 2 + (new_y - self.alpha) ** 2) > 1:
                    new_x = self.x[i] + self.vx[i] * self.dt / 100
                    new_y = self.y[i] + self.vy[i] * self.dt / 100
                    time_interval_revised = self.dt / 100
                    while new_x ** 2 + (new_y - self.alpha) ** 2 < 1:
                        new_x = new_x + self.vx[i] * self.dt / 100
                        new_y = new_y + self.vy[i] * self.dt / 100
                        time_interval_revised = time_interval_revised + self.dt / 100
                    r = math.sqrt((new_x) ** 2 + (new_y - self.alpha) ** 2)
                    dot_product = self.vx[i] * (-new_x / r) + self.vy[i] * (-self.alpha - new_y) / r
                    v_vertical_in_x = dot_product * (-new_x) / r
                    v_vertical_in_y = dot_product * (-self.alpha - new_y) / r
                    v_parallel_in_x = self.vx[i] - v_vertical_in_x
                    v_parallel_in_y = self.vy[i] - v_vertical_in_y
                    v_vertical_out_x = -v_vertical_in_x
                    v_vertical_out_y = -v_vertical_in_y
                    v_parallel_out_x = v_parallel_in_x
                    v_parallel_out_y = v_parallel_in_y
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(v_vertical_out_x + v_parallel_out_x)
                    self.vy.append(v_vertical_out_y + v_parallel_out_y)
                    self.t.append(self.t[i] + time_interval_revised)
                else:
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(self.vx[i])
                    self.vy.append(self.vy[i])
                    self.t.append(self.t[i] + self.dt)


t1 = stadium_billiard(vx_initial = 0.1, vy_initial = 0.2, x_initial = 0.01, y_initial = 0.02, time_interval = 0.01, total_time = 1500, alpha = 0.05)
t2 = stadium_billiard(vx_initial = 0.1, vy_initial = 0.2, x_initial = 0.01006, y_initial = 0.02, time_interval = 0.01, total_time = 1500, alpha = 0.05)
t1.calculate()
t2.calculate()

d = []
for i in range(len(t1.x)):
    d.append(math.sqrt((t1.x[i]-t2.x[i]) ** 2) + (t1.y[i] - t2.y[i]) ** 2)

d_log = []
for i in range(len(t1.x)):
    d_log.append(math.log(d[i]))
