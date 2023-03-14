import math
import re
#习题网址：https://www.nowcoder.com/exam/oj?page=1&tab=Python%E7%AF%87&topicId=314
""" TODO 为牛客网贷练习做一个函数调用列表
功能：运行该python文件会返回所有函数名称列表
     需要显示函数文档内容，为用户了解该函数的作用,并且使用该函数
"""
def_list = []
def show_all_def(def_list):
    def_count = 1
    for def_ in def_list:
        print("%d. 函数名:%s\t函数文档:%s" %(def_count,def_["def_name"],def_["def_document"]))
        def_count += 1
    input_index = int(input("请输入要执行函数的索引:"))
    print(eval(def_list[input_index - 1]["def_name"] + "()"))

""" TODO 将字符串 'Hello World!' 存储到变量str1中，
    再将字符串 'Hello Nowcoder!'存储到变量str2中，
    再使用print语句将其打印出来（一行一个变量）。
"""
def multiline_output():
    str1 = "Hello World"
    str2 = "Hello Nowcoder!"
    print("%s\n%s" % (str1,str2))
    print("-" * 40)
    return
dict_ = {"def_name":"multiline_output","def_document":"多行输出"}
def_list.append(dict_)

""" TODO 小白正在学习Python，从变量输出开始。
    请使用input函数读入一个字符串，然后将其输出。
"""
def output_string():
    input_str = input("请输入一个字符串：")
    print("用户输入的字符串为：%s" % type(input_str))
    print("-" * 40)
    return
dict_ = {"def_name":"output_string","def_document":"输出字符串"}
def_list.append(dict_)

""" TODO 在学会读入字符串以后，小白还想要读入整数，
    请你帮他使用input函数读入数字并输出数字与变量类型。
:param 输入只有整数
"""
def output_int():
    input_int = int(input("请输入一个整数:"))  #input函数返回值为string类型
    print("用户输入的整数:%s\n整数的类型:%s" %(input_int,type(input_int)))
    print("-" * 40)
    return
dict_ = {"def_name":"output_int","def_document":"输出整数"}
def_list.append(dict_)

""" TODO 假设输入的name为Niuniu，则输出I am Niuniu and I am studying Python in Nowcoder!
    请按以上句式输出相应的英文句子。
"""
def output_sentence():
    input_name = input("请输入学生姓名:")
    print("I am %s and I am studying Python in Nowcoder!" % input_name)
    print("-" * 40)
    return
dict_ = {"def_name": "output_sentence", "def_document": "输入姓名，输出句子"}
def_list.append(dict_)

""" TODO 牛牛正在学习Python的输出，他想要使用print函数控制小数的位数，你能帮助它把所有读入的数据都保留两位小数输出吗？
"""
def reserve_decimal():
    input_decimal = float(input("请输入需要保留两位小数的数值:"))
    print("%s保留两位小数结果为:%.2f" % (input_decimal,input_decimal))
    print("-" * 40)
dict_ = {"def_name": "reserve_decimal", "def_document": "输入小数，保留小数点后两位"}
def_list.append(dict_)

""" TODO 日常生活中我们会遇到很多小数，但是有的人不喜欢小数，因此会用四舍五入的方式将其去掉。
    在Python中我们更加简单，可以利用强制类型转换将小数转变成整数，请你试一试。
"""
def integer_to_decimal():
    input_decimal_ = float(input("请输入待转换为整数的小数:"))
    print("%s经过强制类型转换为%s" %(input_decimal_,int(input_decimal_)))
    print("-" * 40)
    return
dict_ = {"def_name": "integer_to_decimal", "def_document": "输入整数，结果转换为小数"}
def_list.append(dict_)

""" TODO 虽说很多人讨厌小数点，但是有时候小数点是必不可少的一项，
    请你使用强制类型转换为输入的整数增加小数点，并输出改变类型后的变量类型。
"""
def decimal_to_integer():
    input_int_ = int(input("请输入待转换为小数的整数:"))
    print("%s经过强制类型转换为%s,且转换后的数据类型为%s" %(input_int_,float(input_int_),type(float(input_int_))))
    print("-" * 40)
    return
dict_ = {"def_name": "decimal_to_integer", "def_document": "输入小数，结果转换为整数"}
def_list.append(dict_)

""" TODO input读入一个十六进制数字，input读入一个十六进制的数字，输出它的十进制数字是多少
    按照字符串的形式包括数字0-9、字母A-F。
"""
def hex_to_decimal():
    input_hex = input("请输入一个16进制的数值，包括0-9，A-F:")
    print("十六进制数字%s,转换为十进制的数值为:%s" %(input_hex,int(input_hex,16)))
    print("-" * 40)
    return
dict_ = {"def_name": "hex_to_decimal", "def_document": "输入16进制数，结果转换为十进制数"}
def_list.append(dict_)

""" TODO  牛牛有两个最好的朋友，他们的名字分别用input读入记录在两个字符串中，
    请使用字符串连接（+）帮助牛牛将两个朋友的名字依次连接在一个字符串中输出。
"""
def string_connect():
    input_name1 = input("请输入一个姓名:")
    input_name2 = input("请再输入一个姓名:")
    print("两个姓名相加得:%s + %s = %s" %(input_name1,input_name2,input_name1+input_name2))
    print("-" * 40)
    return
dict_ = {"def_name": "string_connect", "def_document": "用+进行字符串连接"}
def_list.append(dict_)

""" TODO 牛妹正在学英语，但是背单词实在是太痛苦了，她想让你帮她写一个小程序，能够根据输入的单词，快速得到单词的长度。
"""
def calculate_string_length():
    input_word = input("请输入要计算长度的单词:")
    print("单词%s的长度为:%s" %(input_word,len(input_word)))
    print("-" * 40)
    return
dict_ = {"def_name": "calculate_string_length", "def_document": "内置函数len，计算字符串的长度"}
def_list.append(dict_)

""" TODO 牛牛、牛妹和牛可乐都是Nowcoder的用户，某天Nowcoder的管理员希望将他们的用户名以某种格式进行显示，
    现在给定他们三个当中的某一个名字name，请分别按全小写、全大写和首字母大写的方式对name进行格式化输出（注：每种格式独占一行）。
"""
def transfer_lower_upper():
    input_name_ =input("请输入要不同格式输出的姓名:")
    print("将姓名%s全小写为:%s\n将姓名%s全大写为:%s\n将姓名%s首字母大写为:%s" %(
        input_name_,input_name_.lower(),input_name_,input_name_.upper(),input_name_,input_name_.title()))
    print("-" * 40)
    return
dict_ = {"def_name": "transfer_lower_upper", "def_document": "内置函数lower()/upper()/title()，改变字符串内大小写"}
def_list.append(dict_)

""" TODO 牛牛、牛妹和牛可乐都是Nowcoder的用户，某天Nowcoder的管理员由于某种错误的操作导致他们的用户名的左右两边增加了一些
    多余的空白符（如空格或'\t'等），现在给定他们三个当中的某一个名字name，请输出name去掉两边的空白符后的原本的内容。
"""
def remove_string_bilateral_space():
    input_name__ = input("请输入要去除掉两边空白字符的姓名:")
    print("%s去除两边空白字符的结果为:%s" %(input_name__,input_name__.strip()))
    print("-" * 40)
    return
dict_ = {"def_name": "remove_string_bilateral_space", "def_document": "内置函数strip()，去掉字符串两边的空格"}
def_list.append(dict_)

""" TODO 牛牛正在学习Python，他想多次输出朋友的名字，但是因为还没有学习循环语句，他不知道该怎么输出，
    你能够帮助他将输入的朋友的名字重复输出100次吗？（提示：不可以使用循环或者递归语句，使用字符串 * 运算）
"""
def output_repeat_name():
    input_repeat_name = input("请输入要重复输出100次朋友的名字:")
    print("将名字重复100次，结果为:")
    print("%s\t" %(input_repeat_name) * 100)
    return
dict_ = {"def_name": "output_repeat_name", "def_document": "输出重复的名字"}
def_list.append(dict_)

""" TODO 牛客网正在录入用户的昵称，但是有的昵称太长了，对于这些过长的昵称，
    牛牛觉得截取昵称字符串前10个字符就可以了
"""
def cutout_string():
    cutout_str = input("请输入需要截取的前10位的字符串：")
    print("%s\t截取前10位后的结果位为：\t%s" %(cutout_str,cutout_str[:10]))
    return
dict_ = {"def_name": "cutout_string", "def_document": "截取字符串的前10位"}
def_list.append(dict_)

""" TODO 某公司在面试结束后，创建了一个依次包含字符串 'Allen' 和 'Tom' 的列表offer_list，作为通过面试的名单。
    请你依次对列表中的名字发送类似 'Allen, you have passed our interview and will soon become a member of our company.' 
    的句子。但由于Tom有了其他的选择，没有确认这个offer，HR选择了正好能够确认这个offer的Andy，
    所以请把列表offer_list中 'Tom' 的名字换成 'Andy' ，再依次发送类似 'Andy, welcome to join us!' 的句子。
"""
def send_offer():
    offer_list = ['Allen','Tom']
    for name in offer_list:
        print("%s, you have passed our interview and will soon become a member of our company." % name)
    offer_list[1] = 'Andy'
    for name in offer_list:
        print("%s, welcome to join us!" % name)
    return
dict_ = {"def_name": "send_offer", "def_document": "给两位应聘者发送offer."}
def_list.append(dict_)

