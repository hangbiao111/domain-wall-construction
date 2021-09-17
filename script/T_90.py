import re
import numpy as np
import math


def read_lattice():
    file = open("POSCAR.0")
    all_lines = file.readlines()
    lat_a = None
    lat_c = None
    for line in all_lines:
        if all_lines.index(line) == 2:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            num1 = str_list[0]
            lat_a = float(num1)
        elif all_lines.index(line) == 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            num3 = str_list[2]
            lat_c = float(num3)
    return lat_a, lat_c

def rotation_matrix(n):
    sin = lat_a / (( lat_a * lat_a +lat_c * lat_c) ** (1/2))
    cos = lat_c / (( lat_a * lat_a +lat_c * lat_c) ** (1/2))
    lat_c_new = ( lat_a * lat_a +lat_c * lat_c) ** (1/2)
    clockwise = np.array([[cos, 0, -sin,], [0, 1, 0], [sin, 0, cos]])
    counterclockwise = np.array([[cos, 0, sin,], [0, 1, 0], [-sin, 0, cos]])
    theta = math.asin(sin)
    cos2 = math.cos(math.pi/2 - 2 * theta)
    lat_a_new = lat_c_new * cos2
    lat_a_new_half = lat_a_new * n/4
    return clockwise, counterclockwise, lat_c_new, lat_a_new, lat_a_new_half

def supercell(n):
    file = open("POSCAR.0")
    all_lines = file.readlines()
    file_w = open("POSCAR_supercell", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) == 2:
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
        elif all_lines.index(line) == 4:
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
        elif all_lines.index(line) == 6:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_r = round(float(num1) * n * n)
            new_num2_r = round(float(num2) * n * n)
            new_num3_r = round(float(num3) * n * n)
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
            for count in range(n):
                num1_f = float(num1)
                num1_f = num1_f / float(n) + count / float(n)
                num2 = str_list[1]
                num2_f = float(num2)
                num3 = str_list[2]
                for count1 in range(n):
                    str_list_new = []
                    num3_f = float(num3)
                    num3_f = num3_f / float(n) + count1 / float(n)
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


def read_matrix_direct_right():
    file = open("POSCAR_supercell")
    all_lines = file.readlines()
    # file_w = open("POSCAR", "w")
    new_lines = []
    str_list_matrix_1 = []
    str_list_matrix_2 = []
    for line in all_lines:
        if 2 <= all_lines.index(line) <= 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_matrix.append(new_num1_f)
            str_list_matrix.append(new_num2_f)
            str_list_matrix.append(new_num3_f)
            str_list_matrix_1.append(str_list_matrix)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_matrix.append(new_num1_f)
            str_list_matrix.append(new_num2_f)
            str_list_matrix.append(new_num3_f)
            str_list_matrix_2.append(str_list_matrix)
        else:
            new_lines.append(line)
    matrix_lattice_direct_right = np.array(str_list_matrix_1)
    matrix_positions_direct_right = np.array(str_list_matrix_2)
    return matrix_lattice_direct_right, matrix_positions_direct_right


def direct_cartesian_right():
    file = open("POSCAR_supercell")
    all_lines = file.readlines()
    file_w = open("POSCAR_cartesian_right", "w")
    new_lines = []
    matrix_positions_cartesian = []
    matrix_positions_cartesian = matrix_positions_direct_right.dot(matrix_lattice_direct_right)
    for line in all_lines:
        if all_lines.index(line) == 7:
            new_line = ''
            new_line = 'Cartesian\n'
            new_lines.append(new_line)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            matrix_index = all_lines.index(line) - 8
            str_list_new = ['{:.16f}'.format(i) for i in matrix_positions_cartesian[matrix_index]]
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    file_w.writelines(new_lines)

pass



def read_matrix_cartesian_right():
    file = open("POSCAR_cartesian_right")
    all_lines = file.readlines()
    # file_w = open("POSCAR", "w")
    new_lines = []
    str_list_matrix_1 = []
    str_list_matrix_2 = []
    matrix_positions_cartesian = None
    for line in all_lines:
        if 2 <= all_lines.index(line) <= 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_matrix.append(new_num1_f)
            str_list_matrix.append(new_num2_f)
            str_list_matrix.append(new_num3_f)
            str_list_matrix_1.append(str_list_matrix)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1) - lat_a
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_matrix.append(new_num1_f)
            str_list_matrix.append(new_num2_f)
            str_list_matrix.append(new_num3_f)
            str_list_matrix_2.append(str_list_matrix)
        else:
            new_lines.append(line)
    matrix_lattice_cartesian_right = np.array(str_list_matrix_1)
    matrix_positions_cartesian_right = np.array(str_list_matrix_2)
    return matrix_lattice_cartesian_right, matrix_positions_cartesian_right


