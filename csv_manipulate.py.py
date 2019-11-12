#%%
import pandas as pd
import numpy as np
from numpy import NaN, NAN , nan
#step3
euro12= pd.read_csv("D:\code\Quarter 2\Assignment-2\Euro_2012_stats_TEAM.csv",keep_default_na=False)
#step4
print(euro12.iloc[:,1])
#step5
print("Total teams participating are",len(euro12.index))
#step6
print("Total no of columns",len(euro12.columns))
#step7
new_data=euro12[['Team','Yellow Cards','Red Cards']]
print(new_data)
#step8
redcards = new_data.sort_values(by='Red Cards')
print(redcards)

yellowcards = new_data.sort_values(by='Yellow Cards')
print(yellowcards)

#step9
x = euro12['Yellow Cards'].mean()
print("Mean of yellow cards is =",x)
#step10
print(euro12[euro12['Goals']>6])
#print(filt)
#step11
print(euro12[euro12['Team'].str.match('G')])
#step12
euro12.iloc[:,:7]
#step13
euro12.iloc[:,:-3]
#step14
#%%
#euro12.loc[['England','Russia','Italy'],'Shooting Accuracy']

perf = ['i','e','C','h','e','n','n','a','i', 'P','a','t','n','a','a','q']
len(perf) 
euro12['Performance']=perf

def f(row):
    if row['Goals']<=2:
        val = "Below Average"
    elif row['Goals']>2 and row['Goals']<=5 :
        val = "Average"
    elif row['Goals']>5 and row['Goals']<=10:
        val = "Above Average"
    else:
        val="Excellent"
    return val

euro12['Performance'] = euro12.apply(f, axis=1)
euro12[['Team','Goals','Performance']]




#%%
