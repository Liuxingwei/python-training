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

        8. 收集运算符 *

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

    6. 字典与字符串格式化方法：`format_map(d)`

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
## 十四、进程、线程、协程

1. 进程
2. 线程
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