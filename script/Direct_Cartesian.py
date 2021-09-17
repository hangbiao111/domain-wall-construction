import re
import numpy

def read_file(n):
    file = open("POSCAR.0")
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
            new_num1_f = float(num1)
            new_num2_f = float(num2)
            new_num3_f = float(num3)
            str_list_matrix.append(new_num1_f)
            str_list_matrix.append(new_num2_f)
            str_list_matrix.append(new_num3_f)
            str_list_matrix_2.append(str_list_matrix)
        else:
            new_lines.append(line)
    matrix_lattice = numpy.array(str_list_matrix_1)
    matrix_positions = numpy.array(str_list_matrix_2)
    return matrix_lattice, matrix_positions



def direct_cartesian(n):
    file = open("POSCAR.0")
    all_lines = file.readlines()
    file_w = open("POSCAR", "w")
    new_lines = []
    matrix_positions_cartesian = []
    matrix_positions_cartesian = matrix_positions.dot(matrix_lattice)
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
            # print(matrix_index)
            print(matrix_positions_cartesian)
            str_list_new = ['{:.16f}'.format(i) for i in matrix_positions_cartesian[matrix_index]]
            str_list_new.append('\n')
            new_line += "   ".join(str(i) for i in str_list_new)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    file_w.writelines(new_lines)


pass




if __name__ == '__main__':
    matrix_lattice, matrix_positions = read_file(16)
    direct_cartesian(16)