""" TODO 一串连续的数据用什么记录最合适，牛牛认为在Python中非列表（list）莫属了。
    现输入牛牛朋友们的名字，请使用list函数与split函数将它们封装成列表，再整个输出列表。
"""
def string_compound_list():
    name_string = input("请输入多个姓名，用空格分隔:")
    print("字符串\'%s\'\t经空格切片后得姓名列表为：%s" %(name_string,name_string.split(" ",-1)))
    return
dict_ = {"def_name": "string_compound_list", "def_document": "将字符串经分隔符空格转成列表."}
def_list.append(dict_)

""" TODO 牛牛在牛客网系统录入了一连串数字，数字之间依靠逗号隔开，
    你能帮助他将这些数字存储在列表中吗，列表元素以int的形式。 
"""
def string_to_int_list():
    integater_string = input("请输入多个数字，用英文逗号分隔：")
    string_list = integater_string.split(",",-1)
    index = 0
    for val in string_list:
        string_list[index] = int(string_list[index])
        index += 1
    print("字符串\'%s\'\t经逗号切片后得数字列表为：%s" %(integater_string,string_list))
    return
dict_ = {"def_name": "string_to_int_list", "def_document": "将字符串经分隔符逗号转成列表."}
def_list.append(dict_)

""" TODO 牛牛学会了使用list函数与split函数将输入的连续字符串封装成列表，
    你能够帮他使用len函数统计一些公输入了多少字符串，列表中有多少元素吗？
"""
def calculate_list_length():
    input_string = input("请输入用空格分隔的多个字符串")
    string_list = input_string.split(" ",-1)
    print("字符串\'%s\'用空格分隔后转换成列表后的长度为：%s" %(input_string,len(string_list)))
    return
dict_ = {"def_name": "calculate_list_length", "def_document": "计算字符串用空格分隔后的字符串个数."}
def_list.append(dict_)

""" TODO 为庆祝驼瑞驰在牛爱网找到合适的对象，驼瑞驰通过输入的多个连续字符串创建了一个列表作为派对邀请名单，
    在检查的时候发现少了他最好的朋友“Allen”的名字，你能使用append函数将这个名字加到列表末尾吗？添加完成请输出完整列表。
"""
def name_list_append():
    name_string = input("请输入婚礼要邀请的人员姓名，用空格分隔：")
    name_list = name_string.split(" ",-1)
    while True:
        new_name = input("请输入要补充的人员姓名(如果没有补充人员，可输入0，输出所有人员)：")
        if new_name == '0':
            break
        name_list.append(new_name)
    print("输出的总的人员名单为：%s" % name_list)
    return
dict_ = {"def_name": "name_list_append", "def_document": "策划婚礼的人员名单，可输入补充的人员."}
def_list.append(dict_)

""" TODO 为庆祝驼瑞驰在牛爱网找到合适的对象，驼瑞驰通过输入的多个连续字符串创建了一个列表作为派对邀请名单，
    在检查的时候发现少了他最好的朋友“Allen”的名字，因为是最好的朋友，他想让这个名字出现在邀请列表的最前面，
    你能用insert函数帮他实现吗？请输出插入后的完整列表。
"""
def name_list_insert():
    name_string = input("请输入婚礼要邀请的人员姓名，用空格分隔：")
    name_list = name_string.split(" ", -1)
    while True:
        new_name = input("请输入要补充的人员姓名(如果没有补充人员，可输入0，输出所有人员)：")
        if new_name == '0':
            break
        name_list.insert(0,new_name)
    print("输出的总的人员名单为：%s" % name_list)
    return
dict_ = {"def_name": "name_list_insert", "def_document": "策划婚礼的人员名单，可输入补充的人员."}
def_list.append(dict_)

""" TODO 牛牛在各大互联网公司投入了简历，公司的名字通过字符串的形式在一行中输入，请用列表记录。
    现在牛牛已经确定了第一所公司的HR表露了不录用他的态度，请你使用del函数帮助牛牛从列表中删除第一个元素，然后输出列表。
"""
def company_list():
    company_name = input("请输入所有的公司名字，用英文逗号分隔：")
    company_list = company_name.split(",",-1)
    print("所有公司列表如下：%s" % company_list)
    del_name = input("请输入要删除的公司的名字:")
    del company_list[company_list.index(del_name)]
    print("删除后的公司名字如下：%s" % company_list)
    return
dict_ = {"def_name": "company_list", "def_document": "显示所有公司名单，并且删除对应公司."}
def_list.append(dict_)

""" TODO 牛妹有一个坏习惯，一旦与朋友吵架了，她就要删除好友。现在输入一个行多个字符串表示牛妹的朋友，
    请把它们封装成列表，然后再输入与牛妹吵架的朋友的名字，请使用remove函数帮她从列表中删除这个好友，然后输出完整列表。
"""
def friend_list():
    friend_name = input("请输入所有的朋友名字，用英文逗号分隔：")
    friend_list = friend_name.split(",",-1)
    print("所有朋友列表如下：%s" % friend_list)
    del_name = input("请输入要删除的朋友的名字:")
    friend_list.remove(del_name)
    print("删除后的朋友名字如下：%s" % friend_list)
    return
dict_ = {"def_name": "friend_list", "def_document": "显示所有朋友名字，并且删除吵过架的朋友."}
def_list.append(dict_)

""" TODO 某实验班实行末位淘汰制，期中考试需要淘汰末三位同学。
    现输入一行多个字符串表示按分数排名的该班级同学的名字（数量一定不少于三个），
    请你使用list将其封装为列表，然后使用三次pop函数，去掉末三位同学的名字，最后输出淘汰后的班级名字列表。
"""
def weed_out_schoolmate():
    input_schoolmate = input("请输入所有同学们的名字，用引文逗号分隔：")
    schoolmate_list = input_schoolmate.split(",",-1)
    print("显示所有同学的列表为：%s" % (schoolmate_list))
    schoolmate_list.pop()
    print("淘汰最后一名后，班级显示为：%s" %(schoolmate_list))
    return
dict_ = {"def_name": "weed_out_schoolmate", "def_document": "班级列表，淘汰班级的最后一名同学."}
def_list.append(dict_)

""" TODO 创建一个依次包含字符串'P'、'y'、't'、'h'、'o'和'n'的列表my_list，先使用sorted函数对列表my_list进行临时排序，
    第一行输出排序后的完整列表，第二行输出原始的列表。再使用sort函数对列表my_list进行降序排序，第三行输出排序后完整的列表。
"""
def sort_list():
    sort_list = ["P","y","t","h","o","n"]
    print("原始列表：%s" %(sort_list))
    sort_list.sort()
    print("升序后的列表：%s" %sort_list)
    sort_list.sort(reverse=True)
    print("降序后的列表：%s" %sort_list)
    return
dict_ = {"def_name": "sort_list", "def_document": "对列表进行升序，降序."}
def_list.append(dict_)

""" TODO 牛牛有一个列表记录了各个朋友的喜欢的数字，num = [3, 5, 9, 0, 1, 9, 0, 3]，请你帮他创建列表，然后使用reverse函数将列表反转输出。
"""
def reverse_list():
    number_list = [3,5,9,0,1,9,0,3]
    print("原列表为：%s" % number_list)
    number_list.reverse()
    print("翻转后的列表为：%s" % number_list)
    return
dict_ = {"def_name": "reverse_list", "def_document": "对列表进行翻转."}
def_list.append(dict_)

""" TODO 多维列表,我的朋友们的喜好.
"""
def multiple_list():
    friends_like = []
    name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona']
    friends_like.append(name)
    food = ["pizza","fish","potato","beef"]
    friends_like.append(food)
    number = [3,6,0,3]
    friends_like.append(number)
    for list_ in friends_like:
        print("%s" % list_)
    return
dict_ = {"def_name": "multiple_list", "def_document": "多维列表,我的朋友们的喜好."}
def_list.append(dict_)

""" TODO 牛牛和牛妹一起玩密码游戏，牛牛作为发送方会发送一个4位数的整数给牛妹，牛妹接收后将对密码进行破解。
    破解方案如下：每位数字都要加上3再除以9的余数代替该位数字，然后将第1位和第3位数字交换，第2位和第4位数字交换。
    请输出牛妹破解后的密码。
"""
def play_game():
    input_number = input("请输入一个四位数的整数：")
    input_index = 0
    input_list = []
    for number_ in input_number:
        input_list.append((int(number_)+3)%9)
        input_index += 1
    input_list[0],input_list[1],input_list[2],input_list[3] = input_list[2],input_list[3],input_list[0],input_list[1]
    print(input_list)
    return
dict_ = {"def_name": "play_game", "def_document": "四位数的整数进行破解密码."}
def_list.append(dict_)

""" TODO 栈是一种先进后出的数据结构，类似我们生活中挤电梯，最后进入的肯定是先出来，现我们用Python的列表来模拟栈。
    假设初始的列表为 stack = [1, 2, 3, 4, 5]，请将其视作栈，使用pop函数弹出末尾两个元素，
    再使用append函数将输入元素加入到栈中，每次操作完成后都要输出整个列表。
"""
def cometrue_stack():
    stack = [1,2,3,4,5]
    # 定义要出栈的元素个数,out_stack
    out_stack = 2
    while out_stack >= 0:
        stack.pop()
        out_stack -= 1
    print("两个元素出栈后的列表为：%s" % stack)
    stack.append(4)
    stack.append(5)
    print("两个元素入栈后的结果为：%s" % stack)
    pass
