import os
import shutil
import colorama

# colors
CYAN = colorama.Fore.CYAN
REST = colorama.Fore.RESET
RED = colorama.Fore.RED
SUCCESS = colorama.Fore.GREEN

while True:
    print(REST)
    
    # inputs
    try:
        source_folder = input(f"enter the address of source folder : {CYAN}")
        if not os.path.exists(source_folder):
            print(f"{RED}source folder is not exists ... !")
            continue
    
        destination_folder = input(f"{REST}enter the address of destination folder : {CYAN}")
        if not os.path.exists(destination_folder):
            print(f"{RED}destination folder is not exists ... !")
            continue
        
        format_files = input(f"{REST}enter the format of file that you want (without dot): {CYAN}").lower()
        delete_text = input(f"{REST}enter the delete text that you want to delete in file names : {CYAN}")
    except KeyboardInterrupt:
        break

    print(REST)
    
    # get files of source folder
    source_files = os.listdir(source_folder)

    for index in range(len(source_files)):
        source_files[index] = os.path.join(source_folder, source_files[index])

    # filter files ( gets files that are in {format_files} format)
    filtered_files = []
    for file in source_files:
        format = file.split('\\')[-1].split('.')[-1]
        if format == format_files:
            filtered_files.append(file)

    # rename the files and copy to destination folder
    for file in filtered_files:
        
        filename = str(file).split('\\')[-1]
        
        if delete_text in filename:
            # delete the text from the filename
            replaced_filename = filename.replace(delete_text, '')
            destination_file = os.path.join(destination_folder, replaced_filename)
            
            print(f"{CYAN}{destination_file}{REST} ... ", end='')

            # copy the file
            shutil.copy(file, destination_file)
            
            print(f"{SUCCESS}DONE !{REST}")
