import os
import sys
from shutil import copyfile

#get directory names
def get_directories_filenames():
    path = sys.argv[1]
    print(path)   
    dir_list = os.listdir(path)
    print(dir_list)
    return dir_list

#sort through list to categorize items based on their extensions.
def categorize_items_based_on_ext():
    dir_list = get_directories_filenames()
    exe_list = []
    pdf_list = []
    txt_list = []
    msi_list = []
    zip_list = []
    pdf_ext = "pdf"
    exe_ext = "exe"
    msi_ext = "msi"
    txt_ext = "txt"
    zip_ext = "zip"
    log_ext = "log"

    for item in dir_list:
        ext = item[-3:]
        if ext == pdf_ext:
            pdf_list.append(item)
        elif ext == exe_ext:
            exe_list.append(item)
        elif ext == msi_ext:
            msi_list.append(item)
        elif ext == txt_ext or ext == log_ext:
            txt_list.append(item)
        elif ext == zip_ext:
            zip_list.append(item)

    return pdf_list , exe_list , txt_list , msi_list , zip_list

#organize files based on their extension types.
def organize_files_based_on_ext(pdf_list , exe_list , txt_list , msi_list , zip_list):
    path = sys.argv[1]    
    #pdf_list
    move_files("pdf" , pdf_list , path)
    #exe_list
    move_files("exe" , exe_list , path)
    #txt_list
    move_files("txt" , txt_list , path)
    #msi_list
    move_files("msi" , msi_list , path) 
    #zip_list
    move_files("zip" , zip_list , path) 
   

#move files to desired directory
def move_files(extension , file_list , path):
    dest_folder_name = extension + "_" + "files"
    dest_path_dir = os.path.join(path , dest_folder_name) 
    if not os.path.exists(dest_path_dir):
        os.mkdir(dest_path_dir)
    for item in file_list:
        source_file_path = os.path.join(path , item)
        dest_file_path = os.path.join(dest_path_dir, item)
        print("dest path:" + dest_file_path)   
        print("source path:" + source_file_path) 
        if not os.path.isfile(dest_file_path):
            copyfile(source_file_path , dest_file_path)
            print("file copied" + item)
            os.remove(source_file_path)
            print("file removed from src folder: " + item)
        

#main function
if __name__ == "__main__":
    pdf_list , exe_list , txt_list , msi_list , zip_list = categorize_items_based_on_ext()
    organize_files_based_on_ext(pdf_list , exe_list , txt_list , msi_list , zip_list)

	