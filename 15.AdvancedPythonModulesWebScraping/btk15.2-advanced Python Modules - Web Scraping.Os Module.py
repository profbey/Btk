import os
import datetime

####### IT IS USED TO MAKING AUTOMATIZE TO TERMINAL AFFAIRS #######

#* res = dir(os)
res = os.name   # nt == windows


#* change directory
os.chdir('C:\\')
os.chdir('..')              # bir ust klasore gecer
os.chdir('../..')           # iki kere ust klasore gecer


#* create file & folder
os.mkdir('newFolder')                   # creating new folder
os.makedirs('newFolder/newSubfolder')   # creating folders and subfolders


#* rename file & folder
os.rename('newFolder','yeniKlasor')


#* del file & folder
os.rmdir('yeniKlasor')
os.removedirs('newFolder/newSubfolder')


#* learning active directory 
os.getcwd                   # the location of the file


#* listing
res = os.listdir()          # ['.git', '.vscode', 'Btk']


#* filtering
for file in os.listdir('C:\\'):
    if file.endswith('.py'):
        print(file)


#* gettin' info about a file
res = os.stat('Btk')
res = res.st_size / 1024    # kbayt == 4.0
res = datetime.datetime.fromtimestamp(res.st_ctime)        # 2024-11-19 01:54:47.660669 => creation date
res = datetime.datetime.fromtimestamp(res.st_atime)        # 2024-12-16 14:12:24.160250 => last access date
res = datetime.datetime.fromtimestamp(res.st_mtime)        # 2024-12-16 13:00:29.682598 => last modification date


#* Run the extension
os.system('notepad.exe')


#* path 
res = os.path.abspath('btk15.2-advanced Python Modules - Web Scraping.Os Module.py')    # giving exact path of file 
res = os.path.dirname('D:/Programx64/vs-code-calısmalar/pyhton a1/btk15.2-advanced Python Modules - Web Scraping.Os Module.py') # D:/Programx64/vs-code-calısmalar/pyhton a1
res = os.path.dirname(os.path.abspath('btk15.2-advanced Python Modules - Web Scraping.Os Module.py'))   # finding the file and giving exact path of file 
res = os.path.exists('_os.py')                                                          # False => is there this file?
res = os.path.isdir('D:/Programx64/vs-code-calısmalar/pyhton a1/')                      # True  => is it folder?
res = os.path.isfile('D:/Programx64/vs-code-calısmalar/pyhton a1/btk15.2-advanced Python Modules - Web Scraping.Os Module.py')  # True  => is it file?
res = os.path.join('C:\\','trial','trial2')     # You have created a file and want to move it.
res = os.path.split('C:\\deneme')               # ('C:\\', 'deneme')
res = os.path.splitext('_os.py')                # ('_os', '.py') 

print(res)
