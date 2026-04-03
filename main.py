
from pathlib import Path
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import hashlib
import os 



downloads = Path.home()/"Downloads"
executables = downloads/ "executables"
photos = downloads/ "photos"
videos = downloads/ "videos"
installers_zips = downloads/ "installers_and_zips"
docs = downloads/ "docs"
misc = downloads/ "misc"
txt = downloads/ "txt"





folder_list = [executables, photos, videos, installers_zips, docs, misc, txt]

#remember to write the similar longer hexes first
magic_dict = {


    #images and gif
    "89504E470D0A1A0A" : ".png",
    "FFD8FF"           : ".jpeg",
    "474946383761"     : ".gif",
    #------------------------------
    
    "4D5A" : ".exe",

    #------------------------------
    #audio
    "494433" : ".mp3",
    "FFFB" :".mp3",
    "FFF3": ".mp3",
    "FFF2": ".mp3",
    #------------------------------
    #docs
    "255044462D" : ".pdf",

}

#check if folder exists else create
def check_d_folders():
    for folder in folder_list:
        folder.mkdir(exist_ok=True)

#get hex
def get_file_hex(file_path, i):
    with open(file_path, "rb" ) as f:
            #read first i bytes and translate to hex
            file_bytes = f.read(i) 
            file_magic =file_bytes.hex().upper()
    return file_magic





## check file hash for avoiding corruption
def hash_file(file):
    # open hash blender (md5 bc im cheap)
    h = hashlib.md5()
    #open the file, step through its bytes to add to the hash blender
    with open(file, "rb") as f:
        #lambda here steps the func, else it would return only the first chunk
        # 8192 is just a good size here
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)

    #return the blessing from blender hash god
    return h.hexdigest()

  



#handle renaming and hash checking before copying files
def check_rename_move(file, path, i:int =0):
    #separate name from path for checking duplicates
    name = file.name
    destination = path/name
    if destination.exists():
        #nice recursion
        i += 1
        name = f"{file.stem}({i}){file.suffix}"
        check_rename_move(file, path, i)
    else:
        shutil.copy2(file, destination)
        #if hashes match delete original, and vice versa
        if hash_file(file) == hash_file(destination):
            os.remove(file)
            print(f"Moved: {file} to {destination}")
        else:
            print(f"Failed to move {file} to {destination}")
            os.remove(destination)

    

def sort_d_files():

    file_list = list(downloads.iterdir())
    for file in file_list:
        if not file.is_file():
            continue
        
        try:

            file_magic = get_file_hex(file, 4)

            #loop and get file type from dict
            file_type = None
            for key in magic_dict :
                if file_magic.startswith(key):
                    file_type = magic_dict[key]
                    break
            #handle cases dict didnt catch
            else:
                file_magic = get_file_hex(file, 12)
                if "66747970" in file_magic:
                    file_type = ".mp4"
                #read suffix in case no hex number matches
                else:
                    file_type = file.suffix

            match file_type:
                case ".exe":
                    check_rename_move(file, executables)
                case ".mp4"| ".webm":
                    check_rename_move(file, videos)
                case ".pdf" | ".csv" |".docx":
                    check_rename_move(file, docs)
                case ".msi" | ".msix" | ".zip" | ".7zp":
                    check_rename_move(file, installers_zips)
                case ".jpeg"| ".png"|".jpg"|".gif":
                    check_rename_move(file, photos)
                case ".txt":
                    check_rename_move(file, txt)   
                case _:
                    check_rename_move(file, misc)


        except PermissionError:
            print(f"Permission error for {file}")
            continue
        except Exception as e :
            print(f"failed to read or move {file} : {e} ")
            continue
        

#wait for file to finish downloading
def wait_for_file(file, interval =1):
    #define previous size negative so it doesnt exit early
    previous_size =-1
    while True:
        current_size= os.path.getsize(file)
        if current_size == previous_size:
            break
        previous_size = current_size
        time.sleep(interval)



#define class for handling dir monitoring
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        wait_for_file(event.src_path)
        sort_d_files()
        return super().on_created(event)


def main():
    check_d_folders()
    # instance these first 
    obsrv = Observer()
    handler = MyHandler()

    obsrv.schedule(handler, downloads, recursive = False)
    obsrv.start()

    #sleep main thread untill exit program
    try: 
        while True:
            time.sleep(1)
    
    except KeyboardInterrupt:
        obsrv.stop()
    obsrv.join()


    

if __name__ == "__main__":
    main()
    


        