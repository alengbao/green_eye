# README
## 如何操作
程序的操作很简单，只需要将左侧列表中的列表项拖到右侧的工作区，就能产生一个可以用于编辑流程的节点。
每个节点都有输入项和输出项，将某个节点的输出项和另一个节点连线，这样就可以将前者的输出作为后者的输入。
值得注意的是，必须将开始节点（这个节点会直接出现在工作区）和你希望第一个运行的节点连接，才可以成功运行。
想要运行程序，只需要按下键盘上的R键即可。
想要清空工作区，只需按下C键即可。

## 如何开发新的节点
节点都放在了resource/codes路径下，可以看到里面有不同的文件夹，每个文件夹就是一个tab页。
你可以选择在某个文件夹下新建python文件（.py文件），并将代码写在其中。
文件名就是tab页中列表项的名字。
代码的形式如下：
```python
def 加法(a, b, called=None):
    return a + b


call = 加法
```
定义一个函数，并将函数赋值给变量call，就可以成功定义一个节点。
值得注意的几点是：
1. 注解不是必须的，但是在多返回值的情况下是必须的。
2. 程序中的函数名决定了节点的名字，入参名决定了入参的名字。
3. called参数用于占位，当你想在逻辑上运行一个新的节点，又不想真的给它传参，可以选择连接到called参数。（called参数必须有默认值None）

## TODO
1. 开发可以用于直接输入的节点
2. 开发可以用于选择图片的节点
3. 保存和读取已写的代码