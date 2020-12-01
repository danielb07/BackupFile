import os 
import shutil
import time
import stat

path = 'C:\Users\barraud\Desktop\WhiteHatJR\BackupFiles\test'
day = 20
seconds = 20*24*60*60
if os.path.exists(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_stat = os.stat(file_path)
            ctime = time.ctime(file_stat[stat.ST_CTIME])
            if os.path.isdir(file_path) == False:
                os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_stat = os.stat(dir_path)
            ctime = dir_stat[stat.ST_CTIME]
            if os.path.isdir(dir_path):
                shutil.rmtree(dir_path)
