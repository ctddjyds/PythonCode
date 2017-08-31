
# 用字典表达映射关系
empty_dict = {}
# 初始化的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# 用[]取值
filled_dict["one"]   # => 1


# 用keys获得所有的键。因为keys返回一个可迭代对象，所以在这里把结果包在list里。我们下面会详细介绍可迭代。
# 注意：字典键的顺序是不定的，你得到的结果可能和以下不同。
list(filled_dict.keys())   # => ["three", "two", "one"]


# 用values获得所有的值。跟keys一样，要用list包起来，顺序也可能不同。
list(filled_dict.values())   # => [3, 2, 1]


# 用in测试一个字典是否包含一个键
"one" in filled_dict   # => True
1 in filled_dict   # => False

# 访问不存在的键会导致KeyError
filled_dict["four"]   # KeyError

# 用get来避免KeyError
filled_dict.get("one")   # => 1
filled_dict.get("four")   # => None
# 当键不存在的时候get方法可以返回默认值
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)   # => 4

# setdefault方法只有当键不存在的时候插入新值
filled_dict.setdefault("five", 5)  # filled_dict["five"]设为5
filled_dict.setdefault("five", 6)  # filled_dict["five"]还是5

# 字典赋值
filled_dict.update({"four":4}) #=> {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4  # 另一种赋值方法

# 用del删除
del filled_dict["one"]  # 从filled_dict中把one删除


# 用set表达集合
empty_set = set()
# 初始化一个集合，语法跟字典相似。
some_set = {1, 1, 2, 2, 3, 4}   # some_set现在是{1, 2, 3, 4}

# 可以把集合赋值于变量
filled_set = some_set

# 为集合添加元素
filled_set.add(5)   # filled_set现在是{1, 2, 3, 4, 5}

# & 取交集
other_set = {3, 4, 5, 6}
filled_set & other_set   # => {3, 4, 5}

# | 取并集
filled_set | other_set   # => {1, 2, 3, 4, 5, 6}

# - 取补集
{1, 2, 3, 4} - {2, 3, 5}   # => {1, 4}

# in 测试集合是否包含元素
2 in filled_set   # => True
10 in filled_set   # => False


####################################################
## 3. 流程控制和迭代器
####################################################

# 先随便定义一个变量
some_var = 5

# 这是个if语句。注意缩进在Python里是有意义的
# 印出"some_var比10小"
if some_var > 10:
    print("some_var比10大")
elif some_var < 10:    # elif句是可选的
    print("some_var比10小")
else:                  # else也是可选的
    print("some_var就是10")


"""
用for循环语句遍历列表
打印:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    print("{} is a mammal".format(animal))

"""
"range(number)"返回数字列表从0到给的数字
打印:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
while循环直到条件不满足
打印:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # x = x + 1 的简写

# 用try/except块处理异常状况
try:
    # 用raise抛出异常
    raise IndexError("This is an index error")
except IndexError as e:
    pass    # pass是无操作，但是应该在这里处理错误
except (TypeError, NameError):
    pass    # 可以同时处理不同类的错误
else:   # else语句是可选的，必须在所有的except之后
    print("All good!")   # 只有当try运行完没有错误的时候这句才会运行


# Python提供一个叫做可迭代(iterable)的基本抽象。一个可迭代对象是可以被当作序列
# 的对象。比如说上面range返回的对象就是可迭代的。

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # => range(1,10) 是一个实现可迭代接口的对象

# 可迭代对象可以遍历
for i in our_iterable:
    print(i)    # 打印 one, two, three

# 但是不可以随机访问
our_iterable[1]  # 抛出TypeError

# 可迭代对象知道怎么生成迭代器
our_iterator = iter(our_iterable)

# 迭代器是一个可以记住遍历的位置的对象
# 用__next__可以取得下一个元素
our_iterator.__next__()  #=> "one"

# 再一次调取__next__时会记得位置
our_iterator.__next__()  #=> "two"
our_iterator.__next__()  #=> "three"

# 当迭代器所有元素都取出后，会抛出StopIteration
our_iterator.__next__() # 抛出StopIteration

# 可以用list一次取出迭代器所有的元素
list(filled_dict.keys())  #=> Returns ["one", "two", "three"]



####################################################
## 4. 函数
####################################################

# 用def定义新函数
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y    # 用return语句返回javascript:void(0);

