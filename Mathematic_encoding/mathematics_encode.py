import struct
import binascii
from hex_convertion import *
from collections import Counter

encoded_dicts = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 
                'c': 12, 'd': 13, 'e': 14, 'f': 15}

def create_rating_dic(content,lens=0,multip=1):
	c = Counter(content) #使用这个类效率提高很多
	rating_dicts = dict([(i,(c[i]/lens)*multip) for i in content])
	dicts = {}
	ratio = 0
	for x,y in rating_dicts.items():
		init = ratio
		ratio += y
		dicts.update({x:[init,ratio]})
	return dicts


def demo():
	fn = open('1.wmv','rb')
	fw = open('2.wmv','ab')
	while 1:
		f = fn.read(1024*1024)
		if not f:
			break
		else:
			hexstr = binascii.b2a_hex(f) #转换成二进制数据用十六进制表示 bytes
			me_input = str(hexstr)[2:-1] #十六进制bytes变成字符串类型 str
			
			''' 这里插入加密解密程序 '''
			
			me_output = binascii.a2b_hex(me_input)
			print(len(me_input))

			fw.write(me_output)
	
	fw.close()


# fn = open('1.wmv','rb')
# fw = open('2.wmv','ab')
# f = fn.read()


# hexstr = binascii.b2a_hex(f) 
# me_input = str(hexstr)[2:-1]

# print(me_input,create_rating_dic(me_input))


