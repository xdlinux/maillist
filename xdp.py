#!/usr/bin/python
# -*- coding: utf-8 -*- 
import urllib
import re                       #re 包括正则表达处理的部分
import sys                      #import this for debug sys中包括文件处理的部分
#################################################
####get the web of xdlinux in github 获得网页####
#################################################
url="http://github.com/xdlinux" #set url 设置url 
web=urllib.urlopen(url)         #get the url 获得网页
content=web.read()              #get the content 获得网页内容
#

#print for debug this is not real part of this code 
#print content                  #test the content 测试网页内容
file=open('cache/xdgithub.html','w')                     #open the file  打开文件准备写入
print >> file,content           #save the content to the file 存储网页内容到文件
file.close()                    #close the file 写入结束关闭文件
#
###########################################
####analysis the content 开始处理文件了####
###########################################
f_src=open('cache/xdgithub.html','r')                     #open the source file 以只读的形式打开文件
f_tar=open('data/xdgithub.txt','w+')                       #open the target file  

################





###############

print >> f_tar,"haha"


#debug#########
print "####cache/xdgithub.html####"
f_src.seek(0)                      #go back to the head of file 回到文件开始
print f_src.read(200)              #print the 200 litter in head of file_src  输出开始的200个字
print "####data/xdgithub.txt####"
f_tar.seek(0)
print f_tar.read(200)              #print the content of file_src  
################

f_src.close()
f_tar.close()                    #close the files关闭文件

########################################################
####build the project.html 构建新的xdgithub.html文件####
########################################################
f_src=open('data/xdgithub.txt','r')                       #open the data file 
f_tar=open('project.html','w')

#######





########

##debug## 
#print "data/xdgithub.txt:"
#f_tar.seek(0)
#print f_src.read(200)               #print the files   
#########


print >> f_tar,f_src.read()
f_src.close()
f_tar.close()

