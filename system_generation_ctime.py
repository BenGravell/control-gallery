import numpy as np
from gallery_io import save_system

# Continuous-time linear time invariant system parameters
time_type = 'c'

# Two-mass-spring system in the paper
# "Benchmark Problems for Robust Control Design" by Bong Wie and Dennis S. Bernstein
system_id = 1
m1 = 1
m2 = 1
k = 1
A = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [-k/m1, k/m1, 0, 0],
              [k/m2, -k/m2, 0, 0]])
B = np.array([0, 0, 1/m1, 0])
C = np.array([0, 1, 0, 0])
D = np.array([0])

keys = ['time_type', 'system_id', 'A', 'B', 'C', 'D']
values = [time_type, system_id, A, B, C, D]
save_system(time_type, system_id, keys, values)

# Inverted pendulum
system_id = 2



# The 9000 series of problems are taken from the IFAC report
# "Benchmark Problems for Control System Design" by Davison et al.

# Binary distillation column
# "This problem describes a fairly realistic model of a binary distillation column,
# and has the feature that pressure variation is included in the model's description;
# the system is multivariable, with 3 inputs and 3 outputs, and includes one disturbance input"
# The system A matrix has almost a banded diagonal structure with 11 states, 3 of which are directly measured as output
system_id = 9001
A = np.array([[-1.40e-02, +4.30e-03, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00],
              [+9.50e-03, -1.38e-02, +4.60e-03, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +5.00e-04],
              [+0.00e+00, +9.50e-03, -1.41e-02, +6.30e-03, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +2.00e-04],
              [+0.00e+00, +0.00e+00, +9.50e-03, -1.58e-02, +1.10e-02, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00],
              [+0.00e+00, +0.00e+00, +0.00e+00, +9.50e-03, -3.12e-02, +1.50e-02, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00],
              [+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +2.02e-02, -3.52e-02, +2.20e-02, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00],
              [+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +2.02e-02, -4.22e-02, +2.80e-02, +0.00e+00, +0.00e+00, +0.00e+00],
              [+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +2.02e-02, -4.82e-02, +3.70e-02, +0.00e+00, +2.00e-04],
              [+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +2.02e-02, -5.72e-02, +4.20e-02, +5.00e-04],
              [+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +2.02e-02, -4.83e-02, +5.00e-04],
              [+2.55e-02, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +2.55e-02, -1.85e-02]])
B = np.array([[+0.00e+00, +0.00e+00, +0.00e+00],
              [+5.00e-06, -4.00e-05, +2.50e-03],
              [+2.00e-06, -2.00e-05, +5.00e-03],
              [+1.00e-06, -1.00e-05, +5.00e-03],
              [+0.00e+00, +0.00e+00, +5.00e-03],
              [+0.00e+00, +0.00e+00, +5.00e-03],
              [-5.00e-06, +1.00e-05, +5.00e-03],
              [-1.00e-05, +3.00e-05, +5.00e-03],
              [-4.00e-05, +5.00e-06, +2.50e-03],
              [-2.00e-05, +2.00e-06, +2.50e-03],
              [+4.60e-04, +4.60e-04, +0.00e+00]])
C = np.array([[+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +1.00e+00, +0.00e+00],
              [+1.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00],
              [+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +1.00e+00]])
D = np.zeros([3, 3])
E = np.array([+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +1.00e-02, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00])

keys = ['time_type', 'system_id', 'A', 'B', 'C', 'D', 'E']
values = [time_type, system_id, A, B, C, D, E]
save_system(time_type, system_id, keys, values)


# Drum boiler
# "This problem describes a fairly realistic model of a drum boiler
# and has the feature of being multivariable, unstable, and non-minimum phase"
# NOTE: Problem has a variation where the third input is not used
system_id = 9002
A = np.array([[-3.93e+00, -3.15e-03, +0.00e+00, +0.00e+00, +0.00e+00, +4.03e-05, +0.00e+00, +0.00e+00, +0.00e+00],
              [+3.68e+02, -3.05e+00, +3.03e+00, +0.00e+00, +0.00e+00, -3.77e-03, +0.00e+00, +0.00e+00, +0.00e+00],
              [+2.74e+01, +7.87e-02, -5.96e-02, +0.00e+00, +0.00e+00, -2.81e-04, +0.00e+00, +0.00e+00, +0.00e+00],
              [-6.47e-02, -5.20e-05, +0.00e+00, -2.55e-01, +3.35e-06, +3.60e-07, +6.33e-05, +1.94e-04, +0.00e+00],
              [+3.85e+03, +1.73e+01, -1.28e+01, -1.26e+04, -2.91e+00, -1.05e-01, +1.27e+01, +4.31e+01, +0.00e+00],
              [+2.24e+04, +1.80e+01, +0.00e+00, -3.56e+01, -1.04e-04, -4.14e-01, +9.00e+01, +5.69e+01, +0.00e+00],
              [+0.00e+00, +0.00e+00, +2.34e-03, +0.00e+00, +0.00e+00, +2.22e-04, -2.03e-01, +0.00e+00, +0.00e+00],
              [+0.00e+00, +0.00e+00, +0.00e+00, -1.27e+00, +1.00e-03, +7.86e-05, +0.00e+00, -7.17e-02, +0.00e+00],
              [-2.20e+00, -1.77e-03, +0.00e+00, -8.44e+00, -1.11e-04, +1.38e-05, +1.49e-03, +6.02e-03, -1.00e-10]])
B = np.array([[+0.00e+00, +0.00e+00, +0.00e+00],
              [+0.00e+00, +0.00e+00, +0.00e+00],
              [+1.56e+00, +0.00e+00, +0.00e+00],
              [+0.00e+00, -5.13e-06, +0.00e+00],
              [+8.28e+00, -1.50e+00, +3.95e-02],
              [+0.00e+00, +1.78e+00, +0.00e+00],
              [+2.33e+00, +0.00e+00, +0.00e+00],
              [+0.00e+00, -2.45e-02, +2.84e-03],
              [+0.00e+00, +2.94e-05, +0.00e+00]])
C = np.array([[+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +1.00e+00, +0.00e+00, +0.00e+00, +0.00e+00],
              [+0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00, +1.00e+00]])
D = np.zeros([2, 3])
E = np.array([-1.00e-02, +0.00e+00, +0.00e+00, +0.00e+00, +5.20e+01, +0.00e+00, +0.00e+00, +0.00e+00, +0.00e+00])

keys = ['time_type', 'system_id', 'A', 'B', 'C', 'D', 'E']
values = [time_type, system_id, A, B, C, D, E]
save_system(time_type, system_id, keys, values)