dict_ = {"def_name": "cometrue_stack", "def_document": "python模拟栈结构进行出栈/入栈操作."}
def_list.append(dict_)

""" TODO 队列是一种先进先出的数据结构，类似食堂排队打饭，先入队的元素当然要先出队，先请用Python列表模拟队列。
    现有一列表 queue = [1, 2, 3, 4, 5] 被视作队列，请使用pop函数连续两次取出队首元素，
    再使用append函数将输入元素添加到队尾，每次操作后都要输出完整的列表。
"""
def cometrue_queue():
    queue = [1,2,3,4,5]
    # 定义要出队列的元素个数,out_stack
    out_queue = 2
    while out_queue > 0:
        queue.pop(0)
        out_queue -= 1
    print("两个元素出队列后的列表为：%s" % queue)
    queue.append(1)
    queue.append(2)
    print("两个元素入队列后的结果为：%s" % queue)
    pass
dict_ = {"def_name": "cometrue_queue", "def_document": "python模拟队列结构进行出队列/入队列操作."}
def_list.append(dict_)

""" TODO 创建一个列表group_list，其中依次包含字符串 'Tom', 'Allen', 'Jane', 'William', 'Tony' 表示这个小组成员的名字。
    现有三项任务需要他们去完成，根据不同任务的繁琐度和实际情况需要分别派2人、3人、2人来完成，他们决定通过对列表分片来分配任务。
    使用print()语句和切片来打印列表group_list的前两个元素表示去做第一个任务的人的名字，
    再使用print()语句和切片来打印列表group_list的中间三个元素表示去做第二个任务的人的名字，
    再使用print()语句和切片来打印列表group_list的后两个元素表示去做第三个任务的人的名字。
"""
def section_list():
    group_list = ['Tom','Allen','Jane','William','Tony']
    print("所有成员：%s" %(group_list))
    print("执行第一个任务的成员为：%s" %(group_list[:2]))
    print("执行第二个任务的成员为: %s" %(group_list[1:4]))
    print("执行第三个任务的成员为：%s" %(group_list[-2:]))
dict_ = {"def_name": "section_list", "def_document": "列表的切片，分组执行任务."}
def_list.append(dict_)

""" TODO 为了辅导刚上小学的妹妹做功课，牛牛想用Python写一个加减器帮助妹妹巩固加减运算。现要求输入两个数字x与y，分别输出x+y的结果和x-y的结果。
"""
def add_subtract():
    number1 = int(input("请输入第一个数字："))
    number2 = int(input("请输入第二个数字："))
    print("两数相加得：%s" %(number1+number2))
    print("两数相减得：%s" %(number1-number2))
    pass
dict_ = {"def_name": "add_subtract", "def_document": "计算两数相加减."}
def_list.append(dict_)

""" TODO 刚刚学习Python的牛牛发现，同样的符号出现两次可能代表不同的运算，比如*与**。现输入两个数字x与y，请分别计算x * y 与 x的y次幂。
"""
def multiplication_calculate():
    x = int(input("请输入第一个数字："))
    y = int(input("请输入第二个数字："))
    print("x * y = %s" % (x * y))
    print("x的y次幂 = %s" % (x ** y))
    pass
dict_ = {"def_name": "multiplication_calculate", "def_document": "计算两数相乘和次幂."}
def_list.append(dict_)

""" TODO 我们都知道在计算机里除法有两种，一种是整除，结果有商和余数，另一种则是将其除到有小数。现输入两个数字x与y，分别计算两种除法下x/y的结果。
"""
def divisor_calculate():
    x = int(input("请输入第一个数字："))
    y = int(input("请输入第二个数字："))
    print("x / y = %s" % (x / y))
    print("x %% y = %s" % (x % y))
    pass
dict_ = {"def_name": "divisor_calculate", "def_document": "计算两数相除和取余."}
def_list.append(dict_)

""" TODO 牛牛有一个习惯，新认识一个朋友他就想知道这个朋友和自己的年龄是不是一样大，输入两个整数表示牛牛的年龄和朋友的年龄，
    请输出牛牛的年龄是否等于朋友的年龄的比较结果？
"""
def compare_age():
    age1 = int(input("请输入牛牛的年龄："))
    age2 = int(input("请输入牛牛朋友的年龄："))
    if age1%age2 == 0:
        print("牛牛和她朋友的年龄相等")
    else:
        print("牛牛和她朋友的年龄不相等")
    pass
dict_ = {"def_name": "compare_age", "def_document": "比较牛牛和她朋友的年龄."}
def_list.append(dict_)

""" TODO 牛牛在和牛妹玩猜数字游戏，他们想请你写一个快速判断牛牛的数字是不是大于牛妹数字的程序。
    输入两个整数，以空格间隔，输出第一个数字是否大于第二个数字，第一个数字是否小于第二个数字。
"""
def compare_big():
    number_str = input("请输入两个数字，用空格分开: ")
    number_list = number_str.split(" ",-1)
    if int(number_list[0]) - int(number_list[1]) > 0:
        print("牛牛输入的数字大一些")
    elif int(number_list[0]) - int(number_list[1]) == 0:
        print("牛牛和牛妹输入的数字一样大")
    else:
        print("牛妹输入的数字大一些")
    pass
dict_ = {"def_name": "compare_big", "def_document": "比较牛牛和牛妹输入的数字谁的大."}
def_list.append(dict_)

""" TODO 牛妹去游乐园，对于某项目，如果牛妹的身高k不超过某个标准x，就不需要收取额外费用，
    但是该项目有需要身高不低于y才可以保障安全。现依次输入三个数字k、x、y，牛妹想让你帮她比较一下，她的身高是否不超过x，是否不低于y。
"""
def belong_to_section():
    input_ceil = int(input("请输入身高的上线："))
    input_floor = int(input("请输入身高的下限："))
    input_height = int(input("请输入具体的身高："))
    if input_ceil - input_height > 0 and input_floor - input_height < 0:
        print("她的身高低于上限身高，高于下限身高，可以通过。")
    elif input_ceil - input_height < 0:
        print("她的身高高于上限身高，不可以通过")
    elif input_floor - input_height > 0:
        print("她的身高低于下限身高，运行此项目不安全，不可以通过。")
dict_ = {"def_name": "belong_to_section", "def_document": "测试身高是否符合项目的身高要求."}
def_list.append(dict_)

""" TODO 牛牛想要锻炼自己的逻辑能力，于是输入了两个整型变量x和y，分别判断它们的与、或、非关系，你能帮他输出x与y，x或y，非x，非y的值吗？
"""
def and_or_not():
    number1 = int(input("请输入一个数值："))
    number2 = int(input("请输入判断的另一个数值："))
    print("%s & %s = %s" %(number1,number2,number1 & number2)) #相同为1，不同为0
    print("%s ｜ %s = %s" %(number1,number2,number1 | number2))  #有1则1，无1则0
    print("%s ^ %s = %s" %(number1,number2,number1 ^ number2))  #不同为1，相同为0
    pass
dict_ = {"def_name": "and_or_not", "def_document": "判断两个值的按位与&，按位或｜，按位非^."}
def_list.append(dict_)

""" TODO 正在学习Python的牛可乐，对Python里面的大小比较很疑惑。他知道数字之间可以相等，有大小关系，但是字符串之间怎么比较，
    他就很纳闷了。现在牛可乐输入两个字符串s1与s2，请你帮他比较这两个字符串是否相等，两个字符串各自调用lower函数后还是否相等。
"""
def compare_string():
    str1 = input("请输入一个字符串：")
    str2 = input("请输入比较的另一个字符串：")
    print("比较字符串%s\t%s是否相等结果为 %s" %(str1,str2,str1 == str2))
    print("都执行lower函数后，再次比较字符串%s\t%s是否相等结果为 %s" %(str1,str2,str1.lower() == str2.lower()))
    pass
dict_ = {"def_name": "compare_string", "def_document": "比较两个字符串是否相等."}
def_list.append(dict_)

""" TODO 牛客网内部有一个刷题俱乐部，是大家比拼刷题与交流算法的地方。现在给出俱乐部的名单，请以列表的形式记录它们，
    并使用Python的成员运算检验给出的名字name是否属于这个俱乐部？（名字区分大小写）
"""
def if_include():
    name_list = ["xiaoLi","Xiaoming","xiaowang","XIAOLIU"]
    search_name = input("请输入要查询的会员姓名：")
    print("会员列表是否包含该会员结果为：%s" %(search_name in name_list))
    pass
dict_ = {"def_name": "if_include", "def_document": "判断会员列表是否包含某会员的姓名."}
def_list.append(dict_)

""" TODO Python有位运算，是直接将数字看成二进制，直接对二进制数字的每一位进行运算。
    现输入两个十进制整数x、y，请计算它们的位与、位或，输出按照十进制的形式。
"""
def and_or_binary():
    number1 = int(input("请输入一个数值："))
    number2 = int(input("请输入判断的另一个数值："))
    print("%s & %s = %s" %(number1,number2,number1 & number2)) #相同为1，不同为0
    print("%s ｜ %s = %s" %(number1,number2,number1 | number2))  #有1则1，无1则0
    pass
dict_ = {"def_name": "and_or_binary", "def_document": "判断两个值的按位与&，按位或｜."}
def_list.append(dict_)

