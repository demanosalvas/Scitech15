# This file generates the limiter vs. force coefficients plots.
# The data was copied from the google doc.

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Experimental Data
# Linearly interpolated between to get the data at 15.0 deg for each experiment and the average is reported here.
Cl_exp = np.array([1.4938,1.50826,1.49886])
Cd_exp = np.array([0.018313,0.017449,0.018003])
Cl_exp = np.ones(3)*np.mean(Cl_exp)
Cd_exp = np.ones(3)*np.mean(Cd_exp)



# Data From Google Sheet

limiter = [1,2,3] # This values are just used for plotting.
limiter_labels = ['0.1','1','10'] #limiter coefficient value used for all grids.


# Coarsest Grid G0
# Cl and Cd for alpha = [0,10,15degrees] and limiter = [0.1,1,10]
# None of the forces converged for the limiter coefficient of 10. 
G0 = {}
G0['limiter'] = np.array(limiter)
G0['Cl_0'] = np.array([-0.0000013122,-0.0000021773,np.inf])
G0['Cd_0'] = np.array([0.0093650872,0.0002450769,np.inf])
G0['Cl_10'] = np.array([0.937781304,0.7205364105,np.inf])
G0['Cd_10'] = np.array([0.0449743042,0.0356777066,np.inf])
G0['Cl_15'] = np.array([1.0588826317,0.549381038,np.inf])
G0['Cd_15'] = np.array([0.1827848017,0.1426560954,np.inf])

# Coarsest Grid G1
# Cl and Cd for alpha = [0,10,15degrees] and limiter = [0.1,1,10]
G1 = {}
G1['limiter'] = np.array(limiter)
G1['Cl_0'] = np.array([-0.000002,-0.000002,-0.000002])
G1['Cd_0'] = np.array([0.008492,0.005204,0.007372])
G1['Cl_10'] = np.array([1.07624,1.088251,1.086235])
G1['Cd_10'] = np.array([0.020257,0.0138,0.014639])
G1['Cl_15'] = np.array([1.467075,1.476419,1.475586])
G1['Cd_15'] = np.array([0.047514,0.032396,0.02884])

# Coarsest Grid G2
# Cl and Cd for alpha = [0,10,15degrees] and limiter = [0.1,1,10]
G2 = {}
G2['limiter'] = np.array(limiter)
G2['Cl_0'] = np.array([-0.000003,-0.000003,-0.000003])
G2['Cd_0'] = np.array([0.008098,0.00639,0.008027])
G2['Cl_10'] = np.array([1.097679,1.102034,1.101135])
G2['Cd_10'] = np.array([0.014381,0.012859,0.013362])
G2['Cl_15'] = np.array([1.54909,1.551489,1.55236])
G2['Cd_15'] = np.array([0.027084,0.024296,0.0239])

# Coarsest Grid G3
# Cl and Cd for alpha = [0,10,15degrees] and limiter = [0.1,1,10]
# np.inf these cases were not run. They didn't diverge.
G3 = {}
G3['limiter'] = np.array(limiter)
G3['Cl_0'] = np.array([-0.000003,np.inf,np.inf])
G3['Cd_0'] = np.array([0.008006,np.inf,np.inf])
G3['Cl_10'] = np.array([1.098833,np.inf,np.inf])
G3['Cd_10'] = np.array([0.012774,np.inf,np.inf])
G3['Cl_15'] = np.array([1.557744272,1.560033016,1.560165967])
G3['Cd_15'] = np.array([0.0226367359,0.0219841736,0.0218348323])

# Coarsest Grid G4
# Cl and Cd for alpha = [0,10,15degrees] and limiter = [0.1,1,10]
G4 = {}
G4['limiter'] = np.array(limiter)
G4['Cl_0'] = np.array([0,np.inf,np.inf])
G4['Cd_0'] = np.array([0.008096,np.inf,np.inf])
G4['Cl_10'] = np.array([np.inf,np.inf,np.inf])
G4['Cd_10'] = np.array([np.inf,np.inf,np.inf])
G4['Cl_15'] = np.array([1.557797,1.558714,1.5588])
G4['Cd_15'] = np.array([0.021462,0.021262,0.021245])



# default color list for matplotlib b, g, r, c, m, y, k
# Make G0 be the red one

# Only plot 15 degrees data, others AoA don't have data for all the runs.

