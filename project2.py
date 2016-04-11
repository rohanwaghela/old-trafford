# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 01:15:49 2016

@author: ROHAN
"""

import numpy
import scipy
from scipy.optimize import fsolve
import matplotlib.pyplot as plt 
#Y= concentration/mole fraction in liquid phase (Kg of solute/kg of solvent)
#X= concentration/mole fraction in solid phase (Kg of solute/kg of solid)  

#*****Data*****#
# x:kg carbon/kg soln
# y_star: Equilibrium colour, units/kg soln.
# X:adsorbate concentration, units/kg carbon
# Data = [x Y_star]
Data =numpy.array([[0, 9.6],[0.001, 8.6],[0.004 ,6.3],[0.008, 4.3],[0.02 ,1.7],[0.04, 0.7]]);
Yo = 9.6;# [units of colour/kg soln]
Y1 = 0.1*Yo;# [units of colour/kg soln]
Ls = 1000.0;# [kg soln]
#****************#

n = 1.66;# [slope of line]
# At X = 663, Y_star = 4.3
X = 663;
Y_star = 4.3;
m = Y_star/X**n;
# Freundlich Equation:
def f76(X):
    return m*X**n
X = numpy.arange(0,1000,1);
plt.plot(X,f76(X));
plt.grid('on');
plt.xlabel("units of colour/kg carbon");
plt.ylabel("units of colour/kg solution");
plt.show()
# Single Stage Operation:
# Since fresh carbn is used:
Xo = 0;# [units/kg carbon]
# From scf(30):
X1 = 270;# [units/kg carbon]
Data2 =numpy.array([[Xo, Yo],[X1, Y1]]);

plt.plot(X,f76(X),label="Equilbrium curve")
plt.plot(Data2[:,0],Data2[:,1],label="Operating line curve")
plt.grid('on');
plt.xlabel("units of colour/kg carbon");
plt.ylabel("units of colour/kg solution");
plt.legend(loc='upper left');
plt.title("Single stage operation");
plt.show()
# From Eqn. 11.4:
Ss = Ls*((Yo-Y1)/(X1-Xo));# [kg carbon/kg soln]
print"Quantity of fresh carbon recquired for single stage operation: ",Ss," kg carbon/1000 kg solution\n"

# Two stage cross current operation:
# For the minimumamount of carbon:
X1 = 565;# [units/kg carbon]
Y1 = 3.30;# [units of colour/kg soln]
X2 = 270;# [units/kg carbon]
Y2 = 0.96;# [units of colour/kg soln]
Data3 = numpy.array([[Xo ,Yo],[X1 ,Y1]]);
Data4 = numpy.array([[0 ,Y1],[X2 ,Y2]]);

plt.plot(X,f76(X),label="Equilbrium curve")
plt.plot(Data3[:,0],Data3[:,1],label="First of two Cocurrent")
plt.plot(Data4[:,0],Data4[:,1],label="Second of two Cocurrent")
plt.grid('on');
plt.xlabel("units of colour/kg carbon");
plt.ylabel("units of colour/kg solution");
plt.legend(loc='upper left');
plt.title("Two stage Cross current operation");
plt.show()
# From Eqn. 11.8:
Ss1 = Ls*(Yo-Y1)/(X1-Xo);# [kg]
Ss2 = Ls*(Y1-Y2)/(X2-Xo);# [kg]
Ss = Ss1+Ss2;# [kg]
print"Quantity of fresh carbon recquired for two stage crosscurrent operation: ",Ss," kg carbon/1000 kg solution\n"