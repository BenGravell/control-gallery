import pickle
import os

def filenamer(time_type, system_id):
    system_id_str = time_type + '%010d' % system_id
    filename = 'system_'+system_id_str+'.pkl'
    return filename

def pather(time_type, system_id):
    directory = 'systems_' + time_type + 'time'
    filename = filenamer(time_type, system_id)
    path = os.path.join(directory, filename)
    return path

def save_system(time_type, system_id, keys, values):
    system = {}
    for key, value in zip(keys, values):
        system[key] = value
    path_out = pather(time_type, system_id)
    file_out = open(path_out, 'wb')
    pickle.dump(system, file_out)
    file_out.close()
    return

def load_system(time_type, system_id):
    path_in = pather(time_type, system_id)
    file_in = open(path_in, 'rb')
    system = pickle.load(file_in)
    file_in.close()
    return system