# This file generates the limiter vs. force coefficients plots for G0
# The data was copied from the google doc.

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Data From Google Sheet
# Coarsest Grid G0
# Cl and Cd for alpha = 15degrees
# For limiter value of 10 this diverges.
G0 = {}
G0['limiter'] = np.array([0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.5,2.8,3])
G0['Cl_15'] = np.array([1.132402092,1.058882632,0.955665529,0.858017631,0.7731440578,0.7058578435,0.654236601,0.6118423402,0.6060703159,0.5613000825,0.549381038,0.5402739752,0.5368964237,0.5335710082,0.5257995459,0.5012420718,0.4572776521])
G0['Cd_15'] = np.array([0.1845497871,0.1827848017,0.1741650459,0.1669107215,0.160298775,0.1534846663,0.1492036143,0.1465929162,0.1401358611,0.1443830659,0.1426560954,0.1413189728,0.1393179875,0.1379002617,0.1363347796,0.1319724923,0.1456738211])

### Lift of 15 degrees. ###
fig, ax = plt.subplots()
ax.tick_params(axis='y',labelsize=16)
ax.tick_params(axis='x',labelsize=16)
ax.set_xlabel('$Limiter\,Coefficient$',size=18)
ax.set_ylabel('$C_l$',rotation=0,size=18)
ax.plot(G0['limiter'],G0['Cl_15'],label='$G0$',color='r',linestyle='--',marker='o',markersize=8,lw=2)
ax.set_xticks([0,1,2,3])
#ax.set_xticklabels(limiter_labels,size=16)
#ax.set_yticks([1.46,1.57])
#ax.set_ylim(1.455,1.575)
ax.set_xlim(-0.15,3.15)


# Clean up the graph remove the top part of the box.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Remove the left over ticks at the top.
#ax.tick_params(top='off')
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
major_formatter = mpl.ticker.FormatStrFormatter('%g')
ax.xaxis.set_major_formatter(major_formatter) # This will write over the custom labels.
ax.yaxis.set_major_formatter(major_formatter)

fig.savefig('G0_limiter_effect_lift15deg.pdf')

### Drag of 15 degrees. ###
fig, ax = plt.subplots()
ax.tick_params(axis='y',labelsize=16)
ax.tick_params(axis='x',labelsize=16)
ax.set_xlabel('$Limiter\,Coefficient$',size=18)
ax.set_ylabel('$C_d$',rotation=0,size=18)
ax.plot(G0['limiter'],G0['Cd_15'],label='$G0$',color='r',linestyle='--',marker='o',markersize=8,lw=2)
ax.set_xticks([0,1,2,3])
#ax.set_xticklabels(limiter_labels,size=16)
#ax.set_yticks([1.46,1.57])
#ax.set_ylim(1.455,1.575)
ax.set_xlim(-0.15,3.15)


# Clean up the graph remove the top part of the box.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Remove the left over ticks at the top.
#ax.tick_params(top='off')
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
major_formatter = mpl.ticker.FormatStrFormatter('%g')
ax.xaxis.set_major_formatter(major_formatter) # This will write over the custom labels.
ax.yaxis.set_major_formatter(major_formatter)
fig.savefig('G0_limiter_effect_drag15deg.pdf')


plt.show()



