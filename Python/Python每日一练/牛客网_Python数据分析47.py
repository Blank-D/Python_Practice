"""
Document:
    网址：https://www.nowcoder.com/exam/oj?page=1&tab=Python%E7%AF%87&topicId=326
"""
def_list = []
def def_active(list_):
    """
        针对Python数据分析的47道题进行构建列表，按照索引进行调用执行
    """
    for def_ in list_:
        print("%s. 函数名称：%s\t函数文档：%s" %(list_.index(def_) + 1,def_["name"],def_["document"]))
    active_index = int(input("请输入要执行的函数索引："))
    eval(list_[active_index - 1]['name'] + '()')
    pass

def check_empolyee_data():
    """ TODO 现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
        Nowcoder_ID：用户ID
        Level：等级
        Achievement_value：成就值
        Num_of_exercise：刷题量
        Graduate_year：毕业年份
        Language：常用语言
        你可以使用pandas打开文件，偷偷看一下里面的内容，请输出你看到的前6行数据。
    """
    print("测试调用列表是否可执行")
    pass
def_info = {"name":"check_empolyee_data","document":"用pandas查看牛客网用户数据"}
def_list.append(def_info)

#执行函数列表
def_active(def_list)