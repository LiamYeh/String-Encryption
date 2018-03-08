'''
md5作用 防止加密后的数据被篡改，起校验作用
Denid Key 密码错误
Denid Content 内容已被篡改
---------------------------------
key = 123456
string = 'hello 你好'

加密步骤：
step1.字符串倒置
step2.base64加密
step3.将加密后的字符串转换成ascii码变成一个列表
step4.对每个码值进行运算 公式为 1x+2x+3x+4x+5x-6
step5.计算每个码值的长度 格式按最长的补0对齐
step6.将码表合并成一个字符串并左移一位
step7.字符串倒置
step8.以-分隔符对齐切割

'''

import base64
import hashlib


encoded_dicts = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
				'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
				'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 
				'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

#公式转换
class Compute():
    def __init__(self,num,key):
        self.num = num
        self.key = key

    def trans(self):
        k = str(self.key)
        num = int(self.num)
        output = (int(k[0]) + int(k[1]) + int(k[2]) - int(k[3]) + int(k[4])) * num - int(k[5])
        return str(output)

    def re_trans(self):
        k = str(self.key)
        num = self.num + int(k[5])
        output = num/(int(k[0])+int(k[1])+int(k[2])-int(k[3])+int(k[4]))
        return int(output)

#移位
class RotateString():
    def __init__(self,s,n):
        self.s = s
        self.n = n

    def left(self): 
        s = self.s
        n = self.n
        if len(s) == 0:  
            return ''  
        move = s[0:n]  
        residue = s[n:]  
        return ''.join([residue, move])  

    def right(self): 
        s = self.s
        n = self.n 
        if len(s) == 0:  
            return ''  
        move = s[:-n]  
        residue = s[-n]  
        return ''.join([residue,move])  

#base64解码时的补齐
def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '='* missing_padding
    return base64.b64decode(data)

#加密
def encrypt(string,key,md5_check=False): 
    reverse_1 = string[::-1] #字符串倒置
    str_to_bytes = (reverse_1).encode('utf-8') 
    base64_str = base64.b64encode(str_to_bytes) 
    as_list = [Compute(i,key).trans() for i in base64_str]
    Max = 0
    for i in as_list:
        if len(i) > Max:
            Max = len(i)  #Max = 3
    to_format_0 = [i.zfill(Max) for i in as_list] #格式补齐 zfill函数能在数字前补0
    list_to_str = ''.join([i for i in to_format_0])                                               
    left_string_1 = RotateString(list_to_str, 1).left()
    reverse_2 = left_string_1[::-1] 
    align_cut = []
    for i in range(0,len(left_string_1),Max):
        split_str = left_string_1[i:i+Max]
        align_cut.append(split_str+'-')
    output = ''.join(align_cut)[:-1]

    if md5_check:
        hash = hashlib.md5()
        hash.update(output.encode('utf-8'))
        md5 = hash.hexdigest()
        return output,md5
    else:
        return output

#解密
def decrypt(string,key,md5=None):
    hash = hashlib.md5()
    hash.update(string.encode('utf-8'))
    new_md5 = hash.hexdigest()
    if md5 == None:
        pass
    elif md5 != new_md5:
        print ()
        return 'Denid Content: %s'%string

    str_len = len(string.split('-')[0])
    str1 = string.replace('-','')      
    str2 = RotateString(str1, 1).right()
    str3_list = []
    for i in range(0,len(str2),str_len):
        split_str = str2[i:i+str_len]
        str3_list.append(int(split_str))
    
    try:
        list_to_str = ''.join(chr(Compute(i,key).re_trans()) for i in str3_list)
        decode_bytes = decode_base64(list_to_str)
    except:
        decode_bytes = b'ERROR'

    list_to_str = ''.join(chr(Compute(i,key).re_trans()) for i in str3_list)
    decode_bytes = decode_base64(list_to_str)

    bytes_to_str = str(decode_bytes,encoding='utf-8')

    if bytes_to_str == 'ERROR':
        return 'Denid Key:%d'%key
    else:
        raw_str = bytes_to_str[::-1]
        return raw_str

key = 123456
string = 'hello 你好'
string,md5 = encrypt(string,key,md5_check=True)
content = decrypt(string,123456,md5=md5)

#print (string,md5)
#print (content)

#656-736-033-933-655-263-447-155-054-913-937-996-804-915-967-713 02ce4965fa4ea6016de8ba96a901a62b
#hello 你好
