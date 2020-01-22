import numpy as np
from gallery_io import save_system

# Discrete-time linear time invariant system parameters
time_type = 'd'

# F-16 aircraft short period dynamics from the paper
# "Model-free Q-learning designs for linear discrete-time zero-sum games with application to H-infinity control"
# by Al-Tamimi, Lewis, and Abu-Khalaf
# Based on the continuous-time system in Chapter 3 of the textbook
# "Aircraft Control and Simulation" by Stevens, Lewis, and Johnson
system_id = 1
A = np.array([[0.906488, 0.0816012, -0.0005],
              [0.0741349, 0.90121, -0.000708383],
              [0, 0, 0.132655]])
B = np.array([-0.00150808, -0.0096, 0.867345])
E = np.array([0.00951892, 0.00038373, 0])
T = 0.1
gamma = 1

keys = ['time_type', 'system_id', 'A', 'B', 'E', 'T', 'gamma']
values = [time_type, system_id, A, B, E, T, gamma]
save_system(time_type, system_id, keys, values)


# The 9000 series of problems are taken from the IFAC report
# "Benchmark Problems for Control System Design" by Davison et al.

# Cold rolling mill
# "This problem deals with a two-stand cold rolling mill.
# The process dynamics are dominated by the interstand time delay.
# A discrete 10th order model is given.
# The model includes disturbances, is multivariable and strongly interacting."
system_id = 9004

A = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0.112],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
B = np.array([[2.76, -1.35, -0.46],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])
C = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
D = np.array([[0, 0, 0],
              [-0.223, 1.85, -0.542],
              [28.3, 204, 68.7],
              [-5.21, -0.843, -0.285],
              [-0.101, -6.75, -0.246]])
E = np.array([[0.713, 0.556, -0.183],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])
F = np.array([[0, 0, 0],
              [0.0025, -0.025, 0.222],
              [-0.322, 3.22, 27.6],
              [0.444, 0.347, -0.015],
              [0.002, -0.012, -0.86]])

keys = ['time_type', 'system_id', 'A', 'B', 'C', 'D', 'E', 'F']
values = [time_type, system_id, A, B, C, D, E, F]
save_system(time_type, system_id, keys, values)