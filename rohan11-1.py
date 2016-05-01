# -*- coding: utf-8 -*-
"""
Created on Sat Jan 01 03:49:16 2005

@author: ROHAN
"""

import scipy
from scipy.integrate import odeint
from scipy import linspace

kla1=0.0007 # mass transfer coefficient for CO2
kla2=0.0007 #mass teansfer coefficient for CH4
kgw=0.0000002 # mass transfer coefficient for water
d1=0.04494 # molar density of CO2
d2=0.04474 #molar density of CH4
P=101325.0 # total pressure
T=300.0 #temperature
VP=133.32*scipy.exp(18.3036-3816.44/(T-46.13)) # Antoine equation & VP is in Pa
H1=2.97619 # Henrys constant of CO2
H2=72.325 #Henrys constant of CH4
#parameters are obtained from the internet
#http://www.mpch-mainz.mpg.de/~sander/res/henry.html
Vg=100.0 #flow rate of gas
Vl=100.0 #flow rate of liquid
R=8.314 #ideal gas constant
A=0.004415 # area of column
n=10 #number of points
z=0
yco2=0.5*Vg
ych4=0.5*Vg
yw=0
lco2=0
lch4=0
lw=Vl
e=1; e1=1; e2=1; e3=1;
#conversion of units
while (e2>0.001 and e3>0.001):
        yw=0;yco2=0.5*Vg; ych4=0.5*Vg
        if e1>0.001:
           lch4=(0+z*0.01)*Vl
        if e2>0.001:
            lco2=(0+z*0.01)*Vl;  
        if e3>1:
                lw=1*Vl-lco2-lch4;
        for i in range(n):
        
            def myModel(y,t):
   
               dy1=-kla1*A*(((y[0]*P)/(H1*(y[0]+y[1]+y[2])))-(d1*y[3]/(y[3]+y[4]+y[5])))
               dy2=-kla2*A*(((y[1]*P)/(H2*(y[0]+y[1]+y[2])))-(d2*y[4]/(y[3]+y[4]+y[5])))
               dy3=kgw*A*((y[2]*P/(y[0]+y[1]+y[2]))-VP/(R*T))
               dy4=-kla1*A*(((y[0]*P)/(H1*(y[0]+y[1]+y[2])))-(d1*y[3]/(y[3]+y[4]+y[5])))
               dy5=-kla2*A*(((y[1]*P)/(H2*(y[0]+y[1]+y[2])))-(d2*y[4]/(y[3]+y[4]+y[5])))
               dy6=kgw*A*((y[2]*P/(y[0]+y[1]+y[2]))-VP/(R*T))
               return dy1,dy2,dy3,dy4,dy5,dy6

            time=linspace(0,5,n)
            yinit=[50,50,0,lco2,lch4,lw]
            y= odeint(myModel,yinit,time)
    
    
    
            e1=100-y[n-1,5];
            if e1<0:
                e1=-e1
            e2=y[n-1,3]/Vl;
            if e2<0:
                e2=-e2
            e3=y[n-1,4]/Vl;
            if e3<0:
                e3=-e3
          
print e1,e2,e3
z=z+1;
print y[n-1,5];    
print y[n-1,4]; 
print y[n-1,3];    
print y[n-1,2];
print y[n-1,1];
print y[n-1,0];