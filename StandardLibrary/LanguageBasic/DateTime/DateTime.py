##time包基于C语言的库函数(library functions)。Python的解释器通常是用C编写的，Python的一些函数也会直接调用C语言的库函数。
class DateTime(object):
    """"""

import time

def time_print():
    print("wall clock time, unit: second==>time.time()",time.time())
    print("processor clock time, unit: second==>time.clock()",time.clock())


def time_sleep():
    print("start...")
    time.sleep(3)
    print("wake up...")

def time_show_struct():
    print("---time包还定义了struct_time对象。该对象实际上是将挂钟时间转换为年、月、日、")
    print("---时、分、秒……等日期信息，存储在该对象的各个属性中(tm_year, tm_mon, t")
    print("---...)。下m_mday面方法可以将挂钟时间转换为struct_time对象:")
    print("================================================================>>>")
    print("返回struct_time格式的UTC时间：time.gmtime():",time.gmtime())
    print("返回struct_time格式的当地时间，当地时间根据系统环境决定：time.localtime():",time.localtime())
    print("将struct_time转换成wall clock time:time.mktime(time.gmtime()):",time.mktime(time.gmtime()))



import datetime
datetime_show_note = '''
datetime包是基于time包的一个高级包， 为我们提供了多一层的便利。
datetime可以理解为date和time两个组成部分。date是指年月日构成的日期(相当于日历)，time是指时分秒微秒构成的一天24小时中的具体时间(相当于手表)。你可以将这两个分开管理(datetime.date类，datetime.time类)，也可以将两者合在一起(datetime.datetime类)。由于其构造大同小异，我们将只介绍datetime.datetime类。
'''

def datetime_show():
    print(datetime_show_note)
    dt = datetime.datetime
    print("dt = datetime.datetime;===>",dt)
    dt = datetime.datetime(2016,2,14,22,59,24)
    print("dt = datetime.datetime(2016,2,14,22,59,24);===>",dt)

datetime_cal_note = '''
datetime包还定义了时间间隔对象(timedelta)。一个时间点(datetime)加上一个时间间隔(timedelta)可以得到一个新的时间点(datetime)。比如今天的上午3点加上5个小时得到今天的上午8点。同理，两个时间点相减会得到一个时间间隔。
'''
def datetime_cal():
    print(datetime_cal_note)
    t = datetime.datetime(2016,2,10,20,0,0)
    t_next = datetime.datetime(2016,2,15,0,0,0)
    delta1 = datetime.timedelta(seconds = 600)
    delta2 = datetime.timedelta(weeks = 3)
    print("datetime.datetime(2016,2,10,20,0,0) + datetime.timedelta(seconds = 600)===>",t + delta1)
    print("datetime.datetime(2016,2,10,20,0,0) + datetime.timedelta(weeks = 3)===>",t + delta2)
    print("datetime.datetime(2016,2,15,0,0,0) - datetime.datetime(2016,2,10,20,0,0)===>",t_next - t)
    print("datetime.datetime(2016,2,10,20,0,0) > datetime.datetime(2016,2,15,0,0,0)===>",t > t_next)  


def datetime_convert():
    format = "output-%Y-%m-%d-%H%M%S.txt"
    str = "output-2016-02-15-231411.txt"
    t_next = datetime.datetime(2016,2,15,0,0,0)
    print(t_next.strptime(str,format))
    print(t_next.strftime(format))