# 调用函数
add(5, 6)   # => 印出"x is 5 and y is 6"并且返回11

# 也可以用关键字参数来调用函数
add(y=6, x=5)   # 关键字参数可以用任何顺序


# 我们可以定义一个可变参数函数
def varargs(*args):
    return args

varargs(1, 2, 3)   # => (1, 2, 3)


# 我们也可以定义一个关键字可变参数函数
def keyword_args(**kwargs):
    return kwargs

# 我们来看看结果是什么：
keyword_args(big="foot", loch="ness")   # => {"big": "foot", "loch": "ness"}


# 这两种可变参数可以混着用
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# 调用可变参数函数时可以做跟上面相反的，用*展开序列，用**展开字典。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)   # 相当于 foo(1, 2, 3, 4)
all_the_args(**kwargs)   # 相当于 foo(a=3, b=4)
all_the_args(*args, **kwargs)   # 相当于 foo(1, 2, 3, 4, a=3, b=4)


# 函数作用域
x = 5

def setX(num):
    # 局部作用域的x和全局域的x是不同的
    x = num # => 43
    print (x) # => 43

def setGlobalX(num):
    global x
    print (x) # => 5
    x = num # 现在全局域的x被赋值
    print (x) # => 6

setX(43)
setGlobalX(6)


# 函数在Python是一等公民
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# 也有匿名函数
(lambda x: x > 2)(3)   # => True

# 内置的高阶函数
map(add_10, [1, 2, 3])   # => [11, 12, 13]
filter(lambda x: x > 5, [3, 4, 5, 6, 7])   # => [6, 7]

# 用列表推导式可以简化映射和过滤。列表推导式的返回值是另一个列表。
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]   # => [6, 7]

####################################################
## 5. 类
####################################################


# 定义一个继承object的类
class Human(object):

    # 类属性，被所有此类的实例共用。
    species = "H. sapiens"

    # 构造方法，当实例被初始化时被调用。注意名字前后的双下划线，这是表明这个属
    # 性或方法对Python有特殊意义，但是允许用户自行定义。你自己取名时不应该用这
    # 种格式。
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

    # 实例方法，第一个参数总是self，就是这个实例对象
    def say(self, msg):
        return "{name}: {message}".format(name=self.name, message=msg)

    # 类方法，被所有此类的实例共用。第一个参数是这个类对象。
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法。调用时没有实例或类的绑定。
    @staticmethod
    def grunt():
        return "*grunt*"


# 构造一个实例
i = Human(name="Ian")
print(i.say("hi"))     # 印出 "Ian: hi"

j = Human("Joel")
print(j.say("hello"))  # 印出 "Joel: hello"

# 调用一个类方法
i.get_species()   # => "H. sapiens"

# 改一个共用的类属性
Human.species = "H. neanderthalensis"
i.get_species()   # => "H. neanderthalensis"
j.get_species()   # => "H. neanderthalensis"

# 调用静态方法
Human.grunt()   # => "*grunt*"


####################################################
## 6. 模块
####################################################

# 用import导入模块
import math
print(math.sqrt(16))  # => 4.0

# 也可以从模块中导入个别值
from math import ceil, floor
print(ceil(3.7))  # => 4.0
print(floor(3.7))   # => 3.0

# 可以导入一个模块中所有值
# 警告：不建议这么做
from math import *

# 如此缩写模块名字
import math as m
math.sqrt(16) == m.sqrt(16)   # => True

# Python模块其实就是普通的Python文件。你可以自己写，然后导入，
# 模块的名字就是文件的名字。

# 你可以这样列出一个模块里所有的值
import math
dir(math)


####################################################
## 7. 高级用法
####################################################

# 用生成器(generators)方便地写惰性运算
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# 生成器只有在需要时才计算下一个值。它们每一次循环只生成一个值，而不是把所有的
# 值全部算好。这意味着double_numbers不会生成大于15的数字。
#
# range的返回值也是一个生成器，不然一个1到900000000的列表会花很多时间和内存。
#
# 如果你想用一个Python的关键字当作变量名，可以加一个下划线来区分。
range_ = range(1, 900000000)
# 当找到一个 >=30 的结果就会停
for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break


# 装饰器(decorators)
# 这个例子中，beg装饰say
# beg会先调用say。如果返回的say_please为真，beg会改变返回的字符串。
from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please


print(say())  # Can you buy me a beer?
print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(

