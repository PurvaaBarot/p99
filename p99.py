import os
import shutil
import time

def function():
    deleted_folders_count=0
    deleted_files_count=0

    path = input("Enter path to be deleted")

    days=30

    # seconds = time.time()-(days*24*60*60)
    seconds = time.time()-(2)

    if os.path.exists(path):
        for rootfolder , folders , files in os.walk(path):

            if seconds >=  get_file_or_folder_age(rootfolder):
                remove_folder(rootfolder)
                deleted_folders_count += 1

                break

            else:
                for folder in folders:
                    folderpath = os.path.join(rootfolder,folder)
                   

                    if seconds >= get_file_or_folder_age(folderpath):
                        remove_folder(folderpath)
                        deleted_folders_count += 1

                for file in files:
                    filepath = os.path.join(rootfolder,file)
                   
                    

                    if seconds >= get_file_or_folder_age(filepath):
                        removefile(filepath)
                        deleted_files_count += 1


    else:
        print("Path not found")

    print(f"Total Folders deleted: {deleted_folders_count}")
    print(f"Total Files deleted: {deleted_files_count}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Successfully removed")

    else:
        print("Unable to remove")

def removefile(path):
    if not os.remove(path):
        print("Successfully removed") 

    else:
        print("Unable to remove")

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime

    return ctime


function()    
    
                   





