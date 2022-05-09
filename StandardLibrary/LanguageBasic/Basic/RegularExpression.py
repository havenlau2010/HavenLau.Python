
#防止中文乱码
import re
def reg_fun_show():
     #接收两个参数，第一个'[0-9]'就是我们所说的正则表达式，它告诉Python的是，“听着，我从字符串想要找的是从0到9的一个数字字符”。

     # 搜索整个字符串，直到发现符合的子字符串。
     m = re.search("[0-9]","abcd5efg,hi")
     print("re.search(\"[0-9]\",\"abcd5efg,hi\")=>:",m.group())

     # 从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。
     m = re.match("[0-9]","abcd5efg,hi")
     print("re.match(\"[0-9]\",\"abcd5efg,hi\")=>:",m) #Error:此处如果没有匹配上 调用group()函数会报错。
     m = re.match("[0-9]","9abcd5efg,hi")
     print("re.match(\"[0-9]\",\"9abcd5efg,hi\")=>:",m.group())

     # 在string中利用正则变换pattern进行搜索，对于搜索到的字符串，用另一字符串replacement替换。返回替换后的字符串。
     str = re.sub("[0-9]", "☆", "9abcd5efg,hi") 
     print("str = re.sub(\"[0-9]\",\"☆\",\"9abcd5efg,hi\")=>:",str)

     # 根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
     m = re.split("[0-9]","9abcd5efg,hi")
     print("re.split(\"[0-9]\",\"9abcd5efg,hi\")=>:",m)
     # 根据正则表达式搜索字符串，将所有符合的子字符串放在一给表(list)中返回
     m = re.findall("[0-9]","9abcd5efg,hi")
     print("re.findall(\"[0-9]\",\"9abcd5efg,hi\")=>:",m)
     # 根据正则表达式搜索字符串，将所有符合的子字符串放在一给表(list)中返回
     m = re.search("output_(\d{4})", "output_1986.txt")
     #我们可以m.group(number)的方法来查询群。group(0)是整个正则表达的搜索结果，group(1)是第一个群……
     print("re.search(\"output_(\d{4})\", \"output_1986.txt\")",m.group(1))
     #我们还可以将群命名，以便更好地使用m.group查询:
     m = re.search("output_(?P<year>\d{4})", "output_1986.txt")   
     #(?P<name>...) 为group命名
     print("re.search(\"output_(?P<year>\d{4})\", \"output_1986.txt\")",m.group("year"))