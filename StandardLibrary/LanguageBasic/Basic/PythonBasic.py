#1.基本数据类型


#data-type：int
data = 1
print(data,type(data))

#data-type：float
data = 1.1111
print(data,type(data))

data = 14 * 1.1
print(data,type(data))
#data-type：bool
data = True
print(data,type(data))

#data-type:str
data = 'hello,world!'
print(data,type(data))

#data-type:date 日期转换为字符串
import time
import datetime
localtime = time.localtime(time.time())
print(localtime)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
print(str(datetime.datetime.now())[:19])

#data-type:date 字符串转换为日期
expire_time = "2013-05-21 09:50:35"
d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
print(d)

#data-type:date 获取日期差
oneday = datetime.timedelta(days=1)
#今天，2014-03-21
today = datetime.date.today()
#昨天，2014-03-20
yesterday = datetime.date.today() - oneday
#明天，2014-03-22
tomorrow = datetime.date.today() + oneday
#获取今天零点的时间，2014-03-21 00:00:00
today_zero_time = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')

#0:00:00.001000
print(datetime.timedelta(milliseconds=1)), #1毫秒
#0:00:01
print(datetime.timedelta(seconds=1)), #1秒
#0:01:00
print(datetime.timedelta(minutes=1)), #1分钟
#1:00:00
print(datetime.timedelta(hours=1)), #1小时
#1 day, 0:00:00
print(datetime.timedelta(days=1)), #1天
#7 days, 0:00:00
print(datetime.timedelta(weeks=1))

#data-type:date 获取时间差
#1 day, 0:00:00
oneday = datetime.timedelta(days=1)
#今天，2014-03-21 16:07:23.943000
today_time = datetime.datetime.now()
#昨天，2014-03-20 16:07:23.943000
yesterday_time = datetime.datetime.now() - oneday
#明天，2014-03-22 16:07:23.943000
tomorrow_time = datetime.datetime.now() + oneday
#注意时间是浮点数，带毫秒。

#那么要获取当前时间，需要格式化一下：
print(datetime.datetime.strftime(today_time, '%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.strftime(yesterday_time, '%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.strftime(tomorrow_time, '%Y-%m-%d %H:%M:%S'))


#9.5、获取上个月最后一天
last_month_last_day = datetime.date(datetime.date.today().year,datetime.date.today().month,1) - datetime.timedelta(1)

#9.6、字符串日期格式化为秒数，返回浮点类型：
expire_time = "2013-05-21 09:50:35"
d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
time_sec_float = time.mktime(d.timetuple())
print(time_sec_float)

#9.7、日期格式化为秒数，返回浮点类型：
d = datetime.date.today()
time_sec_float = time.mktime(d.timetuple())
print(time_sec_float)

#9.8、秒数转字符串
time_sec = time.time()
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_sec)))


#2.数据存储

#data-store:sequence

#tuple:元组、定值表
seq = (2,1.3,'love',[2,1.3,'love',[],5.6,False],5.6,False)

print(seq,type(seq))

print(seq[0],type(seq[0]))

print(seq[3],type(seq[3]))

print(seq[3][3],type(seq[3][3]))

#error :IndexError: tuple index out of range.
#print(seq[10],type(seq[10]))

#error:用户代码未处理的TypeError 'tuple' object does not support item assignment .
#seq[3]=[4,1.3,'lover',[],5.5,True]
#print(seq[3],type(seq[3]))
print('seq[3][3],type(seq[3][3])---------->')
#list：表
seq[3][3] = [11,111.3,'lover',[],511.5,True]
print(seq[3][3],type(seq[3][3]))

print('seq[:5]---------->')
print(seq[:5])             # 从开始到下标4 （下标5的元素 不包括在内）
print('seq[2:]---------->')
print(seq[2:])             # 从下标2到最后
print('seq[0:5:2]---------->')
print(seq[0:5:2])          # 从下标0到下标4 (下标5不包括在内)，每隔2取一个元素 （下标为0，2，4的元素）
print('seq[2:0:-1]---------->')
print(seq[2:0:-1])         # 从下标2到下标1

