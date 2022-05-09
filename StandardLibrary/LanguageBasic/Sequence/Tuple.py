#加上此句话，防止IDE自动解码中文
#define 
mytuple = tuple
mytuple = (-1,0,1,2,3,4,5,6,7)

def tuple_fun_show():
    for x in mytuple:
        print(x)
    print("length:=>" + len(mytuple).__str__())  #返回： 序列中包含元素的个数
    print("min:=>" + min(mytuple).__str__()) #返回： 序列中最小的元素
    print("max:=>" + max(mytuple).__str__()) #返回： 序列中最大的元素
    print("all:=>" + all(mytuple).__str__()) #返回： True, 如果所有元素都为True的话
    print("any:=>" + any(mytuple).__str__()) #返回： True, 如果任一元素为True的话
    print("sum:=>" + sum(mytuple)   .__str__())  #      返回：序列中所有元素的和
    # x为元素值，i为下标(元素在序列中的位置)
    print("x:" + x.__str__())
    print("count:=>" + mytuple.count(x)  .__str__())  #   返回： x在s中出现的次数
    print("index:=>" + mytuple.index(x)   .__str__())  #  返回： x在s中第一次出现的下标