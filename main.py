import os
import shutil
import time
from sys import exit

path = input("Enter the path where you need to manage. A new folder will be created in the same path: ")

if not (os.path.isdir(path)):
   print("The path - " + path + " - does not exist. Exiting...")
   time.sleep(2)
   exit(1)
   
folder_name = input("Enter the name of the folder you want to create: ")
file_type = input("Enter the file type you want to manage from " + path + "in " + folder_name + "(PDF,DOCX,DOC,TXT,XLSX,XLS,PNG,JPEG,PNG,PY,SQL formats are accepted): ")
newpath = path + "/" + folder_name
found_file_type = False

try:
   # Create a new path if it does not exist
   if not os.path.exists(newpath):
      os.makedirs(newpath)
   
   os.chdir('C:\\')
            
   # Set the source and destination folders
   dir_src = path+"/"
   dir_dist = newpath
   
   #PDF Files
   if file_type in ('PDF', 'pdf', 'Pdf', '.PDF', '.pdf'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".pdf"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
   
   # DOCX Files
   if file_type in ('DOCX', 'docx', 'Docx', '.DOCX', '.docx'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".docx"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
   
   # DOC Files
   if file_type in ('DOC', 'doc', 'Doc', '.DOC', '.doc'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".doc"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
   
   # TXT Files
   if file_type in ('TXT', 'txt', 'Txt', '.TXT', '.txt'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".txt"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
   
   # XLSX Files
   if file_type in ('XLSX', 'xlsx', 'Xlsx', '.XLSX', '.xlsx'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".xlsx"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
   
   # XLS Files
   if file_type in ('XLS', 'xls', 'Xls', '.XLS', '.xls'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".xls"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
   
   # PNG Files
   if  file_type in ('PNG', 'png', 'Png', '.PNG', '.png'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".png"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
         
   # JPEG Files
   if file_type in ('JPEG', 'jpeg', 'Jpeg', '.JPEG', '.jpeg'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".jpeg"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
            
   # PY Files
   if file_type in ('PY', 'py', 'Py', '.PY', '.py'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".py"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
   
   # SQL Files
   if file_type in ('SQL', 'sql', 'Sql', '.SQL', '.sql'):
      for filename in os.listdir(dir_src):
         if filename.endswith(".sql"):
            shutil.move(dir_src+filename, dir_dist)
            found_file_type = True
   
   print(folder_name, "created successfully!")

except OSError:
   print("The path given, ", path, " does not exist. Exiting...")

if not found_file_type:
   print("The file type given, ", file_type, " is not supported. Exiting...")
   time.sleep(2)
   exit(1)


