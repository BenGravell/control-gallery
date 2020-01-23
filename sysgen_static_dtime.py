import numpy as np
from gallery_io import save_system
import pickle

# Discrete-time linear time invariant system parameters
time_type = 'd'
dyn_rep = 'ss'


description = "F-16 aircraft short period dynamics"
source_paper = "Model-free Q-learning designs for linear discrete-time zero-sum games with application to H-infinity control"
source_authors = ['Al-Tamimi', 'Lewis', 'Abu-Khalaf']
notes = "Based on the continuous-time system in Chapter 3 of the textbook\n" + \
        "'Aircraft Control and Simulation' by Stevens, Lewis, and Johnson"
metadata_keys = ['description', 'source_paper', 'source_authors', 'notes']
metadata_values = [description, source_paper, source_authors, notes]
system_id = 5000000001
A = np.array([[0.906488, 0.0816012, -0.0005],
              [0.0741349, 0.90121, -0.000708383],
              [0, 0, 0.132655]])
B = np.array([-0.00150808, -0.0096, 0.867345])
C = None
D = None
E = np.array([0.00951892, 0.00038373, 0])
T = 0.1
gamma = 1
keys = ['time_type', 'dyn_rep', 'A', 'B', 'C', 'D', 'E', 'T', 'gamma'] + metadata_keys
values = [time_type, dyn_rep, A, B, C, D, E, T, gamma] + metadata_values
system = dict(zip(keys, values))
save_system(system_id, system)


description = "Marginally unstable graph Laplacian system with diffusion dynamics"
source_paper = "On the Sample Complexity of the Linear Quadratic Regulator"
source_authors = ['Dean', 'Mania', 'Matni', 'Recht', 'Tu']
notes = None
metadata_keys = ['description', 'source_paper', 'source_authors', 'notes']
metadata_values = [description, source_paper, source_authors, notes]
system_id = 5000000002
A = np.array([[1.01, 0.01, 0.00],
              [0.01, 1.01, 0.01],
              [0.00, 0.01, 1.01]])
B = np.eye(3)
C = None
D = None
Q = 0.001*np.eye(3)
R = np.eye(3)
keys = ['time_type', 'dyn_rep', 'A', 'B', 'C', 'D', 'Q', 'R'] + metadata_keys
values = [time_type, dyn_rep, A, B, C, D, Q, R] + metadata_values
system = dict(zip(keys, values))
save_system(system_id, system)


description = "Simple diagonal system"
source_paper = "The driver and the engineer: Reinforcement learning and robust control"
source_authors = ['Bernat', 'Chen', 'Matni', 'Doyle']
notes = "alpha parameter selected according to point given in the paper described as the 'uncontrollable regime'"
metadata_keys = ['description', 'source_paper', 'source_authors', 'notes']
metadata_values = [description, source_paper, source_authors, notes]
system_id = 5000000200
alpha = 0.02
A = np.array([[1+alpha, 0],
              [0, 1]])
B = np.array([1, 1])
C = None
D = None
keys = ['time_type', 'dyn_rep', 'A', 'B', 'C', 'D', 'alpha'] + metadata_keys
values = [time_type, dyn_rep, A, B, C, D, alpha] + metadata_values
system = dict(zip(keys, values))
save_system(system_id, system)

description = "Simple diagonal system"
source_paper = "The driver and the engineer: Reinforcement learning and robust control"
source_authors = ['Bernat', 'Chen', 'Matni', 'Doyle']
notes = "alpha parameter selected according to point given in the paper described as the 'benign regime'"
metadata_keys = ['description', 'source_paper', 'source_authors', 'notes']
metadata_values = [description, source_paper, source_authors, notes]
system_id = 5000000201
alpha = 0.6
A = np.array([[1+alpha, 0],
              [0, 1]])
B = np.array([1, 1])
C = None
D = None
keys = ['time_type', 'dyn_rep', 'A', 'B', 'C', 'D', 'alpha'] + metadata_keys
values = [time_type, dyn_rep, A, B, C, D, alpha] + metadata_values
system = dict(zip(keys, values))
save_system(system_id, system)

description = "Simple diagonal system"
source_paper = "The driver and the engineer: Reinforcement learning and robust control"
source_authors = ['Bernat', 'Chen', 'Matni', 'Doyle']
notes = "alpha parameter selected according to point given in the paper described as the 'unstable regime'"
metadata_keys = ['description', 'source_paper', 'source_authors', 'notes']
metadata_values = [description, source_paper, source_authors, notes]
system_id = 5000000202
alpha = 8
A = np.array([[1+alpha, 0],
              [0, 1]])
B = np.array([1, 1])
C = None
D = None
keys = ['time_type', 'dyn_rep', 'A', 'B', 'C', 'D', 'alpha'] + metadata_keys
values = [time_type, dyn_rep, A, B, C, D, alpha] + metadata_values
system = dict(zip(keys, values))
save_system(system_id, system)


description = "Cold rolling mill"
source_paper = "Benchmark Problems for Control System Design"
source_authors = ['Davison']
notes = "This problem deals with a two-stand cold rolling mill.\n" + \
        "The process dynamics are dominated by the interstand time delay.\n" + \
        "A discrete 10th order model is given.\n" + \
        "The model includes disturbances, is multivariable and strongly interacting."
metadata_keys = ['description', 'source_paper', 'source_authors', 'notes']
metadata_values = [description, source_paper, source_authors, notes]
system_id = 5000009004
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

keys = ['time_type', 'dyn_rep', 'A', 'B', 'C', 'D', 'E', 'F'] + metadata_keys
values = [time_type, dyn_rep, A, B, C, D, E, F] + metadata_values
system = dict(zip(keys, values))
save_system(system_id, system)