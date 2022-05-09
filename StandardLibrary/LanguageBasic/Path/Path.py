import os.path
import glob
def path_fun_show():
    path = "D:/源代码/HavenLau.DotNet/HavenLau.DotNet/HavenLau.Python/StandardLibrary/LanguageBasic/test.txt"
    print("\npath====>",path)
    #查询路径中包含的文件名
    print("\n查询路径中包含的文件名====>os.path.basename(path):",os.path.basename(path))
    #查询路径中包含的目录
    print("\n查询路径中包含的目录====>os.path.dirname(path):",os.path.dirname(path))
    info = os.path.split(path)
    #将路径分割成文件名和目录两个部分，放在一个表中返回
    print("\n将路径分割成文件名和目录两个部分，放在一个表中返回====>os.path.split(path):",info)
    #使用目录名和文件名构成一个路径字符串
    print("\n使用目录名和文件名构成一个路径字符串====>os.path.join('/','StandardLibrary','LanguageBasic','test.txt'):",os.path.join('/','StandardLibrary','LanguageBasic','test.txt'))
    #查询多个路径的共同部分
    print("\n查询多个路径的共同部分====>os.path.commonprefix([path,os.path.join('/','StandardLibrary','LanguageBasic','test.txt')]):",os.path.commonprefix([path,os.path.join('/','StandardLibrary','LanguageBasic','test.txt')]))
    #去除路径path中的冗余
    print("\n去除路径path中的冗余====>os.path.normpath([path]):",os.path.normpath(path))
    #查询文件是否存在
    print(path)
    if os.path.exists(path):
        print("\n查询文件是否存在====>os.path.exists(path):",os.path.exists(path))
        #查询文件的大小
        print("\n查询文件的大小====>os.path.getsize(path):",os.path.getsize(path))
        print("\n查询文件上一次读取的时间====>os.path.getatime(path)",os.path.getatime(path))  # 查询文件上一次读取的时间
        print("\n查询文件上一次修改的时间====>os.path.getmtime(path)",os.path.getmtime(path))  # 查询文件上一次修改的时间
        print("\n路径是否指向常规文件====>os.path.isfile(path)",os.path.isfile(path))    # 路径是否指向常规文件
        print("\n路径是否指向目录文件====>os.path.isdir(path)",os.path.isdir(path))     # 路径是否指向目录文件
    else:
        print("\n查询文件是否存在====>os.path.exists(path):",os.path.exists(path))
        print("\n未找到文件。查询大小就会抛出异常")
    print(glob.glob("../StandardLibrary/LanguageBasic/*"))
    
def travelTree(currentPath,count):
    if not os.path.exists(currentPath):
        return
    if os.path.isfile(currentPath):
        fileName = os.path.basename(currentPath)
        printStr = '\t' * count + '├── ' + fileName
        print(printStr)
    elif(os.path.isdir(currentPath)):
        printStr = '\t' * count + '├── ' + currentPath
        pathList = os.listdir(currentPath)
        for eachPath in pathList:
            travelTree(currentPath+'/'+eachPath, count+1)
    

    
         
    
    

    

