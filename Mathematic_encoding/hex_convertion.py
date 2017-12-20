import numpy as np

encoded_dicts = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 
                'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 
                'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 
                'Y': 34, 'Z': 35, 'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 
                'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55, 
                'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61}

reversed_encoded_dicts = dict((y,x) for x,y in encoded_dicts.items())

def n_to_decimal(num,n,dicts=encoded_dicts):
    num_len = len(num) #数字长度
    ascii_str_num = np.array([dicts[i] for i in num[::-1]]) #按编码转换成数字，并放入矩阵
    array_n = np.ones(num_len,dtype=int) * n #构建n进制的矩阵
    array_stride_1 = np.arange(0,num_len) #构建0-n的矩阵
    result = ascii_str_num*(array_n**array_stride_1) #得出结果的矩阵
    result = np.sum(result) #将矩阵的元素相加的到十进制的结果
    return result

def decimal_to_n(num,n,dicts=reversed_encoded_dicts):
    temp_list = []
    while (num > 0):
        part_remainder = num%n #求余数
        num = int(num/n) #取整数
        temp_list.append(part_remainder) #将余数存入列表

    result = ''.join([dicts[i] for i in temp_list[::-1]])
    return result


