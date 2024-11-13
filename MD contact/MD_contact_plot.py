import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import numpy as np

data = pd.read_csv('MD_cnt_305_final.csv')
x=data['Residue']
y=data['average']
y_std=data['std']

#plt.plot(x, y, color='black', linewidth=1)
plt.errorbar(x, y, yerr=y_std, color='black', linewidth=1, marker='^')

plt.title('305 LiGaMD Contact Probability',fontsize='14')
plt.xlabel('Residue', fontsize='14')
plt.ylabel('MD Contact Probability(%)', fontsize='14')
plt.xlim(0,140)
plt.ylim(0,2.0)
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
#y_ticks = [i*0.005 for i in range(5)]
#plt.yticks(y_ticks)

plt.savefig('305_ligamd_MD_contact.png')
plt.show()
