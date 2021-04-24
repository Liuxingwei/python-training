# PYTHON 速览

## 凡例

代码有三类：

一类为 python 文件，在代码前有文件名，文件均可在当前文件夹内找到。

一类为 python 交互脚本，形如：

```python
>>> a = 3 + 2
>>> print(a)
5
```
其中 >>> 后面是输入的脚本，无 >>> 前缀的是脚本的输出

一类为 shell 脚本，形如：

```shell
$ python -c "import huhuhu"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'huhuhu'
```

其中，$ 后面是输入的命令，无 $ 前缀的是命令的输出

## 零、Hello, World!

编写 hello.py 文件，内容：

```python
#!/usr/bin/env python
#encoding:utf8
string = "Hello, world!"
print(string)
```

在命令行输入命令：

```shell
$ python hello.py
```

输出结果：

```shell
Hello, world!
```

1. 脚本语言，无需经过单独的编译步骤，直接通过解释器命令执行
2. 无需 main() 函数，直接顺序执行语句
3. 变量无需定义类型（变量无固定类型）
4. 语句基本以行为单位，不需要使用分号（可以使用分号，在同一行上有两条以上语句时有作用）
5. 语句块以冒号、缩进为标志，不使用大括号；缩进只要宽度一致即可，推荐以四个空格为单位
6. #!/usr/bin/env python 在linux下，可以在将文件设置为可运行时，直接运行文件，将调用系统环境的python运行本文件代码
7. #encoding:utf8 指明文件编码，python3下默认为utf8，如果文件为utf8编码，可不写
8. 注释以 # 开头
9. 区分大小写

## 一、安装

推荐 Anaconda

anacoda 升级：

1. conda update conda
2. conda update anaconda
3. conda update python

## 二、集成开发环境

推荐：

1. PyCharm
2. Visual Studio Code

## 三、命令行

1. 操作系统命令行：
    1. Linux Terminal
    2. Windows cmd
2. 开发环境命令行：
    1. PyCharm：
        1. Terminal
        2. Python Terminal
    2. Visual Studio Code
        1. Terminal
        2. Jupyter Terminal: interactive window

## 四、虚拟环境

1. 虚拟环境：从系统 Python 环境衍生，并与其他（包括系统） Python 环境隔离的 Python 运行环境
2. 好处：相互隔离、可以有不同的库、不同版本的库，可迁移

### 创建虚拟环境

```shell
$ python -m venv --system-site-package /path/to/new/virtual/environment
```

--system-site-package 参数的作用是允许虚拟环境访问原始环境的库。虚拟环境的安装命令将包安装在虚拟环境中。在 Import 包时的优先级顺序为 当前路径、虚拟环境包路径、原始环境包路径。

激活虚拟环境：

命令行激活： 
```shell
$ /path/to/new/virtual/environment/bin/activate
```

### 迁移环境

1. 导出包列表：

```shell
$ pip freeze --local > requirements.txt
```

2. 下载包（新环境不能上网时需此步骤）：

```shell
$ pip download -r requirements.txt
```

3. 创建新环境

```shell
$ python -m venv --system-site-package /path/to/new/virtual/environment
```

4. 安装包

```shell
# 如果可以上网，复制requirements.txt

$ pip install -r requirements.txt

# 如果不能上网，复制下载的安装文件和requirements.txt，在安装文件所在文件夹执行

$ pip install --no-index --find-index=. -r requirements.txt 
```

### 在 IDE 中选用虚拟环境

1. VSCode：Ctrl+Shift+P，输入python，选择 Python: Select Python Interpreter，选择前面步骤创建的虚拟环境。Ctrl+Shift+^ 打开 Terminal，输入 exit，重新打开 Terminal，看到 (venv) ...
2. PyCharm：Settings > Project: xxxxxx > Python Interpreter > Python Interpreter 下拉 > Show all ...

## 五、数据类型及相关运算符、表达式

0. 一切皆为对象

    因此，**变量均为引用**

1. 整数类型

    //（整除）、%（求余）、\*\*（乘方）、有增强型赋值（+=、*=）...

    没有自增、自减，

    函数：

    int(param)： 创建一个值为 param 的整数对象

    divmod()：返回一个由整除的商和余数构成的元组

