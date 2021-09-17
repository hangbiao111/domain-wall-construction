import re


def read_file(n1,n2):
    file = open("POSCAR.0")
    all_lines = file.readlines()
    file_w = open("POSCAR", "w")
    new_lines = []
    lat_a = None
    ref_center = None
    lat_c = None
    for line in all_lines:
        if all_lines.index(line) == 2 or all_lines.index(line) == 3:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    new_num1_f = float(num1) * (n1 + n2 + 2)
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2) * (n1 + n2 + 2)
                            lat_a = float(num2)
                            ref_center = float(num2) * (n1 + n2 + 2) * 0.5
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_f = float(num3) * (n1 + n2 + 2)
                                    lat_c = float(num3)
                                    str_list_new.append('')
                                    str_list_new.append('{:.16f}'.format(new_num1_f))
                                    str_list_new.append('{:.16f}'.format(new_num2_f))
                                    str_list_new.append('{:.16f}'.format(new_num3_f))
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 4:
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
                    str_list_new.append('{:.16f}'.format(new_num1_f))
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2)
                            str_list_new.append('{:.16f}'.format(new_num2_f))
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_f = float(num3)
                                    lat_c = float(num3)
                                    str_list_new.append('{:.16f}'.format(new_num3_f))
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
                    atom_1 = round(float(num1))
                    new_num1_r = round(float(num1) * (n1 + n2 + 2) * (n1 + n2 + 2))
                    str_list_new.append('')
                    str_list_new.append(new_num1_r)
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            atom_2 = round(float(num2) )
                            new_num2_r = round(float(num2) * (n1 + n2 + 2) * (n1 + n2 + 2))
                            str_list_new.append(new_num2_r)
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    atom_3 = round(float(num3))
                                    new_num3_r = round(float(num3) * (n1 + n2 + 2) * (n1 + n2 + 2))
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
                    for count1 in range(n1 + n2 + 2):
                        num1_f = float(num1)
                        num1_f = num1_f / float(n1 + n2 + 2) + count1 / float(n1 + n2 + 2)
                        # str_list_new.append('{:.9f}'.format(num1_f))
                        for index2, num2 in enumerate(str_list):
                            flag = True
                            if index2 == 1 and flag:
                                flag = False
                                for count2 in range(n1 + n2 + 2):
                                    num2_f = float(num2)
                                    num2_f = num2_f / float(n1 + n2 + 2) + count2 / float(n1 + n2 + 2)
                                    for index3, num3 in enumerate(str_list):
                                        flag = True
                                        if index3 == 2 and flag:
                                            flag = False
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
    return lat_a, ref_center, lat_c, atom_1, atom_2, atom_3


def direct_cartesian(n1,n2):
    file = open("POSCAR")
    all_lines = file.readlines()
    file_w = open("POSCAR", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) == 7:
            new_line = ''
            new_line = 'Cartesian\n'
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
                    new_num1_f = float(num1) * lat_a * (n1 + n2 + 2)
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2) * lat_a * (n1 + n2 + 2)
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_f = float(num3) * lat_c
                                    str_list_new.append('{:.16f}'.format(new_num1_f))
                                    str_list_new.append('{:.16f}'.format(new_num2_f))
                                    str_list_new.append('{:.16f}'.format(new_num3_f))
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    file_w.writelines(new_lines)


pass


def four_points(lat_a, lat_c, n1, n2):
    c1 = []
    for index, value in enumerate([0, 0, 0]):
        if index == 0:
            value = lat_a * 1
        elif index == 1:
            value = lat_a * (n1 + 1)
        else:
            value = lat_c
        c1.append(value)
    # print(c1)
    c2 = []
    for index, value in enumerate([0, 0, 0]):
        if index == 0:
            value = lat_a * (n2 +1)
        elif index == 1:
            value = lat_a * 1
        else:
            value = lat_c
        c2.append(value)
    # print(c2)
    c3 = []
    for index, value in enumerate([0, 0, 0]):
        if index == 0:
            value = lat_a * (n1 + 1)
        elif index == 1:
            value = lat_a * (n1 +n2 + 1)
        else:
            value = lat_c
        c3.append(value)
    # print(c3)
    c4 = []
    for index, value in enumerate([0, 0, 0]):
        if index == 0:
            value = lat_a * (n1 + n2 + 1)
        elif index == 1:
            value = lat_a * (n2 +1)
        else:
            value = lat_c
        c4.append(value)
    # print(c4)
    return c1, c2, c3, c4