""" TODO 牛客网为员工举行了一项快速心算大赛，需要程序员大大写一款涉及加减乘除的验算小程序。
    假如输入的数字分别是x、y、z、k，请输出x+y的结果与z-k的结果相乘的值。
"""
def metal_calculate():
    input_string = input("请输入四个值，用/隔开：")
    input_list = input_string.split("/",-1)
    x = int(input_list[0])
    y = int(input_list[1])
    z = int(input_list[2])
    k = int(input_list[3])
    print("(%s+%s)*(%s-%s)的结果为：%s" %(
        x,y,z,k,(x+y)*(z-k)
    ))
    pass
dict_ = {"def_name": "metal_calculate", "def_document": "加减乘的心算验算."}
def_list.append(dict_)

""" TODO Python的条件语句依靠将运算结果转变成布尔值后进行判断，然后分支，如果我们直接判断布尔值会怎么样呢？
    输入布尔变量，使用条件语句判断，如果为真则输出"Hello World!"，否则输出"Erros!"。
"""
def judge_bool_variable():
    input_bool = bool(input("请输入一个bool变量，首字母大写："))
    print(type(input_bool))
    if input_bool:
        print("Hello World!")
    else:
        print("Erros!")
    pass
dict_ = {"def_name": "judge_bool_variable", "def_document": "检验if语句是否可以判断bool变量."}
def_list.append(dict_)

""" TODO 创建一个空列表my_list，如果列表为空，请使用print()语句一行输出字符串'my_list is empty!'，
    否则使用print()语句一行输出字符串'my_list is not empty!'。
"""
def judge_list_isempty():
    list_isempty = [1]
    if len(list_isempty) == 0:
        print("my_list is empty!")
    else:
        print("my_list is not empty!")
    pass
dict_ = {"def_name": "judge_list_isempty", "def_document": "判断列表是否为空."}
def_list.append(dict_)

""" TODO 创建一个依次包含字符串'Niuniu'、'Niumei'、'GURR'和'LOLO'的列表current_users，
    再创建一个依次包含字符串'GurR'、'Niu Ke Le'、'LoLo'和'Tuo Rui Chi'的列表new_users，
    使用for循环遍历new_users，如果遍历到的新用户名在current_users中，
    则使用print()语句一行输出类似字符串'The user name GurR has already been registered! Please change it and try again!'的语句，
    否则使用print()语句一行输出类似字符串'Congratulations, the user name Niu Ke Le is available!'的语句。（注：用户名的比较不区分大小写）
"""
def judge_isinclude():
    current_users = [x.lower() for x in ['Niuniu','Niumei','GURR','LOLO']]
    new_users = [x.lower() for x in ['GurR','Niu Ke Le','LoLo','Tuo Rui Chi']]
    for user in new_users:
        if user in current_users:
            print("The user name GurR has already been registered! Please change it and try again!")
        else:
            print("Congratulations, the user name Niu Ke Le is available!")
    pass
dict_ = {"def_name": "judge_isinclude", "def_document": "判断你用户是否存在某个列表中."}
def_list.append(dict_)

""" TODO 牛客食堂今天准备了很多丰盛的午餐， 'pizza'：10块钱一份，'rice' ：2块钱一份，'yogurt'：5块钱一份，
    剩下的其他菜品都是8块钱一份。牛牛在某窗口点餐，请你根据他输入的字符串，使用if-elif-else语句判断牛牛需要花费多少钱？
"""
def calculate_lunch_price():
    PIZZA_PRICE = 10
    RICE_PRICE = 2
    YOGURT_PRICE = 5

    total_price = 0
    while True:
        input_greens = input("请输入牛牛在牛客食堂点点菜(按0退出)：")
        if input_greens == "pizza":
            total_price += PIZZA_PRICE
        elif input_greens == "rice":
            total_price += RICE_PRICE
        elif input_greens == "yogurt":
            total_price += YOGURT_PRICE
        else:
            break
    print("牛牛点餐总价格为：%s" % total_price)
dict_ = {"def_name": "calculate_lunch_price", "def_document": "计算点餐价格."}
def_list.append(dict_)

""" TODO 牛牛在门头沟大学学习，一学年过去了，需要根据他的成绩计算他的平均绩点，假如绩点与等级的对应关系如下表所示。
    请根据输入的等级和学分数，计算牛牛的均绩（每门课学分乘上单门课绩点，求和后对学分求均值）。
    A   4.0
    B   3.0
    C   2.0
    D   1.0
    F   0
"""
def average_grade():
    dict_credit = {"A":4.0,"B":3.0,"C":2.0,"D":1.0,"F":0}
    credit_sum = 0
    grade_sum = 0
    while True:
        input_credit = input("请输入学分：")
        if input_credit == "False":
            break
        input_grade = float(input("请输入学分对应的成绩："))
        if input_credit == "A":
            grade_sum += input_grade * dict_credit['A']
            credit_sum +=dict_credit[input_credit]
        elif input_credit == "B":
            grade_sum += input_grade * dict_credit['B']
            credit_sum += dict_credit[input_credit]
        elif input_credit == "C":
            grade_sum += input_grade * dict_credit['C']
            credit_sum += dict_credit[input_credit]
        elif input_credit == "D":
            grade_sum += input_grade * dict_credit['D']
            credit_sum += dict_credit[input_credit]
        elif input_credit == "F":
            grade_sum += input_grade * dict_credit['F']
            credit_sum += dict_credit[input_credit]

    print("该学生的成绩的均值为：%.2f" % float(grade_sum/credit_sum))
dict_ = {"def_name": "average_grade", "def_document": "计算学生的总成绩的均值."}
def_list.append(dict_)

""" TODO 牛客网的登录系统需要验证用户名与密码，当二者都正确时才允许登录，
    其中管理员的用户名为'admis'，密码为'Nowcoder666'。请你使用if-else语句，根据输入的用户名ID和密码，判断该用户等否登录。
"""
def verify_user_password():
    input_user = input("请输入你的用户名：")
    input_password = input("请输入你的密码：")
    if input_user == 'admis' and input_password == 'Nowcoder666':
        print("Welcome")
    else:
        print("user id or password is not correct!")
    pass
dict_ = {"def_name": "verify_user_password", "def_document": "验证登陆的用户名和密码."}
def_list.append(dict_)

""" TODO 创建一个依次包含字符串'P'、'y'、't'、'h'、'o'和'n'的列表my_list，
    使用print()语句一行打印字符串'Here is the original list:'，再直接使用print()语句把刚刚创建的列表my_list整个打印出来，
    输出一个换行，再使用print()语句一行打印字符串'The number that my_list has is:'，
    再使用len()函数获取列表my_list里面有多少个字符串，并使用print()函数一行打印该整数。
"""
def string_list_length():
    my_list = ['P','y','t','h','o','n']
    print("Here is the original list:",my_list)
    print("The number that my_list has is:",len(my_list))
    pass
dict_ = {"def_name": "string_list_length", "def_document": "打印列表长度."}
def_list.append(dict_)

""" TODO 牛牛、牛妹和牛可乐都是Nowcoder的忠实用户，又到了一年一度的程序员节（10月24号），毫无疑问，他们都登录Nowcoder了，因为他们还没有刷完牛客题霸...
    Nowcoder的管理员想对他们发送一些简单登录问候消息，并对他们表达了节日祝福。
    请创建一个依次包含字符串 'Niuniu' 、'Niumei' 和 'Niu Ke Le' 的列表users_list，
    请使用for循环遍历列表user_list，依次对列表users_list中的名字输出一行类似 'Hi, Niuniu! Welcome to Nowcoder!' 的字符串，
    for循环结束后，最后输出一行字符串 "Happy Programmers' Day to everyone!"
"""
def cyclic_input_Hi():
    users_list = ['Niuniu','Niumei','Niu Ke Le']
    for user in users_list:
        print("Hi, %s! Welcome to Nowcoder!" % user)
    print("Happy Programmers' Day to everyone!")
    pass
dict_ = {"def_name": "cyclic_input_Hi", "def_document": "给列表成员循环输出问候语."}
def_list.append(dict_)

""" TODO 牛牛刚学循环语句，你能教他使用for语句创建一个从10到50的数字列表吗？
    请输出完整列表，并输出列表的首尾元素检验是否是从10到50.
"""
def cycli_input_number():
    number_list = []
    for sz in range(10,51):
        number_list.append(sz)
    print(number_list)
    print(number_list[0],number_list[-1])
    pass
dict_ = {"def_name": "cycli_input_number", "def_document": "for循环创建10-50的列表."}
def_list.append(dict_)

""" TODO 牛牛有一个列表，记录了他和同事们的年龄，你能用for循环遍历链表的每一个元素，将其累加求得他们年龄的总和与平均数吗？
"""
def calculate_sum_average():
    input_str = input("请输入你和同事们的年龄，用空格隔开：")
    age_list = input_str.split(" ",-1)
    average_ = 0
    sum = 0
    for age_ in age_list:
        sum += int(age_)
    print("所有同时年龄和为：%s，平均数为%.1f" % (sum,sum/(len(age_list))))
    pass
dict_ = {"def_name": "calculate_sum_average", "def_document": "求所有同事的年龄总数和平均数."}
def_list.append(dict_)

""" TODO 通过给函数 range()指定第三个参数来创建一个列表my_list，其中包含 [0, 19]  中的所有偶数；
    再使用一个 for 循环将这些数字都打印出来（每个数字独占一行）。
"""
def front_even():
    my_list = []
    for number in range(0,20,2):
        my_list.append(number)
        print(number)
    pass
