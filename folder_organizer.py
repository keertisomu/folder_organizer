import os
import sys
from shutil import copyfile
import extensions_loader
import logging

#config
logging.basicConfig(filename='folder_organizer.log',level=logging.DEBUG,
format='%(asctime)s:%(levelname)s:%(message)s')

#get directory names
def get_directories_filenames():
    path = sys.argv[1]
    logging.info(path)   
    dir_list = os.listdir(path)
    logging.info(dir_list)
    return dir_list

#sort through list to categorize items based on their extensions.
def categorize_items_based_on_ext(data):
    extensions = data["extensions"]
    path = sys.argv[1]
    dir_list = get_directories_filenames()
    for ext in extensions:
        logging.info("Working on: " + ext + "items...")
        move_files(ext , dir_list , path) 

#move files from src to dest path.
def move_files(extension , dir_list , path):
    #populate list with files of a same extension for example ., pdf
    file_list = []
    for item in dir_list:
        split_list = item.split('.')
        last_item = split_list[len(split_list) - 1]
        #ext = item[-3:]
        if last_item.lower() == extension:
            file_list.append(item)

    #move the file from src path to dest path.        
    dest_folder_name = extension + "_" + "files"
    dest_path_dir = os.path.join(path , dest_folder_name) 
    if not os.path.exists(dest_path_dir):
        os.mkdir(dest_path_dir)
    for item in file_list:
        source_file_path = os.path.join(path , item)
        dest_file_path = os.path.join(dest_path_dir, item)
        logging.info("dest path:" + dest_file_path)   
        logging.info("source path:" + source_file_path) 
        if not os.path.isfile(dest_file_path):
            copyfile(source_file_path , dest_file_path)
            logging.info("file copied" + item)
            os.remove(source_file_path)
            logging.info("file removed from src folder: " + item)
        

        

#main function
if __name__ == "__main__":
    data = extensions_loader.load_ext()   
    categorize_items_based_on_ext(data)

	