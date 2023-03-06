import os
import sys
import filecmp
import schedule
import time
import logging
import shutil


# writing in the file
mylogs=logging.getLogger(__name__)
mylogs.setLevel(logging.DEBUG)

file=logging.FileHandler('storage_file')
file.setLevel(logging.INFO)

fileformat=logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s',
datefmt='%d-%m-%Y %H:%M:%S')
file.setFormatter(fileformat)

mylogs.addHandler(file)

# writing in the console
mylogs=logging.getLogger(__name__)
mylogs.setLevel(logging.DEBUG)

stream=logging.StreamHandler()
stream.setLevel(logging.INFO)
streamformat=logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s',
datefmt='%d-%m-%Y %H:%M:%S')
stream.setFormatter(streamformat)

mylogs.addHandler(stream)


def check(path1, path2, path3):
    # paths according to command line arguments
    path1="C:\\Users\\Helen\\Desktop\\Veeam\\source_folder\\"
    path2="C:\\Users\\Helen\\Desktop\\Veeam\\target_folder\\"
    path3="C:\\Users\\Helen\\Desktop\\Veeam\\"
    source=os.listdir(path1)
    target=os.listdir(path2)

    mylogs.info(f'Source folder before synchronisation: {", ".join([str(x) for x in [*source]])}.')
    mylogs.info(f'Target folder before synchronisation: {", ".join([str(x) for x in [*target]])}.')

    # # the overview which files will be removed from target's folder because there are not in source folder
    deleted_files=[]
    for f in target:
        if f not in source:
            deleted_files.append(f)
    if len(deleted_files)>0:
        for f in deleted_files:
            os.remove(os.path.join(path2,f))
        mylogs.info(f'{", ".join([str(x) for x in [*deleted_files]])} will be deleted from target folder.')
    
    # files which are only in source folder
    created_files=[]
    # files which are in both folders and will be check if their content is same as well
    copied_files=[]
    # files which are in both folders but content is different => after check
    changed_files=[]

    for f in source:
        if f not in target:
            created_files.append(f)
        else:
            copied_files.append(f)

    for item1 in copied_files:
        for item2 in os.listdir(path2):
            if(item1==item2):
                #If shallow is set to False then the comparison is done by comparing the contents of both files.
                res=filecmp.cmp(path1+item1,path2+item2,shallow=False)
                if res==False:
                    changed_files.append(item1)
                    copied_files.remove(item1)
    # info               
    if len(created_files)>0:
        mylogs.info(f'{", ".join([str(x) for x in [*created_files]])} will be created in the target folder.')
    if len(copied_files)>0:
        mylogs.info(f'Files {", ".join([str(x) for x in [*copied_files]])} copied from {path1} to {path2}!')
    if len(changed_files)>0:
        mylogs.info(f'{", ".join([str(x) for x in [*changed_files]])} will be changed in the target folder.')
    
    # new target folder created => easiest way
    shutil.rmtree(path2)
    shutil.copytree(path1,path2,copy_function=shutil.copy)

    #result
    mylogs.info(f'Source folder after synchronisation {", ".join([str(x) for x in [*source]])}.')
    mylogs.info(f'Target folder after synchronisation {", ".join([str(x) for x in [*target]])}.' "\n")

def s(interval, path1, path2, path3):
    schedule.every(int(interval)).minutes.do(check, path1=path1, path2=path2, path3=path3)
    while True:
        schedule.run_pending()
        time.sleep(1)

if sys.argv[1] == "-c":
    check(sys.argv[2], sys.argv[3], sys.argv[5])
    s(sys.argv[4], path1=sys.argv[2], path2=sys.argv[3], path3=sys.argv[5])