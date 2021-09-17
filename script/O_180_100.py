import re


def read_file(n):
    file = open("POSCAR.0")
    all_lines = file.readlines()
    file_w = open("POSCAR", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) == 2:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    new_num1_f = float(num1) * n
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2) * n
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_f = float(num3) * n
                                    str_list_new.append('')
                                    str_list_new.append('{:.9f}'.format(new_num1_f))
                                    str_list_new.append('{:.9f}'.format(new_num2_f))
                                    str_list_new.append('{:.9f}'.format(new_num3_f))
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 3 or all_lines.index(line) == 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    new_num1_f = float(num1)
                    str_list_new.append('')
                    str_list_new.append('{:.9f}'.format(new_num1_f))
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2)
                            str_list_new.append('{:.9f}'.format(new_num2_f))
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_f = float(num3)
                                    str_list_new.append('{:.9f}'.format(new_num3_f))
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 6:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    new_num1_r = round(float(num1) * n)
                    str_list_new.append('')
                    str_list_new.append(new_num1_r)
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_r = round(float(num2) * n)
                            str_list_new.append(new_num2_r)
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_r = round(float(num3) * n)
                                    str_list_new.append(new_num3_r)
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    for count in range(n):
                        num1_f = float(num1)
                        num1_f = num1_f / float(n) + count / float(n)
                        str_list_new.append('{:.9f}'.format(num1_f))
                        for index2, num2 in enumerate(str_list):
                            flag = True
                            if index2 == 1 and flag:
                                flag = False
                                num2_f = float(num2)
                                str_list_new.append('{:.9f}'.format(num2_f))
                                for index3, num3 in enumerate(str_list):
                                    flag = True
                                    if index3 == 2 and flag:
                                        flag = False
                                        num3_f = float(num3)
                                        # num3_f = num3_f / float(n) + count / float(n)
                                        str_list_new.append('{:.9f}'.format(num3_f))
                                        str_list_new.append('\n')
                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    file_w.writelines(new_lines)

pass


def set_dw_center_file(n):
    file = open("POSCAR")
    all_lines = file.readlines()
    file_w = open("POSCAR", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    num1_f = float(num1)
                    str_list_new.append('{:.9f}'.format(num1_f))
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            num2_f = float(num2)
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    num3_f = float(num3)
                                    if num1_f == 0 or num1_f == 0.5:
                                        if 0.3 <= num2_f <= 0.7:
                                            num2_f = float(0.5)
                                            str_list_new.append('{:.9f}'.format(num2_f))
                                            str_list_new.append('{:.9f}'.format(float(num3_f)))
                                            str_list_new.append('\n')
                                            new_line += "   ".join(str(i) for i in str_list_new)
                                        elif num2_f >= 0.8 or num2_f <= 0.2:
                                            num2_f = float(0.0)
                                            str_list_new.append('{:.9f}'.format(num2_f))
                                            str_list_new.append('{:.9f}'.format(float(num3_f)))
                                            str_list_new.append('\n')
                                            new_line += "   ".join(str(i) for i in str_list_new)
                                        else:
                                            num2_f = float(num2)
                                    elif 0.5 < num1_f <= 1:
                                        if num2_f != 0:
                                            num2_f = 1.0 - num2_f
                                            str_list_new.append('{:.9f}'.format(num2_f))
                                            str_list_new.append('{:.9f}'.format(float(num3_f)))
                                            str_list_new.append('\n')
                                            new_line += "   ".join(str(i) for i in str_list_new)
                                        else:
                                            num2_f = float(num2)
                                            str_list_new.append('{:.9f}'.format(num2_f))
                                            str_list_new.append('{:.9f}'.format(float(num3_f)))
                                            str_list_new.append('\n')
                                            new_line += "   ".join(str(i) for i in str_list_new)
                                    else:
                                        num2_f = float(num2)
                                        str_list_new.append('{:.9f}'.format(num2_f))
                                        str_list_new.append('{:.9f}'.format(float(num3_f)))
                                        str_list_new.append('\n')
                                        new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    file_w.writelines(new_lines)


pass

if __name__ == '__main__':
    read_file(8)
    set_dw_center_file(8)