dict_ = {"def_name": "front_even", "def_document": "range的第三个参数是步长,step."}
def_list.append(dict_)

""" TODO 创建一个列表my_list，其中包括 [1, 50] 内全部能被5整除的数字；再使用一个 for 循环将这个列表中的数字都打印出来（每个数字独占一行）。
"""
def five_multiple():
    my_list = []
    for number in range(0, 50, 5):
        my_list.append(number)
        print(number)
    pass
dict_ = {"def_name": "five_multiple", "def_document": "输出1-50以内的5的倍数。"}
def_list.append(dict_)

""" TODO 在Python中， * 代表乘法运算， ** 代表次方运算。
    请创建一个空列表my_list，使用for循环、range()函数和append()函数令列表my_list包含底数2的 [1, 10] 次方，
    再使用一个 for 循环将这些次方数都打印出来（每个数字独占一行）。
"""
def two_power():
    my_list = []
    for number in range(1, 11):
        my_list.append(2 ** number)
        print(2 ** number)
    pass
dict_ = {"def_name": "two_power", "def_document": "输出2的次方数。"}
def_list.append(dict_)

""" TODO Python支持的解析操作，可以根据某些元素创建列表。请你使用列表解析创建一个0-9的列表，并输出该列表。
"""
def list_analysis():
    my_list = [x for x in range(0,10)]
    print("列表推导式解析的列表：",my_list)
    pass
dict_ = {"def_name": "list_analysis", "def_document": "列表推导式解析的列表。"}
def_list.append(dict_)

""" TODO 牛妹有一个暑期想吃的东西的清单，你可以把它视作一个Python的list，
    ['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']。
    牛妹决定从清单最后一种食物开始往前吃，每次吃掉一种食物就把它从list中pop掉，请使用while循环依次打印牛妹每次吃掉一种食物后剩余的清单。
"""
def format_list():
    my_list = ['apple','ice cream','watermelon','chips','hotdogs','hotpot']
    while my_list != []:
        my_list.pop()
        print(my_list)
    pass
dict_ = {"def_name": "format_list", "def_document": "格式化清单，while循环，pop函数。"}
def_list.append(dict_)

""" TODO 创建一个依次包含字符串'Niuniu'、'Niumei'、'HR'、'Niu Ke Le'、'GURR' 和 'LOLO' 的列表users_list，
    使用for循环遍历users_list，如果遍历到的用户名是 'HR' ，
    则使用print()语句一行打印字符串 'Hi, HR! Would you like to hire someone?'，
    否则使用print()语句一行打印类似字符串 'Hi, Niuniu! Welcome to Nowcoder!' 的语句。
"""
def find_HR():
    users_list = ['Niuniu','Niumei','HR','Niu Ke Le','GURR','LOLO']
    for user in users_list:
        if user == "HR":
            print("Hi, HR! Would you like to hire someone?")
        else:
            print("Hi, %s! Would you like to hire someone?" % user)
    pass
dict_ = {"def_name": "find_HR", "def_document": "for循环查找内容输出"}
def_list.append(dict_)

""" TODO 牛牛在牛客网举行抽奖游戏，他准备了一个列表的元素[3, 45, 9, 8, 12, 89, 103, 42, 54, 79]，
    打算依次输出这些元素。他让牛妹随便猜一个数字x，在输出的时候如果输出的元素等于牛妹猜的x，就不再继续输出。
    请你使用Python的for循环模拟这个输出过程，并根据输入的x使用break语句提前结束循环。
"""
def end_cyclic():
    my_list = [3,45,9,8,12,89,103,42,54,79]
    input_int = int(input("请猜测一个数字："))
    for number in my_list:
        if input_int == number:
            print(number,end=" ")
            break
        else:
            print(number,end=" ")
    pass
dict_ = {"def_name": "end_cyclic", "def_document": "break结束循环"}
def_list.append(dict_)

""" TODO 牛客网在玩数数字游戏，员工一致认为13是一个“不详的数字”，请你使用for循环帮他们从1数到15，并使用continue语句跳过13。
"""
def jump_number():
    for number in range(1,16):
        if number == 13:
            continue
        else:
            print(number,end=" ")
    pass
dict_ = {"def_name": "jump_number", "def_document": "for循环用continue跳过指定数字"}
def_list.append(dict_)

""" TODO 牛牛正在做矩阵运算，他知道n个矩阵相加，就是将矩阵中每个位置的元素都乘上n。现有一个矩阵
    1 2 3
    4 5 6
    7 8 9，请使用list记录该矩阵，对于牛牛输入的数字n，输出n个该矩阵相加的结果。
"""
def matrix_add():
    matrix_list = [[1,2,3],[4,5,6],[7,8,9]]
    print("原始矩阵为：%s" %(matrix_list))
    input_n = int(input("请输入一个数值："))
    for row in matrix_list:
        index = 0
        for column in row:
            row[index] = column * input_n
            index += 1
    print("计算之后的矩阵为:%s" % (matrix_list))
    pass
dict_ = {"def_name": "matrix_add", "def_document": "多层循环累加"}
def_list.append(dict_)

""" TODO 牛客运动会上有一项双人项目，因为报名成功以后双人成员不允许被修改，因此请使用元组（tuple）进行记录。
    先输入两个人的名字，请输出他们报名成功以后的元组。
"""
def create_tuple():
    input_name1 = input("请输入成员姓名：")
    input_name2 = input("请输入成员姓名：")
    tuple_list = (input_name1,input_name2)
    print(tuple_list)
    pass
dict_ = {"def_name": "create_tuple", "def_document": "新建元组"}
def_list.append(dict_)

""" TODO 牛牛和牛妹报名了牛客运动会的双人项目，但是由于比赛前一天牛妹身体不适，不能参加第二天的运动，于是想让牛可乐代替自己。
    请创建一个依次包含字符串'Niuniu'和'Niumei'的元组entry_form，并直接输出整个元组。
    然后尝试使用try- except代码块执行语句：entry-form[1] = 'Niukele'，若是引发TypeError错误，请输出'The entry form cannot be modified!'。
"""
def modify_list():
    entry_form = ('Niuniu','Niumei')
    try:
        entry_form[1] = 'Niukele'
    except:
        print("The entry form cannot be modified!")
    pass
dict_ = {"def_name": "modify_list", "def_document": "修改元组，捕获异常try except"}
def_list.append(dict_)

""" TODO 学校录入考试排名信息以后，为了防止修改，都会记录为Python元组。
    请你根据输入的字符串，使用tuple函数将它们作为考生姓名记录到元组中，并使用切片法输出前三名同学的名字。
"""
def output_grade():
    input_str = input("请输入考试排名信息的学生姓名(用空格分开)：")
    tuple_list = tuple(input_str.split(" ",-1))
    print("输出前三名的学生姓名：",tuple_list[0:3])
    pass
dict_ = {"def_name": "output_grade", "def_document": "切片显示元组的前三名"}
def_list.append(dict_)

""" TODO 牛客网有一份秘密名单，['Tom', 'Tony', 'Allen', 'Cydin', 'Lucy', 'Anna']，请将它们创建为不可被修改的Python元组后，输出整个元组。
    对于牛牛输入的名字name，请使用成员运算检验它是否出现在这份秘密名单中，若是在名单中则输出'Congratulations!'，否则输出'What a pity!'.
"""
def judge_isinclude():
    secrecy_list = ('Tom','Tony','Allen','Cydin','Lucy','Anna')
    print("保密名单内容为：",secrecy_list)
    verify_name = input("请输入要查询是否在名单中的姓名：")
    if verify_name in secrecy_list:
        print("Congratulations!")
    else:
        print("What a pity!")
    pass
dict_ = {"def_name": "judge_isinclude", "def_document": "判断元组内是否包含指定内容。"}
def_list.append(dict_)

""" TODO 牛牛有一个元组，其中记录数字1-5，请创建该元组，并使用len函数获取该元组的长度。
    牛牛觉得这个元组太短了，想要在该元组后再连接一个6-10的元祖，请输出连接后的元组及长度。
"""
def increase_tuple_length():
    tuple_list = (1,2,3,4,5)
    print("原始元组为：%s,该元组长度为：%s" %(tuple_list,len(tuple_list)))
    new_tuple_list = tuple_list + (6,7,8,9,10)
    print("修改后元组为：%s,该元组长度为：%s" %(new_tuple_list,len(new_tuple_list)))
    pass
dict_ = {"def_name": "increase_tuple_length", "def_document": "给元组增加长度。"}
def_list.append(dict_)

""" TODO 创建一个依次包含键-值对'<': 'less than'和'==': 'equal'的字典operators_dict，
    先使用print()语句一行打印字符串'Here is the original dict:'，
    再使用for循环遍历 已使用sorted()函数按升序进行临时排序的包含字典operators_dict的所有键的列表，
    使用print()语句一行输出类似字符串'Operator < means less than.'的语句；

    对字典operators_dict增加键-值对'>': 'greater than'后，
    输出一个换行，再使用print()语句一行打印字符串'The dict was changed to:'，
    再次使用for循环遍历 已使用sorted()函数按升序进行临时排序的包含字典operators_dict的所有键的列表，
    使用print()语句一行输出类似字符串'Operator < means less than.'的语句，确认字典operators_dict确实新增了一对键-值对。
"""
def traverse_dict():
    operators_dict = {'<':"less than",'==':'equal'}
    print("Here is the original dict:",end=" ")
    sorted(operators_dict)
    for operators_key in operators_dict:
        print(operators_key,end=" ")
    print("Operator < means less than.")
    operators_dict['>'] = 'greater than'
    print("The dict was changed to:",end=" ")
    sorted(operators_dict)
    for operators_key in operators_dict:
        print(operators_key,end=" ")
    print("Operator < means less than.")
    pass
