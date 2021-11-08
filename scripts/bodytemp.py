#!/usr/bin/env python3
import numpy as np

class BodyTemp():
    def __init__(self,debug=False):
        self.maxtemp=40.0
        self.mintemp=33.0
        self.debug=debug
        self.temp=[]
        if self.debug:
            print("max",self.maxtemp)
            print("min",self.mintemp)
    def read(self,Otemp,Atemp=[0,0]):
        self.AT=Atemp[0] | Atemp[1]<<8
        self.OT=Otemp[0] | Otemp[1]<<8
    def bodytemp(self):
        '''
        return
            -1  0:error
            other:Body Temperature and Number of recorded data
        '''
        #値変換
        AmbientTemp = round((self.AT) *0.02 -273.15,2)#周辺温度
        ObjectTemp = round((self.OT) *0.02 -273.15,2)#物体温度
        if self.AT!=0:
            htemp=ObjectTemp-AmbientTemp
        else:
            htemp=ObjectTemp
        #制限
        if htemp>self.maxtemp:
            htemp=-1
            self.temp=[]
        elif htemp<self.mintemp:
            htemp=-1
            self.temp=[]
        else:
            if not(htemp in self.temp):#self.tempの中に同じ値が含まれていないとき
                self.temp.append(htemp)
            temp=np.array(self.temp)#numpyのリストに変換
            htemp=round(np.median(temp),1)#中央値
        if self.debug:
            print("AmbientTemp:",AmbientTemp,"[℃]/ObjectTemp",ObjectTemp,"[℃]/",htemp,"[℃]/",len(self.temp))
        return htemp,len(self.temp)