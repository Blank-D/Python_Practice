#功能：
#   主程序功能代码
#       ①、程序入口
#       ②、每一次启动名片管理系统都通过main这个文件启动
import cards_tools

while True:
    # TODO(小明)   显示系统菜单
    cards_tools.show_menu()

    action = input("请选择操作的功能：")

    print("您选择的操作是：%s" % action)

    if action in ["1","2","3"]:
        if action == "1":
            cards_tools.new_card()

        if action == "2":
            cards_tools.show_all()

        if action == "3":
            cards_tools.search_card()

    elif action == "0":
        print("欢迎再次使用【名片管理系统】")

        break
    else:
        print("输入错误，请重新输入")
