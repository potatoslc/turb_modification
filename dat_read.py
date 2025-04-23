#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 16:25:07 2025

@author: potato
"""
import pandas as pd
import math

file = "/Users/potato/Downloads/hit_ic_4_128.dat"

df1 = pd.read_csv(file)
import math

"""
dict1 = {}
for i in range(len(df1)):
    temp_s = str(df1.iloc[i,3]) +str(df1.iloc[i,4]) +str(df1.iloc[i,5])
    if (temp_s in dict1):
        print("duplicated")
        break
    else:
        dict1[temp_s] = 0

        
speed_ttl=[]
for i in range(len(df1)):
    speed_ttl.append( math.sqrt( (df1.iloc[i,3])**2 +  (df1.iloc[i,4])**2  +   (df1.iloc[i,5])**2) )
"""
def modify(df,shape):
    headers = df.columns
    xyz_header = list(headers[0:3])
    speed_header = list(headers[3:])
    x,y,z = headers[0],headers[1],headers[2]
    new_df = df.sort_values(by=xyz_header)
    # basic case: all ones 
    xyz_df =new_df[xyz_header]
    speed_df = new_df[speed_header]
    cutoff = round(math.pi,4)
    new_df[' u'].loc[new_df['# x']>cutoff ]=0
    new_df[' v'].loc[new_df['# x']>cutoff ]=0
    new_df[' w'].loc[new_df['# x']>cutoff ]=0
    
    return new_df