#从上面可以看到，在范围引用的时候，如果写明上限，那么这个上限本身不包括在内。

#尾部元素引用
print('seq[-1]---------->')
print(seq[-1])             # 序列最后一个元素
print('seq[-3]---------->')
print(seq[-3])             # 序列倒数第三个元素

#同样，如果s1[0:-1], 那么最后一个元素不会被引用 （再一次，不包括上限元素本身）



#字符串是一种特殊的元素，因此可以执行元组的相关操作。
seq[3][3][2] = 'newlover'
print(seq[3][3][2],type(seq[3][3][2]))
print(seq[3][3][2][0])
print(seq[3][3][2][1])
print(seq[3][3][2][2])

print(seq[3][3][2][0:1])
print(seq[3][3][2][0:2])
print(seq[3][3][2][0:3])

print(seq[3][3][2][0:8:1])
print(seq[3][3][2][0:8:2])
print(seq[3][3][2][0:8:3])


print(seq[3][3][2][-1])
print(seq[3][3][2][-2])
print(seq[3][3][2][-3])


print(seq[3][3][2][0:-1])
print(seq[3][3][2][0:-2])
print(seq[3][3][2][0:-3])


#数据运算

#1.0数学运算
print(1 + 2)
# ERROR:unsupported operand type(s) for +: 'int' and 'str'
# print(1+'2');
print(1 + 2.2222)
print(2 * 1.1111)
print(2 * 5)
print(2 * "2")#print 22
print(5 / 3)
print(6 / 3)
print(7 / 3)
print(3 ** 2)
print(4 ** 2)
print(7 % 3)
print(6 % 3)
print(5 % 3)


#2.0判断
print(5 == 6)               # =， 相等
print(8.0 != 8.0)           # !=, 不等
print(3 < 3, 3 <= 3)          # <, 小于; <=, 小于等于
print(4 > 5, 4 >= 0)          # >, 大于; >=, 大于等于
print(5 in [1,3,5])       # 5是list [1,3,5]的一个元素

#3.0逻辑
print(True and True, True and False)      # and, “与”运算， 两者都为真才是真
print(True or False)                      # or, "或"运算， 其中之一为真即为真
print(not True)                           # not, “非”运算， 取反
'''
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below. The following values are considered false:

None

False

zero of any numeric type, for example, 0, 0L, 0.0, 0j.

any empty sequence, for example, '', (), [].

any empty mapping, for example, {}.

instances of user-defined classes, if the class defines a __nonzero__() or __len__() method, when that method returns the integer zero or bool value False. [1]

All other values are considered true — so objects of many types are always true.

真值判断：
None,False,0,'',(),[],{},返回值为0或者False的function 这些都为false
'''
print(None == False)
print(False == False)
print(0 == False)
print('' == False)
print(() == False)
print([] == False)
print({} == False)



#缩进和选择
i = 1
x = 1
if i > 0:
    x = x + 1
print(x)
    
i = 1
if i > 0:
    print('positive i')
    i = i + 1
elif i == 0:
    print('i is 0')
    i = i * 10
else:
    print("negative i")
    i = i - 1
print('new i:',i)



#循环
for x in [3,4,'love',[1,2,3,4]]:
    print(x)

print('-------------------------------------------->')
idx = range(5)
print(idx)
for x in idx:
    print(x)
print('-------------------------------------------->')
while i < 10:
    print(i)
    i = i + 1

print('-------------------------------------------->')
for x1 in range(10):
    if x1 == 2:
        continue
    print(x1)    
print('-------------------------------------------->')
for x2 in range(10):
    if x2 == 2:
        break
    print(x2)
    

print('-------------------------------------------->')
#函数
def square_sum(a,b):#def，这个关键字通知python：我在定义一个函数。square_sum是函数名。括号中的a, b是函数的参数，是对函数的输入。
    #参数可以有多个，也可以完全没有（但括号要保留）。
    c = a ** 2 + b ** 2# 这一句是函数内部进行的运算
    return c,b,a#return可以返回多个值，以逗号分隔。相当于返回一个tuple(定值表)。