def boundary1(c1, c2, c):
    k = (c1[1] - c2[1]) / (c1[0] - c2[0])
    b = c1[1] - k * c1[0]
    # print(k)
    # print(b)
    # print(c[0] * k - c[1] + b)
    if c[0] * k - c[1] + b <= 0 + 0.00000001:
        return True  # true means reserved
    return False

def boundary2(c1, c3, c):
    k = (c1[1] - c3[1]) / (c1[0] - c3[0])
    b = c1[1] - k * c1[0]
    # print(k)
    # print(b)
    # print(c[0] * k - c[1] + b)
    if c[0] * k - c[1] + b >= 0 - 0.00000001:
        return True
    return False

def boundary3(c3, c4, c):
    k = (c3[1] - c4[1]) / (c3[0] - c4[0])
    b = c3[1] - k * c3[0]
    # print(k)
    # print(b)
    # print(c[0] * k - c[1] + b)
    if c[0] * k - c[1] + b > 0 + 0.00000001:
        return True
    return False

def boundary4(c2, c4, c):
    k = (c2[1] - c4[1]) / (c2[0] - c4[0])
    b = c2[1] - k * c2[0]
    # print(k)
    # print(b)
    # print(c[0] * k - c[1] + b)
    if c[0] * k - c[1] + b < 0 - 0.00000001:
        return True
    return False

def boundary_logic(c1, c2, c3, c4, c):
    if boundary1(c1, c2, c) and boundary2(c1, c3, c) and boundary3(c3, c4, c) and boundary4(c2, c4, c):
        return True
    return False

def cartesian_cell(n1,n2,c1,c2,c3,atom_1, atom_2, atom_3):
    file = open("POSCAR")
    all_lines = file.readlines()
    file_w = open("POSCAR", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) == 2:
            str_list_new = []
            new_line = ''
            vector_a_x = c2[0] - c1[0]
            vector_a_y = c2[1] - c1[1]
            str_list_new.append('')
            str_list_new.append('{:.16f}'.format(vector_a_x))
            str_list_new.append('{:.16f}'.format(vector_a_y))
            str_list_new.append('{:.16f}'.format(0.0))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 3:
            str_list_new = []
            new_line = ''
            vector_b_x = c3[0] - c1[0]
            vector_b_y = c3[1] - c1[1]
            str_list_new.append('')
            str_list_new.append('{:.16f}'.format(vector_b_x))
            str_list_new.append('{:.16f}'.format(vector_b_y))
            str_list_new.append('{:.16f}'.format(0.0))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    new_num1_f = float(num1)
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2)
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
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
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    new_num1_r = round(float(atom_1) * (n1 * n1 + n2 * n2))
                    str_list_new.append('')
                    str_list_new.append(new_num1_r)
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_r = round(float(atom_2) * (n1 * n1 + n2 * n2))
                            str_list_new.append(new_num2_r)
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_r = round(float(atom_3) * (n1 * n1 + n2 * n2))
                                    str_list_new.append(new_num3_r)
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_big = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    num1_f = float(num1)
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
                                    str_list_new = []
                                    str_list_new.append(float('{:.16f}'.format(num1_f)))
                                    str_list_new.append(float('{:.16f}'.format(num2_f)))
                                    str_list_new.append(float('{:.16f}'.format(num3_f)))
                            str_list_big.append(str_list_new)
                            points_list = []
                            # z=str_list_big
                            # print(z)
                            new_line = ''
                            for c in str_list_big:
                                y = boundary_logic(c1, c2, c3, c4, c)
                                print(c)
                                # print(y)
                                if y:
                                    points_list = ['{:.16f}'.format(float(str(i))) for i in c]
                                    points_list.append('\n')
                                    new_line += "   ".join(str(i) for i in points_list)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    file_w.writelines(new_lines)

pass



