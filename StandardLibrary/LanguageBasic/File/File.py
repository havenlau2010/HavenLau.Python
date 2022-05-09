import os
def file_fun_show():
    path = "StandardLibrary/LanguageBasic/EmptyPath"
    print(path)
    if os.path.exists(path):
        print("StandardLibrary/LanguageBasic 目录已经存在")
    else:
        print("创建新目录，path为一个字符串，表示新目录的路径。相当于$mkdir命令====>os.mkdir(path)：")
        os.mkdir(path)
    
    print("删除空的目录，path为一个字符串，表示想要删除的目录的路径。相当于$rmdir命令====>os.rmdir(path)")
    os.rmdir(path)
    newpath = "StandardLibrary/LanguageBasic/EmptyPath"
    os.mkdir(newpath)
        
    print("返回目录中所有子文件。相当于$ls命令。====>os.listdir(path):",os.listdir(newpath))
    #print("删除path指向的文件。====>os.remove(path):",os.remove(newpath))
    filePath = "StandardLibrary/LanguageBasic/new.txt"
    if os.path.exists(filePath) :
        filePath = "StandardLibrary/LanguageBasic/"
        #os.rename(filePath + "new.txt",filePath + "newName.txt")
        print("重命名文件。====>os.rename('oldName.file','newName.file'):",os.listdir(filePath))
        print("删除path指向的文件。====>os.remove(path):")
        #os.rename(filePath + "newName.txt",filePath + "new.txt")
        #os.remove("StandardLibrary/LanguageBasic/new.txt");
    else :
        os.mkdir("StandardLibrary/LanguageBasic/new.txt");

    print("查询当前工作路径。====>os.getcwd():",os.getcwd());

