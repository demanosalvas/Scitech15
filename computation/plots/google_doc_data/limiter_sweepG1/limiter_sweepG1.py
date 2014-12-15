# This file generates the limiter vs. force coefficients plots for G1
# The data was copied from the google doc.

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Data From Google Sheet
# Grid G1
# Cl and Cd for alpha = 15degrees
G0 = {}
G0['limiter'] = np.array([0.1,1,5,10,15,18])
G0['Cl_15'] = np.array([1.467075,1.476419,1.4815620954,1.475586,1.475252,1.475214])
G0['Cd_15'] = np.array([0.047514,0.032396,0.0289800851,0.02884,0.029697,0.030044])

### Lift of 15 degrees. ###
fig, ax = plt.subplots()
ax.tick_params(axis='y',labelsize=16)
ax.tick_params(axis='x',labelsize=16)
ax.set_xlabel('$Limiter\,Coefficient$',size=18)
ax.set_ylabel('$C_l$',rotation=0,size=18)
ax.plot(G0['limiter'],G0['Cl_15'],label='$G0$',color='b',linestyle='--',marker='o',markersize=8,lw=2)
ax.set_xticks(G0['limiter'])
#ax.set_xticklabels(limiter_labels,size=16)
#ax.set_yticks([1.46,1.57])
#ax.set_ylim(1.455,1.575)
ax.set_xlim(-0.9,18.9)


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

fig.savefig('G1_limiter_effect_lift15deg.pdf')

### Drag of 15 degrees. ###
fig, ax = plt.subplots()
ax.tick_params(axis='y',labelsize=16)
ax.tick_params(axis='x',labelsize=16)
ax.set_xlabel('$Limiter\,Coefficient$',size=18)
ax.set_ylabel('$C_d$',rotation=0,size=18)
ax.plot(G0['limiter'],G0['Cd_15'],label='$G0$',color='b',linestyle='--',marker='o',markersize=8,lw=2)
ax.set_xticks(G0['limiter'])
#ax.set_xticklabels(limiter_labels,size=16)
#ax.set_yticks([1.46,1.57])
#ax.set_ylim(1.455,1.575)
ax.set_xlim(-0.9,18.9)


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
fig.savefig('G1_limiter_effect_drag15deg.pdf')


plt.show()



