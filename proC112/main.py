import os
import shutil 
from_dir='C:/Users/HAJEERA RUBAI/Downloads/doc file'
to_dir='C:/Users/HAJEERA RUBAI/Downloads/img file'
list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,ext=os.path.splitext(file_name)
    if ext=='':
        continue
    if ext in ['.pdf']:
        path1=from_dir+"/"+file_name
        path2=to_dir+'/'+'img_files'
        path3=to_dir+'/'+'img_files'+'/'+file_name

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)    

    
    

