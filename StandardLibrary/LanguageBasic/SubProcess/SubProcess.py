import subprocess
def showTitle():
    title = '''
            这里的内容以Linux进程基础和Linux文本流为基础。
            subprocess包主要功能是执行外部的命令和程序。
            比如说，我需要使用wget下载文件。我在Python中调用wget程序。
            从这个意义上来说，subprocess的功能与shell类似。
            -----------------------------------------------------------------
            当我们运行python的时候，我们都是在创建并运行一个进程。正如我们在Linux进程基础中介绍的那样，一个进程可以fork一个子进程，并让这个子进程exec另外一个程序。在Python中，我们通过标准库中的subprocess包来fork一个子进程，并运行一个外部的程序(fork，exec见Linux进程基础)。
            subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。

            使用subprocess包中的函数创建子进程的时候，要注意:

            1) 在创建子进程之后，父进程是否暂停，并等待子进程运行。

            2) 函数返回什么

            3) 当returncode不为0时，父进程如何处理。

            subprocess.call()
            父进程等待子进程完成
            返回退出信息(returncode，相当于exit code，见Linux进程基础)
            subprocess.check_call()

            父进程等待子进程完成
            返回0

            检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try...except...来检查(见Python错误处理)。

            subprocess.check_output()

            父进程等待子进程完成

            返回子进程向标准输出的输出结果

            检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性和output属性，output属性为标准输出的输出结果，可用try...except...来检查。
            '''
    print(title)

def subprocess_fun_show():
    showTitle()
    waitchild = subprocess.Popen('ping -c4 www.baidu.com',shell=True)
    print("parent process")
    #waitchild = subprocess.Popen(["notepad.exe", "test.txt"])
    subprocess.Popen.wait(waitchild)
    waitchild.poll()
    waitchild.send_signal("123")
    waitchild.terminate()
    waitchild.kill()
    
    print("wait parent process")
    #subprocess.Popen("cmd.exe /C notepad.exe test.txt", shell=True)
    
    #child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
    #child2 = subprocess.Popen(["wc"],
    #stdin=child1.stdout,stdout=subprocess.PIPE)
    #out = child2.communicate()
    #print(out)
    #child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
    #child.communicate("vamei")
    subprocess.call("cd ..",shell = True);