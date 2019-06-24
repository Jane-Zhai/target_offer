"""
单例模式： 确保某一个类中，只有一个实例
要点：某个类中只有一个实例
      必须自行创建这个实例
      必须自行向整个系统提供这个实例

多线程 看 https://www.cnblogs.com/huchong/p/8244279.html
"""


"""
法一： 使用模块
python的模块就是天然的单例模式，模块在第一次导入时，会生成.pyc文件，第二次导入时，会直接加载.pyc文件，而不会再次执行模块代码
因此，只需把相关函数定义在一个模块中，就可以获得一个单例对象了
"""
# # singleton.py
# class Singleton(object):
#     def foo(self):
#         pass
# singleton = Singleton()
# # 将上面代码保存，使用时，直接在其他文件中导入此文件的对象，这个对象即是单例模式的对象

from singleton import singleton
my_singleton.foo()


"""
法二： 装饰器
"""
def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class MyClass(object):
    a = 1
    def __init__(self, x=0):
        self.x = x


one = MyClass3()
two = MyClass3()
two.a = 3
print(one.a)            # 3
print(id(one))          # 8842576
print(id(two))          # 8842576
print(one == two)       # True
print(one is two)       # True
one.x = 1
print(one.x)            # 1
print(two.x)            # 1


"""
法三：__new__方法
当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），实例化对象；然后再执行类的__init__方法，对这个对象进行初始化
"""
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):  # hasattr() 函数用于判断对象是否包含对应的属性。
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = Myclass()
two = Myclass()
print(id(one))
print(id(two))
print(one == two)       # True
print(one is two)       # True
two.a = 3
print(one.a)    # 3


'''
法四：共享属性；所谓单例就是所有引用（实例、对象）拥有相同的的状态（属性）和行为（方法）
同一个类的所有实例天然拥有相同的行为（方法）
只需要保证一个类的所有实例具有相同的状态（属性）即可
所有实例共享属性的最简单方法就是__dict__属性指向（引用）同一个字典（dict）
'''
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob
class MyClass2(Borg):
    a = 1
one = MyClass2()
two = MyClass2()
two.a = 3
print(one.a)
# one 和 two 是两个不同的对象，id，==，is对比结果可以看出
print(id(one))          # 18410480
print(id(two))          # 18410512
print(one == two)       # False
print(one is two)       # False
# 但是one和two具有相同的（同一个）__dict__属性
print(id(one.__dict__)) # 14194768
print(id(two.__dict__)) # 14194768
