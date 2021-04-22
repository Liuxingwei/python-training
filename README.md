# PYTHON 速览

## 前言 Hello, World!

编写 hello.py 文件，内容：

```python
#!/usr/bin/env python
#encoding:utf8
string = "Hello, world!"
print(string)
```

在命令行输入命令：

```shell
$python hello.py
```

输出结果：

```shell
$Hello, world!
```

1. 脚本语言，无需经过单独的编译步骤，直接通过解释器命令执行
2. 无需 main() 函数，直接顺序执行语句
3. 变量无需定义类型（变量无固定类型）
4. 语句基本以行为单位，不需要使用分号（可以使用分号，在同一行上有两条以上语句时有作用）
5. 语句块以冒号、缩进为标志，不使用大括号；缩进只要宽度一致即可，推荐以四个空格为单位
6. #!/usr/bin/env python 在linux下，可以在将文件设置为可运行时，直接运行文件，将调用系统环境的python运行本文件代码
7. #encoding:utf8 指明文件编码，python3下默认为utf8，如果文件为utf8编码，可不写

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
$python -m venv --system-site-package /path/to/new/virtual/environment
```

--system-site-package 参数的作用是允许虚拟环境访问原始环境的库。虚拟环境的安装命令将包安装在虚拟环境中。在 Import 包时的优先级顺序为 当前路径、虚拟环境包路径、原始环境包路径。

激活虚拟环境：

命令行激活： 
```shell
$/path/to/new/virtual/environment/bin/activate
```

### 迁移环境

1. 导出包列表：

```shell
$pip freeze --local > requirements.txt
```

2. 下载包（新环境不能上网时需此步骤）：

```shell
$pip download -r requirements.txt
```

3. 创建新环境

```shell
$python -m venv --system-site-package /path/to/new/virtual/environment
```

4. 安装包

```shell
# 如果可以上网，复制requirements.txt

$pip install -r requirements.txt

# 如果不能上网，复制下载的安装文件和requirements.txt，在安装文件所在文件夹执行

$pip install --no-index --find-index=. -r requirements.txt 
```

### 在 IDE 中选用虚拟环境

1. VSCode：Ctrl+Shift+P，输入python，选择 Python: Select Python Interpreter，选择前面步骤创建的虚拟环境。Ctrl+Shift+^ 打开 Terminal，输入 exit，重新打开 Terminal，看到 (venv) ...
2. PyCharm：Settings > Project: xxxxxx > Python Interpreter > Python Interpreter 下拉 > Show all ...

## 五、数据类型及相关运算符、表达式

1. 整数类型

//（整除）、%（求余）、\*\*（乘方），函数：int()、divmod()...，没有自增、自减，仅有增强，赋值（+=、*=）

2. 布尔类型

True(1) False(0) bool()函数

3. 浮点数

支持整除、求余，float()

decimal类，精确数字，decimal.Decimal()，参数必须是整数或字符串，不能是浮点数

4. 字符串



## 六、元组、列表、字典

1. 序列
    1. 元组
    2. 列表
2. 字典

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