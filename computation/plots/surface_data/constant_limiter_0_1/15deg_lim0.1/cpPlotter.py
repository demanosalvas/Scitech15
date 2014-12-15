#
# File: cpPlotter.py
# Script for visualizing the cp distribution.
# Plots the experimental Cp plus the Cp for each grid for limiter value of 0.1
# 

# Import statements for native python modules.

import sys, os

# Import statements for additional packages or user-created modules.

import numpy as np
import pandas as pd # it can read the SU2 csv files. the csv module wasn't capable of it.
from matplotlib import pyplot as plt
from matplotlib import mlab # read a csv file directly into a numpy record

# Function read each surface file and return x, cp in the right order.
def read_surface_file(filename):
    File = pd.read_csv(filename)
    # Sort the file
    File = File.sort('Global_Index')
    # write the sorted file
    File.to_csv('temp.csv', index=False)
    # read the sorted file into numpy record array
    File  = mlab.csv2rec('temp.csv')
    # Remove temporary flow solution csv file
    os.remove('temp.csv')
    x = File.x_coord
    cp = File.pressure_coefficient
    # Append the first point to close the Cp plot
    x = np.append(x,x[0])
    cp = np.append(cp,cp[0])

    return x, cp

# Experimental run
file_exp = 'CP_Gregory_expdata_15.dat'
exp_data = pd.read_csv(file_exp,delim_whitespace=True,skiprows=4)
x_exp = exp_data['x/c']
cp_exp = exp_data.cp

# CFD runs
filename0 = 'surface_flowG0_Lim0.1_AoA15.csv'
filename1 = 'surface_flowG1_Lim0.1_AoA15.csv'
filename2 = 'surface_flowG2_Lim0.1_AoA15.csv'
filename3 = 'surface_flowG3_Lim0.1_AoA15.csv'
filename4 = 'surface_flowG4_Lim0.1_AoA15.csv'

x0, cp0 = read_surface_file(filename0)
x1, cp1 = read_surface_file(filename1)
x2, cp2 = read_surface_file(filename2)
x3, cp3 = read_surface_file(filename3)
x4, cp4 = read_surface_file(filename4)

# Plotting the data
fig, ax = plt.subplots()
ax.tick_params(axis='y',labelsize=16)
ax.tick_params(axis='x',labelsize=16)
ax.set_xlabel('$x/c$',size=18)
ax.set_ylabel('$C_p$',rotation=0,size=18)
ax.plot(x0,cp0,label='$G0$',color='r',lw=2)
ax.plot(x1,cp1,label='$G1$',color='b',lw=2)
ax.plot(x2,cp2,label='$G2$',color='g',lw=2)
ax.plot(x3,cp3,label='$G3$',color='c',lw=2)
ax.plot(x4,cp4,label='$G4$',color='m',lw=2)
ax.plot(x_exp,cp_exp,label='$exp$',color='k',linestyle='o',marker='o',fillstyle='none',markersize=8)
ax.legend(loc='best',fancybox=True)
ax.set_yticks([-11,-5,1])
ax.set_xticks([0,1])
ax.set_ylim(-12.07,2.07)
ax.set_xlim(-0.05,1.05)

ax.set_ylim(ax.get_ylim()[::-1]) #flip the y axis.
fig.savefig('Cp_vs_Grid_Lim_0_1_deg15.pdf')
plt.show()


