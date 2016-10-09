import pylab as pl
import math
class duel_decay:
    """docstring for "duel decay"."""
    def __init__(self, number_of_nuclei_nA = 100, number_of_nuclei_nB = 0, time_costant = 1, time_of_duration = 5, time_interval = 0.05):
        self.nA = [number_of_nuclei_nA]
        self.nB = [number_of_nuclei_nB]
        self.n_A_true = [number_of_nuclei_nA]
        self.n_B_true = [number_of_nuclei_nB]
        self.N = number_of_nuclei_nA + number_of_nuclei_nB
        self.t = [0]
        self.tau = time_costant
        self.dt = time_interval
        self.time = time_of_duration
        self.steps = int(time_of_duration // time_interval + 1)
        print('Initial number of type A nuclei ->', number_of_nuclei_nA)
        print('Initial number of type B nuclei ->', number_of_nuclei_nB)
        print('Time interval ->', time_interval)
        print('Total time ->', time_of_duration)
    def calculate(self):
        for i in range(self.steps):
            tmp_A = self.nA[i] + (self.nB[i] - self.nA[i]) / self.tau * self.dt
            tmp_B = self.nB[i] + (self.nA[i] - self.nB[i]) / self.tau * self.dt
            self.nA.append(tmp_A)
            self.nB.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
            tmp_A_true = self.N / 2 - math.exp(- 2 * self.t[i + 1] / self.tau) * (self.N - 2 * self.n_A_true[0]) / 2 
            tmp_B_true = self.N - tmp_A_true
            self.n_A_true.append(tmp_A_true)
            self.n_B_true.append(tmp_B_true)
    def show_results(self):
        pl.plot(self.t, self.nA, 'b', label = 'Number of Nuclei A')
        pl.plot(self.t, self.nB, 'r', label = 'Number of Nuclei B')
        pl.plot(self.t, self.n_A_true, 'r--', label='True Number of Nuclei A')
        pl.plot(self.t, self.n_B_true, 'g', label='True Number of Nuclei B')
        pl.title('Change of Nuclei Relative to the Time')
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc = 'best')
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.nA[i], self.nB[i], self.n_A_true[i], self.n_B_true[i], file = myfile)
        myfile.close()


a = duel_decay()
a.calculate()
a.show_results()
a.store_results()