def right_part_rotate():
    file = open("POSCAR_cartesian_right")
    all_lines = file.readlines()
    file_w = open("POSCAR_right_rotate", "w")
    new_lines = []
    matrix_positions_cartesian_right_rotate = []
    matrix_positions_cartesian_right_rotate = matrix_positions_cartesian_right.dot(clockwise)
    for line in all_lines:
        if all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            matrix_index = all_lines.index(line) - 8
            str_list_new = ['{:.16f}'.format(i) for i in matrix_positions_cartesian_right_rotate[matrix_index]]
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    file_w.writelines(new_lines)

pass

def supercell_reversal():
    file = open("POSCAR_supercell")
    all_lines = file.readlines()
    file_w = open("POSCAR_supercell_reversal", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            new_line = ''
            num1 = str_list[0]
            num1_f = float(num1)
            num2 = str_list[1]
            num2_f = float(num2)
            num3 = str_list[2]
            num3_f = float(num3)
            if num3_f != 0:
                num3_f = 1 - num3_f
                str_list_new = []
                str_list_new.append('{:.16f}'.format(num1_f))
                str_list_new.append('{:.16f}'.format(num2_f))
                str_list_new.append('{:.16f}'.format(num3_f))
                str_list_new.append('\n')
                new_line += "   ".join(str(i) for i in str_list_new)
            else:
                num3_f = num3_f
                str_list_new = []
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


def read_matrix_direct_left():
    file = open("POSCAR_supercell_reversal")
    all_lines = file.readlines()
    # file_w = open("POSCAR", "w")
    new_lines = []
    str_list_matrix_1 = []
    str_list_matrix_2 = []
    for line in all_lines:
        if 2 <= all_lines.index(line) <= 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_matrix.append(new_num1_f)
            str_list_matrix.append(new_num2_f)
            str_list_matrix.append(new_num3_f)
            str_list_matrix_1.append(str_list_matrix)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_matrix.append(new_num1_f)
            str_list_matrix.append(new_num2_f)
            str_list_matrix.append(new_num3_f)
            str_list_matrix_2.append(str_list_matrix)
        else:
            new_lines.append(line)
    matrix_lattice_direct_left = np.array(str_list_matrix_1)
    matrix_positions_direct_left = np.array(str_list_matrix_2)
    return matrix_lattice_direct_left, matrix_positions_direct_left

def direct_cartesian_left():
    file = open("POSCAR_supercell_reversal")
    all_lines = file.readlines()
    file_w = open("POSCAR_cartesian_left", "w")
    new_lines = []
    matrix_positions_cartesian = []
    matrix_positions_cartesian = matrix_positions_direct_left.dot(matrix_lattice_direct_left)
    for line in all_lines:
        if all_lines.index(line) == 7:
            new_line = ''
            new_line = 'Cartesian\n'
            new_lines.append(new_line)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            matrix_index = all_lines.index(line) - 8
            str_list_new = ['{:.16f}'.format(i) for i in matrix_positions_cartesian[matrix_index]]
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    file_w.writelines(new_lines)

pass

def read_matrix_cartesian_left(n):
    file = open("POSCAR_cartesian_left")
    all_lines = file.readlines()
    # file_w = open("POSCAR", "w")
    new_lines = []
    str_list_matrix_1 = []
    str_list_matrix_2 = []
    matrix_positions_cartesian = None
    for line in all_lines:
        if 2 <= all_lines.index(line) <= 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_matrix.append(new_num1_f)
            str_list_matrix.append(new_num2_f)
            str_list_matrix.append(new_num3_f)
            str_list_matrix_1.append(str_list_matrix)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1) - lat_a
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_matrix.append(new_num1_f)
            str_list_matrix.append(new_num2_f)
            str_list_matrix.append(new_num3_f)
            str_list_matrix_2.append(str_list_matrix)
        else:
            new_lines.append(line)
    matrix_lattice_cartesian_left = np.array(str_list_matrix_1)
    matrix_positions_cartesian_left = np.array(str_list_matrix_2)
    return matrix_lattice_cartesian_left, matrix_positions_cartesian_left

