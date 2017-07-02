#coding=utf-8
'''
根据rebuild_db改写而来，粗糙粗暴
@暂不考虑unicode字符问题
@不考虑shuffle随机数据库

重写思路：函数模块，内存中生成array整体，一次性灌入

1、函数find_list('.')找出所有音频文件，返回file_list,以文件基名排好序

2、函数bulid_seg(song),生成每一段 seg = entry[558]

3、主函数：循环迭代由file_list替换\\而来的song_list ，构建array并写入

'''

import os,sys,os.path,array

def list_folder(folder):
	global file_list
	for a in os.listdir(folder):
		file_path = os.path.join(folder,a)
		if os.path.isdir(file_path):
			list_folder(file_path)
		else:			
			if file_path.lower().endswith('.mp3') or file_path.lower().endswith('.m4a')\
			or file_path.lower().endswith('.m4b') or file_path.lower().endswith('.m4p')\
			or file_path.lower().endswith('.wav') or file_path.lower().endswith('.aa') :
				file_list.append(file_path)
	file_list.sort(lambda a,b:cmp(a.lower(),b.lower()))
	return file_list

def build_seg(song):
	ext = song.split('/')[-1].split('.')[-1].lower()
	entry = [0]*558
	entry[1]=0x02
	entry[2]=0x2E
	entry[3]=0x5A
	entry[4]=0xA5
	entry[5]=0x01
	entry[26]=0x64
	entry[29]=0x01
	entry[31]=0x02
	entry[13]=0x02
	entry[555] = 0x01
	if ext in ['mp3','aa']:
		entry[13] = 1
	elif ext == 'wav':
		entry[13] = 4
	if ext in ['m4b','aa']:
		entry[555] = 0
	t1 = [ord(i) for i in list(song)]
	pos = 1
	for t in t1:
		entry[32+pos] = t
		pos += 2
	return entry

def main():
	song_list = [l.replace('\\','/')[1:] for l in list_folder('.')]
	db_array = array.array("B")
	db_array.fromlist([0]*18)
	db_array[3]=0x01
	db_array[4]=0x06
	db_array[8]=0x12
	for song in song_list:
		db_array.fromlist(build_seg(song))
	total_count = len(song_list)
	db_array[2]=total_count&0xFF
	db_array[1]=total_count>>8
	try:
		iTunesSD = file("iPod_Control/iTunes/iTunesSD","wb")
		db_array.tofile(iTunesSD)
	except IOError:
		print 'Critical error: cannot write iTunesSD database file!'
		sys.exit(1)
	print 'iPod shuffle database was rebuilt successfully.Total %s songs' % total_count

file_list=[]
if __name__ == '__main__':
	main()
