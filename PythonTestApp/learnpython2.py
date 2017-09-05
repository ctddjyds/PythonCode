# 单行注释
""" 多行字符串可以用
    三个引号包裹，不过这也可以被当做
    多行注释
"""

####################################################
### 1. 原始数据类型和操作符
####################################################
#from __future__ import division 
# 数字类型
3  # => 3
a=0xAF #=>175小写的x或者或者大写的X都可以
b=0o10 #=>8 不是10 第二字母是o，小写的o或者大写的O都可以； Python 2.7中,可以用o10//第一是字母o/O
a=(1+3j)*(9+4j) #=>(-3+31j) 提供对复数的支持

# 简单的算数
1 + 1  # => 2
8 - 1  # => 7
10 * 2  # => 20
35 / 5  # => 7
2**3  #=>8
#Python 3.x “/”除将得到浮点数，“//”除才仍是整数
# 整数的除法会自动取整
b=5 / 2  # => 2.5 Python 2.7中 =2
a=1/2
a=5//2 # => 2 整除向下取整
a=5.0 // 3.0 # => 1.0 # 浮点数也可以
a=5 % 2  # => 1

# 要做精确的除法，我们需要引入浮点数
2.0     # 浮点数
11.0 / 4.0  # => 2.75 精确多了

# 括号具有最高优先级
(1 + 3) * 2  # => 8
test='Spam!' * 8  #


# 字符串通过 " 或 ' 括起来
"This is a string."
'This is also a string.'
#字符串本身包含 '，可以用" "括起来表示：
"I'm OK"
#字符串本身包含 "，可以用' '括起来表示：
'Learn "Python" in imooc'
#字符串既包含 ' 又包含 "，需要对字符串的某些特殊字符进行“转义”，Python字符串用\进行转义
'Bob said \"I\'m OK\".'
# 字符串通过加号拼接
"Hello " + "world!"  # => "Hello world!"
# 字符串可以被视为字符的列表list
"This is a string"[0]  # => 'T'

