# Automatically generate system description documentation

import glob, os
from gallery_io import load_system

ID_START = 7
ID_LENGTH = 10
ID_END = ID_START + ID_LENGTH

DTIME_ID_START = 5000000000

ctime_header_str = '\n## Continuous-time systems'+'\n\n'
dtime_header_str = '\n## Discrete-time systems'+'\n\n'

with open('system_descriptions.md', 'w') as text_file:
    text_file.write('# System descriptions'+'\n')

    ctime_flag = 0
    dtime_flag = 0

    for file in glob.glob("./systems/*.pkl"):
        system_id_str = file.split('_')[1][:ID_LENGTH]
        system_id = int(system_id_str)
        system = load_system(system_id)

        if system_id < DTIME_ID_START and not ctime_flag:
            text_file.write(ctime_header_str)
            ctime_flag = True
        elif system_id >= DTIME_ID_START and not dtime_flag:
            text_file.write(dtime_header_str)
            dtime_flag = True


        text_file.write('### ' + system['description'] + '\n')
        text_file.write('ID ' + system_id_str + '\n\n')
        if system['source_paper'] is not None:
            text_file.write('Source paper title: *' + system['source_paper'] + '*\n\n')
        if system['source_authors'] is not None:
            text_file.write('Source paper authors: ' + ', '.join(system['source_authors']) + '\n\n')
        if system['notes'] is not None:
            text_file.write('Notes: ' + system['notes'] + '\n\n')
