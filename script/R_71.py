import re


def supercell(n):
    file = open("POSCAR.0")
    all_lines = file.readlines()
    file_w = open("POSCAR", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) == 3:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1) * n
            new_num2_f = float(num2) * n
            new_num3_f = float(num3) * n
            str_list_new.append('')
            str_list_new.append('{:.16f}'.format(new_num1_f))
            str_list_new.append('{:.16f}'.format(new_num2_f))
            str_list_new.append('{:.16f}'.format(new_num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 2 or all_lines.index(line) == 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_new.append('')
            str_list_new.append('{:.16f}'.format(new_num1_f))
            str_list_new.append('{:.16f}'.format(new_num2_f))
            str_list_new.append('{:.16f}'.format(new_num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 6:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_r = round(float(num1) * n)
            new_num2_r = round(float(num2) * n)
            new_num3_r = round(float(num3) * n)
            str_list_new.append('')
            str_list_new.append(new_num1_r)
            str_list_new.append(new_num2_r)
            str_list_new.append(new_num3_r)
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            for count in range(n):
                str_list_new = []
                num1_f = float(num1)
                num2_f = float(num2)
                num2_f = num2_f / float(n) + count / float(n)
                num3_f = float(num3)
                str_list_new.append('{:.16f}'.format(num1_f))
                str_list_new.append('{:.16f}'.format(num2_f))
                str_list_new.append('{:.16f}'.format(num3_f))
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
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            str_list_new.append('{:.16f}'.format(num1_f))
            num2_f = float(num2)
            str_list_new.append('{:.16f}'.format(num2_f))
            num3_f = float(num3)
            if num2_f <= 0.125 / float(n) or 0.5 - 0.125 / float(n) <= num2_f <= 0.5 + 0.125 / float(n) or num2_f >= 1 - 0.125 / float(n):
                if 0.3 <= num3_f <= 0.7:
                    num3_f = float(0.5)
                    str_list_new.append('{:.16f}'.format(float(num3_f)))
                    str_list_new.append('\n')
                    new_line += "   ".join(str(i) for i in str_list_new)
                elif num3_f >= 0.8 or num3_f <= 0.2:
                    num3_f = float(0.0)
                    str_list_new.append('{:.16f}'.format(float(num3_f)))
                    str_list_new.append('\n')
                    new_line += "   ".join(str(i) for i in str_list_new)
                else:
                    num3_f = float(num3_f)
                    str_list_new.append('{:.16f}'.format(float(num3_f)))
                    str_list_new.append('\n')
                    new_line += "   ".join(str(i) for i in str_list_new)
            elif 0.5 + 0.125 / float(n) < num2_f < 1 - 0.125 / float(n):
                if num3_f != 0:
                    num3_f = 1.0 - num3_f
                    str_list_new.append('{:.16f}'.format(float(num3_f)))
                    str_list_new.append('\n')
                    new_line += "   ".join(str(i) for i in str_list_new)
                else:
                    num3_f = float(num3_f)
                    str_list_new.append('{:.16f}'.format(float(num3_f)))
                    str_list_new.append('\n')
                    new_line += "   ".join(str(i) for i in str_list_new)
            else:
                num3_f = float(num3_f)
                str_list_new.append('{:.16f}'.format(float(num3_f)))
                str_list_new.append('\n')
                new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    file_w.writelines(new_lines)

pass

if __name__ == '__main__':
    supercell(8)
    set_dw_center_file(8)