dict_ = {"def_name": "traverse_dict", "def_document": "对字典进行排序。新增键-值对"}
def_list.append(dict_)

""" TODO 又到了毕业季，牛牛作为牛客大学的学生会主席，决定对本校的应届毕业生进行就业调查。
    他创建了一个依次包含字符串'Niumei'、'Niu Ke Le'、'GURR'和'LOLO'的列表survey_list，作为调查名单；
    又创建了一个依次包含键-值对'Niumei': 'Nowcoder'和'GURR': 'HUAWEI'的字典result_dict，作为已记录的调查结果。
    请遍历列表survey_list，如果遍历到的名字已出现在 包含字典result_dict的全部键的列表 里，
    则使用print()语句一行输出类似字符串'Hi, Niumei! Thank you for participating in our graduation survey!'的语句以表达感谢，
    否则使用print()语句一行输出类似字符串'Hi, Niu Ke Le! Could you take part in our graduation survey?'的语句以发出调查邀请。
"""
def get_job_servey():
    survey_list = ['Niumei','Niu Ke Le','GURR','LOLO']
    result_dict = {'Niumei':'Nowcoder','GURR':'HUAWEI'}
    for survey_item in survey_list:
        if survey_item in result_dict:
            print("Hi, %s! Thank you for participating in our graduation survey!" %(survey_item))
        else:
            print("Hi, %s! Could you take part in our graduation survey?" %(survey_item))
    pass
dict_ = {"def_name": "get_job_servey", "def_document": "遍历列表查找存在跟字典键相同的人员。"}
def_list.append(dict_)

""" TODO 创建一个依次包含键-值对{'name': 'Niuniu'和'Student ID': 1}的字典my_dict_1，
    创建一个依次包含键-值对{'name': 'Niumei'和'Student ID': 2}的字典my_dict_2，
    创建一个依次包含键-值对{'name': 'Niu Ke Le'和'Student ID': 3}的字典my_dict_3，
    创建一个空列表dict_list，使用append()方法依次将字典my_dict_1、my_dict_2和my_dict_3添加到dict_list里，
    使用for循环遍历dict_list，对于遍历到的字典，使用print()语句一行输出类似字符串"Niuniu's student id is 1."的语句以打印对应字典中的内容。
"""
def name_student_number():
    my_dict_1 = {'name': 'Niuniu','Student ID': 1}
    my_dict_2 = {'name': 'Niumei','Student ID': 2}
    my_dict_3 = {'name': 'Niu Ke Le','Student ID': 3}
    dict_list = []
    dict_list.append(my_dict_1)
    dict_list.append(my_dict_2)
    dict_list.append(my_dict_3)
    for dict_single in dict_list:
        print("%s's student id is %d." %(dict_single['name'],dict_single['Student ID']))
    pass
dict_ = {"def_name": "name_student_number", "def_document": "遍历列表里面的字典。"}
def_list.append(dict_)

""" TODO 创建一个依次包含键-值对'Beijing': {Capital: 'China'}、'Moscow': {Capital: 'Russia'}和'Paris': {Capital: 'France'}的字典cities_dict，
    请使用for循环遍历"已使用sorted()函数按升序进行临时排序的包含字典cities_dict的所有键的列表"，
    对于每一个遍历到的城市名，使用print()语句一行输出类似字符串'Beijing is the capital of China!'的语句。
"""
def country_dict():
    cities_dict = {'Beijing':{'Capital':'China'},'Moscow':{'Capital':'Russia'},'Paris':{'Capital':'France'}}
    sorted(cities_dict)
    for cities_obj in cities_dict:
        print("%s is the capital of %s!" %(cities_obj,cities_dict[cities_obj]['Capital']))
    pass
dict_ = {"def_name": "country_dict", "def_document": "遍历字典中的字典。"}
def_list.append(dict_)

""" TODO 驼瑞驰调查了班上部分同学喜欢哪些颜色，并创建了一个依次包含键-值对
    'Allen': ['red', 'blue', 'yellow']、'Tom': ['green', 'white', 'blue']和'Andy': ['black', 'pink']的字典result_dict，
    作为已记录的调查结果。现在驼瑞驰想查看字典result_dict的内容，你能帮帮他吗？
    使用for循环遍历"使用sorted()函数按升序进行临时排序的包含字典result_dict的所有键的列表"，
    对于每一个遍历到的名字，先使用print()语句一行输出类似字符串"Allen's favorite colors are:"的语句，
    然后再使用for循环遍历该名字在字典result_dict中对应的列表，依次输出该列表中的颜色。
"""
def survey_color():
    result_dict = {'Allen':['red','blue','yellow'],'Tom':['green','white','blue'],'Andy':['black','pink']}
    sorted(result_dict)
    for name_key in result_dict:
        print("%s's favorite colors are:" % name_key,end=" ")
        for color in result_dict[name_key]:
            print(color,end=" ")
        print()
    pass
dict_ = {"def_name": "survey_color", "def_document": "遍历字典中的列表。"}
def_list.append(dict_)

""" TODO 牛牛有两份列表，一份记录了牛客网用户的名字，另一份记录他们使用的语言。
    假设两份列表一一对应，请使用zip函数将两份列表封装为字典，以名字为key，语言为value，然后直接输出字典。
"""
def packaging_dict():
    name_list = input("请输入客户的名字，用空格区分开来：").split(" ",-1)
    language_list = input("请输入客户的使用的语言，用空格区分开来：").split(" ",-1)
    zipped = zip(name_list,language_list)
    print(dict(zipped))
    pass
dict_ = {"def_name": "packaging_dict", "def_document": "用列表打包字典，内置函数zipped。dict(zipped)"}
def_list.append(dict_)

""" TODO 正在学习英语的牛妹笔记本上准备了这样一个字典：
    {'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down'}。
    请你创建这样一个字典，对于牛妹输入的字母，查询有哪些单词？
"""
def search_dict():
    dictionary = {'a':['apple','abandon','ant'],'b':['banana','bee','become'],'c':['cat','come'],'d':'down'}
    search_word = input("请输入要查询的单词：")
    dictionary_count = len(dictionary)
    for first_word in dictionary:
        if first_word == search_word[0]:
            for word in dictionary[first_word]:
                if word == search_word:
                    print("该单词存在")
                    break
                elif word == dictionary[first_word][-1]:
                    print("存在单词的首字母，但是该单词不存在")
        elif dictionary_count == 1:
            print("没有该首字母的单词")
        dictionary_count -= 1
    pass
dict_ = {"def_name": "search_dict", "def_document": "输入单词在字典中查找。"}
def_list.append(dict_)

""" TODO 正在学习英语的牛妹创建了一个字典：
    {'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down'}。
    现牛妹新学了一个字母letter，以及一个新单词word，请把它们增加到字典中，再输出更新后的字典。
"""
def increase_word():
    dictionary = {'a':['apple','abandon','ant'],'b':['banana','bee','become'],'c':['cat','come'],'d':'down'}
    search_word = input("请输入要新增的单词：")
    dictionary_count = len(dictionary)
    for first_word in dictionary:
        if first_word == search_word[0]:
            try:
                if dictionary[first_word].index(search_word) >= 0:
                    print("该单词已存在，请勿重复添加")
                    print(dictionary)
                    break
            except:
                dictionary[first_word].append(search_word)
                dictionary[first_word].sort()
                print("单词已添加至对应首字母目录下。")
                print(dictionary)
                break
        elif dictionary_count == 1:
            dictionary[search_word[0]] = search_word
            sorted(dictionary)
        dictionary_count -= 1
    pass
dict_ = {"def_name": "increase_word", "def_document": "在字典中新增单词。"}
def_list.append(dict_)

""" TODO Python的字典可以用来计数，让要被计数的元素作为key值，它出现的频次作为value值，只要在遇到key值后更新它对应的value即可。
    现输入一个单词，使用字典统计该单词中各个字母出现的频次。
"""
def word_times():
    input_string = input("请输入一个单词：")
    word_times_dict = {}
    for word in input_string:
        if word not in word_times_dict:
            word_times_dict[word] = 1
        else:
            word_times_dict[word] += 1
    print(word_times_dict)
    pass
dict_ = {"def_name": "word_times", "def_document": "计算单词中字母出现的次数，放在字典里面。"}
def_list.append(dict_)

""" TODO 牛牛给了牛妹一个一串无规则的数字，牛妹将其转换成列表后，使用max和min函数快速的找到了这些数字的最值，你能用Python代码实现一下吗？
"""
def calculate_value():
    input_string = input("请输入一串数字，用空格分隔：")
    number_list = input_string.split(" ",-1)
    print("计算输入的数字最大值为：%s" % max(number_list))
    print("计算输入的数字最小值为：%s" % min(number_list))
    pass
dict_ = {"def_name": "calculate_value", "def_document": "内置函数计算最大值最小值。"}
def_list.append(dict_)

