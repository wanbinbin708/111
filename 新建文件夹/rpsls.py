#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2020��11��20��
"""

import random
def name_to_number(name):
    if name == "ʯͷ":
        return 0
    elif name == "ʷ����":
        return 1
    elif name == "ֽ":
        return 2
    elif name == "����":
        return 3
    elif name == "����":
        return 4
def number_to_name(number):
    if number == 0:
        return "ʯͷ"
    elif number == 1:
        return "ʷ����"
    elif number == 2:
        return "ֽ"
    elif number == 3:
        return "����"
    elif number == 4:
        return "����"
def rpsls(player_choice):
    print("--------")
    print("����ѡ��Ϊ:"+str(player_choice))
    comp_number = random.randrange(0, 5)
    m = number_to_name(comp_number)
    print("�������ѡ��Ϊ��"+m)
    if comp_number == 0:
        if player_choice == "ֽ" or player_choice == "ʷ����":
            print("��Ӯ��")
        elif player_choice == "����" or player_choice == "����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͻ�����ѡ��һ����")
    elif comp_number == 1:
        if player_choice =="ֽ" or player_choice == "����":
            print("��Ӯ��")
        elif player_choice == "ʯͷ" or player_choice == "����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͻ�����ѡ��һ����")
    elif comp_number == 2:
        if player_choice == "����" or player_choice == "����":
            print("��Ӯ��")
        elif player_choice == "����" or player_choice == "����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͻ�����ѡ��һ����")
    elif comp_number == 3:
        if player_choice == "����" or player_choice == "ʯͷ":
            print("��Ӯ��")
        elif player_choice == "ֽ" or player_choice == "ʷ����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͻ�����ѡ��һ����")
    elif comp_number == 4:
        if player_choice == "ʯͷ" or player_choice == "ʷ����":
            print("��Ӯ��")
        elif player_choice == "ֽ" or player_choice == "����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͻ�����ѡ��һ����")
     # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
player_choice=input("���������ѡ��")
if player_choice == "ʯͷ" or player_choice == "����" or player_choice == "ֽ" or player_choice == "����" or player_choice == "ʷ����":
    print(rpsls(player_choice))
else:
    print("Error:No Correct Name")



