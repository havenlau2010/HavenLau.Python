#加上此句话，防止IDE自动解码中文
#import PythonBasic/StandardLibrary/LanguageBase as pb
#pb.array_function_test();


#import 导入包的用法
import sys
print("===================================Python import mode===================================")
print(sys.getdefaultencoding())

print("The command line arguments are:")
for x in sys.argv:
    print(x)
print("\n The python path",sys.path)



from StandardLibrary.m import *
print(printName)
f("\n Hello,world!")

#======================================LanguageBase=======================================
#sequence=>tuple
from StandardLibrary.LanguageBasic.Sequence.Tuple import *
tuple_fun_show()

#sequence=>list
from StandardLibrary.LanguageBasic.Sequence.List import *
list_fun_show()

from StandardLibrary.LanguageBasic.Basic.String import *
string_fun_show()


''' 1.
写一个程序，判断2008年是否是闰年。

写一个程序，用于计算2008年10月1日是这一年的第几天？（2008年1月1日是这一年的第一天）
'''

''' 2.
name, age, score

tom, 12, 86

Lee, 15, 99

Lucy, 11, 58

Joseph, 19, 56

第一栏为姓名(name)，第二栏为年纪(age)，第三栏为得分(score)

现在，写一个Python程序，

1）读取文件

2）打印如下结果：

得分低于60的人都有谁？

谁的名字以L开头？

所有人的总分是多少?

3）姓名的首字母需要大写，该record.txt是否符合此要求？ 如何纠正错误的地方？
'''

from StandardLibrary.LanguageBasic.Basic.RegularExpression import *
reg_fun_show()


'''
        dataid,
        vipinfo.cardnum = row[cardnum"].ToString();
        '''
'''
        '' , -- vipid - varchar(20)
        @Vipid varchar(20),
        '''
def readFile(source,result,entityZip,rowName):
    f = open(source,"r")
    content = f.readlines()
    wf = open(result,"w")
    for x in content:
        if x != "\n":
            newtext = x.replace(" ","")
            '''
            finalText = entityZip + "." + newtext[0].upper() + newtext[1:- 2] + "=" + rowName + "[\"" + newtext[0: - 2] + "\"]" + ".ToString();\n"
            finalText = finalText.replace("		","")
            '''
            #newtext = newtext[newtext.index(',--')+3:len(newtext)]
            #newtext = newtext[0].upper() + newtext[1:len(newtext)]
            #newtext = ('@'+newtext).replace('-',' ')

            #@Vipid => vipid = @Vipid

            #'',--vipid-varchar(20)
            #vipinfo.Vipid = row["vipid"].ToString();
            #

            field = newtext[newtext.index("--") + 2:newtext.rindex('-')]

            lowerField = field[0].lower() + field[1:len(field)]

            field = field[0].upper() + field[1:len(field)]

            type = newtext[newtext.rindex('-') + 1:len(newtext)]
            type = type.strip()
            if type.rfind('(') > -1:
                type = type[0:type.rfind('(')].strip()
            final = ""
            if type in ["varchar","char","nvarchar"]:
                final = "vipinfo." + field + "=row[\"" + lowerField + "\"].ToString();"
            if type in ["numeric","decimal"]:
                final = "vipinfo." + field + "=row[\"" + lowerField + "\"] == DBNull.Value ? 0 : Convert.ToDecimal(row[\"" + lowerField + "\"]);"
            if type in ["datetime"]:
                final = "vipinfo." + field + "=row[\"" + lowerField + "\"].ToString();"
            if type in ["int"]:
                final = "vipinfo." + field + "=row[\"" + lowerField + "\"] == DBNull.Value ? 0 : Convert.ToInt32(row[\"" + lowerField + "\"]);"
            #newtext =
            #"db.AddInParameter(dc,\"@"+field+"\",SqlDbType."+type+",info."+field+");"
            #print(final)
            print(type,final)
            wf.writelines(final + "\n")
    wf.flush()
    wf.close()
def readNewFile(url):
    f = open(url,"r")
    content = f.readlines()
    for x in content:
        print(x)
#f = open("test.txt","w")
#writeFile(f)
#readFile("convert.txt","result.txt","levelInfo","levelRow")
#readNewFile("result.txt");
list = [1,2,3,4,5]
e = 1
if e in list:
    print("in")


from StandardLibrary.LanguageBasic.DateTime.DateTime import *
time_print()
time_sleep()
time_show_struct()
datetime_show()
datetime_cal()
datetime_convert()

from StandardLibrary.LanguageBasic.Path.Path import *
path_fun_show()
travelTree('D:/源代码/HavenLau.DotNet/HavenLau.DotNet/HavenLau.Python/StandardLibrary/',1)

from StandardLibrary.LanguageBasic.File.File import *
file_fun_show()

from StandardLibrary.LanguageBasic.Shutil.Shutil import *
shutil_fun_show()

from StandardLibrary.LanguageBasic.Pickle.Pickle import *
pcikle_fun_show()

from StandardLibrary.LanguageBasic.SubProcess.SubProcess import *
subprocess_fun_show()

from StandardLibrary.LanguageBasic.Signal.Signal import *
signal_fun_show()

from StandardLibrary.LanguageBasic.Threading.Threading import *
#threading_fun_show()
from StandardLibrary.LanguageBasic.MultiProcessing.MultiProcessing import *
#multiProcessing_fun_show();
#pipe_fun_show();
#queue_fun_show();
from StandardLibrary.LanguageBasic.Math.Math import *
math_fun_show()

from StandardLibrary.LanguageBasic.Random.Random import *
random_fun_show();