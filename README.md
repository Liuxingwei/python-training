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

    序列类似于其它语言的数组，相对于静态类型语言，序列的不同之处是它的元素类型不限。

    1. 元组

        元组（`tuple`）相当于不可变数组。python 的很多函数都会返回元组。

        元组的定义有两种方法，其一为使用 `tuple([seq])` 方法，它会将 seq 置换为元组，seq 参数必须是一个序列，如果不提供参数，则创建一个空元组。

        另一个定义方法是字面量，用逗号间隔的值，就构成了元组。一些情况下，需要在元组的外面加上括号：比如 空元组、使用元组做函数参数、允许使用逗主但实际是想使用元组的情况、以及仅包含一个元素的元组。对于只包含一个元素的元组，还需要在唯一元素的后面加逗号，这是为了区别加了括号的值，因为 (45) 和 45 是一样的。

            seq = 1, 2, 3, 4, 5

            seq = (1, 2, 3, 4, 5)

            seq = tuple((1, 2))

            seq = ()

            seq = tuple()

            seq = (4,) #注意它与 seq = (4) 的区别

        元组可以嵌套定义

            seq = 1, 2, (3, 4), 5

        元组适用的操作有：

        1. 相加

            使用 + 将两个序列拼接成一个新元组。
        
        2. 长度

            计算序列的长度使用 `len(seq)`

        3. 索引

            使用数字索引获取序列中指定位置的元素。

            从前向后数，第一个元素的索引为 0，最后一个元素的索引为 len(str) - 1。

            从后向前数，最后一个元素的索引为-1，第一个元素的索引为 - len(str)。

        4. 切片

            冒号分割的两个索引和步长，分别为切片的起始索引（包含在切片中）和切片后余下部分的的第一个元素的索引（不包含在切片中），如果要切到最后一个，则第二个索引可以为len(str)。第三部分为步距，默认为 1,可以为负。

                >>> (1, 2, 3, 4, 5)[2:4]
                (3, 4)
                >>> (1, 2, 3, 4, 5)[2:5]
                (3, 4, 5)

            可以使用负数索引。

            默认情况下，只能从前向后截，即后一个索引必须位于前一索引之后，否则结果为空

                >>> (1, 2, 3, 4, 5)[-3:0]
                ()

            可以省略，省略第一个索引，则从第一个元素开始切片，相当于索引 0 或 -len(str)；如果省略第二个索引，则一直切到最后一个元素，相当于 len(str)。

            如果两个索引都省略，即可复制序列。

        5. 乘法

            序列可以与整数相乘，以得到重复多次的序列

        6. in 运算

            in 运算符，用于判断一个值是否在包含在序列中。

                >>> 'a' in ('a', 'b', 'c')
                True
                >>> 'e' in  ('a', 'b', 'c')
                True
                >>> 3, 4 in (1, 2, (3, 4), 5)
                False
                >>> (3, 4 ) in (1, 2, (3, 4), 5)
                True

        7. 解包

            将序列同时赋给多个变量，称为序列解包。

                >>> x, y, z = 1, 2, 3
                >>> print(x, y, z)
                1 2 3

            一个很小但很方便的应用：交换变量的值

                >>> x, y = 1, 2
                >>> y, x = x, y
                >>> print(x, y)
                2 1

            当函数返回元组时，可以使用序列解包，轻松将返回值赋给多个变量

            序列解包时，需要左侧的变量数据与序列的元素数量一致，否则会出错

        8. 收集和解包 *

            在将序列赋给多个变量时，序列个数多于变量个数，在最后一个变量前加 *，剩余的序列元素将以元组的形式赋给最后一个变量，最后一个变量的类型与序列的类型一致

                >>> x, *y = 1, 2, 3
                >>> print(x)
                1
                >>> print(y)
                2 3
                >>> isinstance(y, tuple)
                True

                >>> x, *y = [1, 2, 3]
                >>> print(x)
                1
                >>> print(y)
                2 3
                >>> isinstance(y, tuple)
                False
                >>> ininstance(y, list)
                True

            * 号在某些情况下，还有解包的作用：

                >>> t1 = (3, 4)
                >>> t2 = (1, 2, *t1, 5, 6)
                >>> print(t2)
                (1, 2, 3, 4, 5, 6)

        9. max(seq, key=None)、min(seq, key=None)

            获取序列中值最大的元素： `max(seq, key=None)`，`key` 参数接受一个函数，如果提供了 `key` 参数，则对序列中的每个元素调用 `key` 指向的函数，返回 `key(item)` 值最大的元素。

            获取序列中值最小的元素：`min(seq, key=None)`，`key` 参数接受一个函数，如果提供了 `key` 参数，则对序列中的每个元素调用 `key` 指向的函数，返回 `key(item)` 值最小的元素。



        10. 元组的方法

            元组的方法属于序列的通用方法，几乎所有的序列都可使用这些方法：

            | 方法 | 描述 |
            |----|----|
            | l.count(param) | 计算 param 在序列 l 中出现的次数 |
            | l.index(x[, start[, end]]) | 返回 x 在序列 l （或其切片）中最左边出现的索引值，如果 x 不存在，抛出 ValueError 异常 |

    2. 命名元组

        命名元组不是内置类型，是由 `collections` 模块实现的。其特殊是可以根据名称引用元组的项。

        命名元组先要用如下方法定义：

            import collections
            People = collections.namedtuple('MyTuple', 'name sex age')

        其中第一个参数是自定义元组数据类型的标志，第二个参数是用空白间隔的元组元素名称列表。此方法的返回值，即为一个命名元组。

        定义了命名元组之后，就可以使用它定义命名元组变量了：

            tina = People('lixue', 'male', 18)

        命名元组元素的读取方法有两种，作为 `tuple` 类的子类，可以像元组一样使用索引引用，还可以象访问对象属性的一样：

            >>> tina[0]
            'lixue'
            >>> tina.name
            'lixue' 

    3. 列表

        列表类似于可变数组。

        定义有两种方法，其一为使用 `list([seq])` 方法，它会将 seq 置换为元组，seq 参数必须是一个序列，如果不提供参数，则创建空列表。

        另一个定义方法是字面量，用空方括号或方括号内逗号间隔值，就构成了列表。

            l = [1, 2, 3, 4, 5]

            seq = []

            seq = list((4,))

        序列可以嵌套定义

            seq = 1, [2, (3, 4), 5], 9

        所有的元组操作均可用于列表，除此而外，因为列表可以修改，还有如下适用的操作：

        1. 修改元素的值

                >>> l = [3, 4, 5]
                >>> l[1] = 9
                >>> print(l)
                [3, 9, 5]

        2. 删除元素

            del 指定（不是函数）

                >>> l = [3, 4, 5]
                >>> del l[2]
                >>> print(l)
                [3, 4]

        3. 给切片赋值

            给切片赋值可以实现将切片替换为不同长度的序列，可以实现删除切片，插入序列

                >>> l = [3, 4, 5. 6, 7, 8]
                >>> l[1:3] = [9, 10, 11]
                >>> print(l)
                [3, 9, 10, 11, 6, 7, 8]
                >>> l[4:6] = [2, 1]
                >>> print(l)
                [3, 9, 10, 11, 2, 1]
                >>> l[3:4] = []
                >>> print(l)
                [3, 9, 10, 2, 1]
                >>> l[1:1] = [6, 5]
                >>> print(l)
                [3, 6, 5, 9, 10, 2, 1]
        
        列表的常用方法是可变序列的通用方法

        | 方法 | 描述 | 
        |----|----|
        | l.append(param) | 将 param 追加到列表 l 末尾 |
        | l.clear() | 清空列表 |
        | l.extend(m) | 将 m 逐项添加到 l 的末尾 |
        | l.insert(i, x) | 在索引位置 i 处将数据项 x 插入列表 l |
        | l.pop(i = (len(l) - 1)) | 返回并移除列表索引位置 i 的元素 |
        | l.remove(x) | 移除列表 l 中最左边出现的数据项 x，如果 x 不在 l 中，抛出 ValueError 异常 |
        | l.reverse() | 翻转列表 l 的元素 |
        | l.sort(key=None, reverse=False) | 对列表进行排序，如果提供了 key 函数，对列表的每一项调用函数，并按返回结果排序；如果 reverse 设置为 True，则以倒序排序 |

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

    字典是映射类型，即键值对。

    定义列表有两种方法，一是使用 `dict([param])` 方法，一种是使用字面量。

    先简后繁，先说字面量。字典字面量是用 `{}`，空的花括号定义了空的字典，非空字典语法如下：

        {key1: value1, key2: value2....}

    不可变类型均可用做字典的键：int、float、str、tuple等等。

    字典的值可以为任意类型。

    需要注意的是，不带有键值对格式的花括号是定义集合（set）的。

    使用 `dict([param])` 语法，参数形式比较多：

    1. 不带参数

        创建空字典。

        dict()

    2. 映射类型

        映射类型的参数，直接返回以该参数为基础的字典。

            dict({"id": 1948, "name": "Washer", "size": 3})

    3. 嵌套序列

        序列的每个元素都是由两个值的序列组成的，其中的第一个值被用作键，第二个值被用作值。

            dict([("id", 1948), ("name", "Washer"), ("size", 3))])

    4. 命名参数

        参数名用途键，参数值用途值。

            dict(id=1948, name="Washer", size=3)

    字典的常用操作：

    1. 获取字典的长度：

            >>> len({"k1": "v1", "k2": "v2"})
            2

    2. 获取指定键的值：

            >>> d = {"k1": "v1", "k2": "v2"}
            >>> d["k1"]
            'v1'

    3. 给指定的键赋值：

            >>> d = {"k1": "v1", "k2": "v2"}
            >>> d["k2"] = 30
            >>> d["k2"]
            30

        还可以通过给不存在的键赋值，来为字典添加元素：

            >>> d["k3"] = {1, 2, 3}
            >>> d
            {'k1': 'v1', 'k2': 30, 'k3': {1, 2, 3}}

    4. 删除指定键

            >>> d = {"k1": "v1", "k2": "v2"}
            >>> del d["k2"]
            >>> d
            {'k1': 'v1'}

    5. 判断指定键是否存在

        注意这一运算与列表的不同。

            >>> d = {"k1": "v1", "k2": "v2"}
            >>> "k1" in d
            True
            >>> "v2" in d
            False

    6. 字典解包 **

        字典解包的作用类似于序列解包，示例如下：

            >>> d1 = {'sex': '女', 'length': 1.72}
            >>> d2 = {'name': '花木梅', **d1, 'weight': 100}
            >>> print(d2)
            {'name': '花木梅', 'sex': '女', 'length': 1.72, 'weight': 100}
   
    7. 字典与字符串格式化方法：`format_map(d)`

        使用字符串的 `format_map(d)` 方法，并传递给它一个字典作为参数，可以用字典中存在的键作为字符串中的占位符。

            >>> phonebook = {'Jason': '8425', 'David': '7833', 'Ketty': '9622'}
            >>> "Jason's phone number is {Jason}.".format_map(phonebook)

    字典方法

    | 方法 | 描述 |
    |----|----|
    | d.clear() | 清空字典 d |
    | d.copy() | 生成字典 d 的浅拷贝 |
    | d.fromkeys(key[, value]) | 生成一个新字典，如果参数 p 是序列类型，则用 p 的值做键，如果提供了第二个参数，则以第二个参数作为所有键的值，否则，所有键的值均为 None；如果参数 p 是字典，则用 p 的键做键，如果提供了第二个参数，则以第二个参数作为所有键的值，否则，所有键的值均为 None |
    | d.get(key[, default]) | 获取键 key 的值。与 d[key] 的不同是，在键 key 不存在时，d.get(key) 方法返回 None（或者在提供了第二个套数时，返回第二个参数的值），而 d[key] 则会抛出异常。 |
    | d.items() | 返回字典 d 所有键值对构成的视图，视图的值类似于列表，其每个成员都是一个由键、值构成的元组 `{'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}.items()` 的结果是 `dict_items([('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')])` |
    | d.keys() | 返回一个由字典的键组成的视图 |
    | d.pop(key) | 返回指定键的值，并从字典中删除键值对 |
    | d.popitem() | 随机返回一个键值对，并从字典中删除它。返回结果为键和值构成的元组 |
    | d.setdefault(key, default) | 获取 key 的值，如果 key 不存在，则在字典中插入 key，其值为 default |
    | d.update(param) | 使用与 dict 相同的规则，将参数 param 转化为字典，使用该字典更新字典 d，向 d 中插入不存在的键值对，更新已存在的键值对，不改变 param 中不存在的键值对。 |
    | d.values() | 返回字典 d 中所有值的视图 |

    关于字典视图：

    `d.items()`、`d.items()` 和 `d.items()` 方法返回的都是字典的视图，它们的特点是本身不可改变，但会随字典的变化而变化。

        >>> d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0} 4 >>> d.items()
        dict_items([('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')])
        >>> d['spam'] = 1
        >>> ('spam', 0) in it 
        False
        >>> d['spam'] = 0
        >>> ('spam', 0) in it 
        True