#raw字符串：标识里面的字符不需要转义
r'''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''
#r'...'表示法:需注意 ' 和 "的使用
# r'...' --里面r 的第一个 ' 和 Let' 的 ' 匹配了
#print r'Python is created by "Guido". Let's start learn Python in imooc!' 
#不会报错
print(r'Python is created by "Guido".') 

# 老式的格式化语法 %：可以用来格式化字符串，用指定的参数替代 %s，如程序需在Python2.5以下环境运行才建议使用
"%s can learn" % 123
# % 右侧一般使用元组来指定多个值
"%s can be %s" % ("strings", "interpolated")
# 推荐使用方法 format 方法来格式化字符串
"{0} can be {1}".format("strings", "formatted")
# 可以重复参数以节省时间
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
#=> "Jack be nimble, Jack be quick, Jack jump over the candle stick"
# 也可以用变量名代替数字
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

#模板字符串
from string import Template
t=Template('Make $$ selling $x!')
t.substitute(x='slurm')
#strip(rm) 删除字符串中开头、结尾处的 rm 序列的字符
#当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')
t='     123\n'.strip() #=>'123'


# 布尔值也是基本的数据类型
True
False

# 布尔值的与或非运算
True and True   # ==> True
True and False   # ==> False
False and False   # ==> False
True or True   # ==> True
True or False   # ==> True
False or False   # ==> False
not True  # => False
not False  # => True

# 相等
1 == 1  # => True
2 == 1  # => False

# 不等
1 != 1  # => False
2 != 1  # => True

# 更多的比较操作符
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# 比较运算可以连起来写！
1 < 2 < 3  # => True
2 < 3 < 2  # => False

#短路计算
a = True
print(a and 'a=T' or 'a=F') #=> a=T

# None 是对象
None  # => None

# 不要用相等 `==` 符号来和None进行比较
# 要用 `is`，is是用来比较两个变量是否指向同一个对象
# 'is'操作符在比较原始数据时没多少用，但是比较对象时必不可少
"etc" is None  # => False
None is None  # => True

# None, 0, 空字符串，空列表，空字典都被算作 False
# 其他的均为 True
0 == False  # => True
"" == False  # => True
bool([]) #=> False
bool({}) #=> False


####################################################
## 2. 变量和数据结构
####################################################
# print输出
#print "I'm Python. Nice to meet you!"
print('The quick brown fox', 'jumps over', 'the lazy dog')
print("I'm Python. Nice to meet you!") # Python 3.x的语句方式


# 给变量赋值前不需要事先声明
# 一般建议使用小写字母和下划线组合来做为变量名
some_var = 5    
some_var  # => 5
# 访问未赋值的变量会抛出异常
#some_other_var  # 抛出 NameError


# 列表用来保存序列
li = []
# 可以直接初始化列表
other_li = [4, 5, 6]
# 在列表末尾添加元素
li.append(1)    # li 现在是 [1]
li.append(2)    # li 现在是 [1, 2]
li.append(4)    # li 现在是 [1, 2, 4]
li.append(5)    # li 现在是 [1, 2, 4,5]
#在列表中插入元素
li.insert(2,3)    # li 现在是 [1, 2, 3, 4]
# 像其他语言访问数组一样访问列表
li[0]  # => 1
# 使用倒序索引，访问最后一个元素
li[-1]  # => 4
# 越界会抛出异常
#li[4]  # 抛出越界异常
# 删除特定元素--del语句
del li[2]  # li 现在是 [1, 2, 4]
#remove方法，移除列表中某个值的第一个匹配项,修改了列表无返回值
li.remove(5)
# pop()移除列表末尾元素，并且返回这个元素
li.pop()        # => 4 li 现在是 [1, 2]
#pop(index)方法删掉list中指定索引的元素，并且返回这个元素
li.pop(1)
# 重新加进去
li.insert(1,2)
li.insert(2,3)
li.append(4)    # li is now [1, 2, 3, 4] again.
#替换元素
li[3]=5   # [1, 2, 3, 5]
#统计元素在列表出现次数
li.count(3)
# 列表末尾追加序列多个值函数
li.extend(other_li)  # li 是 [1, 2, 3, 4, 5, 6]
#查找某个元素第一个匹配项的索引位置,必须先验证元素是否存在，否则会报ValueError异常
li.index(3)
#列表生成式
[x * x for x in range(1, 11)]   #=>[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[x * x for x in range(1, 11) if x % 2 == 0] #=>[4, 16, 36, 64, 100]
[m + n for m in 'ABC' for n in '123'] #=>['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
M = [[1, 2, 3],          # A 3X3 matrix, as nested lists
         [4, 5, 6],          # Code can span lines if bracketed
         [7, 8, 9]]
G = (row for row in M)  # Create a generator of row sums
t=next(G)
G={sum(row) for row in M}
G={i:sum(M[i]) for i in range(3)}

# 元组类似于列表，但它是不可改变的
tup = (1, 2, 3)
tup[0]  # => 1
#tup[0] = 3  # 类型错误
#定义单元素的tuple要多加一个逗号“,”，避免歧义
t = (1,)
#打印单元素tuple时，自动添加了一个“,”，为了更明确地告诉你这是一个tuple
print(t)  #=>(1,)
#多元素 tuple 加不加这个额外的“,”效果是一样的：
t = (1, 2, 3,)
print(t)   #=>(1, 2, 3)
#tuple可变性
t = ('a', 'b', ['A', 'B'])
L = t[2]
L[0] = 'X'
L[1] = 'Y'
print(t) # =>('a', 'b', ['X', 'Y'])
# 你可以将元组解包赋给多个变量
a, b, c = (1, 2, 3)     # a 是 1，b 是 2，c 是 3
# 如果不加括号，将会被自动视为元组
d, e, f = 4, 5, 6
# 现在我们可以看看交换两个数字是多么容易的事
e, d = d, e     # d 是 5，e 是 4


# 切片语法需要用到列表的索引访问
# 可以看做数学之中左闭右开区间
li=[1, 2, 3, 5]
li[1:3]  # => [2, 3]
# 省略末尾的元素
li[2:]  # => [3, 5]
# 省略开头的元素
li[:3]  # => [1, 2, 3]
#指定步进--步进为正
li[::2] # =>[1,3]
#步进为负，必须让开始索引大于结束索引否则获取的是空列表
temp=li[::-1]   # => [5, 3, 2, 1]
temp=li[3:0:-1] #=>[5, 3, 2]
#倒序切片
L = range(1, 101)
print(L[4::5][-10:]) #[55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
tup[:2]  # => (1, 2)
#分片赋值,不能用于不可变的序列（元组，字符串，Unicode字符串）
#不等长序列替换
name=list('Perl')
name[1:]=list('ython')
numbers=[1,5]
#插入元素
numbers[1:1]=[2,3,4]
#删除元素
numbers[2:4]=[]

# 序列拼接（相加）--生成一个新的序列，不会改变这原始序列
li + other_li  # => [1, 2, 3, 4, 5, 6]
#li+"World" #=>TypeError
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
#乘法
temp=[1,2]*4 #=>[1, 2, 1, 2, 1, 2, 1, 2]
temp=(2,3)*4 #=>(2,3,2,3,2,3,2,3)
sequence=[None]*10 #=>创建多个元素空间的空列表的方式
#成员资格：用 in 来返回元素是否在序列中
1 in li  # => True
2 in tup  # => True
# 返回长度，最大值，最小值
len(li)  # => 6
len(tup)  # => 6
max(li)
max(tup)
min(li)
min(tup)


# 字典用来储存映射关系
empty_dict = {}
# 字典初始化
filled_dict = {"one": 1, "two": 2, "three": 3}

# 字典也用中括号访问元素
filled_dict["one"]  # => 1

# 判断一个键是否存在
"one" in filled_dict  # => True
1 in filled_dict  # => False

# 查询一个不存在的键会抛出 KeyError
#filled_dict["four"]  # KeyError

# 用 get 方法来避免 KeyError
filled_dict.get("one")  # => 1
filled_dict.get("four")  # => None
# get 方法支持在不存在的时候返回一个默认值
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4)  # => 4

# 把所有的键保存在列表中
filled_dict.keys()  # => ["three", "two", "one"]
# 键的顺序并不是唯一的，得到的不一定是这个顺序

# 把所有的值保存在列表中,和键的顺序相同,也不是唯一顺序
filled_dict.values()  # => [3, 2, 1]
# 
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
d.items()   #[('Lisa', 85), ('Adam', 95), ('Bart', 59)]

# setdefault 是一个更安全的添加字典元素的方法
filled_dict.setdefault("five", 5)  # filled_dict["five"] 的值为 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] 的值仍然是 5


# 集合储存无顺序的元素
empty_set = set()
# 初始化一个集合
some_set = set([1, 2, 2, 3, 4])  # some_set 现在是 set([1, 2, 3, 4])

# Python 2.7 之后，大括号可以用来表示集合
filled_set = {1, 2, 2, 3, 4}  # => {1 2 3 4}

# 用 in 来判断元素是否存在于集合中
2 in filled_set  # => True
10 in filled_set  # => False

# 向集合添加元素
filled_set.add(5)  # filled_set 现在是 {1, 2, 3, 4, 5}

# 从集合删除元素
#filled_set.remove(6) # 元素不存在set,抛出KeyError

# 用 & 来计算集合的交
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# 用 | 来计算集合的并
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# 用 - 来计算集合的差
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}


####################################################
## 3. 控制流程
####################################################
some_var = 5
# 这是个 if 语句，在 python 中缩进是很重要的。
# 下面的代码片段将会输出 "some var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # 这个 elif 语句是不必须的
    print("some_var is smaller than 10.")
else:           # 这个 else 也不是必须的
    print("some_var is indeed 10.")

# if 语句可以作为表达式来使用
"yahoo!" if 3 > 2 else 2  # => "yahoo!"

"""
用for循环遍历列表
输出:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # 你可以用 % 来格式化字符串
    print("%s is a mammal" % animal)

#多重循环
for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print(x + y)

#while break
sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print(sum)

# 用 try/except 块来处理异常
# Python 2.6 及以上适用:
try:
    # 用 raise 来抛出异常
    raise IndexError("This is an index error")
except IndexError as e:
    pass    # pass 就是什么都不做，不过通常这里会做一些恢复工作

####################################################
## 4. 函数
####################################################

# 用 def 来新建函数
def add(x, y):
    print("x is %s and y is %s" % (x, y))
    return x + y    # 通过 return 来返回值

# 调用带参数的函数
add(5, 6)  # => 输出 "x is 5 and y is 6" 返回 11

# 通过关键字赋值来调用函数
add(y=6, x=5)   # 顺序是无所谓的

#函数返回多值，其实就是返回一个tuple，可以省略括号
import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)

#递归函数需要注意防止栈溢出
def Hanoi(n, a, b, c):
    if n==1:
        print (a,'-->',c)#只有一个圆盘-从A到C
        return #这是结束递归，省略了None
    Hanoi(n-1,a,c,b) #将A柱的n-1个盘移到B柱
    print(a,'-->',c) #打印移动步骤
    Hanoi(n-1,b,a,c)#过渡柱子B上（n-1）个圆盘B递归移动到目标柱子C
Hanoi(4, 'A', 'B', 'C')

#可变参数列表:可以定义接受多个变量的函数，这些变量是按照顺序排列的
def varargs(*args):
    if args:
        return args
    else:
        return 0.0
varargs(1, 2, 3)  # => (1,2,3)

#参数的分拆：当你要传递的参数已经是一个列表，但调用的函数却接受分开一个个的参数值
#使用* 操作符来自动把参数列表进行拆分:
args=[3,6]
x=list(range(*args)) # *args 将列表 args 拆分成3，6 两个参数
print(x)
#使用 ** 操作符自动进行参数字典的分拆:
def parrot(voltage,state='a stiff',action='voom'):
    return voltage,state,action    
d={"voltage":"four million", "state":"bleedin demised","action":"voom"}
x=parrot(**d)
x=parrot(*d)
d={"state":"bleedin demised","action":"voom"}
#x=parrot(**d) # 无法自动匹配时，无法继续执行
def keyword_args(**kwargs):
    return kwargs
# 实际效果：
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}

# 可以同时将一个函数定义成两种形式
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""
# 当调用函数的时候，我们也可以进行相反的操作，把元组和字典展开为参数
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)  # 等价于 foo(1, 2, 3, 4)
all_the_args(**kwargs)  # 等价于 foo(a=3, b=4)
all_the_args(*args, **kwargs)  # 等价于 foo(1, 2, 3, 4, a=3, b=4)

# 函数在 python 中是一等公民
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)  # => 13
create_adder(10)(3)

#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#限制:只能有一个表达式，不写return，返回值就是该表达式的结果。
(lambda x: x > 2)(3)  # => True

# 内置高阶函数
#map接收一个函数f和一个list，并通过把函数f依次作用在list的每个元素上，得到一个新的list并返回
map(add_10, [1, 2, 3])  # => [11, 12, 13] 
#reduce()函数接收一个函数f一个list，传入的函数f必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值，如果序列是空值抛出异常
def f(x, y):
    return x + y
reduce(f, [1, 3, 5, 7, 9]) # =>25  f(1, 3) -> f(f(1,3),5) >>>>
#reduce()还可以接收第3个可选参数，作为计算的初始值
reduce(f, [1, 3, 5, 7, 9], 100) #=>125
#接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
filter(lambda x: x > 5, [3, 4, 5, 6, 7])  # => [6, 7]
# sorted()函数可对有序集合进行排序
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
sorted([36, 5, 12, 9, 21], reversed_cmp)

# 可以用列表方法来对高阶函数进行更巧妙的引用
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

#enumerate() 函数自动把每个元素变成 (index, element) 这样的tuple
L = ['Adam', 'Lisa', 'Bart', 'Paul']
enumerate(L) #=>[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]

"""
`range(number)` 返回从0到number的等差级数链表
生成的链表中不包括结束值number
"""
for i in range(4):
    print(i)
"""
输出:
    0
    1
    2
    3
"""
#指定一个数值开始的链表
for i in range(5, 10):
    print(i)
"""
输出:
    5
    6
    7
    8
    9
"""
#指定一个数值开始和步进值的链表
for i in range(-10, -100,-30):
    print(i)
"""
输出:
    -10
    -40
    -70   
"""
#偏函数：functools.partial就是帮助我们创建一个偏函数，可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值
import functools
max2 = functools.partial(max, 10) #会把10作为*args的一部分自动加到左边
max2(5, 6, 7) #=>args = (10, 5, 6, 7)

####################################################
## 5. 类
####################################################

# 我们新建的类是从 object 类中继承的
class Human(object):
     # 类属性，由所有类的对象共享
    species = "H. sapiens"
    # 基本构造函数
    def __init__(self, name):
        # 将参数赋给对象成员属性
        self.name = name

    # 成员方法，参数要有 self
    def say(self, msg):
        return "%s: %s" % (self.name, msg)

    # 类方法由所有类的对象共享
    # 类方法在调用时，会把类本身传给第一个参数
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法是不需要类和对象的引用就可以调用的方法
    @staticmethod
    def grunt():
        return "*grunt*"

# 实例化一个类
i = Human(name="Ian")
print(i.say("hi"))     # 输出 "Ian: hi"

j = Human("Joel")
print(j.say("hello"))  # 输出 "Joel: hello"

# 访问类的方法
i.get_species()  # => "H. sapiens"

# 改变共享属性
Human.species = "H. neanderthalensis"
i.get_species()  # => "H. neanderthalensis"
j.get_species()  # => "H. neanderthalensis"

# 访问静态变量
Human.grunt()  # => "*grunt*"

import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
# 方法也是一个属性，所以，它也可以动态地添加到实例上，只是需要用 types.MethodType() 把一个函数绑定到一个属性上；
# 并不常见，直接在class中定义要更直观
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print(p1.get_grade()) # => A
print(isinstance(p1, Person)) #=>true 判断变量的类型

####################################################
## 6. 模块
####################################################

# 我们可以导入其他模块
import math
print(math.sqrt(16))  # => 4
import os
print(os.getcwd())

# 我们也可以从一个模块中导入特定的函数
from math import ceil, floor,log
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# 从模块中导入所有的定义
# 警告：不推荐使用
from math import *

from logging import log as logger   # logging的log现在变成了logger
print(log(10))   # 调用的是math的log
logger(10, 'import from logging')   # 调用的是logging的log
# 简写模块名
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# Python的模块其实只是普通的python文件
# 你也可以创建自己的模块，并且导入它们
# 模块的名字就和文件的名字相同
# 也可以通过下面的方法查看模块中有什么属性和方法
import math
dir(math)
dir()#当前模块的定义，但不会列出内置函数和变量名，他们在标准模块‘_builtin_’中定义
import __builtin__
print(dir(__builtin__))
import function
import sys
print(sys.path)
sys.path.append(r"C:\Program Files")