#在Python中，当程序执行到return的时候，程序将停止执行函数内余下的语句。return并不是必须的，当没有return,
#或者return后面没有返回值时，函数将自动返回None。None是Python中的一个特别的数据类型，用来表示什么都没有，相当于C中的NULL。None多用于关键字参数传递的默认值。
#（Python有丰富的参数传递方式，还有关键字传递、表传递、字典传递等，基础教程将只涉及位置传递）
print(square_sum(2,3))

print('-------------------------------------------->')
a = 1
def change_integer(a):
    a = a + 1
    return a
print(change_integer(a))
print(a)

print('-------------------------------------------->')
b = [1,2,3]
def change_list(b):
    b[0] = b[0] + 1
    return b
print(change_list(b))
print(b)


def IsYear(year,month,day):
    return year >= 0 and month >= 0 and day >= 0 and month <= 13 and day <= 31 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


print(IsYear(2015,11,11))

print(IsYear(2016,11,11))


#面向对象
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self,dx,dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()
print(summer.have_feather,summer.way_of_reproduction)
print('after move:',summer.move(5,8))
    
class Chicken(Bird):
    way_of_move = "walk"
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = "fly"
    possible_in_KFC = False

summer = Chicken()
print(summer.have_feather,summer.move(3,2),summer.possible_in_KFC)


class Animal(object):
    name = "Animal"
    age = 10
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)
    def sayHello(self):
        print("hello ,I'm " + self.name + ".I'm " + self.age + " years old.")


class Person(Animal):
    def sayHello(self):
        print("hello ,I'm " + self.name + ".I'm " + (str)(self.age) + " years old.")
        

person = Person()
person.name = "LiXiaoLei"
person.age = 25
person.sayHello()


class Engineer(Person):
    job = "Engineer"
    def __init__(self):
        self.age = 30
        self.name = "Engineer"
    def __init__(self,newAge,newName):
        self.age = newAge
        self.name = newName
    def __init__(self,newAge,newName,newJob):
        self.age = newAge
        self.name = newName
        self.job = newJob
    def sayHello(self):
        if self.job:
            print("hello ,I'm " + self.name + ".I'm " + (str)(self.age) + " years old.My job is " + self.job)
        else:
            print("hello ,I'm " + self.name + ".I'm " + (str)(self.age) + " years old.I have no job.")


print("------------------------------------------------->>>>")
eng = Engineer(30,"HavenLau","Engineer")
eng.sayHello()


class Human(object):
    can_talk = True
    can_walk = True
    age = 0
    gender = ""
    name = ["Li","Lei"]
    def __init__(self, input_gender):
        self.gender = input_gender
    def printGender(self):
        print(self.gender)
li_lei = Human("男")
li_lei.printGender()


'''
python 类在实例化的时候，
如果成员变量的为引用类型，那么实例化的属性值均为同样的引用值；可以理解为，class在加载的时候，引用类型的数据就已经在内存块里了；  ===>这里解释为什么a.name[0]都变成了王
而在java类实例化的时候，会在内存中开辟一块新的内存，再赋值引用类型的给成员变量。
'''
a = Human("男")
a.age+=1
a.name[0] = "王"
print(a.age,a.name)

b = Human("女")
print(b.age,b.name)

#print(help(list))

#print(dir(list))
n1 = [1,2,3,4,'n1']
print("------------------------------------------------->>>>")
print(type(n1))

newli = [1,2,3,4,'n1']
print("------------------------------------------------->>>>")
print((n1 == newli)) #竟然是True？？？
b.age+=1
print("------------------------------------------------->>>>")
print((a.age == b.age))

print("------------------------------------------------->>>>")
print(n1.count("5"))

n1.append("5")
print("------------------------------------------------->>>>")
print(n1)
print("------------------------------------------------->>>>")
print(n1.count(5))
print("------------------------------------------------->>>>")
print(n1.count("5"))

