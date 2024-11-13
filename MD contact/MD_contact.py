import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('MD_cnt_total.csv')
x=data['Residue']
y=data['MD_contact_probability']

plt.plot(x,y, color='black', linewidth=1)

plt.title('801 LiGaMD Contact Probability',fontsize='14')
plt.xlabel('Residue', fontsize='14')
plt.ylabel('MD Contact Probability', fontsize='14')

plt.savefig('801_ligamd_MD_contact.png')
plt.show()
