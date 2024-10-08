#功能
#   所有名片功能函数
#       ①、将对名片的新增、查询、修改、删除等功能封装在不同的函数中
import cards_input

def show_menu():
    """显示菜单"""
    menu_ = cards_input.menu
    for item in menu_:
        print("%s.%s" %(menu_.index(item)+1,item))

def new_card():
    """新建名片"""
    card_info = {}
    print("请输入新增名片的详细信息:")
    card_info["姓名"] = input("姓名：")
    card_info["电话"] = input("电话：")
    card_info["QQ"] = input("QQ：")
    card_info["email"] = input("email：")
    cards_input.list_.append(card_info)
    print("已输入完毕")

def show_all():
    """显示全部名片

    :param cards_input  导入的模块
    :param list_    名片列表(每一项为集合)
    """

    if len(cards_input.list_) == 0:
        print("提示：没有任何名片记录")
        return

    for card in cards_input.list_:
        for (key,value) in card.items():
            print("%s:%s" %(key,value))
        print("-" * 10)

def search_card():
    """根据相关信息搜索名片

     cards_input:  导入的模块
     list_:    名片列表(每一项为集合)
    """

    search_name = input("请输入要搜索的名片姓名：")

    #遍历名片列表进行查询
    for cardItem in cards_input.list_:
        if cardItem["姓名"] == search_name:
            print("%s\t\t%s\t\t%s\t\t%s" %(
                cardItem["姓名"],
                cardItem["电话"],
                cardItem["QQ"],
                cardItem["email"]))
            print("-" * 20)
            # 处理搜索到的名片信息
            deal_card(cardItem)
            break
        if (cardItem["姓名"] == cards_input.list_[-1]["姓名"])\
                and cardItem["姓名"] != search_name:
            print("没有找到 %s" % search_name)



def deal_card(find_dict):
    """操作搜索到的名片字典

    :param find_dict:   名片字典
    """

    action_str = input("请输入对名片的操作: 1、修改  2、删除  0、返回上级菜单")

    if action_str == "1":
        find_dict["姓名"] = cards_input.input_card_info(find_dict["姓名"],
                                                      "请输入姓名[回车不修改]:")
        find_dict["电话"] = cards_input.input_card_info(find_dict["电话"],
                                                      "请输入电话[回车不修改]:")
        find_dict["QQ"] = cards_input.input_card_info(find_dict["QQ"],
                                                      "请输入QQ[回车不修改]:")
        find_dict["email"] = cards_input.input_card_info(find_dict["email"],
                                                         "请输入邮箱[回车不修改]:")
        print("%s 的名片修改成功" % find_dict["姓名"])

    elif action_str == "2":
        cards_input.list_.remove(find_dict)

        print("删除名片成功！")