print("------------------------------------------------->>>>")
print(n1.index(3))

print([1,2,3,4] + [4,5])

class superList(list):
    def __sub__(self,b):
        a = self[:]
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a
print(superList([1,2,3,4]) - superList([4,5]))

#Internet开发，多线程，文本处理的对象。
#numpy, tkinter, django等用于科学计算，GUI开发，web开发的库，定义了各种各样的对象。
    

#dictionary词典
dic = {'s1':'HavenLau','s2':'LiLei','s3':'HanMeimei'}
print(dic['s1'])
dic["s4"] = "ZhangWuji"
print(dic)

for x in dic:
    print("key:" + x + " value:" + dic[x])
print("------------------------------------------------->>>>")
print(dic.keys)
print("------------------------------------------------->>>>")
print(dic.values)
print("------------------------------------------------->>>>")
print(dic.items)

print(len(dic))

del(dic["s2"])
print(len(dic))

# del("LiLei") ERROR!!!
# print(len(dic));


#文本的输入输出

#创建文件对象
def writeFile(f):
    f.writelines("")
    for x in dic:
        f.writelines(("Key:" + x + " Value:" + dic[x] + "\n"))
        print("ok")
    f.flush()
    f.close()
def readFile():
    f = open("test.txt","r")
    content = f.readlines()
    for x in content:
        print(x)


f = open("test.txt","w")
writeFile(f)
readFile()

import First as b
b.laugh()
from First import laugh
laugh()


#函数的参数对应
def f(a,b,c=3):
    return a + b - c

print(f(1,2,3))

print(f(a=1,b=2,c=3))

print(f(c=3,a=1,b=2))
 
   
#参数默认值
print(f(1,2))

print(f(a=1,b=2))

#包裹传递 在func的参数表中，所有的参数被name收集，根据位置合并成一个元组(tuple)，这就是包裹位置传递。
#*name是元组 **name是字典
def func(*name):
    print(type(name))
    print(name)

def fundic(**dic):
    print(type(dic))
    print(dic)
func(1,4,6)
func(5,6,7,1,2,3)


fundic(a=1,b=2)
fundic(m=2,n=1,c=3)


#解包裹
def sfunc(a,b,c):
    print(a,b,c)
args = (1,3,4)
sfunc(*args)


dict = {'a':'1','b':'3','c':'4'}
fundic(**dict)


#range(beginindex,endindex,splitindex)
#从开始索引 到 结束索引，每隔 splitindex个字符截取一个元素
sfunc(**dict)#=>Key:Value的模式去解析
sfunc(*dict)#=>Key的模式去解析
s = 'abcdefghijk'
for x in range(0,len(s),3):
    print(s[x])

#enumerate() 在每次循环中得到下标和元素
for (index,char) in enumerate(s):
    print("Index:" + index.__str__() + " Char:" + char)


#zip 多个等长的序列，然后想要每次循环时从各个序列分别取出一个元素
ta = [1,2,3,4,5]
tb = ['4','5','6','7','8']
tc = ['a','b','c','d','e']
for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c)

zipped = zip(ta,tb)
for x in zipped:
    print(x)

newzip = zip(ta,tc)
(ta,tc) = zip(*newzip)
print(ta,tc)

#循环对象
#what:比如 循环对象[a,b,c] for循环的过程是调用next()方法读出第一个元素，然后放到内存地址里面，用一个变量去指向这个内存地址。
#why:相对于序列，用循环对象的好处在于：不用在循环还没有开始的时候，就生成好要使用的元素。所使用的元素可以在循环过程中逐次生成。这样，节省了空间，提高了效率，编程更灵活。
#how:listObj.__next__();
note = open("test.txt")
obj = note.__next__()
print(obj)


for line in open("test.txt",'r'):
    #for结构自动调用next()方法，将该方法的返回值赋予给line。循环知道出现StopIteration的时候结束。
    print(line)