""" TODO 牛牛想知道自己小组内的同事们的年龄和都有多少，他输入一串年龄序列，请将其转换成列表，并使用sum函数直接获取列表的和。
"""
def calculate_sum():
    input_string = input("请输入朋友的年龄，用空格分隔：")
    number_list = [ int(age_) for age_ in  input_string.split(" ",-1)]
    print("计算输入的年龄总和为：%s" % sum(number_list))
    pass
dict_ = {"def_name": "calculate_sum", "def_document": "内置函数计算年龄总和。"}
def_list.append(dict_)

""" TODO 牛牛想要这样一个程序，只要是输入一个整数，不管正负，它一定转换为正数，即获取该数字的绝对值，你能用abs函数实现吗？
"""
def calculate_abs():
    input_int = int(input("请输入一个数值："))
    print("该数取正数为：%s" % abs(input_int))
    pass
dict_ = {"def_name": "calculate_abs", "def_document": "内置函数取正数。"}
def_list.append(dict_)

""" TODO 牛牛刚学习了ASCII码，他知道计算机中的字母很多用的都是这个编码方式，现在输入一个字母，你能使用ord函数将其转换为ASCII码对应的数字吗？
"""
def calculate_ord():
    input_string = input("请输入一个字符：")
    print("将输入的字母转为ASCII字符为：%s" % ord(input_string))
    pass
dict_ = {"def_name": "calculate_ord", "def_document": "内置函数ord,将输入的字母转为ASCII字符为。"}
def_list.append(dict_)

""" TODO 牛妹刚学习进制转换，对这方面掌控还不太熟练，她想请你帮她写一个十进制到十六进制的进制转换器，你能使用hex函数帮助她完成这个任务吗？
"""
def calculate_hex():
    input_int = int(input("请输入一个十进制的数字："))
    print("将数字转换为十六进制为：%s" % hex(input_int))
    pass
dict_ = {"def_name": "calculate_hex", "def_document": "内置函数hex,将输入的数字转换为十六进制。"}
def_list.append(dict_)

""" TODO 计算机内部都由二进制组成，但是早就习惯使用十进制的牛牛根本不知道这个数字的二进制是什么，你能使用bin函数帮助他将十进制数字转换成二进制吗？
"""
def calculate_bin():
    input_int = int(input("请输入一个数字："))
    print("将数字转换为二进制为：%s" % bin(input_int))
    pass
dict_ = {"def_name": "calculate_bin", "def_document": "内置函数bin,将输入的数字转换为二进制。"}
def_list.append(dict_)

""" TODO 在Python中，除了使用两个乘号相连外，还能使用pow函数表示幂运算。
    现牛牛输入正整数x与y，请你使用两种方法分别计算xy与yx。
"""
def calculate_pow():
    input_string = input("请输入两个数字，用空格分开：")
    int_list = [int(number) for number in input_string.split(" ",-1)]
    print("将数字转换为二进制为：%s" % pow(int_list[0],int_list[1]))
    pass
dict_ = {"def_name": "calculate_pow", "def_document": "内置函数pow,计算次幂运算。"}
def_list.append(dict_)

""" TODO 在牛客网内部使用1标记正确回答的题，使用0表示回答错误的题。
    牛牛拿到自己的作答记录是一串01序列，他想知道自己一共答错了多少次，你能将这串序列转换为列表，使用count函数帮助牛牛统计一下吗？
"""
def calculate_times():
    input_string = input("请输入做题结果，用空格分开：")
    string_list = input_string.split(" ",-1)
    print("做题的错误个数为：%s" % string_list.count('0'))
    pass
dict_ = {"def_name": "calculate_times", "def_document": "字符串函数count,计数。"}
def_list.append(dict_)

""" TODO 牛客网有一个打卡系统，记录了每个人这一个星期上班打卡的记录（以名字的形式）。
    牛牛想知道自己在这一个星期是第几个打卡的人，你用将这份名字记录转换为列表，然后使用index函数找到'NiuNiu'的位置吗？
"""
def calculate_index():
    input_name = input("请输入打卡人员的姓名，用空格分开：")
    name_list = input_name.split(" ",-1)
    print("NiuNiu在本周是是第%d个打卡的人" % (name_list.index('NiuNiu') + 1))
    pass
dict_ = {"def_name": "calculate_index", "def_document": "字符串函数index,返回第一个出现的索引。"}
def_list.append(dict_)

""" TODO Python有内置函数isalpha、isdigit、isspace可以分别判断字符串是否只包含字母、数字、空格，现在输入一个字符串，
    请分别输出这三个函数的判断结果。
"""
def isalpha_isdigit_isspace():
    input_string = input("请输入一个字符串：")
    print("判断字符串是否全部为字母，结果为：%s" % input_string.isalpha())
    print("判断字符串是否全部为数字，结果为：%s" % input_string.isdigit())
    print("判断字符串是否全部为空格，结果为：%s" % input_string.isspace())
    pass
dict_ = {"def_name": "isalpha_isdigit_isspace", "def_document": "比较内置函数,isalpha_isdigit_isspace。"}
def_list.append(dict_)

""" TODO 牛客网公布中奖信息了，中奖信息是一个很长的字符串，牛牛想知道自己的名字（'NiuNiu'）有没有出现在其中，
    你能帮助他使用字符串的find函数查找一下吗？
"""
def calculate_find():
    input_string = input("请输入一个中奖名单的全部人员字符串：")
    print("查询NiuNiu是否在中奖名单里面，结果为：%s" % input_string.find("NiuNiu"))
    pass
dict_ = {"def_name": "calculate_find", "def_document": "字符串函数find,查找子字符串是否在全部字符串里面，存在返回起始索引，不存在返回-1"}
def_list.append(dict_)

""" TODO 牛客网喜欢'Niu'这个词，各个地方的称号、标语都会出现。现在给你一定长字符串patten，你能使用count函数找到'Niu'在其中出现的次数吗？
"""
def calculate_amount():
    input_string = input("请输入查询的字符串：")
    print("子字符串在全部字符串中的个数为：%s" % input_string.count("Niu"))
    pass
dict_ = {"def_name": "calculate_amount", "def_document": "计算子字符串在全部字符串中的数量"}
def_list.append(dict_)

""" TODO 英文句子都是由单词之间通过空格间隔而组成，牛牛想知道一句英语句子里面包含有哪些单词，
    你能使用split函数将它们全部按照空格分割，记录进列表中吗，请输出列表。
"""
def calculate_word_times():
    input_string = input("请输入一串英文句子：")
    words_list = input_string.split(" ",-1)
    print(words_list)
    print("将句子拆分乘单词：",end="")
    for word in words_list:
        if word.isalpha():
            print(word,end=" ")
    return ""
dict_ = {"def_name": "calculate_word_times", "def_document": "计算英文句子中存在多少单词"}
def_list.append(dict_)

""" TODO 牛牛在和牛妹做一个游戏，牛牛给定了牛妹一些单词字符串，
    他想让牛妹把这些单词拼接成以空格间隔开的句子，很可惜牛妹Python没有学好，你能使用join函数帮帮她吗？
"""
def organization_words():
    words = ''
    while True:
        input_word = input("请输入单词(结束请输入0)：")
        if input_word == '0':
            print("输入的单词组织成句子为：%s" % words)
            break
        words += " " + input_word
    pass
dict_ = {"def_name": "organization_words", "def_document": "单词组织成句子"}
def_list.append(dict_)

""" TODO 牛客网在录入用户名字信息发生了错误，所有的字符子串'ab'都被录成'a*'，运营同学急坏了。
    你能使用Python字符串的replace函数，将名字信息中的'a*'全部修改回'ab'吗？
"""
def replace_word():
    input_words = input("请输入单词：")
    new_string = input_words.replace("a*","ab")
    print("将'a*'替换为'ab'的结果为：%s" % new_string)
    pass
dict_ = {"def_name": "replace_word", "def_document": "字符串函数replace，字符串中批量替换单词"}
def_list.append(dict_)

""" TODO 牛客网的财务同学很苦恼，各个部门提交的资料中关于金额的小数保留简直是乱七八糟，
    你能使用round函数，帮助财务同学将输入数字的小数位修正为四舍五入保留至最多两位小数吗？（请不要使用字符串格式化输出保留小数位）
"""
def save_two_decimal():
    input_float = float(input("请输入需要保留的小数："))
    print("将%s保留两位小数为：%s" % (input_float,round(input_float,2)))
    pass
dict_ = {"def_name": "save_two_decimal", "def_document": "用函数round将小数位保留两位。"}
def_list.append(dict_)

""" TODO 牛牛听说Python中有一个很神奇的函数eval()，只要输入的字符串是一个公式，它能够直接计算这个公式的值。
    现牛牛以字符串地形式输入一个公式，请你使用eval()计算结果。
"""
def def_eval():
    input_string = input("请输入一个公式：")
    print("公式的结果为：%s" % eval(input_string))
    pass
dict_ = {"def_name": "def_eval", "def_document": "eval函数计算公式。"}
def_list.append(dict_)

""" TODO 某公司内部报名年会活动，因为是匿名报名，有的同事可能偷偷“帮助”别人报名了，导致一个名字出现多次。
    后台营运同学希望你能用set函数将这些名字记录为一个集合，以到达去重的目的，请输出这些名字创建的集合，输出的时候使用sorted函数对集合排序。
"""
def remove_duplicates():
    input_string = input("请输入多个姓名(用空格分开)：")
    name_list = input_string.split(" ",-1)
    set_x = set(name_list)
    set_y = set(name_list)
    print("去重后的结果为：%s" % (set_x & set_y))
    pass