def left_part_rotate():
    file = open("POSCAR_cartesian_left")
    all_lines = file.readlines()
    file_w = open("POSCAR_left_rotate", "w")
    new_lines = []
    matrix_positions_cartesian_left_rotate = []
    matrix_positions_cartesian_left_rotate = matrix_positions_cartesian_left.dot(clockwise)
    for line in all_lines:
        if all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            str_list_matrix = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            matrix_index = all_lines.index(line) - 8
            # print(matrix_positions_right)
            str_list_new = ['{:.16f}'.format(i) for i in matrix_positions_cartesian_left_rotate[matrix_index]]
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    file_w.writelines(new_lines)

pass



def boundary_logic_right(c):
    if 0 <= c[0] < lat_a_new_half and 0 <= c[2] < lat_c_new:
        return True
    return False

def boundary_logic_left(c):
    if 0 < c[0] <= lat_a_new_half and 0 <= c[2] < lat_c_new:
        return True
    return False


def right_part_rotate_cut(n):
    file = open("POSCAR_right_rotate")
    all_lines = file.readlines()
    file_w = open("POSCAR_right_rotate_cut", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) == 6:
            new_line = ''
            str_list_new = []
            new_num1_r = round(3 * n / 2)
            new_num2_r = round(n / 2)
            new_num3_r = round(n / 2)
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
            str_list_new = []
            str_list_big = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append(float('{:.16f}'.format(num1_f)))
            str_list_new.append(float('{:.16f}'.format(num2_f)))
            str_list_new.append(float('{:.16f}'.format(num3_f)))
            str_list_big.append(str_list_new)
            for c in str_list_big:
                y = boundary_logic_right(c)
                if y:
                    points_list = ['{:.16f}'.format(float(str(i))) for i in c]
                    points_list.append('\n')
                    new_line += "   ".join(str(i) for i in points_list)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    file_w.writelines(new_lines)

pass


def left_part_rotate_cut(n):
    file = open("POSCAR_left_rotate")
    all_lines = file.readlines()
    file_w = open("POSCAR_left_rotate_cut", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) == 6:
            new_line = ''
            str_list_new = []
            new_num1_r = round(3 * n / 2)
            new_num2_r = round(n / 2)
            new_num3_r = round(n / 2)
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
            str_list_new = []
            str_list_big = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append(float('{:.16f}'.format(num1_f)))
            str_list_new.append(float('{:.16f}'.format(num2_f)))
            str_list_new.append(float('{:.16f}'.format(num3_f)))
            str_list_big.append(str_list_new)
            for c in str_list_big:
                y = boundary_logic_left(c)
                if y:
                    points_list = ['{:.16f}'.format(float(str(i))) for i in c]
                    points_list.append('\n')
                    new_line += "   ".join(str(i) for i in points_list)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    file_w.writelines(new_lines)

pass


def left_part_rotate_cut_reversal():
    file = open("POSCAR_left_rotate_cut")
    all_lines = file.readlines()
    file_w = open("POSCAR_left_rotate_cut_reversal", "w")
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
            num1_f = -float(num1)
            num2_f = float(num2)
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

def read_lines_right(n):
    file = open("POSCAR_right_rotate_cut")
    all_lines = file.readlines()
    # file_w = open("POSCAR_right_rotate_cut_move", "w")
    new_lines = []
    new_lines_right_1 = []
    new_lines_right_2 = []
    new_lines_right_3 = []
    for line in all_lines:
        if 8 <= all_lines.index(line) < 8 + n / 2 * 3:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines_right_1.append(new_line)
        elif 8 + n / 2 * 3 <= all_lines.index(line) < 8 + n / 2 * 3 + n / 2:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines_right_2.append(new_line)
        elif 8 + n / 2 * 3 + n / 2 <= all_lines.index(line) < 8 + n / 2 * 3 + n:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines_right_3.append(new_line)
        else:
            new_lines.append(line)
    return new_lines_right_1, new_lines_right_2, new_lines_right_3

