import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('pmf.csv')
x=data['RC']
y=data['average']
y_std=data['std']

plt.errorbar(x, y, yerr=y_std, color='black', linewidth=1, marker='^')

plt.xlim(0,30)
plt.ylim(0,8)
plt.xlabel('Host-Guest Distance (Å)', fontsize='14')
plt.ylabel('PMF (kcal/mol)', fontsize='14')

plt.savefig('pmf.png')