dict_ = {"def_name": "remove_duplicates", "def_document": "set函数进行去重。"}
def_list.append(dict_)

""" TODO 请定义一个函数cal()，该函数返回两个参数相减的差。
    输入第一个数字记录在变量x中，输入第二个数字记录在变量y中，将其转换成数字后调用函数计算cal(x, y)，再交换位置计算cal(y, x)。
"""
def def_calculate_diff():
    def cal(a,b):
        return a-b
    x = int(input("请输入一个数值x："))
    y = int(input("请输入一个数值y："))
    print("计算x-y = %s" % cal(x,y))
    print("计算y-x = %s" % cal(y,x))
    pass
dict_ = {"def_name": "def_calculate_diff", "def_document": "定义函数cal,用函数返回差值。"}
def_list.append(dict_)

""" TODO 兔子的数量以这样的方式增长：每个月的兔子数量等于它前一个月的兔子数量加它前两个月的兔子数量，即f(n)=f(n-1)+f(n-2)。
    假设第1个月的兔子有2只，第2个月的兔子有3只，你能使用递归的方法求得第n个月的兔子有多少只吗？
"""
def sum_rabit_amount():
    def n_month_rabit(n):
        if n == 2:
            return 3
        if n == 1:
            return 2
        return n_month_rabit(n-1) + n_month_rabit(n-2)
    n = int(input("请输入要计算兔子数量的月份："))
    print("计算n个月的兔子数量为：%s" % n_month_rabit(n))
    pass
dict_ = {"def_name": "sum_rabit_amount", "def_document": "求n个月的兔子数量。"}
def_list.append(dict_)

""" TODO 球的表面积公式为V=4πr(2次幂)，请写一个函数，输入球的半径，返回球的表面积。
    球的半径如下：[1, 2, 4, 9, 10, 13]，请输出这些半径下的表面积，π取math库的math.pi。
"""
def superficial_area():
    radius_list = [1,2,4,9,10,13]
    for r in radius_list:
        area = 4 * math.pi * pow(int(r),2)
        print("球的半径为：%s，表面积为：%.2f" % (r,area))
    pass
dict_ = {"def_name": "superficial_area", "def_document": "球的表面积。"}
def_list.append(dict_)

""" TODO 牛牛的Python老师为了更好地管理班级，利用一个类Student来管理学生，
    这个类包含了学生姓名（str）、学号（str）、分数（int）、每次作业等级（list[str]）等信息。
    请你帮助牛牛的老师实现这样一个类，并定义构造方法实现初始化，定义打印函数实现打印学生的姓名、学号、分数、提交作业的次数、每次作业的等级。
"""
def class_student_info():
    class Student(object):
        def __init__(self,name,number,grade,homework_level = []):
            self.name = name
            self.number = number
            self.grade = grade
            self.homework_level = homework_level
        def output_info(self):
            print("-" * 40)
            print("姓名:%s\n学号:%s\n分数:%s\n作业等级:%s" %(self.name,self.number,self.grade,self.homework_level))
    input_name = input("请输入学生姓名：")
    input_number = int(input("请输入学生学号："))
    input_grade = int(input("请输入学生成绩："))
    input_homework_level = input("请输入学生作业等级：").split(" ",-1)
    student = Student(input_name,input_number,input_grade,input_homework_level)
    student.output_info()
    pass


dict_ = {"def_name": "class_student_info", "def_document": "用类保存学生信息。"}
def_list.append(dict_)

""" TODO 请为牛客网的员工创建一个Employee类，包括属性有姓名（name）、（salary），并设置初始化。
    同时该类包括一个方法printclass，用于输出类似'NiuNiu‘s salary is 4000, and his age is 22'的语句。
    请根据输入的name与salary为该类创建实例e，并调用printclass方法输出信息，如果没有年龄信息则输出错误信息"Error! No age"。
    根据输入的年龄为实例e直接添加属性age等于输入值，再次调用printclass方法输出信息。（printclass方法中建议使用try...except...结构）
"""
def modify_property1():
    class Employee(object):
        def __init__(self,name,salary):
            self.name = name
            self.salary = salary
        def output_info(self):
            print("-" * 40)
            try:
                print("%s's salary is %s, and his age is %s" %(self.name,self.salary,self.age))
            except:
                print("Error! No age")
    input_name = input("请输入员工姓名：")
    input_salary = int(input("请输入员工薪水："))
    input_age = int(input("请输入员工年龄："))
    employee = Employee(input_name,input_salary)
    employee.age = input_age
    employee.output_info()
    pass
dict_ = {"def_name": "modify_property1", "def_document": "调用try except报错，修改类里面的属性1。"}
def_list.append(dict_)

""" TODO 请为牛客网的员工创建一个Employee类，包括属性有姓名（name）、（salary），并设置初始化。
    同时该类包括一个方法printclass，用于输出类似'NiuNiu‘s salary is 4000, and his age is 22'的语句。
    请根据输入的信息为Employee类创建一个实例e，调用hasattr方法检验实例有没有属性age，如果存在属性age直接调用printclass输出，
    否则使用setattr函数为其添加属性age，并设置值为输入后，再调用printclass输出。
"""
def modify_property2():
    class Employee(object):
        def __init__(self,name,salary):
            self.name = name
            self.salary = salary
        def output_info(self):
            print("-" * 40)
            try:
                print("%s's salary is %s, and his age is %s" %(self.name,self.salary,self.age))
            except:
                print("Error! No age")
    input_name = input("请输入员工姓名：")
    input_salary = int(input("请输入员工薪水："))
    employee = Employee(input_name,input_salary)
    if hasattr(employee,'age'):
        employee.output_info()
    else:
        print("该对象中不包含age属性")
        input_age = int(input("请输入员工年龄："))
        employee.age = input_age
        employee.output_info()
    pass
dict_ = {"def_name": "modify_property2", "def_document": "hasattr判断属性是否存在，修改类里面的属性2。"}
def_list.append(dict_)

""" TODO 请创建一个Coordinate类表示坐标系，属性有x和y表示横纵坐标，并为其创建初始化方法__init__。
    请重载方法__str__为输出坐标'(x, y)'。
    请重载方法__add__，更改Coordinate类的相加运算为横坐标与横坐标相加，纵坐标与纵坐标相加，返回结果也是Coordinate类。
    现在输入两组横纵坐标x和y，请将其初始化为两个Coordinate类的实例c1和c2，并将坐标相加后输出结果。
"""
def heavy_load_calculate():
    class Coordinate(object):
        def __init__(self,x,y):
            self.x = x
            self.y = y
        def __str__(self):
            return "该类的坐标为%s,%s" %(self.x,self.y)
        def __add__(self,other):
            return Coordinate(self.x+other.x,self.y+other.y)
    c1_xy = [int(c) for c in input("请输入x和y(用空格间隔)：").split(" ",-1)]
    c2_xy = [int(c) for c in input("请输入x和y(用空格间隔)：").split(" ",-1)]
    c1 = Coordinate(c1_xy[0],c1_xy[1])
    c2 = Coordinate(c2_xy[0],c2_xy[1])
    print(c1+c2)
    pass
dict_ = {"def_name": "heavy_load_calculate", "def_document": "覆盖类方法__str__，__add__"}
def_list.append(dict_)

""" TODO 牛牛最近正在研究网址，他发现好像很多网址的开头都是'https://www'，
    他想知道任意一个网址都是这样开头吗。于是牛牛向你输入一个网址（字符串形式），
    你能使用正则函数re.match在起始位置帮他匹配一下有多少位是相同的吗？（区分大小写）
"""
def match_address():
    input_string = input("请输入网址：")
    result = re.match("^https://www",input_string)
    print("字符开头进行匹配，累计匹配%s个字符" % len(result.group()))
    pass
dict_ = {"def_name": "match_address", "def_document": "匹配网址前缀https://www"}
def_list.append(dict_)

""" TODO 牛牛翻看以前记录朋友信息的电话薄，电话号码几位数字之间使用-间隔，
    后面还接了一下不太清楚什么意思的英文字母，你能使用正则匹配re.sub将除了数字以外的其他字符去掉，
    提取一个全数字电话号码吗？
"""
def get_number_phone():
    input_string = input("请输入电话号码：")
    #result = re.sub("-|[a-z]|[A-Z]","",input_string,0) #下面脚本同理
    result = re.sub("\D","",input_string,0)
    print(result)
    pass
dict_ = {"def_name": "get_number_phone", "def_document": "获取字符串中的手机号码"}
def_list.append(dict_)

""" TODO 牛牛记录电话号码时，习惯间隔几位就加一个-间隔，方便记忆，
    同时他还会在电话后面接多条#引导的注释信息。拨打电话时，-可以被手机正常识别，
    #引导的注释信息就必须要去掉了，你能使用正则匹配re.match将前面的数字及-信息提取出来吗，
    去掉后面的注释信息。
"""
def cut_off_phone():
    input_string = input("请输入电话号码：")
    result1 = re.match("\d+-\d+-\d+",input_string)
    result2 = re.sub("#.*","",input_string)
    print(result1.group())
    print(result2)
    pass
dict_ = {"def_name": "cut_off_phone", "def_document": "截断电话号码"}
def_list.append(dict_)

#显示所有函数的列表，供用户进行执行
show_all_def(def_list)