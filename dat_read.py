#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 16:25:07 2025

@author: potato
"""
import pandas as pd
import math

file = "/home/u0890475/Documents/SW_file/PeleLMeX/Submodules/PelePhysics/Support/TurbFileHIT/hit_ic_4_128_org.dat"

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
def modify(df,shape:int):
    headers = df.columns
    xyz_header = list(headers[0:3])
    speed_header = list(headers[3:])
    x,y,z = headers[0],headers[1],headers[2]
    new_df = df.sort_values(by=xyz_header)
    # basic case: all ones 
    xyz_df =new_df[xyz_header]
    speed_df = new_df[speed_header]
    cutoff = round(math.pi,4)
    new_df[' u'].loc[new_df['# x']>cutoff ]=0.01
    new_df[' v'].loc[new_df['# x']>cutoff ]=0.01
    new_df[' w'].loc[new_df['# x']>cutoff ]=0.01
    new_df.to_csv('test1.dat',sep=',',index = False)
    return new_df

def modify_iso1(df):
    headers = df.columns
    xyz_header = list(headers[0:3])
    speed_header = list(headers[3:])
    x,y,z = headers[0],headers[1],headers[2]
    new_df = df.sort_values(by=xyz_header)
    # basic case: all ones 
    xyz_df =new_df[xyz_header]
    speed_df = new_df[speed_header]
    cutoff_2 = round(math.pi,4)
    cutoff_1 = cutoff_2/2
    cutoff_3 = math.pi*1.5
    #calculate the sum of x values 
    u_sum = sum(new_df[' u'][new_df[x]<=cutoff_1])
    v_sum = sum(new_df[' v'][new_df[x]<=cutoff_1])
    w_sum = sum(new_df[' u'][new_df[x]<=cutoff_1])
    #4 sections, first section keep,2nd section reduced 2/3 of cumulated speed
    #3rd section reduced 1/3 of cumulated speed, 4th sections all zeros
    new_df[' u'].loc[(new_df['# x']>cutoff_1)& (new_df['# x']<=cutoff_2)]-=u_sum/349525.333
    new_df[' v'].loc[(new_df['# x']>cutoff_1)& (new_df['# x']<=cutoff_2) ]-=v_sum/349525.333
    new_df[' w'].loc[(new_df['# x']>cutoff_1)& (new_df['# x']<=cutoff_2) ]-=w_sum/349525.333
    
    new_df[' u'].loc[(new_df['# x']>cutoff_2)& (new_df['# x']<=cutoff_3)]-=u_sum/174762.6667
    new_df[' v'].loc[(new_df['# x']>cutoff_2)& (new_df['# x']<=cutoff_3) ]-=v_sum/174762.6667
    new_df[' w'].loc[(new_df['# x']>cutoff_2)& (new_df['# x']<=cutoff_3) ]-=w_sum/174762.6667
    new_df[' u'].loc[new_df['# x']>cutoff_3 ]=0.01
    new_df[' v'].loc[new_df['# x']>cutoff_3 ]=0.01
    new_df[' w'].loc[new_df['# x']>cutoff_3 ]=0.01
    
    #new_df.to_csv('test1.dat',sep=',',index = False)    
    
    return





