4. 集合（set）

    集合是 0 个或多个对象引用的无序组合，其元素必须是可哈希的（有 __hash__() 方法）。所有内置的不可变数据类型都是可哈希的，如 int、float、str、tuple、namedtuple、frozenset 等；内置可变数据类型是不可哈希的，如 dict、list、set等。

    集合的初始化：
    使用 `set([param])` 函数，不带参数创建空集合，带一个 `set` 类型的参数，创建一个 `set` 的浅拷贝，其它类型的参数，则尝试将给定的参数转换为集合。
    非空集合也可以使用花括号定义，直接将用逗号间隔的元素放入一对花括号即可。**不能用空花括号定义空集合**，空花括号是定义空字典的。花括号内的元素可以是不同的类型，但不能包含键值对。

    集合不包含重复元素，向集合内添加已有元素不报错，但也没有意义。集合的这一特性可以用来去重。

    集合无序，不能像列表、元组一样用索引引用其元素。集合无键，也不能像字典一样，使用键引用其元素。

    可以迭代集合，但其顺序不可依赖。

    如果一定要使用索引引用集合，可以利用 `list(s)` 函数将其转换为列表。

    集合的常用操作：

    1. 长度：`len(x)`
    2. 判断一个元素是否在集合中：`x in s`
    3. 并集： `s | t`
    4. 差集：`s - t`
    5. 比较：`s == t`、`s != t`、`s > t`、`s >= t`、`s < t`、`s <= t`
    6. 交集：`s & t`
    7. 并集与交集的差：`s ^ t`

    集合的方法：

    | 方法 | 描述 |
    |----|----|
    | s.add(x) | 如果 s 中不存在 x，将 x 添加到 s 中 |
    | s.clear() | 清空集合 s |
    | s.copy() | 返回集合的浅拷贝 |
    | s.difference(t) | s - t |
    | s.dirrerenct_update(t) | s -= t |
    | s.discard(x) | 如果 x 存在于 s 中，就移除 x，如果没有，也不报异常 |
    | s.intersection(t) | s & t |
    | s.intersection_update(t) | s &= t|
    | s.isdisjoint(t) | 如果 s 和 t 没有相同的项，返回 True |
    | s.issubset(t) | s <= t |
    | s.issuperset(t) | s >= t |
    | s.pop() | 返回并移除一个随机元素，如果是空集，抛出 KeyError 异常 |
    | s.remove(x) | 如果 x 存在于 s 中，就移除 x，如果没有，抛出 KeyError 异常 |
    | s.symmetric_difference(t) | s ^ t |
    | s.symmetric_difference_update(t) | s ^= t |
    | s.union(t) | s | t |
    | s.update(t) | s |= t |
## 七、流程控制

1. 输入输出

    1. `input([prompt])`

        `input`函数接受键盘输入并返回输入的字符串（不包含回车）。函数的参数将作为提示信息显示在控制台上。

    2. `print(*params, sep=' ', end='\r')`

        `print`方法可以接受用逗号间隔的多个参数，这些参数类型可以不一致，输出时以 `sep` 参数指定的字符进行间隔，默认间隔符为空格。还可以指定结束符，默认为换行。

2. pass

    `pass` 是空语句，相当于类 C 语言的 ;

    `pass` 通常用于占位

3. 分支

        if boolean_expression1:
            suite1
        elif boolean_expression2:
            suite2
        ...
        elif boolean_expressionN: 
            suiteN
        else: 
            else_suite

    关于分支，只说三点和其他语言的不同：

    1. 条件表达式不需要括号
    2. 语句块用冒号和缩进标记，不使用花括号
    3. 其它语言的 else if 写作 elif

    **条件表达式：** 对于语句部分仅有一个表达式的两分支语句，可以缩减为单一的条件表达式：

        expression1 if condition else expression2

    在条件为 `True` 时条件表达式的结果为 `expression1`，相反则为 `expression2`。