def cartesian_direct(n1,n2,c1,c2,c3):
    file = open("POSCAR")
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
                   new_num1_f = float(num1)
                   a11 = new_num1_f
                   for index2, num2 in enumerate(str_list):
                       flag = True
                       if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2)
                            a12 = new_num2_f
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_f = float(num3)
                                    a13 = new_num3_f
                                    a11_new = (a11 * a11 + a12 * a12) ** (1/2)
                                    str_list_new.append('')
                                    str_list_new.append('{:.16f}'.format(a11_new))
                                    str_list_new.append('{:.16f}'.format(0.0))
                                    str_list_new.append('{:.16f}'.format(new_num3_f))
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
           new_lines.append(new_line)
        elif all_lines.index(line) == 3:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    new_num1_f = float(num1)
                    a21 = new_num1_f
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2)
                            a22 = new_num2_f
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_f = float(num3)
                                    a23 = new_num3_f
                                    a22_new = (a21 * a21 + a22 * a22) ** (1/2)
                                    str_list_new.append('')
                                    str_list_new.append('{:.16f}'.format(0.0))
                                    str_list_new.append('{:.16f}'.format(a22_new))
                                    str_list_new.append('{:.16f}'.format(new_num3_f))
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            for index1, num1 in enumerate(str_list):
                flag = True
                if index1 == 0 and flag:
                    flag = False
                    new_num1_f = float(num1)
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2)
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_f = float(num3)
                                    a33 = new_num3_f
                                    str_list_new.append('')
                                    str_list_new.append('{:.16f}'.format(new_num1_f))
                                    str_list_new.append('{:.16f}'.format(new_num2_f))
                                    str_list_new.append('{:.16f}'.format(new_num3_f))
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 7:
            new_line = ''
            new_line = 'Direct\n'
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
                    new_num1_f = float(num1)
                    for index2, num2 in enumerate(str_list):
                        flag = True
                        if index2 == 1 and flag:
                            flag = False
                            new_num2_f = float(num2)
                            for index3, num3 in enumerate(str_list):
                                flag = True
                                if index3 == 2 and flag:
                                    flag = False
                                    new_num3_f = float(num3)
                                    Ax = 1 / (c1[0] - c2[0])
                                    Bx = -1 / (c1[1] - c2[1])
                                    Cx = c2[1] / (c1[1] - c2[1]) - c2[0]/(c1[0] - c2[0])
                                    Ay = 1 / (c1[0] - c3[0])
                                    By = -1 / (c1[1] - c3[1])
                                    Cy = c3[1] / (c1[1] - c3[1]) - c3[0]/(c1[0] - c3[0])
                                    new_num1_direct = abs((Ay * new_num1_f + By * new_num2_f + Cy)/((Ay * Ay + By * By) ** 0.5)/a11_new)
                                    new_num2_direct = abs((Ax * new_num1_f + Bx * new_num2_f + Cx)/((Ax * Ax + Bx * Bx) ** 0.5)/a22_new)
                                    new_num3_direct = new_num3_f / a33
                                    str_list_new.append('{:.16f}'.format(new_num1_direct))
                                    str_list_new.append('{:.16f}'.format(new_num2_direct))
                                    str_list_new.append('{:.16f}'.format(new_num3_direct))
                                    str_list_new.append('\n')
                                    new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    file_w.writelines(new_lines)


pass


if __name__ == '__main__':
    lat_a, ref_center, lat_c, atom_1, atom_2, atom_3 = read_file(1,4)
    direct_cartesian(1,4)
    c1, c2, c3, c4 = four_points(lat_a, lat_c, 1,4)
    cartesian_cell(1,4,c1,c2,c3,atom_1, atom_2, atom_3)
    cartesian_direct(1,4,c1,c2,c3)





# if __name__ == '__main__':
#     lat_a, ref_center, lat_c = read_file(7)
#     direct_cartesian(7)
#     c1, c2, c3, c4 = four_points(lat_a, lat_c, 7)
#     # for c in all_points():
#     c=[23.20368837,	15.46921582,	4.03216]
#     # y=boundary1(c1, c2, c)
#     # y=boundary2(c1, c3, c)
#     # y=boundary3(c3, c4, c)
#     y=boundary4(c2, c4, c)
#     print(y)

# def test(p=[]):
#     new_line = ''
#     new_line += "   ".join('{:.16f}'.format(float(str(i))) for i in p)
#     print(new_line)
# pass
#
# if __name__ == '__main__':
#     test([23.203768907484424, 19.33647408957036, 0.0])