### Lift of 15 degrees. ###
fig, ax = plt.subplots()
ax.tick_params(axis='y',labelsize=16)# The xaxis size is set below.
ax.set_xlabel('$Limiter\,Coefficient$',size=18)
ax.set_ylabel('$C_l$',rotation=0,size=18)
# Empty G0, helps for getting legend correct
ax.plot(G0['limiter'],np.array([np.inf,np.inf,np.inf]),label='$G0$',color='r',linestyle='--',marker='o',markersize=8,lw=2)
ax.plot(G1['limiter'],G1['Cl_15'],label='$G1$',color='b',marker='s',markersize=8,lw=2)
ax.plot(G2['limiter'],G2['Cl_15'],label='$G2$',color='g',marker='^',markersize=8,lw=2)
ax.plot(G3['limiter'],G3['Cl_15'],label='$G3$',color='c',marker='v',markersize=8,lw=2)
ax.plot(G4['limiter'],G4['Cl_15'],label='$G4$',color='m',marker='d',markersize=8,lw=2)
ax.plot(limiter,Cl_exp,label='exp',color='k',linestyle='-.')
#lgd = ax.legend(loc='upper center',fancybox=True, bbox_to_anchor=(0.5,-0.12),ncol=5)
lgd = ax.legend(loc='best',fancybox=True)
ax.set_xticks(limiter)
ax.set_xticklabels(limiter_labels,size=16)
ax.set_yticks([1.46,1.57])
ax.set_ylim(1.455,1.575)


# Put G0 on its own axis.
ax2 = ax.twinx()
ax2.plot(G0['limiter'],G0['Cl_15'],label='$G0$',color='r',linestyle='--',marker='o',markersize=8,lw=2)
for label in ax2.get_yticklabels():
  label.set_color('red')
ax2.set_yticks([0,0.55,1.06,1.57])
ax2.set_ylim([-0.07,1.64])
ax2.set_xlim(0.9,3.1) # Make x-axis nicer looking.
ax2.tick_params(axis='y',labelsize=16)

# Clean up the graph remove the top part of the box.
ax.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
# Remove the left over ticks at the top.
#ax.tick_params(top='off')
ax.xaxis.tick_bottom()
# Change color of right axis
ax2.spines['right'].set_color('r')
major_formatter = mpl.ticker.FormatStrFormatter('%g')
#ax.xaxis.set_major_formatter(major_formatter) # This will write over the custom labels.
ax.yaxis.set_major_formatter(major_formatter)
ax2.yaxis.set_major_formatter(major_formatter)

fig.savefig('limiter_vs_lift_15deg.pdf',bbox_extra_artists=(lgd,), bbox_inches='tight')# allows the legend to be outside the box when saving the figure.




### Drag of 15 degrees. ###
fig, ax = plt.subplots()
ax.tick_params(axis='y',labelsize=16)# The xaxis size is set below.
ax.set_xlabel('$Limiter\,Coefficient$',size=18)
ax.set_ylabel('$C_d$',rotation=0,size=18)
#ax.set_title('$15\, deg$')
# Empty G0, helps for getting legend correct
ax.plot(G0['limiter'],np.array([np.inf,np.inf,np.inf]),label='$G0$',color='r',linestyle='--',marker='o',markersize=8,lw=2)
ax.plot(G1['limiter'],G1['Cd_15'],label='$G1$',color='b',marker='s',markersize=8,lw=2)
ax.plot(G2['limiter'],G2['Cd_15'],label='$G2$',color='g',marker='^',markersize=8,lw=2)
ax.plot(G3['limiter'],G3['Cd_15'],label='$G3$',color='c',marker='v',markersize=8,lw=2)
ax.plot(G4['limiter'],G4['Cd_15'],label='$G4$',color='m',marker='d',markersize=8,lw=2)
ax.plot(limiter,Cd_exp,label='exp',color='k',linestyle='-.')
#lgd = ax.legend(loc='upper center',fancybox=True, bbox_to_anchor=(0.5,-0.12),ncol=5)
lgd = ax.legend(loc='best',fancybox=True)
ax.set_xticks(limiter)
ax.set_xticklabels(limiter_labels,size=16)
#ax.set_yticks([0.02,0.05])
#ax.set_ylim(0.019,0.051)
ax.set_yticks([0.015,0.05])
ax.set_ylim(0.014,0.051)


# Put G0 on its own axis.
ax2 = ax.twinx()
ax2.plot(G0['limiter'],G0['Cd_15'],label='$G0$',color='r',linestyle='--',marker='o',markersize=8,lw=2)
for label in ax2.get_yticklabels():
    label.set_color('red')
#ax2.set_yticks([0.14,0.185])
#ax2.set_ylim([0.1385,0.1865])
ax2.set_yticks([0.02,0.14,0.185])
ax2.set_ylim([0.0145,0.1905])
ax2.set_xlim(0.9,3.1) # Make x-axis nicer looking.
ax2.tick_params(axis='y',labelsize=16)

# Clean up the graph remove the top part of the box.
ax.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
# Remove the left over ticks at the top.
#ax.tick_params(top='off')
ax.xaxis.tick_bottom()
# Change color of right axis
ax2.spines['right'].set_color('r')
major_formatter = mpl.ticker.FormatStrFormatter('%g')
#ax.xaxis.set_major_formatter(major_formatter) # This will write over the custom labels.
ax.yaxis.set_major_formatter(major_formatter)
ax2.yaxis.set_major_formatter(major_formatter)


fig.savefig('limiter_vs_drag_15deg.pdf',bbox_extra_artists=(lgd,), bbox_inches='tight')# allows the legend to be outside the box when saving the figure.



plt.show()



