import os
import latex_stuff as lst

logdir = lst.logdir
phdtex = lst.phdtex
phddvi = lst.phddvi
taskpath = lst.taskpath

class log_utils:
    @staticmethod
    def clean_files():
        os.system('rm notes/logs/*.aux')
        os.system('rm notes/logs/*.dvi')
        os.system('rm notes/logs/*.log')

    @staticmethod
    def create_new_log(logpath=phdtex, author='Chad Moorman'):
        logtitle = logpath[len(logdir):-4]
        with open(logpath, 'w') as f:
            f.write('\documentclass{article}\n')
            f.write('\n')
            f.write('\\author{'+author+'}\n')
            f.write('\\title{'+logtitle+'}')
            f.write('\n')
            f.write('\\begin{document}\n')
            f.write('\maketitle\n')
            f.write('\n')
            f.write('\n')
            f.write('\end{document}\n')

        print('Created new log: '+logtitle)
        compile_log()
        send_to_Suttree()

    @staticmethod
    def send_to_Suttree():
        os.system('scp  '+phdtex+' '+phddvi+' chad@Suttree.nya.pub:/home/chad/notes/logs')

    @staticmethod
    def compile_log():
        os.system('latex '+phdtex)
        os.system('mv *.aux '+logdir)
        os.system('mv *.dvi '+logdir)
        os.system('mv *.log '+logdir)

        print('Compiled the log')

    def read_log():
        os.system('xdvi '+phddvi)

class log:
    def __init__(self, logname,author):
        self.logname = logname
        self.author = author
        self.logpath = logdir+self.logname+'.tex'
        self.logpath_dvi = logdir+self.logname+'.dvi'
        log_utils.create_new_log(self.logpath, self.author)
        log_utils.send_to_Suttree()

