#加上此句话，防止IDE自动解码中文
mylist = list()
mylist = [1,3,5,'hello,world',11.1,True,None,'',False]
def list_fun_show():
    for x in mylist:
        print(x)
    print("length:=>" + len(mylist).__str__())
    # print("min:=>"+min(mylist).__str__());
    #Error:unorderable types: str()>int()
    # print("max:=>"+max(mylist).__str__());
    #Error:unorderable types: str()>int()
    print("any:=>" + all(mylist).__str__())
    print("all:=>" + any(mylist).__str__())
    #print("sum:=>" + sum(mylist) .__str__()) # 返回：序列中所有元素的和
    #Error:unsupported operand type(s) for +: 'int' and 'str'

    # x为元素值，i为下标(元素在序列中的位置)
    print("x:" + x.__str__())
    print("count:=>" + mylist.count(x)  .__str__())  #   返回： x在s中出现的次数
    print("index:=>" + mylist.index(x)   .__str__())  #  返回： x在s中第一次出现的下标
    #由于定值表的元素不可变更，下面方法只适用于表:
    print("mylist:",mylist)
    mylist.extend([12])        #在表l的末尾添加表l2的所有元素
    print("mylist:",mylist)
    mylist.append(x)         #在l的末尾附加x元素
    print("mylist:",mylist)
    # mylist.sort() #对l中的元素排序
    #Error:unorderable types: str() < int()
    print("mylist:",mylist)
    mylist.reverse()         #将l中的元素逆序
    print("mylist:",mylist)
    mylist.pop()             #返回：表l的最后一个元素，并在表l中删除该元素
    print("mylist:",mylist)
    del mylist[0]            #删除该元素
    print("mylist:",mylist)
    #(以上这些方法都是在原来的表的上进行操作，会对原来的表产生影响，而不是返回一个新表。)