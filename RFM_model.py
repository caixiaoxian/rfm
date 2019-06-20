#encoding:utf-8
"""
@author:cmx
@file:RFM_model.py
@time:2019/5/26 18:31
"""
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
import pylab

if __name__ == "__main__":
    inputfile='RFM_model.xlsx'
    k=3

    #读取数据并进行聚类分析
    data=pd.read_excel(inputfile)
    data=data.ix[:,1:4]

    #调用kmeans
    kmodel=KMeans(n_clusters=k,n_jobs=4)

    result=kmodel.fit_predict(data)

    label=list(kmodel.labels_)

    writer=pd.ExcelWriter('save1.xlsx')
    df=pd.DataFrame(data=label)
    df.to_excel(writer,'Sheet1')
    writer.save()

    ax=plt.subplot(111,projection='3d')
    ax.scatter(data.ix[:,0],data.ix[:,1],data.ix[:,2],c=label)

    ax.set_xlabel('R')
    ax.set_ylabel('F')
    ax.set_zlabel('M')
    plt.show()
