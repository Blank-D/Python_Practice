#功能
#   保存修改名片时输出的名片信息

"""界面显示的菜单按钮列表"""
menu = ["新建名片","显示全部","查询名片"]

"""名片"""
list_ = [{
    "姓名":"张三",
    "电话":110,
    "QQ":12345,
    "email":"zs@itheima.com"
},{
    "姓名":"李四",
    "电话":120,
    "QQ":66666,
    "email":"ls@itheima.com"
},{
    "姓名":"王五",
    "电话":119,
    "QQ":99999,
    "email":"ww@itheima.com"
}]

def input_card_info(dict_value,tip_message):
    """输入名片信息

    :param dict_value: 字典原有值
    :param tip_message: 输入提示信息
    :return:如果输入，返回输入内容，否则返回字典原有值
    """

    # 1、提示用户输入内容
    result_str = input(tip_message)

    # 2、针对用户的输入进行判断，如果用户输入了内容，直接直接返回结果
    if len(result_str) > 0:
        return result_str

    # 3、如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value

