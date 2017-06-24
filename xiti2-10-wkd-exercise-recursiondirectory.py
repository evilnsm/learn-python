#coding=utf-8
import os
import glob
'''
用递归枚举文件夹内的文件、目录名
'''

#print os.listdir('c:\\')

def list_folder(folder='d:\\newbie'):
    if not os.path.exists('f:\\list_file.txt'):
        f = open('f:\\list_file.txt','w')
        f.close()

    if not os.path.isdir(folder):
        return '%s is not a valuable directory' % folder
    
    for a in os.listdir(folder):
        file_path = os.path.join(folder,a)
        if os.path.isdir(file_path):        
            list_folder(file_path)
        else:
            con = open('f:\\list_file.txt','a+')
            con.write(file_path+'\r\n')
            con.close()
            
list_folder()


