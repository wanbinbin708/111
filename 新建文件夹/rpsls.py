#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：万彬彬
日期：2020年11月20日
"""

import random
def name_to_number(name):
    if name == "石头":
        return 0
    elif name == "史波克":
        return 1
    elif name == "纸":
        return 2
    elif name == "蜥蜴":
        return 3
    elif name == "剪刀":
        return 4
def number_to_name(number):
    if number == 0:
        return "石头"
    elif number == 1:
        return "史波克"
    elif number == 2:
        return "纸"
    elif number == 3:
        return "蜥蜴"
    elif number == 4:
        return "剪刀"
def rpsls(player_choice):
    print("--------")
    print("您的选择为:"+str(player_choice))
    comp_number = random.randrange(0, 5)
    m = number_to_name(comp_number)
    print("计算机的选择为："+m)
    if comp_number == 0:
        if player_choice == "纸" or player_choice == "史波克":
            print("您赢了")
        elif player_choice == "剪刀" or player_choice == "蜥蜴":
            print("机器赢了")
        elif m == player_choice:
            print("您和机器的选择一样呢")
    elif comp_number == 1:
        if player_choice =="纸" or player_choice == "蜥蜴":
            print("您赢了")
        elif player_choice == "石头" or player_choice == "剪刀":
            print("机器赢了")
        elif m == player_choice:
            print("您和机器的选择一样呢")
    elif comp_number == 2:
        if player_choice == "剪刀" or player_choice == "蜥蜴":
            print("您赢了")
        elif player_choice == "剪刀" or player_choice == "蜥蜴":
            print("机器赢了")
        elif m == player_choice:
            print("您和机器的选择一样呢")
    elif comp_number == 3:
        if player_choice == "剪刀" or player_choice == "石头":
            print("你赢了")
        elif player_choice == "纸" or player_choice == "史波克":
            print("机器赢了")
        elif m == player_choice:
            print("您和机器的选择一样呢")
    elif comp_number == 4:
        if player_choice == "石头" or player_choice == "史波克":
            print("您赢了")
        elif player_choice == "纸" or player_choice == "蜥蜴":
            print("机器赢了")
        elif m == player_choice:
            print("您和机器的选择一样呢")
     # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    pass #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
player_choice=input("请输入你的选择：")
if player_choice == "石头" or player_choice == "剪刀" or player_choice == "纸" or player_choice == "蜥蜴" or player_choice == "史波克":
    print(rpsls(player_choice))
else:
    print("Error:No Correct Name")



