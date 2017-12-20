from main import *
import json

def hide_code(apath,bpath,key):
	f = open(apath,'r',encoding='utf-8')
	dicts = dict()
	for line in f.readlines():
		string,md5 = encrypt(line,key,md5_check=True)
		dicts.update({md5:string})
	f.close()

	with open(bpath, 'w') as f:
		json.dump(dicts, f)

def show_code(apath,bpath,key):
	with open(apath, 'r') as f:
		dicts = json.load(f)

	fw = open(bpath,'w',encoding='utf-8')
	for md5 in dicts.keys():
		fw.write(decrypt(dicts[md5],key,md5=md5))
	fw.close()

if __name__ == '__main__':
	apath = 'F:/我的影音/视频相关文档/password.json' #加密后的json文件
	bpath = 'F:/我的影音/视频相关文档/password.txt' #解密后存放的文件
	key = '123456' #解密密码
	#show_code(apath,bpath,key)

	apath = 'F:/我的影音/视频相关文档/password.txt' #待加密的文件
	bpath = 'F:/我的影音/视频相关文档/password.json' #加密后放入的文件
	key = '123456' #加密密码
	hide_code(apath, bpath, key)

