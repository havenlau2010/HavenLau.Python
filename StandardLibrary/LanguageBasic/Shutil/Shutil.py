import shutil
import os
def shutil_fun_show():
    rootPath = os.getcwd()
    filePath = rootPath + "/FilePath"
    if os.path.exists(filePath):
        print("exists")
    else:
        os.mkdir(filePath)    
    if not os.path.exists(filePath + "/TargetPath"):
        os.mkdir(filePath + "/TargetPath")
    if not os.path.exists(filePath + "/SourcePath"):
        os.mkdir(filePath + "/SourcePath")
    print("复制文件，从src到dst。相当于$cp命令")

    if os.path.exists(filePath + "/SourcePath/source.txt"):
        #os.remove(filePath + "/SourcePath/source.txt")
        print("exists")
    else :
        os.mkdir(filePath + "/SourcePath/source.txt")  
    if os.path.exists(filePath + "/TargetPath/source.txt"):
        #os.remove(filePath + "/TargetPath/source.txt")
        print("exists")
    else:
        shutil.copy(filePath + "/SourcePath/source.txt",filePath + "/TargetPath/Source.txt")