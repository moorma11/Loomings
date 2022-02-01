import numpy as np
import log_utils as utils
from datetime import date, time 
import latex_stuff
import os
import sys

logdir = latex_stuff.logdir
phdtex = latex_stuff.phdtex
phddvi = latex_stuff.phddvi
taskpath = latex_stuff.taskpath

#Call me Ishmael
option = str(sys.argv[1])

if(option=='quicklog'):
    with open(phdtex) as f:
        read_data = f.readlines()

    end_document = read_data[-1]

    today = str(date.today())

    print('Entry title')
    header = input()

    title = ':'.join([today,header])
    section_title = '\section{'+title+'}\n'

    document = read_data[:-1]

    print('Log:\n')
    log = input()

    document.append(section_title)
    document.append(log)
    document.append('\n')
    document.append(end_document)

    with open(phdtex, 'w') as f:
         for line in document:
             f.write(line)

    utils.log_utils.compile_log()
    utils.log_utils.send_to_Suttree()
    print('Log added.')

elif(option=='tasks'):
    latex_stuff.filter_out_tasklist()
    latex_stuff.add_tasks()
    latex_stuff.add_tasklist_to_tex()
    utils.log_utils.compile_log()
    utils.log_utils.send_to_Suttree()
    print('Successfully added tasks.')

elif(option=='task'):
    latex_stuff.filter_out_tasklist()
    latex_stuff.add_task()
    latex_stuff.add_tasklist_to_tex()
    utils.log_utils.compile_log()
    utils.log_utils.send_to_Suttree()
    print('Successfully added task.')

elif(option=='newlog'):
    print('Enter new log name')
    #Verify that new log is uniquely named
    logname = str(input())
    print('Enter Author name')
    author = str(input())
    lg = utils.log(logname, author)

elif(option=='compile'):
    utils.log_utils.compile_log()

elif(option=='clean'):
    utils.log_utils.clean_files()

elif(option=='read'):
    utils.log_utils.read_log()

elif(option == 'rc'):
    utils.log_utils.compile_log()
    utils.log_utils.read_log()

elif(option == 'hark'):
    latex_stuff.list_tasks()

elif (option=='log'):
    os.system('vi '+utils.log_utils.logpath)

elif (option == 'filter'):
    latex_stuff.filter_out_tasklist()

elif (option == 'completed'):
    if (len(sys.argv) > 2):
        task = int(sys.argv[2])
    latex_stuff.remove_task(task)
    utils.log_utils.compile_log()
    utils.log_utils.send_to_Suttree()

elif (option == 'update_tasks'):
    latex_stuff.refresh_tasklist()

    utils.log_utils.compile_log()
    utils.log_utils.send_to_Suttree()

################################################################################################################
if (len(sys.argv) > 2):
   read_ye = sys.argv[2]
else:
    read_ye = 'noshow'

if (read_ye == 'show'):
    utils.log_utils.read_log()

