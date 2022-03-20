import os 
import shutil
import time 

def main ():
    deletedFolderCount=0
    deletedFileCount=0
    path='C:/Users/Friends/Desktop/path_to_delete'
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        print('yes')
    
    else:
        print('no')

main()