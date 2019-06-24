[TOC]

## inspect模块——获取函数上下文信息

- 需要将一些调试信息集中在函数中打印
- inspect.stack()
  - 第一列是对象名，第二列是当前脚本文件名，第三列是行数，第四列是函数名，第五列是具体执行的程序。
  - 第一行是当前函数，第二行是父级函数，。。以此往上钻取，基本上只有前两三行有用。

```python
def debug():
    import inspect
    caller_name = inspect.stack()[1][3]
    print "[DEBUG]: enter {}()".format(caller_name)   

def say_goodbye():
    debug()
    print "goodbye!"

if __name__ == '__main__':
    say_goodbye()
```

问题：每个业务函数里都要调用一下`debug()`函数，引入 装饰器

## 装饰器——为已经存在的函数或对象添加额外的功能

https://www.cnblogs.com/cicaday/p/python-decorator.html#996603658

- 最简单的装饰器。

  ```python
  def debug(func):
      def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
          print "[DEBUG]: enter {}()".format(func.__name__)
          print 'Prepare and say...',
          return func(*args, **kwargs)
      return wrapper  # 返回

  @debug
  def say(something):
      print "hello {}!".format(something)
  ```

- 高级一点的装饰器

  - 带参数的装饰器，不仅仅能在进入某个函数后打出log信息，还需指定log的级别

  ```python
  def logging(level):
      def wrapper(func):
          def inner_wrapper(*args, **kwargs):
              print "[{level}]: enter function {func}()".format(
                  level=level,
                  func=func.__name__)
              return func(*args, **kwargs)
          return inner_wrapper
      return wrapper

  @logging(level='INFO')
  def say(something):
      print "say {}!".format(something)

  # 如果没有使用@语法，等同于
  # say = logging(level='INFO')(say)

  @logging(level='DEBUG')
  def do(something):
      print "do {}...".format(something)

  if __name__ == '__main__':
      say('hello')
      do("my work")
  ```

  - 基于类实现的装饰器
    - 装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。在Python中一般callable对象都是函数，但也有例外。只要某个对象重载了`__call__()`方法，那么这个对象就是callable的。
    - 我们可以让类的构造函数`__init__()`接受一个函数，然后重载`__call__()`并返回一个函数，也可以达到装饰器函数的效果。

  ```python
  class logging(object):
      def __init__(self, func):
          self.func = func

      def __call__(self, *args, **kwargs):
          print "[DEBUG]: enter function {func}()".format(
              func=self.func.__name__)
          return self.func(*args, **kwargs)
  @logging
  def say(something):
      print "say {}!".format(something)
  ```

  - 带参数的类装饰器

  ```python
  class logging(object):
      def __init__(self, level='INFO'):
          self.level = level
          
      def __call__(self, func): # 接受函数
          def wrapper(*args, **kwargs):
              print "[{level}]: enter function {func}()".format(
                  level=self.level,
                  func=func.__name__)
              func(*args, **kwargs)
          return wrapper  #返回函数

  @logging(level='INFO')
  def say(something):
      print "say {}!".format(something)
  ```

  - 内置的装饰器

    - @property

    ```python
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value
        
    def delx(self):
       del self._x

    # create a property
    x = property(getx, setx, delx, "I am doc for x property")
    ```

    ```python
    @property
    def x(self): ...

    # 等同于

    def x(self): ...
    x = property(x)
    ```

    - @staticmethod, @classmethod

    ```python
    class Foo(object):

        @staticmethod
        def bar():
            pass
        
        # 等同于 bar = staticmethod(bar)
    ```

## 单例——一个类中只有一个实例存在

## 算法
- 排序和查找
    - 二分查找  排序（或部分排序）数组中，查找某数字，或统计某个数字出现次数
    - 并归排序，快速排序

- 二维数组（迷宫，棋盘，走格子等）搜索路径
    - 回溯法————递归/栈

- 最优解，可分为多个子问题————动态规划
    - 自下而上的循环，即把子问题的最优解算出来并用数组保存下来，基于子问题的解计算大问题的解
    - 存在特殊选择，采用该特殊选择一定得到最优解————贪婪算法
    
- 位运算

##代码质量
- 规范性：布局，命名
- 完整性：功能、边界、负面