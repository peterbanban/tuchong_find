# _*_ coding:utf-8 _*_
#GVIM 添加汉字注释

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#以上定义字符集 使得代码可用汉字

import json
import urllib2
import urllib
import xlrd
import xlwt 
import os
from bs4 import BeautifulSoup
import httplib

###共8页的分类信息，遍历获得类别名称作为类别的链接地址
for i in range(4,9):
    kind_url='https://tuchong.com/rest/tag-categories/subject?page='+str(i)+'&count=20'
    request=urllib2.Request(kind_url)
    response=urllib2.urlopen(request,timeout=20)
    result=json.loads(response.read())
    data=result['data']

    for a in data['tag_list']:
        tag_name= a['tag_name']
        print tag_name

        ###遍历具体的某个类别,每类有100页，逐层获取到imageId和userId作为图片链接地址
        for page in range(1,101):
            image_url='https://tuchong.com/rest/tags/'+tag_name+'/posts?page='+str(page)+'&count=20'      
            try:
                request=urllib2.Request(image_url)
                response=urllib2.urlopen(request,timeout=20)
                result=json.loads(response.read())
            except:
                continue
            for b in result['postList']:
                count=b['image_count']
                nomber=1

                ###遍历每一标题下的所有图片
                for i in range (0,count):
                    images=b['images'][i]
                    user_id=images['user_id']
                    image_id=images['img_id']
                    title=b['title']
                    if title=='':
                        title=str(user_id)+str(nomber)
                    else:
                        title=title+str(nomber)
                    nomber=nomber+1
                    print title.encode('gbk','ignore')+'-'+str(user_id)+'-'+str(image_id)
                    url='https://photo.tuchong.com/'+str(user_id)+'/f/'+str(image_id)+'.webp'
                    
                    ###通过获取到的图片链接保存图片到本地
                    try:
                        f=open('C:\Users\Administrator\Desktop\image\\'+title+'.webp','wb')
                        req=urllib2.urlopen(url)
                        buf=req.read()
                        f.write(buf)
                        f.close()
                    except:
                        continue;
                print '-------------------'
             



            



