
#encoding:utf-8
"""
@author:cmx
@file:crowd_feature
@time:2019/5/27 19:07
"""

import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from sklearn.cluster import KMeans


if __name__ == "__main__":
    inputfile='RFM_model.xlsx'
    data=pd.read_excel(inputfile)
    data=data.ix[:,[1,2,3,4]]
    crowd_one=data.loc[data['LABEL']==0]
    crowd_one_num=len(crowd_one.index)
    crowd_two=data.loc[data['LABEL']==1]
    crowd_two_num=len(crowd_two.index)
    crowd_three=data.loc[data['LABEL']==2]
    crowd_three_num=len(crowd_three.index)

    print('第一类人群特征({}人)：\n{}\n第二类人群特征({}人):\n{}\n第三类人群特征({}人):\n{}'.format(crowd_one_num,crowd_one.mean(),crowd_two_num,crowd_two.mean(),crowd_three_num,crowd_three.mean()))

    ax=plt.subplot(321)
    plt.axis([0,30,0,25000])
    plt.xlabel(u'crowd_one_R')
    plt.ylabel(u'crowd_one_M')
    plt.scatter(crowd_one.ix[:,0],crowd_one.ix[:,2],s=5)

    ax=plt.subplot(322)
    plt.axis([0,30,0,25000])
    plt.xlabel(u'crowd_one_F')
    plt.ylabel(u'crowd_one_M')
    plt.scatter(crowd_one.ix[:,1],crowd_one.ix[:,2],s=5)

    ax=plt.subplot(323)
    plt.axis([0,30,20000,80000])
    plt.xlabel(u'crowd_one_R')
    plt.ylabel(u'crowd_one_M')
    plt.scatter(crowd_two.ix[:,0],crowd_two.ix[:,2],s=5)

    ax=plt.subplot(324)
    plt.axis([0,120,20000,80000])
    plt.xlabel(u'crowd_one_F')
    plt.ylabel(u'crowd_one_M')
    plt.scatter(crowd_two.ix[:,1],crowd_two.ix[:,2],s=5)

    ax=plt.subplot(325)
    plt.axis([0,16,50000,300000])
    plt.xlabel(u'crowd_one_R')
    plt.ylabel(u'crowd_one_M')
    plt.scatter(crowd_three.ix[:,0],crowd_three.ix[:,2],s=5)

    ax=plt.subplot(326)
    plt.axis([0,230,50000,300000])
    plt.xlabel(u'crowd_one_F')
    plt.ylabel(u'crowd_one_M')
    plt.scatter(crowd_three.ix[:,1],crowd_three.ix[:,2],s=5)

    plt.show()