4. 迭代（循环）

    1. while

            while boolean_express:
                suite1
            else: 
                suite2

        可选的 `else` 子句在没有 `break` 的循环结束时执行。
    2. for

            for var in iterable:
                suite1
            else:
                suite2

        对于 `for` 语句中的 `var`，通常指的是迭代对象的元素，**但在迭代字典时，略有不同，其值为字典的键**：

            >>> d = 1{'key1`: 'val1', 'key2': 'val2'}
            >>> for key in d:
            >>>    print(key, d[key], sep='=')
            key1=val1
            key2=val2

    3. break 和 continue

    4. 迭代工具函数

        1. `range(start, stop[, step])` 和 `range(stop)`

            `range` 函数生成可迭代的整数序列。

            `range(start, stop[, step])` 语法，是以 `start` 开始（包含 `start`），至 `stop` 结束（不包含 `stop`），`step` 为步长，步长默认为 `1`。步长可以为负值。

                >>> for i in range(0, 10):
                >>>    print(i, end=' ')
                0 1 2 3 4 5 6 7 8 9
                >>> for i in range(9, -1, -1):
                >>>    print(i, end=' ')
                9 8 7 6 5 4 3 2 1 0

            `range(stop)` 语法，以 `0` 为 `start`，步长为 `1`。

                >>> for i in range(10):
                >>>    print(i, end=' ')
                0 1 2 3 4 5 6 7 8 9

        2. 并行迭代

            `zip(...)` 函新将多个序列缝合成一个新序列，新序列的每个元素是一个由各序列相同序号的值构成的元组。

                >>> names = ['anne', 'beth', 'george', 'damon']
                >>> ages = [12, 45, 32, 102]
                >>> sexs = ['male', 'female', 'female', 'male']
                >>> for name, age, sex in zip(names, ages, sexes):
                >>>    print(name, age, sex)
                'anne' 12 'male'
                'beth' 45 'female'
                'george' 32 'female'
                'damon' 102 'male'

        3. 迭代时获取索引

            `enumerate(seq)` 函数返回一个新序列，由 `seq` 的索引和值组成的元组构成。

                >>> for index, name in enumerate(names):
                >>>    print(i, name)
                0 'anne'
                1 'beth'
                2 'george'
                3 'damon'

        4. 反向迭代

            `reversed(seq)` 返回一个倒序的新序列

        5. 排序后迭代

            `sorted(seq, key=None)` 函数返回一个排序后的新序列，如果指定了 `key`，则对每个元素调用 `key` 函数，并对结果进行排序。

5. 简单推导

    1. 列表推导：

        `[valueexpression for val1, val2... in iterable]`

        相当于：

            temp = []
            for val1, val2 in iterable:
                temp.append(valueexpression)

        并返回 `temp`。

        `[valueexpression for val1, val2... in iterable if condition]`

        相当于：

            temp = []
            for val1, val2 in iterable:
                if condition:
                    temp.append(valueexpression)

        并返回 `temp`。

    2. 集合推导：

        {valueexpression for val1, val2... in iterable if condition}

    3. 字典推导：

        {keyexpression:valueexpression for val1, val2... in iterable if condition}

6. 异常

    1. 捕获异常

            try: 
                suite
            except exception_group1 as variable1:
                except_suite1
            ...
            except exception_groupN as variableN:
                except_suite2
            else:
                else_suite
            finally:
                finally_suite

        `exception_group`：在一个 `except` 中可以捕获一种异常，也可以捕获多种异常，如果捕获多种异常，则需将用逗号分隔的多个异常类型放在括号中。

        `else` 子句在异常没有发生时执行。
        
    2. 追踪异常

        可以直接打印异常变量：

            try:
                ...
            except ValueError as e:
                print(e)

        这和打印 `e.message()` 是一样的。

        如果要打印整个异常栈，则需要使用 `trackback` 模块或 `logging` 模块：

            import trackback

            try:
                ...
            except IndexError as e:
                print(trackback.print_exc())

        或者
            
            import logging
            try:
                ...
            except IndexError as e:
                logging.exception(e)

    3. 抛出异常和异常传播

        可以使用 `raise` 语句抛出异常，有几种语法：

            raise exception

        这种语法仅使用异常类名作为表达式，输出标准异常信息

            raise exception(strs)

        这种语法的参数格式类似于 `print(strs)`，除了输出标准异常信息，还会输出参数中的文本信息

            raise

        这种语法一般用在捕获异常后又抛出的情况，可以直接抛出捕获到的异常

        前面三种语法，如果用在 `except` 子句中，则抛出的异常将作为新抛出异常的**上下文**,存储在异常堆栈中。

        如下语法可以提供自己的上下文：

            raise exception(strs) from original_exception

        如果 `original_exception` 的值为 `None`，则禁用上下文 。

    4. 自定义异常

        `python` 的自定义异常极其简单：

            class exceptionName(baseException): pass

7. `eval` 和 `exec`

    `eval` 函数用于将一个字符串作为**表达式**进行解析并执行，并返回表达式的值。

        eval(expression[, globals=None[, locals=None]])

    `expression` 参数是一个字符串表达式，其值必须是可以执行的 `python` **表达式**。如果提供了 `globals` 字典，则 `globals` 将作为被执行语句的全局命名空间（只读），如果提供了 `locals`，则 `locals` 将作为执行语句的局部命名空间（只读）。如果后两个参数均不提供，将会读取外围命名空间。
    一般第三个参数很少使用，但第二个参数用的较多，用于隔离全局命名空间。

        >>> def func():
        ...    a = 3
        ...    b = eval('a * a')
        ...    print(b)
        ...
        >>> func()
        9

        >>> def func():
        ...    a = 3
        ...    context = {'a': 5}
        ...    b = eval('a * a', context)
        ...    print(b)
        >>> func()
        25

    `exec` 函数用于将一个字符串作为语句进行解析并执行，没有返回值。

        exec(expression[, globals=None[, locals=None]])

    `expression` 参数是一个字符串表达式，其值必须是可以执行的 `python` **语句**表达式。如果提供了 `globals` 字典，则 `globals` 将作为被执行语句的全局命名空间（读写），如果提供了 `locals`，则 `locals` 将作为执行语句的局部命名空间（读写）。如果后两个参数均不提供，将会读取外围命名空间。
    一般第三个参数很少使用，但第二个参数用的较多，用于保护全局命名空间。

        >>> def func():
        ...    a = 3
        ...    exec('a += 1')
        ...    print(a)
        ...
        >>> func()
        3

        >>> def func():
        ...    a = 3
        ...    context = {'a': a}
        ...    eval('a += 1', context)
        ...    print(context['a'])
        >>> func()
        4
## 八、自定义函数

1. 基本格式

        def functionName(paramters):
            suite

2. 位置参数和关键字参数

    `python` 中的变量均为对象引用，函数参数也是引用传递。

    在调用函数时，可以像其他语言一样，只提供参数值，但这时候，参数的顺序将极为重要：

        >>> def func(param1, param2):
        >>>    return param1 - param2
        >>> func(3, 2)
        1
        >>> func(2, 3)
        -1

    但 `python` 还提供了另一种调用方法，即在调用时指定参数名，这种方式的参数叫**关键字参数**，关键字参数可以无视顺序，这在参数较多，或参数易混淆时，非常有用：

        >>> def func(param1, param2):
        >>>    return param1 - param2
        >>> func(param1=3, param2=2)
        1
        >>> func(param2=2, param1=3)
        1

    参数可以有默认值，对于有默认值的参数，调用时可以不提供。在定义带有默认值参数的函数时，不能将无默认值的参数定义在有默认值参数之后。

    调用函数时，也可以混合使用位置参数和关键字参数，顺序上依然要位置参数在前，关键字参数在后。无论如何，无默认值的参数一定要提供。

    以上两点，为 `python` 的函数定义和调用，提供了极大的灵活性：

        >>> def hello_4(name, greeting='Hello', punctuation='!'):
        >>>    print('{}, {}{}'.format(greeting, name, punctuation))
        >>> hello_4('Mars') 
        Hello, Mars!
        >>> hello_4('Mars', 'Howdy')
        Howdy, Mars!
        >>> hello_4('Mars', 'Howdy', '...')
        Howdy, Mars...
        >>> hello_4('Mars', punctuation='.')
        Hello, Mars.
        >>> hello_4(punctuation='.', name='Mars')
        Hello, Mars.
        >>> hello_4(greeting='Top of the morning to ya', punctuation='.', name='Mars')
        Top of the morning to ya, Mars.

3. 收集参数

    收集参数有两类
    
    1. 位置参数收集，可以理解为在定义函数时指定了一个元组类型的参数，而在调用时提供逗号间隔的位置参数列表，列表中的值依顺序成为元组参数的元素，语法：

            def funcationName(*parameters):
                suite

        简单示例：

            >>> def print_param(*params):
            >>>    print(params)
            >>> print_param('hello', 'butty')
            ('hello', 'butty')
            >>> print_param('hello')
            ('hello',)

    2. 关键字参数收集，可以理解为定义函数时指了一个字典类型的参数，而在调用时提供了逗号间隔的关键字参数列表，列表中的项将成为字典参数的元素，语法：

            def funcationName(**keyParameters):
                suite

        简单示例：

            >>> def collection_dict_params(**dict_parameters):
            >>>     print(dict_paramters)
            >>> collection_dict_params(name='野比大雄', sex='男')
            {'name': '野比大雄', 'sex': '男'}

    还可以混合使用位置参数收集和关键字参数收集，位置参数收集在前，关键字参数收集在后：

        def functionName(*params, **keyParameters):
            suite

    最复杂的形式是命名参数和收集参数混合使用的情况，顺序上可以是如下两种形式之一：

        def functionName(param1, param2, ..., paramN, *params, key1=value1, key2=value2, ..., keyN=valueN, **keyParameters):
            suite

        def functionName(param1, param2, ..., paramN, *params, key1=value1, key2=value2, ..., keyN=valueN, **keyParameters):
            suite

    例如，`print` 函数的签名即为：

        print(*value, sep=' ', end='\n', file=sys.stdout, flush=False)

4. 分配参数

    分配参数是指在调用函数时，使用 `*` 和 `**` 运算符。

    如果使用 `*` 后接一个序列的形式作为实参调用函数，则序列会被解包成参数列表。

        >>> def func(a, b, c):
        >>>     print(a, b, c)
        >>> n = 3, 4, 5
        >>> func(*n)
        3 4 5

    `**` 在函数调用中的使用与此类似，只是实参类型换成了字典，

        >>> def func(a, b, c):
        >>>     print(a, b, c)
        >>> n = {'a': 3, 'b': 4, 'c': 5}
        >>> func(**n)
        3 4 5

5. 返回值

    函数使用 `return` 语句返回值。形式上可以返回多个值，不过实际上返回多值的结果即为元组。利用序列解包的特性，可以直接将返回多值的函数调用赋值给多个变量。

        >>> def func(a, b, c):
        ...     return a + a, b * b, c ** c
        ...
        >>> print(func(1, 2, 3))
        (2, 4, 27)
        >>> m, n, p = func(1, 2, 3)
        >>> print(m, n, p)
        2 4 27

6. lambda表达式

    `python` 的 `lambda` 表达式较之其它语言要更简单，适用范围也更窄：

        lambda paramters: expression

    参数可选，支持普通函数参数的全部形式。

    表达式不能含有分支和循环，可以有条件表达式和推导式。不能含有 `return` 语句，不能是生成器。

    调用结果是一个匿名函数，对匿名函数的调用将返回 `expression` 的计算结果，如果 `expression` 是一个元组字面量，需要使用括号包含起来。

7. doc

    `python` 中为函数或类撰写文档很容易，只要在函数或类的第一行内容写下一串字符串即可。这样的字符串被称为**文档字符串**（docstring）。

        def square(x):
            '计算数字 x 的平方'
            return x * x
    
    可以通过函数的 `__doc__` 属性访问文档字符串：

        >>> square.__doc__
        '计算数字 x 的平方'

    如果文档字符串较长，且有多行（比如包含使用示例等），可以使用三引号语法。此类文档，通常第一行为概述，换两行，再详细对函数加以说明。

8. 函数是一等公民

    面向对象语言中，一等公民指对象。在 `python`、`javascript` 等动态语言中，函数也是对象。可以将函数赋给变量，然后就可以像函数一样使用变量（类似于 `C` 语言的函数指针）：

        >>> def square(x):
        ...    '计算数字 x 的平方'
        ...    return x * x
        ...
        >>> func = square
        >>> func(3)
        9
        >>> func.__doc__
        '计算数字 x 的平方'

9.  嵌套函数（局部函数）与闭包

    嵌套函数是指在一个函数内部定义的函数，由于作用域的缘故，也被称为局部函数、本地函数。

    局部函数可以访问其外部作用域（外部函数的作用域）内的变量。默认情况下，外部作用域对局部函数是只读的，如果要改变外部作用域的变量，可以使用 `nonlocal` 关键字对外部作用域变量加以说明。

    局部函数的一大用途就是闭包：闭包是指一个能访问其外部作用域的对象（或称为持有其外部环境的对象），在函数式编程语言中，一般是用返回局部函数的方式实现：

        >>> def external_func(param):
        ...    a = 3
        ...    b = 4
        ...    def internal_func():
        ...        print(a)
        ...        print(param)
        ...        nonlocal b
        ...        b += 9
        ...        return b
        ...    return internal_func
        ...
        >>> i = external_func('try')
        >>> i()
        3
        'try'
        13

    局部函数的另外一个常见的用途是局部代码的递归。

10. 修饰器

    修饰器是一个函数，将被修饰的函数（或方法）作为其唯一的参数，返回一个新的函数（或方法），新函数（或方法）是对被修饰函数（或方法）的包装。在被修饰方法前使用 `@` 符号引导修饰器方法，则在调用被修饰方法时， `python` 将按如下顺序完成调用：
    
    1. 先调用修饰器方法，得到其返回的包装方法，
    2. 再以调用被修饰方法的参数，调用返回的包装方法。 

    包装器的实际实现，是闭包、收集参数、分配参数的综合运用：

        def positive_result(function):
            '此包装器实现了在被修饰函数结果为正数时正常返回，为负数时抛出异常的功能'
            def wrapper(*args, **keyargs):
                result = function(*args, **keyargs)
                assert result >= 0, function.__name__ + "() result isn't >= 0"
                return result
            wrapper.__name__ = function.__name__
            wrapper.__doc__ = function.__doc__
            return wrapper

        @positive_result
        def discriminant(a, b, c):
            '完成对二次项系数为a，一次项系数为b，常数项为c的一元二次方程判别式的计算'
            return (b ** 2) - (4 * a * c)

    如果要实现带参数的修饰器，修饰器语法本身是不支持的，可以利用双层嵌套函数来实现：

        import functools
        def bounded(minimum, maximum):
            def decorated(function):
                @functools.wraps(function)
                def wrapper(*args, **kwargs):
                    result = function(*args, **keyargs):
                    if result < minus:
                        return minimum
                    elif result > maximum:
                        return maximum
                    return result
                return wrapper
            return decorated
        
        @bounded(0, 100)
        def func(a, b):
            ...

    上面的例子中，`python` 解释器在遇到 `@bounded(0, 100)` 这一行时，会先调用 `bounded(0, 100)`，此调用返回 `decorated(func)` 函数，这个函数才是与 `@` 搭配的修饰器。

    在后续调用被修饰的 `func(a, b)` 函数时，会按前述的步骤完成修饰器的调用。因为修饰器 `decorated` 是个局部函数，它可以使用外部函数 `bounded` 接收到的两个参数。这样就间接实现了带有参数的修饰器。

    另外这一段代码中，对包装函数使用了 `@functools.wraps`，这个函数实现了前面的 `wrapper.__name__ = function.__name__`、`wrapper.__doc__ = function.__doc__` 等一些功能，并且在自省和 `unwrap` 时有用。

11. 判断一个对象是否为函数（方法、类）

    `callable(__obj)` 函数用于判断一个对象是否可调用（函数、方法和类都是可调用的）。
## 九、类与对象

1. 类、属性、方法

    定义类有两种语法：

        class className:
            suite

        class className(baseClass):
            suite

    如果要指定超类，就使用第二种语法，在括号内指定超类。如果不指定超类，则直接继承自顶层类（`object`），也即是说，第一种语法与在括号内指定 `object` 是等效的。

    方法的定义语法：

        class className:
            def func(self, ...):
                suite

    方法的第一个参数，是隐式传递的，与调用方法的对象关联，因此在方法内部，就可以使用 `self.` 语法访问关联对象的方法和属性。`self` 并非关键字，与普通变量名无异，可以自由命名，使用 `self` 仅是惯例。

    `python` 中，对象的属性与普通变量类似，无需预告定义，赋值后即可使用，但不能直接读取未赋值的属性。

2. 访问控制

    `python` 没有用于访问控制类的关键字，也没有绝对意义上的访问控制。

    如果想让属性或方法在类外不能访问，可以让属性或方法名以两个下划线开头，不过这只是想让其他程序员明白，这些属性或变量不希望被在外部访问。底层实现仅仅是对两个下划线开头的名称进行了替换，再前面加了一个下划线和类名，使用替换后的名称仍然可以访问：

        >>> class className:
        ...    __prop = 10
        ...
        >>> c = className()
        >>> print(c.__prop) #抛出异常
        >>> print(c._className__prop)
        10

    更弱一点的方式是，以一个下划线开头命名属性或方法，以警告其他程序员，这些属性和方法不希望被外部访问。在使用 `import *` 导入模块时，不会导入以一个下划线开头的名称。

    `python` 有数个拦截对象访问的特殊方法：

    1. `__getattr__(self, name)`

        在属性被访问，但对象没有此属性时调用

    2. `__setattr__(self, name, value)`

        试图给属性赋值时调用 

    3. `__delattr__(self, name)`

        试图删除属性时调用

    4. `__getattribute__(self, name)`

        在属性被访问时调用

    在使用 `__setattr__` 和 `__getattribute__` 方法时要注意避免递归调用。

    避免 `__setattr__` 递归的方法，是对不需要拦截的名称直接使用 `__dict__` 属性。

    避免 `__getattribute__` 递归的方法，是对不需要拦截的名称调用超类的同名方法。

        class Rectangle:

            def __init__(self):
                self.width = 0
                self.height = 0

            def __setattr__(self, name, value):
                if 'size' == name:
                    self.width, self.height = value
                else:
                    self.__dict__[name] = value

            def __getattr__(self, name):
                if 'size' == name:
                    return self.width, self.height
                else:
                    raise AttributeError

            def __getattribute__(self, name):
                if 'size' == name:
                    return self.width, self.height
                else:
                    return super().__getattribute__(name)

    `getattr(__o, name[, __default])` 函数可以用来获取对象的属性，并可在对象属性不存在时提供一个默认值。它将调用对象的 `__getattr(self, name)` 方法。

    `setattr(__o, name, value)` 函数则可以用来为对象属性赋值。它将调用对象的 `__setattr(self, name)` 方法。

3. 特性

    特性是指以属性的语法访问，但实际是调用了存取方法，这是用 `property` 函数实现的：

        property([fget=None[, fset=None[, fdel=None[, doc=None]]]])

    第一个参数是用于获取特性的方法，第二个参数是给特性赋值的方法，第三个参数是删除特性的方法，第四个参数则是 `docstring`。

        class Rectangle:

            def set_size(self, size):
                self.width, self.height = size

            def get_size(self):
                return self.width, self.height

            size = property(get_size, set_size, doc='矩形的尺寸为长、宽')


        >>> r = Rectangle()
        >>> r.width = 10
        >>> r.height = 5
        >>> r.size
        (5, 10)
        >>> r.size = 150, 100
        >>> r.width
        150
        >>> Rectangle.size.__doc__
        '矩形的尺寸为长、宽'

    `property` 的各个参数均可省略。如果省略 `doc`，则会尝试使用 `fget` 方法的 `docstring`。

    特性更常用的方式是使用 `@property` 修饰器，使用该修饰器修饰的方法名将作为特性名，被修饰的方法将作为特性的 `fget` 方法，该方法的 `docstring` 将作为特性的 `docstring`。同时会生成 `特性名.setter` 和 `特性名.deleter` 修改器，用这两个修改器修饰的方法将分别作为特性的 `fset` 和 `fdel` 方法。

    使用修饰器时，甚至可以使用同名的方法：

        class C(object):
            def __init__(self):
                self._x = None

            @property
            def x(self):
                """I'm the 'x' property."""
                return self._x

            @x.setter
            def x(self, value):
                self._x = value

            @x.deleter
            def x(self):
                del self._x

    有一个小细节需要注意：特性名与要存取的属性名不能相同，否则会造成递归调用。

4. 继承、多继承与多态、接口

    继承：在定义类的时候，可以在括号内指定超类。

    多继承：`python` 支持多继承，只需在定义类时，指定超类列表。

    当多个超类有相同的方法时，超类列表中居前的方法将遮蔽位于后面的类的同名方法。

    判断一个类是否为另一个类的子类，可以使用 `issubclass` 函数：

         issubclass(subClassName, superClassName)

    获取一个类的所有直接超类，可以使用类的 `__bases__` 属性。

    判断一个对象是否是一个类（或其子类）的实例，可以使用 `isinstance` 函数：

        isinstance(objectName, className)

    通过对象的 `__class__` 属性或使用 `type(objectName)` 可以获取对象所属的类。

    访问超类的方法和属性，需要先调用 `supper()` 函数，再调用其返回对象的方法：

        class Bird:

            def __init__(self):
                self.hungry = True

            def eat(self):
                if self.hungry:
                    print('Aaaah...')
                    self.hungry = False
                else:
                    print('No, thanks')


        class SongBird(Bird):

            def __init__(self):
                super().__init()
                self.sound = 'Squawk!'

            def sing(self):
                print(self.sound)

    `super` 的完整语法：

        super([t=currentClass[, obj=self]])

    在一些旧的代码中，上例中的 `super` 可能写成这样：

        super(SongBird, self).__init__()

    不同于强类型语言，`python` 的多态，沿袭了鸭子类型（duck typing），而不是接口继承。`python` 中也没有专门的接口语法，如果一定要作用接口，可以使用多继承加纯抽象类（不含有非抽象方法的类）来实现。


5. 静态方法

    使用 `@staticmethod` 修饰器修饰的方法为静态方法，**静态方法与实例方法的区别在于，它不需要与对象关联的参数（self）**。当然它也无法访问对象属性和方法。

        class MyClass:

            @staticmethod
            def smeth(*parameters):
                print('This is a static method')
                print(parameters)

6. 类方法

    使用 `@classmethod` 修饰器修饰的方法为类方法，**类方法的第一个参数，在调用时自动与调用方法的类相关联，惯例上这个参数命名为 `cls`**。

        class MyClass:

            prop = 'Class’s property'

            @classmethod
            def cmeth(cls):
                print('This is a class method')
                print(cls.prop)

7. 静态属性、类属性、实例属性

    不同于静态方法和类方法，静态属性和类属性在 `python` 中是同一概念，即使用类名访问的属性。

    而实例属性则是用对象来访问的。

    在 `python` 中，属性均无需定义，赋值即可使用。因此，类属性和实例属性的关系比较微妙。

    在类定义中，方法外赋值的属性，可以被视为类属性，而在方法内，用 `self.属性名` 的形式赋值的属性，则为实例属性。

    在类外访问时，使用 `className.属性` 赋值的即是类属性，使用 `objectName.属性` 赋值的即是实例属性。

    读取时，在没有同名实例属性（即没有给同名实例属性赋值）的前提下，既可以使用 `className.属性` 形式，也可以使用 `self.属性`、`objectName.属性` 形式访问。

    一旦给实例属性赋了值，则再使用 `self.属性` 或 `objectName.属性` 形式，则只能访问实例属性。

        >>> class first_cls:
        ...    a = 0
        ...
        >>> fcls = first_cls()
        >>> print('first_cls.a:', first_cls.a)
        first_cls.a: 0
        >>> print('fcls.a:', fcls.a)
        fcls.a: 0
        >>> first_cls.a = 9
        >>> print('first_cls.a:', first_cls.a)
        first_cls.a: 9
        >>> print('fcls.a:', fcls.a)
        fcls.a: 9
        >>> fcls.a = 13
        >>> print('first_cls.a:', first_cls.a)
        first_cls.a: 9
        >>> print('fcls.a:', fcls.a)
        fcls.a: 13
        >>> first_cls = 30
        >>> print('first_cls.a:', first_cls.a)
        first_cls.a: 30
        >>> print('fcls.a:', fcls.a)
        fcls.a: 13

    如下形式在很多代码示例中出现过：

        class MyClass:
            a = 10
            def increment(self):
                self.a += 1

8. 构造函数与初始化函数

    `python` 中在创建对象之后，会自动调用 `__init__(self, ...)` 方法对对象进行初始化。如果超类不是 `object`，通常需要在 `__init__(self, ...)` 方法中先调用超类的 `__init__(self, ...)` 方法，以完成父类的初始化步骤。见第四小节的例子。

    会有很多资料说 `__init__(self, ...)` 方法是构造方法，这是因为真正的构造方法用的较少，才会有此误会。

    `python` 中的构造方法是 `__new__(cls, ...)`，这是一个类方法，它的第一个参数是与类关联的，`__new__(cls, ...)` 方法需要有一个返回值，这个返回值就是创建的对象。

    构造函数的一个典型用途是继承并修改不可变类型，有兴趣可以参看：https://www.cnblogs.com/shenxiaolin/p/9307496.html

9. 运算符重载及其它特殊方法

    运算符重载方法：

    | 方法 | 重载的运算符 |
    |----|----|
    | __pos__(self) | + self |
    | __neg__(self) | - self |
    | __invert__(self) | ~ self |
    | __add__(self, other) | self + other |
    | __iadd__(self, other) | self += other |
    | __radd__(self, other) | other + self |
    | __sub__(self, other) | self - other |
    | __isub__(self, other) | self -= other |
    | __rsub__(self, other) | other - self |
    | __mul__(self, other) | self * other |
    | __imul__(self, other) | self *= other |
    | __rmul__(self, other) | other * self |
    | __mod__(self, other) | self % other |
    | __imod__(self, other) | self %= other |
    | __rmod__(self, other) | other % self |
    | __floordiv__(self, other) | self // other |
    | __ifloordiv__(self, other) | self //= other |
    | __rfloordiv__(self, other) | other // self |
    | __truediv__(self, other) | self / other |
    | __itruediv__(self, other) | self /= other |
    | __rtruediv__(self, other) | other / self |
    | __pow__(self, other) | self ** other |
    | __ipow__(self, other) | self **= other |
    | __rpow__(self, other) | other ** self |
    | __and__(self, other) | self & other |
    | __iand__(self, other) | self &= other |
    | __rand__(self, other) | other & self |
    | __or__(self, other) | self \| other |
    | __ior__(self, other) | self \|= other |
    | __ror__(self, other) | other \| self |
    | __xor__(self, other) | self ^ other |
    | __ixor__(self, other) | self ^= other |
    | __rxor__(self, other) | other ^ self |
    | __lshift__(self, other) | self << other |
    | __ilshift__(self, other) | self <<= other |
    | __rlshift__(self, other) | other << self |
    | __rshift__(self, other) | self >> other |
    | __irshift__(self, other) | self >>= other |
    | __rrshift__(self, other) | other >> self |
    | __lt__(self, other) | self < other |
    | __le__(self, other) | self <= other |
    | __eq__(self, other) | self == other |
    | __ne__(self, other) | self != other |
    | __gt__(self, other) | self > other |
    | __ge__(self, other) | self >= other |

    函数调用相关特殊方法

    | 方法 | 对应函数调用 | 
    |----|----|
    | __abs__(self) | abs(self) |
    | __float__(self) | float(self) |
    | __int__(self) | int(self) |
    | __index__(self) | bin(self) oct(self) hex(self) |
    | __round__(self,, digits) | round(self, digits) |
    | __complex__(self) | complex(self) |
    | __bool__(self) | bool(self) |
    | __hash__(self) | hash(self) |
    | __str__(self) | str(self) |
    | __ascii__(self) | ascii(self) |
    | __repr__(self) | repr(self) |
    | __format__(self, format_spec) | "{0}".format(self) |

10. 动态扩充和修改类

    不同于 `Java`，`python` 的类并不是定义之后就一成不变的，可以随时根据需要对类进行扩充和修改。并且这种扩展和修改对已经创建的类实例也是有效的。

        >>> class mc:
        ...     def __init__(self):
        ...         pass

        >>> m = mc()
        >>> mc.newfunc = lambda self, a, b: a + b
        >>> mc.newprop = 30
        >>> n = mc()
        >>>> m.newfunc(3, 4)
        7
        >>> n.newfunc(3, 4)
        7
        >>> m.newprop
        30
        >>> m.newprop
        30
        >>> mc.__init__ = lambda self: print("I'm new init function.")
        >>> nm = mc()
        I'm new init function.

11. 局部类（内部类）

    定义在函数或方法内的类，称为局部类（内部类）。

    与局部函数类似，局部类也可以访问其外部作用域，而且 `python` 的类也是对象，是可以传递的。

    因此可以像闭包函数一样，让外部函数或方法返回局部类，这可以用于动态定义类。

12. 类修饰器

    类修饰器用于对类进行包装，它接收一个类作为唯一参数，并返回一个对传入的类进行包装的类，不同于函数修饰器的是，通常不需要另外定义一个类，仅需要对被包装进行修改和扩展，将修改后的类返回即可。

    如下修饰器将为实现了 `__le__` 方法的类添加其他五种比较运算符重载方法：

        def complete_comparisons(cls):
            assert cls.__lt__ is not object.__lt__, "{0} must define <.".format(cls.__name__)
            cls.__eq__ = lambda self, other: (not (cls.__lt__(self, other) or cls.__lt__(other, self)))
            cls.__ne__ = lambda self, other: not cls.__eq__(self, other)
            cls.__gt__ = lambda self, other: cls.__lt__(other, self)
            cls.__le__ = lambda self, other: not cls.__lt__(other, self)
            cls.__ge__ = lambda self, other: not cls.__lt__(self, other)

13. 抽象基类

    抽象基类不能实例化，仅能作为其它类的超类。

    `python` 中的抽象基类必须同时满足如下两个条件‘

    1. 元类是 `abc.ABCMeta`，或者其超类链中有元类为 `abc.ABCMeta` 的类。
    2. 类中包含抽象方法或抽象特性。

    用于定义抽象方法的方法的修饰器有三个：
    
    1. `abc.abstractmethod`
    2. `abc.abstractclassmethod`
    3. `abc.abstractstaticmethod`

    用于定义抽象特性的修饰器有：

    `abc.abstractproperty`

    下面的例子较长，展示了抽象方法和抽象特性：

        >>> import abc
        ... class haha:
        ...     def haha(self):
        ...         print('haha')
        ... class Appliance(haha, metaclass=abc.ABCMeta):
        ...     @abc.abstractmethod
        ...     def __init__(self, model, price):
        ...         self.__model = model
        ...         self.__price = price
        ...
        ...     @abc.abstractproperty
        ...     def price(self):
        ...         return self.__price
        ...     @price.setter
        ...     def set_price(self, price):
        ...         self.__price = price
        ...     @property
        ...     def model(self):
        ...         return self.__model
        ...     @model.setter
        ...     def model(self, model):
        ...         self.__model = model
        ... class MyAppliance(Appliance):
        ...     def __init__(self, model, price):
        ...         super().__init__(model, price)
        ...     @property
        ...     def price(self):
        ...         return super().price
        ...     @price.setter
        ...     def set_price(self, price):
        ...         super().set_price(self, price)
        ... ma = MyAppliance('kabang', 150)
        >>> ma.price
        150
        >>> ma.haha()
        'haha'

    需要注意的是，抽象方法仅仅只是要求子类必须实现的方法，它本身并没有特殊的语法，不能像其他语言的抽象方法那样没有方法体。

14. 元类（略）
15. 函子

    函子是实现了 `__call__` 方法的对象，它是另一种类型的函数对象。对它的函数形式的调用即是对它的 `__call__` 方法的调用。

        >>> class Strip:
        ...     def __init__(self, characters):
        ...         self.charactors = characters
        ...     def __call__(self, string)
        ...         return string.strip(sef.characters)
        ...
        >>> strip_punctuation = Strip(",;:.!?")
        >>> strip_punctuation("Land, ahoy!")
        Land ahoy

    函数不能执有状态，这就是函子的发挥场景，但很多时候，使用 `闭包` 更符合动态语言的习惯。

16. 描述符（略）
17. 内省

    `python` 的内省机制类似于 `Java` 等语言的反射，使用的是 `inspect` 模块。

    `inspect` 模块有四类用途：

    1. 类型和成员

        1、`getmembers(object[, predicate])`

            返回对象的成员列表。如果提供了第二参数，则仅返回第二参数为真的成员。第二个参数主要使用以 `is` 开头的函数，这类函数也可单独使用。

        1. `isxxxx(object)` 方法

            这一组方法用于判断，比如判断是否为函数：

                >>> def a():
                ...     pass
                ...
                >>> inspect.isfunction()
                True

            列表如下：
            `ismodule`、`isclass`、`ismethod`、`isfunction`、`isgeneratorfunction`、`isgenerator`、`iscoroutinefunction`、`iscoroutine`、`isawaitable`、`isasyncgenfunction`、`isaayncgen`、`istraceback`、`isframe`、`iscode`、`isbuiltin`、`isroutine`、`isabstract`、`ismethoddescriptor`、`isdatadescriptor`、`isgetsetdescriptor`、`ismemberdescriptor`

        2. `getmodulename`

            获取区块名称

    2. 获取源代码

        `getdoc`、`getcomments`、`getfile`、`getmodule`、`getsourcefile`、`getsourcelines`、`getsource`、`cleandoc`

    3. 获取类或函数信息

        `signature`、`getclasstree`、`getargspec`、`getfullargspec`、`getargvalues`、`formatargspec`、`formatargvalues`、`getmro`、`getcallargs`、`getclosurevars`、`unwrap`

    4. 解析堆栈

        `stak`、`trace`、`getframeinfo`、`getouterframes`、`getinnerframes`、`currentframe`

18. `__dict__` 和 `__slots__`

    对象的 `__dict__` 是一个字典类型的属性，存储了所有的实例属性。它是可以动态改变的。

    如果想要有固定的属性项，可以使用 `__slots__`，它是一个元组。

        >>> class employee:
        ...    __slots__ = ('name', 'sex', 'age', 'height', 'weight')
        ...
        >>> e = employee()
        >>> e.address = 'dalian'
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AttributeError: 'employee' object has no attribute 'address'

    使用 `__slots__` 时要注意，不要使用同名的类变量，否则会使实例变量失效（赋值时提示对象属性只读，读取时读取类变量的值）。

19. 上下文管理器和 `with` 块

    上下文管理器是指有 `__enter__` 和 `__exit__` 方法的对象。

    上下文管理器与 `with` 语句块组合使用，可以达到自动释放资源的目的。

        with expression as variable:
            suite

    `expression` 表达式必须是或必须生成一个上下文管理器。在开始执行语句块前，将自动调用上下文管理器的 `__enter__` 方法，如果提供了可选的 `as variable` 部分，则 `variable` 将引用 `__enter__` 方法的返回的对象（通常该方法将返回上下管理器本身）。

    在退出 `with` 范围时，将自动调用上下文管理器的 `__exit__` 方法（即使语句块发生异常）。

    在资源本身是上下文管理器，且其退出方法保证了资源关闭的情况下，不需要使用 `finally` 子句保证资源的关闭。

        try:
            with open(filename) as fh:
                for line in fh:
                    process(line)
        expect EnvironmentError as err:
            print(err)

    `with` 也支持多个上下文管理器：

        try:
            with open(source) as fin, open(target, 'w') as fout:
                for line in fin:
                    fout.write(process(line))
        expect EnvironmentError as err:
            print(err)

## 十、迭代器和生成器

1. 迭代器

    迭代器协议要求迭代器对象必须实现 `__next__` 方法，可迭代对象必须实现 `__iter__` 方法，且该方法需要返回一个迭代器。

    `for` 循环的 `in` 子句需要一个可迭代对象，实际迭代的则是可迭代对象的 `__iter__` 方法返回的迭代器，每次迭代调用迭代器的 `__next__` 方法，生成迭代变量。
    
        >>> class Fibs:
        ...    def __init__(self):
        ...        self.a = 0
        ...        self.b = 1
        ...    def __next__(self):
        ...        self.a, self.b = self.b, self.a + self.b
        ...        return self.a
        ...
        >>> class FibsIter:
        ...    def __iter__(self):
        ...        return Fibs()
        ...
        >>> for f in FibsIter():
        ...    if f > 1000:
        ...        print(f)
        ...        break
        ...
        1597

    实际应用中，通常可迭代对象和迭代器对象是二合一的，通称为迭代器：

        >>> class Fibs:
        ...    def __init__(self):
        ...        self.a = 0
        ...        self.b = 1
        ...    def __next__(self):
        ...        self.a, self.b = self.b, self.a + self.b
        ...        return self.a
        ...    def __iter__(self):
        ...        return Fibs()
        ...
        >>> for f in Fibs():
        ...    if f > 1000:
        ...        print(f)
        ...        break
        ...
        1597

    可以使用 `iter` 函数调用迭代器的 `__iter__` 方法，获得返回的迭代器对象。
    可以使用 `next` 函数调用迭代器的 `__next__` 方法，进行一次迭代。

        >>> class Fibs:
        ...    def __init__(self):
        ...        self.a = 0
        ...        self.b = 1
        ...    def __next__(self):
        ...        self.a, self.b = self.b, self.a + self.b
        ...        return self.a
        ...
        >>> class FibsIter:
        ...    def __iter__(self):
        ...        return Fibs()
        ...
        >>> fibs = iter(FibsIter())
        >>> next(fibs)
        1
        >>> next(fibs)
        1
        >>> next(fibs)
        2
        >>> next(fibs)
        3
        >>> next(fibs)
        5

2. 生成器

    生成器函数是包含了 `yield` 表达式的函数。

        >>> def sum_seq(min, max, step):
        ...    s = 0
        ...    while min < max:
        ...        s += min
        ...        min += step
        ...        yield s

    调用这个函数，并不会执行循环，而是返回一个迭代器（同时也是生成器）。

    对这个迭代器的每次迭代，都会返回 `yield` 表达式中子表达式的值，并冻结函数，直到下一次迭代时被唤醒，从 `yield` 表达式的下一行继续执行。

    如果生成器的代码执行结束，或执行了一个 return 语句，将产生 `StopIterationException`，`for` 循环在遇到此异常时，将直接终止循环。

        >>> ss = sum_seq(3, 99, step)
        >>> next(ss)
        3
        >>> next(ss)
        8
        >>> next(ss)
        15

        >>> for s in sum_seq(3, 99, step):
        >>>     pass
        >>> else:
        >>>     print(s)
        ...
        2400

    生成器函数返回的生成器，还有 `send`、`throw` 和 `close` 方法。

    方法 `throw` 用于在生成器中 `yield` 表达式处引发异常，调用时可提供一个异常类型、一个可选值和一个traceback对象。
    
    方法 `close` 用于停止生成器，调用时无需提供任何参数。调用此方法后，再试图从生成器获取值将导致 `RuntimeError` 异常。

    `yield` 表达式除了可返回其子表达式的值，也可以通过接收调用 `send` 方法传递的值。`__next__` 方法和 `send(None)` 作用相同。

        >>> def quarters(next_quarter=0.0):
        ...     while True:
        ...         received = (yield next_quarter)
        ...         if received is None:
        ...             next_quarter += 0.25
        ...         else:
        ...             next_quarter = received
        ...
        >>> generator = quarter()
        >>> next(generator)
        0.0
        >>> next(generator)
        0.25
        >>> generator.send(1.0)
        1.0
        >>> next(generator)
        1.25
        >>> generator.send(None)

    需要注意的是，仅当生成器被挂起后，传递值才有意义，否则会报错，因此第一次迭代生成器，需要作用 `next` 函数或调用参数为 `None` 的 `send`方法。
## 十一、模块和包

1. 模块
2. 包
3. 标准库
4. 导入语句综述
5. 模块查找
6. 自定义模块

## 十二、常用模块

1. 日期和时间
2. XML
3. JSON
4. 邮件
5. 网络编程
6. Web
7. 数据库
8. 正则表达式
## 十三、调试和测试

1. 断点调试
2. 单元测试
## 十四、线程、进程、协程

1. 线程

    1. 使用 `threading` 模块实现多线程，有两种模式：
    
        1. 调用 `threading.Thread` 方法，传递函数及其参数，创建线程

                >>> import time
                ... import threading
                ... def demo(n):
                ...     while n >= 0:
                ...         print('n:', n)
                ...         n -= 1
                ...         time.sleep(1)
                ...
                >>> t = threading.Thread(target=demo, args=(10,))
                >>> t.start()
                10
                >>> t.join()
                9
                8
                7
                6
                5
                4
                3
                2
                1
                0

            `threading.Thread` 方法的签名：

                threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)

            `group` 参数是保留的参数，目前必须是 `None`。

            `target` 参数即为要调用的函数。

            `name` 是线程的名字。如果为 `None`，`python` 会自动为线程指定一个名称。

            `args` 是要传递给被调用函数的位置参数元组，默认为 ()。

            `kwargs` 是要传递给被调用函数的关键字参数字典，默认为 {}。

            `daemon` 用于指定线程是否为守护模式。如果为 `None`，将继承当前线程的守护模式属性，如果为 `True` 则为守护线程，如果为 `False` 则为非守护线程。

        2. 继承 `threading.Thread` 类，实现其 `run()` 方法。

            启动线程，调用 `threading.Thread` 实例的 `start()` 方法，它会调用线程的 `run()` 方法。

                >>> import threading
                >>> import time
                >>> class myThread (threading.Thread):
                ...    def __init__(self, threadID, name, counter):
                ...        threading.Thread.__init__(self)
                ...        self.threadID = threadID
                ...        self.name = name
                ...        self.counter = counter
                ...    def run(self):
                ...        print ("开始线程：" + self.name)
                ...        print_time(self, self.counter, 5)
                ...        print ("退出线程：" + self.name)
                ...
                >>> def print_time(thread, delay, counter):
                ...    while counter:
                ...        time.sleep(delay)
                ...        print ("%s: %s" % (thread.name, time.ctime(time.time())))
                ...        counter -= 1
                ...
                >>> thread1 = myThread(1, "Thread-1", 1)
                >>> thread2 = myThread(2, "Thread-2", 2)
                >>> thread1.start()
                开始线程：Thread-1
                >>> thread2.start()
                开始线程：Thread-2
                >>> thread1.join()
                Thread-1: Wed May  5 18:35:21 2021
                Thread-1: Wed May  5 18:35:22 2021
                Thread-2: Wed May  5 18:35:22 2021
                Thread-1: Wed May  5 18:35:23 2021
                Thread-2: Wed May  5 18:35:24 2021
                Thread-1: Wed May  5 18:35:24 2021
                Thread-1: Wed May  5 18:35:25 2021
                退出线程：Thread-1
                >>> thread2.join()
                Thread-2: Wed May  5 18:35:26 2021
                Thread-2: Wed May  5 18:35:28 2021
                Thread-2: Wed May  5 18:35:30 2021
                退出线程：Thread-2
                >>> print ("退出主线程")
                退出主线程

            需要注意的是，继承 `threading.Thread` 类的线程类，如果实现了自己的 `__init__` 方法，必须调用 `threading.Thread` 的 `__init__` 方法。

            调用线程的 `join(timeout=None)` 方法，将会阻塞启动该线程的线程，等待该线程终结后（或者在指定的超时时间后）恢复。判断线程是否超时，是在 `join()` 方法后调用线程的 `is_alive()` 方法，如果在阻塞恢复后，`is_alive()` 仍然返回 `True`，则表明线程已超时。

        3. `Lock` 对象

            锁有两种状态：「锁定」和「非锁定」。刚刚创建完的锁处于非锁定状态。它有两个基本方法：`acquire(blocking=True, timeout=-1)` 和 `release()`。

            `acquire(blocking=True)` 调用，如果锁处理「非锁定」状态，将锁「锁定」，并返回 `True`；如果锁处理「锁定」状态，将阻塞直到锁被释放，然后加锁并返回 `True`。如果带有 `timeout` 参数，则最多阻塞 `timeout` 设定的秒数，超时则返回 `False`。

            `acquire(blocking=False)` 调用，如果锁处理「非锁定」状态，加锁并返回 `True`，否则立即返回 `False`。

            `threading` 模块有两个锁：原始锁 `Lock` 和可重入锁 `RLock`，两者的不同在于可重入锁可以被同一线程多次 `acquire`，但也要有同样次数的 `release`，才能被其他线程获取。

            为确保锁被释放，可以借助 `finally` 子句：

                some_lock.acquire()
                try:
                    # do something
                finally:
                    some_lock.release()

            另外，锁也遵循上下文管理器协议，在进入语句块时 `acquire()` 方法被调用（这是通过让锁的 `__enter__()` 方法引用 `acquire()` 方法实现的），退出语句块时 `release()` 方法被调用（这是通过让 `__exit__()` 方法调用 `release()` 方法实现的），如下代码与上面的代码相当：

                with some_lock:
                    # do something

            不过对非阻塞锁不适用。

        4. `Condition` 对象

            `Condition` 对象总是与锁相关联，创建 `Condition` 对象时，可以为其指定关联的锁，如果创建 `Condition` 对象时没有指定关联锁，则自动创建一个可重用锁。

                import threading

                condition = threading.Condition(threading.Lock())

                consition_default = threading.Condition()

            `Condition` 对象也有 `acquire` 方法和 `release` 方法，会对关联锁的同名方法进行调用。

            另外 `Condition` 对象还有 `wait()`、`notify()`、`notify_all()` 和 `wait_for()`方法。

            `wait(timeout=None)` 方法释放锁，然后阻塞当前线程，直到其他线程调用同一 `Condition` 对象的 `notify()` 方法或 `notify_all()` 方法唤醒它，或者可选的超时发生。一旦被唤醒或超时，将尝试重新获得锁，并在获得锁时返回。

            `wait_for(predicate, timeout=None)` 方法的第一个参数是一个可调用对象，它的返回值应该可以转换为 `bool` 值。此方法会重复调用 `wait()` 直到条件满足或发生超时。

                wait_for(predicate)

            大致相当于：

                while not predicate():
                    condition.wait()

            `notify()` 方法和 `notify_all()` 方法不会释放锁，需要另外调用 `release()` 方法。

            `Condition` 对象遵循上下文管理器协议，在进入语句块时 `acquire()` 方法被调用，退出语句块时 `release()` 方法被调用。

        5. `Semaphore` 对象

            信号量对象用于资源个数受限的场景。

            在初始化时，可以指定信号量总量。

                threading.Semaphore(value=1)

            调用 `acquire()` 方法时，判断计数器是否大于 `0`，如果大于 `0`，则将其减 `1` 并立即返回；如果为 `0`，则阻塞并等待其它线程调用 `release()`方法唤醒，一量被唤醒，将计数器减 `1` 并返回。

            调用 `release()`方法 将内部计数器加 `1`，如果当时计数器为 `0`，在加 `1` 后唤醒正在等待的线程。

            `Semaphore` 对象的 `release()`方法 和 `acquire()`方法 的调用次数可以不相等，当调用 `release()` 方法的次数多于 `acquire()` 方法的次数，计数器的值会超过初始值。

            如果计数器的值超过初始值可能会引起问题，可以使用有界信号量：`BoundedSemaphore(value=maxconnections)`，当调用 `BoundedSemaphore` 对象的 `release()` 方法可能会造成计数器超过设定的最大值时，会抛出 `ValueError` 异常。

            `Semaphore` 对象和 `BoundedSemaphore` 对象遵循上下文管理器协议，在进入语句块时 `acquire()` 方法被调用，退出语句块时 `release()` 方法被调用。

        6. `Event` 对象

            `Event` 对象管理一个内部标志，此标志仅有 `False` 和 `True` 两种状态，默认为 `False`。

            `Event` 有如下方法：

            1. `wait()`

                如果 `Event` 的状态为 `True`，直接返回。如果 `Event` 的状态为 `False`，阻塞线程，直到 `Event` 的状态为 `True`。

            2. `set()`

                将 `Event` 对象的状态设置为 `True`。所有被同一 `Event` 对象的 `wait()` 方法阻塞的线程都将被唤醒。

            3. `clear()`

                将 `Event` 对象的状态设置为 `False`。之后调用同一 `Event` 对象的 `wait()` 方法的线程都将被阻塞。

            4. `is_set()`

                当且仅当状态为 `True` 时返回 `True`。

        7. `Timer` 对象

            `Timer` 类是 `Thread` 类的子类，也是一个线程。用于指定一个可调用对象在等待一定的时间高运行。

            调用 `Timer` 对象的 `start()` 方法启动它。在定时结束前调用 `Cancel()` 方法则可以停止计时器。如果计时已经结束，调用些方法没有意义。

                >>> def hello():
                ...    print('hello, world!')
                ... t = Timer(30.0, hello)
                ... t.start()

        8. `Barrier` 对象

            `Barrier` 对象用于应对固定数量的线程需要彼此相互等待的情况。线程调用 wait() 方法后将阻塞，直到所有线程都调用了 wait() 方法。此时所有线程将被同时释放。

                b = Barrier(2, timeout=5)

                def server():
                    start_server()
                    b.wait()
                    while True:
                        connection = accept_connection()
                        process_server_connection(connection)

                def client():
                    b.wait()
                    while True:
                        connection = make_connection()
                        process_client_connection(connection)

            `Barrier` 有如下方法和特性：

            1. `threading.Barrier(parties, action=None, timeout=None)`

                创建一个需要 `parties` 个线程的栅栏对象。如果提供了可调用的 `action` 参数，它会在所有线程被释放时在其中一个线程中自动调用。 `timeout` 是默认的超时时间。

            2. `wait(timeout=None)`

                当栅栏中所有线程都已经调用了这个函数，它们将同时被释放。`timeout` 参数优先于创建栅栏对象时提供的 `timeout` 参数。

                此函数返回值是一个整数，取值范围在 `0` 到 `parties - 1` 之间，每个线程中的返回值均不相同。返回值可用于从所有线程中选择唯一的一个线程执行一些特别的工作。

                    i = barrier.wait()
                    if i == 0:
                        # Only one thread needs to print this
                        print("passed the barrier")

                如果创建栅栏对象时在构造函数中提供了 `action` 参数，它将在其中一个线程释放前被调用。如果此调用引发了异常，栅栏对象将进入损坏态。

                如果发生了超时，栅栏对象将进入破损态。

                如果栅栏对象进入破损态，或重置栅栏时仍有线程等待释放，将将导致所有已经调用和未来调用的 `wait()` 方法引发 `BrokenBarrierError` 异常。

            3. `reset()`

                重置栅栏为默认的初始态。如果栅栏中仍有线程等待释放，这些线程将会收到 `BrokenBarrierError` 异常。

                注意使用此函数时，如果有某些线程状态未知，则可能需其它的同步来确保线程已被释放。如果栅栏进入了破损态，最好废弃它并新建一个栅栏。

            4. `abort()`

                使栅栏进入破损态。这将导致所有已经调用和未来调用的 `wait() `方法中引发 `BrokenBarrierError` 异常。使用这个方法的一种情况是需要中止程序以避免死锁。

                更好的方式是：创建栅栏时提供一个合理的超时时间，来自动避免某个线程出错。

            5. `parties`

                线程数量。

            6. `n_waiting`

                当前时刻正在栅栏中阻塞的线程数量。

            7. `broken`

                一个布尔值，值为 True 表明栅栏为破损态。

            `exception threading.BrokenBarrierError`

            异常类，是 `RuntimeError` 异常的子类，在 `Barrier` 对象重置时仍有线程阻塞时和对象进入破损态时被引发。
    2. queue

        `queue` 模块实现了多生产者、多消费者队列，可以安全的在多线程之间共享，并且自带锁机制，无需由线程实现锁。

        共有三种队列：
        1. `queue.Queue(maxsize=0)` 先进选出队列
        2. `queue.LifoQueue(maxsize=0)` 后进选出队列（堆栈）
        3. `queue.PriortyQueue(maxsize=0)` 排序队列：最小值最先被取出，最小值条目为 sorted(list(entries))[0]

        `Queue` 有如下方法：

        1. `put(item, block=True, timeout=None)`

            将 `item` 放入队列。如果 `block` 为 `True`，则在 `Queue` 已满时阻塞，直到 `Queue` 有了空槽可用，或者超过 `timeout` 指定的秒数（如果给出 `timeout` 参数的话）。如果 `block` 为 `False` 则不会阻塞，在 `Queue` 已满时直接抛出 `Queue.Full` 异常。

        2. `put_nowait(item)`

            相当于 `put(item, False)

        3. `get(block=True, timeout=None)`

            从 `Queue` 中返回并移除一个 `item`。如果 `block` 为 `True`，则在 `Queue` 为空时阻塞，直到 `Queue` 中有了新进的 `item` 或超过 `timeout` 指定的秒数（如果给出 `timeout` 参数的话）。如果 `block` 为 `False` 则不会阻塞，在 `Queue` 为空时直接抛出 `Queue.Empty` 异常。

        4. `get_nowait()`

            相当于 `get(False)`。

        5. `task_down()`

            每个 `get()` 被用于获取一个任务，后续调用 `task_down()` 表示获取的任务已完成。如果使用了 `join()` 阻塞了线程，则所有 `item` 都处理完成后，将解除阻塞。

        6. `join()`

            阻塞至队列中所有的元素都被接收和处理完毕。

            `put(item)` 未完成任务的计数就会增加，`task_down()` 未完成的任务计数会减少。当未完成计数降为 `0`，`join()` 阻塞被解除。

        7. `qsize()`

            返回队列的大致大小。并非可靠值，不可依赖。

        8. `empty()`

            队列是否为空，为空时返回 `True`。仅可参考，不可依赖。

        9.  `full()`

            队列是否已满，已满时返回 `True`。仅可参考，不可依赖。

        `get()`方法在 `blocking` 为 `True` 时，如果队列为空，会一直阻塞，如果在队列的任务全部处理完毕后，退出主线程，并不会使被 `get()` 阻塞的线程退出。

        网上有一个等待队列完成的例子：

            def worker():
                while True:
                    item = q.get()
                    do_work(item)
                    q.task_done()

            q = Queue()
            for i in range(num_worker_threads):
                t = Thread(target=worker)
                t.start()

            for item in source():
                q.put(item)

            q.join()       # block until all tasks are done

        官方文档有一个功能相同的示例：

            def worker():
                while True:
                    item = q.get()
                    if item is None:
                        break
                    do_work(item)
                    q.task_done()

            q = queue.Queue()
            threads = []
            for i in range(num_worker_threads):
                t = threading.Thread(target=worker)
                t.start()
                threads.append(t)

            for item in source():
                q.put(item)

            # block until all tasks are done
            q.join()

            # stop workers
            for i in range(num_worker_threads):
                q.put(None)
            for t in threads:
                t.join()

        可以自己尝试一下，看看结果有什么不同。

2. 进程

    `multiprocessing` 模块采用了和 `threading` 模板相似的 `API`，用子进程代替了线程。

    1. `multiprocessing.Procee` 类

        这个类的 `Api` 完全复制了 `threading.Thread` 类，只是使用子进程代替了线程，并提供了额外的几个方法和属性。

        其使用方法，也与 `threading.Thread` 类似：

        1. 直接使用 `threading.Thread` 方法，并传递一个可调用对象。
        2. 继承 `threading.Thread` 类，并实现其 `run` 方法。

        与 `threading.Thread` 相同的有：

        1. 构造方法
        2. `run` 方法
        3. `start` 方法
        4. `join` 方法
        5. `is_alive` 方法
        6. `name` 属性
        7. `daemon` 属性

        额外增加的方法和属性：

        1. terminate()

            终止进程，在类 `unix` 上使用 `SIGTERM` 信号完成，在 `Windows` 上使用 `TerminateProcess()`。此方法直接终止进程，不会执行退出处理和 `finally` 子句。

            注意，进程的后代进程不会被终止，它们将变成孤立进程。且可能造成其它破坏，比如死锁。慎用！

        2. kill()

            与 `terminate()` 作用相同，区别仅在于，在类 `Unit` 系统上使用 `SIGKILL` 信号。慎用！

        3. close()

            关闭 `Proccess` 对象，释放与之关联的所有资源。

        4. pid

            进程ID。

    2. Pool
3. 协程

## 十五、程序打包

1. Setuptools
2. 打包
3. py2exe 和 py2app

## 十六、应用

1. 运维脚本
2. Web
3. 爬虫
4. 数据挖掘和数据可视化
5. 机器学习