...


2. 布尔类型

    True(1) False(0) 

    == 相等判断

    函数：

    bool(param)：创建一个 bool 对象，参数为整数、浮点数，则等于0时为假值，否则为真值；参数为字符串，空串为假值，否则为真值；其它对象，则调用对象的__bool__()方法

3. 浮点数

    支持整除、求余

    函数：

    float(param)：创建一个值为 param 的浮点数对象

    decimal类，精确数字，decimal.Decimal(param)，参数必须是整数或字符串，不能是浮点数


## 六、列表、元组、字符串、字典

1. 序列
    1. 列表
    2. 元组
2. 字符串

    1. 定界符

        定界符有长短之分，短格式定界符为单引号或双引号

        长格式定界符为三分号（单双均可）,长格式字符串可以换行

    2. 转义

        \ 为转义字符串标志

    3. 原始字符串

        在字符串常量前缀 r 即为原始字符串，其中的 \ 不再是转义标志

            r'abc\n3'

    4. 字符串连接

        字符串连接运算符 +

        连续的多个字符串常量自动连接

    5. 字符串序列

        1. 不可变

        2. 长度

            len(str)函数

        3. 索引

            使用数字索引获取指定位置的字符。

            从前向后数，第一个元素的索引为 0，最后一个的索引为 len(str) - 1。

            从后向前数，最后一个元素的索引为-1，第一个元素的索引为 - len(str)。

        4. 切片

            分号分割的两个索引，分别为切片的起始索引（包含在切片中）和切片后余下元素的第一个元素的索引（不包含在切片中），如果要切到最后一个，则第二个索引可以为len(str)

                >>> 'hello'[2:4]
                'll'
                >>> 'hello'[2:5]
                'llo'

            可以使用负数索引。

            只能从前向后截，即后一个索引必须位于前一索引之后，否则即为容串

                >>> 'hello'[-3:0]
                ''

            可以省略，省略第一个索引，则从第一个元素开始切片，相当于索引 0 或 -len(str)；如果省略第二个索引，则一直切到最后一个元素，相当于 len(str)。

            如果两个索引都省略，即可复制字符串。
        
        5. 乘法

            字符串可以与整数相乘，以得到重复多次的字符串

        6. in

            in 运算符，用于判断一个字符串是否在包含在另一个字符串中。

                >>> 'a' in 'abc'
                True
                >>> 'bc' in 'abcd'
                True
                >>> 'bc' in 'abcd'
                False

        7. 解包

            实用意义不大，需注意字符串是可以解包的，可能会引发非期望的结果

        8. max()、min()

            获取字符串中最大的字符：max(string)

            获取字符串中最小的字符：min(string)

        9. str(param)

            创建值为param的字符串。

        10. 格式化（变量置换）

            1. 旧式语法：

                与 C 语言的格式化输出语法类似，使用 % 作为点位符和运算符
                    name = "张三"
                    age = 32
                    height = 1.83
                    "姓名：%10s；年龄：%3i；身高：%4.2f" % (name, age, height)

            2. format() 函数

                原字符串使用{}做占位符（如需在字符串中使用花括号，使用连续的两个花括号 {{ 和 }} ），调用字符串对象的format()函数，完成变量置换

                第一种，使用位置参数的位置序号点位

                    name = "张三"
                    age = 32
                    height = 1.83
                    "姓名：{2}；年龄：{1}；身高：{0}".format(height, age, name)

                第二种，使用关键字参数的键点位

                    name = "张三"
                    age = 32
                    height = 1.83
                    "姓名：{a}；年龄：{b}；身高：{c}".format(b=age, a=name, c=height)
                
                以上两种方式，参数均可重复使用

                第三种，无占位标志

                    name = "张三"
                    age = 32
                    height = 1.83
                    "姓名：{}；年龄：{}；身高：{}".format(name, age, height)

                第三种方式，仅按参数默认顺序，且不能重复使用参数

                如果参数是对象，还可以引用其属性；如果参数是序列或字典，还可以通过索引引用其元素。

                    import math
                    "{.pi}".format(math)
                    "{0[2]}".format((1, 3, 9))
                    "name[1]".format(name="古天乐")

                格式指令：格式指令在占位标志之后，与占位标志以冒号分隔，无占位标志时直接以冒号开始，由八部分构成，依顺序依次是：
                
                1. 填充字符：

                    在指定了宽度时，如果给定的值长度不足，用于填补空缺的字符，默认为空

                2. 对齐标志：

                    < 左对齐，左侧用填充字符补齐

                    \> 右对齐，右侧用填充字符补齐

                    ^ 居中，两侧用填充字符补齐

                    = 符号和数字间用填充字符补齐

                3. 符号标志：

                    - 表示如果为负数，前导符号为负号

                    + 表示如果为负数，前导符号为负号，如果为正数或 0，前导符号为正号

                    空格 表示如果为负数，前导符号为负号，如果为正数或 0,前导符号为空格

                4. 进制标志：

                    \# 对于二进制、八进制、十六进制的整数，指定#号将显示进制标志

                5. 宽度：整数，指定数值所占宽度

                6. 千位分隔标志：

                    逗号：整数部分超过三位的十进制数值，将为整数部分添加千位分隔符（逗号）

                7. 小数部分的精度：
                
                    .n：一个句点带一个整数，用于指定十进制浮点数的小数部分精度

                8. 转换标志：

                    !b|o|d|x|X|e|E|f|F|g|n|G|%|s

            一个两次format的示例，string_format.py：

                width = int(input('Please enter width: '))

                fruits = [
                    ['Apples', 0.4],
                    ['Pears', 0.5],
                    ['Cantaloupes', 1.92],
                    ['Dired Apricots (16 oz.)', 8],
                    ['Prunes (4 lbs.)', 12]
                ]

                price_width = 10
                item_width = width - price_width

                header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
                fmt = '{{0[0]:{}}}{{0[1]:>{}.2f}}'.format(item_width, price_width)

                print('=' * width)

                print(header_fmt.format('Item', 'Price'))

                print('-' * width)

                for fruit in fruits:
                    print(fmt.format(fruit))

                print('=' * width)

        11. 字符串的常用方法

            | 方法 | 描述 |
            |:----|:----|
            | s.capitalize() | 返回字符串s首字母大写的副本 |
            | s.center(width, char="") | 字符串占据 width 宽度，两侧以 char 填充，默认为空格|
            | s.count(t[, start[, end]]) | 返回字符串 s （或其切片）中，字符串 t 出现的次数 |
            | s.encode(encoding, err='strict') | 返回指定编码的 bytes 对象，可选参数用于指定超出指定字符集的字符的处理方式 |
            | s.endswith(x[, start[, end]]) | 如果字符串 s （或其分片）以指定字符串结尾，返回 True |
            | s.expendtabs(size) | 返回字符串 s 的副本，其中的制表符使用指定数量的空格替换 | 
            | s.find(t[, start[, end]]) | 返回字符串 s （或其分片）中，字符串 t 首次出现的位置（自左侧搜索），如果没找到，返回 -1 |
            | s.format(...) | 见字符串格式化 |
            | s.index(t[, start[, end]]) | 返回字符串 s （或其分片）中，字符串 t 首次出现的位置（自左侧搜索），如果没找到，抛出 ValueError 异常 |
            | s.isalnum() | 判断字符串 s 是否全部由字母数字组成 |
            | s.isalpha() | 判断字符串 s 是否全部由字母组成 |
            | s.isdecimal() | 判断字符串 s 是否全部由 Unicode数字，全角数字（双字节） 组成 |
            | s.isdigit() | 判断字符串 s 是否全部由 Unicode数字，全角数字（双字节） 组成 |
            | s.isidentifier() | 判断字符串 s 是否为有效标识 |
            | s.islower() | 如果字符串 s 中至少有一个小写字符，并且所有可小写的字符均为小写，返回 True |
            | s.isnumeric() | 判断字符串 s 是否全部由 Unicode数字，全角数字（双字节），罗马数字，汉字数字 组成|
            | s.isprintable() | 判断字符串 s 是否全部由可打印字符组成 |
            | s.isspace() | 判断字符串 s 是否全部由空白字符组成 |
            | s.istitle() | 判断字符串 s 是否全部由首字母大写的单词组成 |
            | s.isupper() | 如果字符串 s 中至少有一个大写字符，并且所有可大写的字符均为大写，返回 True |
            | s.join(sql) | 以字符串 s 作为分隔符，将 seq 中所有项合并为一个新的字符串 |
            | s.ljust(width, char='') | 返回一个原字符串左对齐，并使用字符 char 填充至长度 width 的新字符串 |
            | s.lower() | 返回字符串 s 中所有可小写字母小写的结果 |
            | s.ltrip(char='') | 返回截掉 s 开头处被包含在字符串 char 中的字符的结果 |
            | s.partition(t) | 从字符串 t 出现的第一个位置起,把字符串 s 分成一个3元素的元组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string |
            | s.replace(t, u, n) | 把字符串 s 中的 字符串 t 替换成字符串 u，如果指定了 n，则最多替换 n 次 |
            | s.rfind(t[, start[, end]]) | 类似于 s.find() ，返回字符串 s （或其分片）中，字符串 t 首次出现的位置（自右侧搜索），如果没找到，返回 -1 |
            | s.rindex(t[, start[, end]]) | 返回字符串 s （或其分片）中，字符串 t 首次出现的位置（自右侧搜索），如果没找到，抛出 ValueError 异常 |
            | s.rjust(width, char='') | 返回一个原字符串右对齐，并使用字符 char 填充至长度 width 的新字符串 |
            | s.rpartition(t) | 从字符串 t 出现的最后一个位置起，把字符串 s 分成一个3元素的元组 (string_post_str,str,string_pre_str),如果 string 中不包含str 则 string_pre_str == string |
            | s.rstrip(tchar='') | 返回截掉 s 结尾处被包含在字符串 char 中的字符的结果 |
            | s.split(t, n) | 以字符串 s 为分割符，分割字符串 t，如果 s 为空，则以空白为分割符，如果指定了 n，则最多分割 n 次 |
            | s.splitlines(f=False) | 以行终结符为分割符，分割字符串 s，如果参数为 True，保留行终结符，如果参数 False，删除行终结符 |
            | s.startswith(x[, start[, end]]) | 如果字符串 s （或其分片）以指定字符串开头，返回 True |
            | s.swapcase() | 返回将字符串 s 中的字符翻转大小写的结果 |
            | s.title() | 返回的字符串 s 中所有单词都是以大写开始，其余字母均为小写的结果 |
            | s.upper() | 返回字符串 s 中所有可大写字母大写的结果 |
            | s.zfill(w) | 返回长度为 w 的字符串，原字符串 string 右对齐，前面填充0

3. 字典

## 七、流程控制

1. 分支
2. 循环
3. 简单推导
4. 异常

## 八、函数

1. 基本格式
2. 位置参数和关键字参数
3. 收集参数和分配参数
4. lambda表达式
5. doc
6. 嵌套函数与闭包
7. 修饰器

## 九、类与对象

1. 类、属性、方法
2. 特性
3. 继承与多态：多继承
4. 静态方法
5. 类方法
6. 构造函数与初始化函数
7. 抽象类
8. 接口和内省
9. __dict__和__slots__

## 十、迭代器和生成器

1. 迭代器
    1. 可迭代对象
    2. 迭代器
2. 生成器

## 十一、模块和包

1. 模块
2. 包
3. 标准库
4. 导入语句综述
5. 模块查找
6. 自定义模块

## 十二、调试和测试

1. 断点调试
2. 单元测试

## 十三、进程、线程、协程

1. 进程
2. 线程
3. 协程

## 十四、程序打包

1. Setuptools
2. 打包
3. py2exe 和 py2app

## 十五、其它

1. 网络编程
2. Web
3. 数据库
4. 正则表达式

## 十六、应用

1. 运维脚本
2. Web
3. 爬虫
4. 数据挖掘和数据可视化
5. 机器学习