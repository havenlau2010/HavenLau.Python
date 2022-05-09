import pickle
import time
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    date = ""

def pickleObject():
    newSummer = Bird()
    newSummer.have_feather = True
    newSummer.way_of_reproduction = "sex"
    newSummer.date = time.localtime()
    fn = 'abc.pkl'
    # open file with write-mode
    with open(fn,'wb') as f:
        # serialize and save object
        picklestring = pickle.dump(newSummer,f)
    

def pcikle_fun_show():
    #在内存中New一个对象
    summer = Bird()
    #使用pickle.dumps()方法可以将对象summer转换成了字符串 picklestring(也就是文本流)。
    picklestring = pickle.dumps(summer)
    pickleObject()
    loadPickleObject()

def loadPickleObject():
    fn = "abc.pkl"
    with open(fn,'rb') as f:
        newSummer = pickle.load(f)
    print(newSummer.date,newSummer.way_of_reproduction);
    