#! -*-coding: utf-8 -*-

import os
import shutil

def copy_and_rename(source_dir,target_dir):
    i = 1
    # 遍历
    for root,dirs,files in os.walk(source_dir):
        for filename in files:
            tempfile = os.path.join(root,filename)
            tempsplit = os.path.split(root)
            # 找到所有最后文件夹路径为动漫的
            if (tempsplit[1] == '动漫'):
                tarfilename = str(i) + os.path.splitext(filename)[1]
                i+=1
                tarfile = os.path.join(target_dir , tarfilename)
                shutil.copyfile(tempfile,tarfile)

def tree(source_dir):
    for root,dirs,files in os.walk(source_dir):
        level = root.replace(source_dir,'').count(os.sep)
        dir_indent = "|   " * (level-1) + "|-- "  
        file_indent = "|   " * level + "|-- "  
        if not level:  
            print('.')  
        else:  
            print('{}{}'.format(dir_indent, os.path.basename(root)))  
        #for f in files:  
            #print('{}{}'.format(file_indent, f))   

    
        
if __name__ == '__main__':
    path='D:\\桌面\\Desktop\\壁纸\\2017壁纸精选合集'
    targetpath='D:\\桌面\\Desktop\\壁纸\\动漫'

    tree(path)
    #copy_and_rename(path,targetpath)

