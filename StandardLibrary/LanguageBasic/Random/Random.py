import random
def random_fun_show():
    print("生成伪随机数====>random.seed(10):",random.seed(10))
    print("生成伪随机数====>random.seed():",random.seed())
    # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
    lst = range(10)
    print("从序列的元素中随机挑选一个元素====>random.choice(range(10)):",random.choice(range(10)))
    print("从序列的元素中随机挑选几个元素====>random.sample(range(10),2):",random.sample(range(10),2))
    
    all_people = ['Tom', 'Vivian', 'Paul', 'Liya', 'Manu', 'Daniel', 'Shawn']
    print("将序列的所有元素随机排序====>random.shuffle(range(10)):",random.shuffle(all_people))
    random.shuffle(all_people)
    for i,name in enumerate(all_people):
        print(i,':' + name)
    print("从1到22中随机抽取5个整数 （这5个数字不重复）:",random.sample(range(1,23),5))
    num = [1,2,3,4,5,6]
    print("随机产生一个8位数字，每位数字都可以是1到6中的任意一个整数:",random.choice(num) * 10000000 + random.choice(num) * 1000000 + random.choice(num) * 100000 + random.choice(num) * 10000 + random.choice(num) * 1000 + random.choice(num) * 100 + random.choice(num) * 10 + random.choice(num))
     
    
       