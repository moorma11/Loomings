import numpy as np

item_line = '\item'

#File paths
logdir = '/home/moormanc212/notes/logs/'
phdtex = logdir+'/PhD.tex'
phddvi = logdir+'/PhD.dvi'
taskpath = 'utilities/tasklist.tsk'

bgn_itemize = '\\begin{itemize}\n'
end_itemize = '\end{itemize}\n'


def bulleted_list(lst):
    bllt_pnts = [bgn_itemize]
    pnt = '    \item '

    for item in lst:
        if (item == '\n'):
            continue
        else:
            bllt_pnts.append(pnt+item)

    bllt_pnts.append(end_itemize)

    return bllt_pnts

def list_tasks():
    with open('/home/moormanc212/utilities/tasklist.tsk') as f:
        task_list = f.readlines()

    print('Active tasks')
    print('***************************************************************')
    for i,task in enumerate(task_list):
        num = str(i+1)
        print(num+'*'+task)

def write_to_tasklist(task):
    with open(taskpath,'a') as f:
        f.write(task)

def add_tasks():
    task = ''
    while (task != 'q\n'):
        print('Task to add: (press q when done)')
        task = input()+'\n'
        if (task != 'q\n'):
            write_to_tasklist(task)
    
def add_task():
    print('Task to add:')
    task = input()+'\n'
    write_to_tasklist(task)

def filter_out_tasklist():
    with open(phdtex, 'r') as f:
        read_data = f.readlines()
    end_document = read_data[-1]
    document = read_data[:-1]

    with open(phdtex, 'w') as f:
        for line in document:
            if (line==bgn_itemize):
                continue
            elif (line==end_itemize):
                continue
            elif (len(line) >= len(item_line)):
                strp_line = line.strip()
                if (strp_line[:5] == item_line):
                    continue
            f.write(line)
        f.write(end_document)


def read_in_tasks():
    with open(taskpath) as f:
        tasklist = f.readlines()
    return tasklist

def remove_task(task_no):
    task_list = read_in_tasks()
    print('taskno -1', task_no - 1)
    task = task_list[task_no-1]
    print('removing task '+task)
    task_list.remove(task)
    with open(taskpath,'w') as f:
        for task in task_list:
            f.write(task)
    refresh_tasklist()

def refresh_tasklist():
    filter_out_tasklist()
    add_tasklist_to_tex()
    

def add_tasklist_to_tex():
    with open(phdtex, 'r') as f:
        doc = f.readlines()

    enddoc = doc[-1]
    document = doc[:-1]

    tasklist = read_in_tasks()
    formatted_tasklist = bulleted_list(tasklist)

    for bllt in formatted_tasklist:
        document.append(bllt)

    with open(phdtex, 'w') as f:
        for l in range(len(document)):
            line = document[l]
            f.write(document[l])
        f.write(enddoc)



