#加上此句话，防止IDE自动解码中文
def string_fun_show():
    mystring = "Nice to meet you.Lilei"
    sub = "l"
    print("mystring:",mystring,"\n","sub:",sub)
    print("mystring.count(sub):",mystring.count(sub))# 返回：sub在str中出现的次数

    print("mystring.find(sub):",mystring.find(sub))# 返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1

    print("mystring.index(sub):",mystring.index(sub))      #返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误

    print("mystring.rfind(sub):", mystring.rfind(sub))       #返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1

    print("mystring.rindex(sub):", mystring.rindex(sub))      #返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误

 

    print("mystring.isalnum():",mystring.isalnum())        #返回：True， 如果所有的字符都是字母或数字

    print("mystring.isalpha():",mystring.isalpha())        #返回：True，如果所有的字符都是字母

    print("mystring.isdigit():",mystring.isdigit())        #返回：True，如果所有的字符都是数字

    print("mystring.istitle():",mystring.istitle())        #返回：True，如果所有的词的首字母都是大写

    print("mystring.isspace():",mystring.isspace())        #返回：True，如果所有的字符都是空格

    print("mystring.islower():",mystring.islower())        #返回：True，如果所有的字符都是小写字母

    print("mystring.isupper():",mystring.isupper())        #返回：True，如果所有的字符都是大写字母

 
    sep = '$'
    max = 5
    #print("mystring.split([sep, [max]]):",mystring.split([sep, [max]]))
    #返回：从左开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.split(',')的方式使用逗号或者其它分割符

    #print("mystring.rsplit([sep, [max]]):",mystring.rsplit([sep, [max]]))
    #返回：从右开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.rsplit(',')的方式使用逗号或者其它分割符

 
    s = '|'
    print("mystring.join(s):",mystring.join(s))                #返回：将s中的元素，以str为分割符，合并成为一个字符串。

    print("mystring.strip([sub]):",mystring.strip(sub))           #返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub
    new_sub = '='
    print("mystring.replace(sub, new_sub):",mystring.replace(sub, new_sub))  #返回：用一个新的字符串new_sub替换str中的sub

         

    print("mystring.capitalize():",mystring.capitalize())           #返回：将str第一个字母大写

    print("mystring.lower():",mystring.lower())                #返回：将str全部字母改为小写

    print("mystring.upper():",mystring.upper())                #返回：将str全部字母改为大写

    print("mystring.swapcase():",mystring.swapcase())             #返回：将str大写字母改为小写，小写改为大写

    print("mystring.title():",mystring.title())                #返回：将str的每个词(以空格分隔)的首字母大写

 
    width = 10
    print("mystring.center(width):",mystring.center(width))          #返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。

    print("mystring.ljust(width):",mystring.ljust(width))           #返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。

    print("mystring.rjust(width):",mystring.rjust(width))           #返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。