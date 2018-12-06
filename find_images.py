# -*- coding: utf-8 -*-
"""
Wrote by Li Gantong

Time:2018-12-6
"""
import os
import pandas as pd
from PIL import Image



def get_file_list(file_dir):
    """
    参数：
        file_dir:要搜索的文件夹所在目录
    功能：
        获取目录下的所有图片的文件夹目录，图片名称，尺寸，模式
    返回值：
        root_list：目录下每张图片所在的文件夹列表
        file_list：目录下每张图片的名称列表
        size_list：目录下每张图片的尺寸列表，每个尺寸均为元组(height,width)
        mode_list：目录下每张图片的模式列表，每个模式为字符串
    """
    root_list=[]
    file_list=[]
    size_list=[]
    mode_list=[]
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            if ".jpg" in file.lower():
                root_list.append(root)
                file_list.append(file)
                img=Image.open(os.path.join(root,file))
                size_list.append(img.size)
                mode_list.append(img.mode)
        print("正在处理：",root)
    return root_list,file_list,size_list,mode_list

if __name__=="__main__":
    #分别获取两个目录下的图片信息
    root_list,file_list,size_list,mode_list=get_file_list("D:\\test1")
    root_list2,file_list2,size_list2,mode_list2=get_file_list("C:\\test2\\images")
    #两个目录下的图片信息叠加
    root_list+=root_list2
    file_list+=file_list2
    size_list+=size_list2
    mode_list+=mode_list2
    #将两个目录下的图片信息存为csv图片
    data=pd.DataFrame({"number":list(range(1,len(root_list)+1)),"root":root_list,"file_list":
        file_list,"size":size_list,"mode":mode_list})
    data.to_csv("analysis.csv",index=False,header=True,encoding="gb2312")