#迭代器
#what:从技术上来说，循环对象和for循环调用之间还有一个中间层，就是要将循环对象转换成迭代器(iterator)。这一转换是通过使用iter()函数实现的。但从逻辑层面上，常常可以忽略这一层，所以循环对象和迭代器常常相互指代对方。
#why:
#how:循环对象 == 》迭代器（iterator）[iter()]==>object 供 for调用

#生成器
#what 用户自定义的循环对象
#why 循环对象
#how 和函数定义类似，只不过return 改为yield 。生成器中可以有多个yield。
#===》调用生产器=》生成循环对象=》生成器遇到 yield ，暂停运行生成器 ，返回yield后面的值
def gen():
    a = 100
    yield a
    a = a * 8
    yield a
    yield 1000

for x in gen():
    print(x)

def gen():
    for i in range(4):
        yield i

for x in gen():
    print(x)

G = (x for x in range(4))
for x in G:
    print(x)


#表推导
#what:快速生成表的一种方法。
#why:语法简单，很有实用价值
#how:
L = []
for x in range(4):
    L.append(x)
print(L)
#与生成器表达式类似，只不过用的是中括号
L = [x for x in range(4)]
print(L)
L = [x ** 2 for x in range(4)]
print(L)

x1 = [1,3,5]
y1 = [9,12,13]
L = [x ** 2 for (x,y) in zip(x1,y1) if y > 10]
print(L)


#函数对象
#Note:秉承着一切皆对象的理念，我们再次回头来看函数(function)。函数也是一个对象，具有属性（可以使用dir()查询）。
#===》作为对象，它还可以赋值给其它对象名，或者作为参数传递。

#lambda 函数
func = lambda x,y:x + y
print(func(3,5))

def func(x,y):
    return x + y
print(func(3,5))


#函数作为参数传递
#what:函数可以作为一个对象，进行参数传递
#why:提高程序的灵活性
#how:
def test(f,a,b):
    print("test")
    print(f(a,b))

test(func,5,8)
test = lambda f,a,b:print(f(a,b))
test(func,5,18)
test((lambda x,y:x ** 2 + y),6,9)

print("------------------------------------------->>>>>>>>>>>>>>>map函数")
#map函数
#what :list =map(funobj,element_table);
#why :将函数对象依次作用于表的每一个元素。每次作用的结果储存于返回的表re中。map通过读入的函数来操作数据（表中的每一个元素）
#how : 第一种：re = map((lambda x:x**2),[1,3,5,7]);
#         第二种：re = map((lambda x,y:x*y),[1,3,5,7],[2,4,6,8])
#return :表
#re = map((lambda x,y:x*y),[1,3,5,7],[2,4,6,8])
for x in map((lambda x,y:x * y),[1,3,5,7],[2,4,6,8]):
    print(x)
print("------------------------------------------->>>>>>>>>>>>>>>filter函数")
#filter函数
#what :iterator = filter(funobj,element_table);
#why
#:将函数对象（funobj）作用于element_table中的每一个element运算过的值存储于返回的循环对象（iterator）中
#how :def fun(a)
#            return a>100:
#        print(filter(fun,[100,80,101,155]))
#return :循环boolean对象列表
mapresult = map((lambda x,y:x + y > 7),[1,3,5,7],[2,4,6,8])
print(mapresult)
for x in mapresult:
    print(x)
def fun(a):
    return a > 100
mapresult = map(fun,[89,95,101,120,199])
print(list(mapresult))
for x in mapresult:
    print(x)
print("------------------------------------------->>>>>>>>>>>>>>>reduce函数")
#reduce函数
#what :operate_value = reduce(funobj,element_table);
#why :累进的将函数作用于各个参数
#how : print(reduce(funobj),list)
#return :list中元素1和元素2的运算值，然后运算值和元素3的运算值，一直到最后一个元素
from _functools import reduce
print(reduce(lambda x,y:x + 2 * y,[1,2,5,7,9]))


#异常处理
re = iter(range(5))
try:
    for i in range(10):
        print(re.__next__())