def read_lines_left(n):
    file = open("POSCAR_left_rotate_cut_reversal")
    all_lines = file.readlines()
    new_lines = []
    new_lines_left_1 = []
    new_lines_left_2 = []
    new_lines_left_3 = []
    for line in all_lines:
        if 8 <= all_lines.index(line) < 8 + n / 2 * 3:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines_left_1.append(new_line)
        elif 8 + n / 2 * 3 <= all_lines.index(line) < 8 + n / 2 * 3 + n / 2:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines_left_2.append(new_line)
        elif 8 + n / 2 * 3 + n / 2 <= all_lines.index(line) < 8 + n / 2 * 3 + n:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines_left_3.append(new_line)
        else:
            new_lines.append(line)
    return new_lines_left_1, new_lines_left_2, new_lines_left_3


def glue_left_right(n):
    file = open("POSCAR.0")
    all_lines = file.readlines()
    file_w = open("POSCAR_glue", "w")
    new_lines = []
    for line in all_lines:
        if all_lines.index(line) == 2:
            num1_f = float(lat_a_new_half * 2)
            num2_f = float(0.0)
            num3_f = float(0.0)
            new_line = ''
            str_list_new = []
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 3:
            num1_f = float(0.0)
            num2_f = float(lat_a)
            num3_f = float(0.0)
            new_line = ''
            str_list_new = []
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 4:
            num1_f = float(0.0)
            num2_f = float(0.0)
            num3_f = float(lat_c_new)
            new_line = ''
            str_list_new = []
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 6:
            num1_r = round(n * 3)
            num2_r = round(n)
            num3_r = round(n)
            new_line = ''
            str_list_new = []
            str_list_new.append('')
            str_list_new.append(num1_r)
            str_list_new.append(num2_r)
            str_list_new.append(num3_r)
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) == 7:
            new_line = ''
            new_line = 'Cartesian\n'
            new_lines.append(new_line)
        elif all_lines.index(line) == 8:
            new_line = ''
            glue = new_lines_right_1 + new_lines_left_1 + new_lines_right_2 + new_lines_left_2 + new_lines_right_3 + new_lines_left_3
            new_line += "   ".join(str(i) for i in glue)
            new_lines.append(new_line)
        elif all_lines.index(line) >= 9:
            new_line = ''
        else:
            new_lines.append(line)
    file_w.writelines(new_lines)

pass

def glue_left_right_move():
    file = open("POSCAR_glue")
    all_lines = file.readlines()
    file_w = open("POSCAR", "w")
    new_lines = []
    for line in all_lines:
        if 2 <= all_lines.index(line) <= 4:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1)
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append('')
            str_list_new.append('{:.16f}'.format(num1_f))
            str_list_new.append('{:.16f}'.format(num2_f))
            str_list_new.append('{:.16f}'.format(num3_f))
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        elif all_lines.index(line) >= 8:
            str_list = line.replace("\t", " ").replace("\n", " ").split(" ")
            str_list = [i for i in str_list if i != '']
            str_list_new = []
            new_line = ''
            num1 = str_list[0]
            num2 = str_list[1]
            num3 = str_list[2]
            num1_f = float(num1) + lat_a_new_half
            num2_f = float(num2)
            num3_f = float(num3)
            str_list_new.append('')
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


if __name__ == '__main__':
    lat_a, lat_c = read_lattice()
    clockwise, counterclockwise, lat_c_new, lat_a_new, lat_a_new_half = rotation_matrix(16)

    supercell(20)
    matrix_lattice_direct_right, matrix_positions_direct_right = read_matrix_direct_right()
    direct_cartesian_right()
    matrix_lattice_cartesian_right, matrix_positions_cartesian_right = read_matrix_cartesian_right()
    right_part_rotate()

    supercell_reversal()
    matrix_lattice_direct_left, matrix_positions_direct_left = read_matrix_direct_left()
    direct_cartesian_left()
    matrix_lattice_cartesian_left, matrix_positions_cartesian_left = read_matrix_cartesian_left(16)
    left_part_rotate()

    right_part_rotate_cut(16)
    left_part_rotate_cut(16)
    left_part_rotate_cut_reversal()
    new_lines_right_1, new_lines_right_2, new_lines_right_3 = read_lines_right(16)
    new_lines_left_1, new_lines_left_2, new_lines_left_3 = read_lines_left(16)
    glue_left_right(16)
    glue_left_right_move()


