# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:48:46 2020

@author: AbbieEnders
"""

c = 'present'
b = 'not present'
# do you want the user to state a title for the graph? If not remove line 11
# title = 'Confusion Matrix for Carboxylica Identification'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

conf_arr = [[5,0], 
            [0,5]]

norm_conf = []
for i in conf_arr:
    a = 0
    tmp_arr = []
    a = sum(i, 0)
    for j in i:
        tmp_arr.append(float(j)/float(a))
    norm_conf.append(tmp_arr)

fig = plt.figure()
plt.clf()
ax = fig.add_subplot(111)
ax.set_aspect(1)
res = ax.imshow(np.array(conf_arr), cmap=cm.summer, 
                interpolation='nearest', vmin=0, vmax=5)



for x in range(2):
    for y in range(2):
        ax.annotate("{:.0f}".format(conf_arr[x][y]), xy=(y, x), 
                    horizontalalignment='center',
                    verticalalignment='center',
                    color ='black',
                    size = '12')

cb = fig.colorbar(res)
#plt.title(title)
plt.xlabel('Predicted Group')
plt.ylabel('Actual Group')
plt.xticks(range(2), [c,b])
plt.yticks(range(2), [c,b])
plt.savefig('perfect_10000_0_01.svg', format='svg')
plt.show()