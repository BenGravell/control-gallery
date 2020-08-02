import pickle
import os

def filenamer(system_id):
    system_id_str = '%010d' % system_id
    filename = 'system_'+system_id_str+'.pkl'
    return filename

def pather(system_id):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    systems_directory = 'systems'
    filename = filenamer(system_id)
    path = os.path.join(location, systems_directory, filename)
    return path

def save_system(system_id, system):
    path_out = pather(system_id)
    file_out = open(path_out, 'wb')
    pickle.dump(system, file_out)
    file_out.close()
    return

def load_system(system_id):
    path_in = pather(system_id)
    file_in = open(path_in, 'rb')
    system = pickle.load(file_in)
    file_in.close()
    return system