from gallery_io import load_system
import matplotlib.pyplot as plt


system_id = 107
system = load_system(system_id)
for key in system.keys():
    print(key)
    print(system[key])
    print('')