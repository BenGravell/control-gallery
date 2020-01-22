from gallery_io import load_system
import matplotlib.pyplot as plt

time_type = 'c'
system_id = 9002
system = load_system(time_type, system_id)
for key in system.keys():
    print(key)
    print(system[key])