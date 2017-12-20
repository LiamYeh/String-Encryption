from collections import Counter
import binascii
'''
f = open('5','rb').read()
fw = open('6','wb')
hexstr = binascii.b2a_hex(f) 
me_input = str(hexstr)[2:-1]

content = me_input
length = len(content)

c = Counter(content)
ratio = {} #存放每个字符出现的概率
for alp,count in c.items():
	ratio.update({count/length:alp})

index = sorted(ratio) #按概率由小到大排序
alp_len = len(index) #统计有多少字符
encode_dic = {} #编码后的字典

if 16 >= alp_len > 8:
	list_0_to_8 = list(range(7,-1,-1)) 
	list_negative = list(range(-(alp_len-8),0,1))
	negative_to_8 = [(-i)+80 for i in list_negative]
	interval_list = negative_to_8 + list_0_to_8 #生成序列，按负号最少原则
	
	for inval,raio in zip(interval_list,index):
		encode_dic.update({ratio[raio]:inval})

elif 0 < alp_len <= 8:
	interval_list = list(range(alp_len-1,-1,-1)) 

	for inval,raio in zip(interval_list,index):
		encode_dic.update({ratio[raio]:inval})

else:
	raise ValueError(alp_len)


new_str = str()
for i in content:
	new_str = new_str + str(encode_dic[i])

new_str_len = len(new_str)
if new_str_len%2 != 0:
	new_str = '9' + new_str
	new_str_len = new_str_len + 1

compress_ratio = new_str_len/length

print(compress_ratio)
buffer_ = binascii.a2b_hex(new_str)
fw.write(buffer_)


###it does not work###
'''