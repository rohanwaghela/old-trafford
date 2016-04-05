# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 01:52:46 2016

@author: ROHAN
"""

Ma=1 #Mass flow rate of A
Mb=2 #Mass flow rate of B
P=1.0 #perimeter
U=100.0 #overall heat transfer coefficient
L=10.0 #length of heat exchanger
n=10.0 #no of points(including start and endpoint)
Z=0;t1=300;e=0.4;
while e>0.001:
    to=400;h=0.1;t2=t1+Z*0.001;
    tB=t2;
    for i in range(10):
        tb=t2;
        ta=to;
        deltax=L/(n-1);
        Cpa=4000+10*ta+0.01*ta*ta;
        da=-P*U/(Ma*Cpa);
        dtadx=da*(ta-tb);
        to=ta+dtadx*deltax;
        ta=to;
        Cpb=3000+5*tb+0.02*tb*tb;
        db=-P*U/(Mb*Cpb);
        dtbdx=db*(ta-tb);
        t2=tb+dtbdx*deltax;
    e=t2-300;
    if e<0:
        e=300-t2;
    Z=Z+1;
Ea=Ma*(4000*(400-ta)+10*0.5*(400*400-ta*ta)+0.01*0.33333*(400*400*400-ta*ta*ta))
Eb=Mb*(3000*(tB-t2)+5*0.5*(tB*tB-t2*t2)+0.33333*0.02*(tB*tB*tB-t2*t2*t2))
perce=100*(Ea-Eb)/Ea;
print "n=" ,n;
print "Tinlet of B = " , t1;
print "Toutlet of A= " ,ta;
print "Toutlet of B= " ,tb;
print "Tinlet of A= " , "400";
print "Percent Error in enthalpy (loss)=" , perce;


Ma=1 #Mass flow rate of A
Mb=2 #Mass flow rate of B
P=1.0 #perimeter
U=100.0 #overall heat transfer coefficient
L=10.0 #length of heat exchanger
n=30.0 #no of points(including start and endpoint)
Z=0;t1=300;e=0.4;
while e>0.001:
    to=400;h=0.1;t2=t1+Z*0.001;
    tB=t2;
    for i in range(30):
        tb=t2;
        ta=to;
        deltax=L/(n-1);
        Cpa=4000+10*ta+0.01*ta*ta;
        da=-P*U/(Ma*Cpa);
        dtadx=da*(ta-tb);
        to=ta+dtadx*deltax;
        ta=to;
        Cpb=3000+5*tb+0.02*tb*tb;
        db=-P*U/(Mb*Cpb);
        dtbdx=db*(ta-tb);
        t2=tb+dtbdx*deltax;
    e=t2-300;
    if e<0:
        e=300-t2;
    Z=Z+1;
Ea=Ma*(4000*(400-ta)+10*0.5*(400*400-ta*ta)+0.01*0.33333*(400*400*400-ta*ta*ta))
Eb=Mb*(3000*(tB-t2)+5*0.5*(tB*tB-t2*t2)+0.33333*0.02*(tB*tB*tB-t2*t2*t2))
perce=100*(Ea-Eb)/Ea;
print "n=" ,n;
print "Tinlet of B = " , t1;
print "Toutlet of A= " ,ta;
print "Toutlet of B= " ,tb;
print "Tinlet of A= " , "400";
print "Percent Error in enthalpy (loss)=" , perce;


Ma=1 #Mass flow rate of A
Mb=2 #Mass flow rate of B
P=1.0 #perimeter
U=100.0 #overall heat transfer coefficient
L=10.0 #length of heat exchanger
n=50.0 #no of points(including start and endpoint)
Z=0;t1=300;e=0.4;
while e>0.001:
    to=400;h=0.1;t2=t1+Z*0.001;
    tB=t2;
    for i in range(50):
        tb=t2;
        ta=to;
        deltax=L/(n-1);
        Cpa=4000+10*ta+0.01*ta*ta;
        da=-P*U/(Ma*Cpa);
        dtadx=da*(ta-tb);
        to=ta+dtadx*deltax;
        ta=to;
        Cpb=3000+5*tb+0.02*tb*tb;
        db=-P*U/(Mb*Cpb);
        dtbdx=db*(ta-tb);
        t2=tb+dtbdx*deltax;
    e=t2-300;
    if e<0:
        e=300-t2;
    Z=Z+1;
Ea=Ma*(4000*(400-ta)+10*0.5*(400*400-ta*ta)+0.01*0.33333*(400*400*400-ta*ta*ta))
Eb=Mb*(3000*(tB-t2)+5*0.5*(tB*tB-t2*t2)+0.33333*0.02*(tB*tB*tB-t2*t2*t2))
perce=100*(Ea-Eb)/Ea;
print "n=" ,n;
print "Tinlet of B = " , t1;
print "Toutlet of A= " ,ta;
print "Toutlet of B= " ,tb;
print "Tinlet of A= " , "400";
print "Percent Error in enthalpy (loss)=" , perce;


Ma=1 #Mass flow rate of A
Mb=2 #Mass flow rate of B
P=1.0 #perimeter
U=100.0 #overall heat transfer coefficient
L=10.0 #length of heat exchanger
n=100.0 #no of points(including start and endpoint)
Z=0;t1=300;e=0.4;
while e>0.001:
    to=400;h=0.1;t2=t1+Z*0.001;
    tB=t2;
    for i in range(100):
        tb=t2;
        ta=to;
        deltax=L/(n-1);
        Cpa=4000+10*ta+0.01*ta*ta;
        da=-P*U/(Ma*Cpa);
        dtadx=da*(ta-tb);
        to=ta+dtadx*deltax;
        ta=to;
        Cpb=3000+5*tb+0.02*tb*tb;
        db=-P*U/(Mb*Cpb);
        dtbdx=db*(ta-tb);
        t2=tb+dtbdx*deltax;
    e=t2-300;
    if e<0:
        e=300-t2;
    Z=Z+1;
Ea=Ma*(4000*(400-ta)+10*0.5*(400*400-ta*ta)+0.01*0.33333*(400*400*400-ta*ta*ta))
Eb=Mb*(3000*(tB-t2)+5*0.5*(tB*tB-t2*t2)+0.33333*0.02*(tB*tB*tB-t2*t2*t2))
perce=100*(Ea-Eb)/Ea;
print "n=" ,n;
print "Tinlet of B = " , t1;
print "Toutlet of A= " ,ta;
print "Toutlet of B= " ,tb;
print "Tinlet of A= " , "400";
print "Percent Error in enthalpy (loss)=" , perce;

#lineplot.py
import pylab as plt
x=[10,30,50,100]
y=[1.173,0.365,0.21589,0.107]
plt.plot(x,y,)
plt.show()