except StopIteration:
    print("here is end"),i
finally:
    print('HaHaHaHa')


#动态类型
#what:Python的变量(variable)不需要声明，而在赋值时，变量可以重新赋值为任意值。这些都与动态类型的概念相关。
#
#在我们接触的对象中，有一类特殊的对象，是用于存储数据的。常见的该类对象包括各种数字，字符串，表，词典。
#在C语言中，我们称这样一些数据结构为变量。而在Python中，这些是对象。
#对象是储存在内存中的实体。但我们并不能直接接触到该对象。
#我们在程序中写的对象名，只是指向这一对象的引用(reference)。
#
#引用和对象分离，是动态类型的核心。引用可以随时指向一个新的对象：
#a = 3
#a = 'at'
#第一个语句中，3是储存在内存中的一个整数对象。通过赋值，引用a指向对象3。
#第二个语句中，内存中建立对象‘at’，是一个字符串(string)。引用a指向了'at'。此时，对象3不再有引用指向它。
#Python会自动将没有引用指向的对象销毁(destruct)，释放相应内存。
#
#(对于小的整数和短字符串，Python会缓存这些对象，而不是频繁的建立和销毁。)
#a = 5
#b = a
#a = a + 2
#再看这个例子。通过前两个句子，我们让a,b指向同一个整数对象5(b = a的含义是让引用b指向引用a所指的那一个对象)。
#但第三个句子实际上对引用a重新赋值，让a指向一个新的对象7。此时a,b分别指向不同的对象。
#我们看到，即使是多个引用指向同一个对象，如果一个引用值发生变化，那么实际上是让这个引用指向一个新的引用，并不影响其他的引用的指向。
#从效果上看，就是各个引用各自独立，互不影响。
#
#其它数据对象也是如此:
#L1 = [1,2,3]
#L2 = L1
#L1 = 1
#
#但注意以下情况
#L1 = [1,2,3]
#L2 = L1
#L1[0] = 10
#print L2
#在该情况下，我们不再对L1这一引用赋值，而是对L1所指向的表的元素赋值。结果是，L2也同时发生变化。
#
#原因何在呢？因为L1，L2的指向没有发生变化，依然指向那个表。表实际上是包含了多个引用的对象（每个引用是一个元素，比如L1[0]，L1[1]...,
#每个引用指向一个对象，比如1,2,3), 。而L1[0] = 10这一赋值操作，并不是改变L1的指向，而是对L1[0],
#也就是表对象的一部份(一个元素)，进行操作，
#所以所有指向该对象的引用都受到影响。
#
#（与之形成对比的是，我们之前的赋值操作都没有对对象自身发生作用，只是改变引用指向。）
#
#列表可以通过引用其元素，改变对象自身(in-place change)。这种对象类型，称为可变数据对象(mutable
#object)，词典也是这样的数据类型。
#而像之前的数字和字符串，不能改变对象本身，只能改变引用的指向，称为不可变数据对象(immutable object)。
#我们之前学的元组(tuple)，尽管可以调用引用元素，但不可以赋值，因此不能改变对象自身，所以也算是immutable object.

#why:
#how:
#return:
print("------------------------------------------->>>>>>>>>>>>>>>从动态类型上来看函数的参数传递,传递不可变参数")
#从动态类型上来看函数的参数传递
def f(x):
    x = 100
    print(x)

a = 1
f(a)
print(a)
#Note:参数x是一个新的引用，指向a所指的对象。如果参数是不可变(immutable)的对象，a和x引用之间相互独立。对参数x的操作不会影响引用a。
#     这样的传递类似于C语言中的值传递。
print("------------------------------------------->>>>>>>>>>>>>>>从动态类型上来看函数的参数传递,传递可变参数")
def f(x):
    x[0] = 100
    print(x)
a = [1,2,3]
f(a)
print(a)



#序列（Array）的方法
def array_function_test():
    s = [1,35,7,9]
    print(min(s),max(s),len(s),all(s),any(s));

