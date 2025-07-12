# Dont use for over cluttered data!

import matplotlib.pyplot as plt

#plt.pie(values, labels=label_list, colors='color_list, autopct ='%1.f%%)

regions = ['North', 'South', 'East' , 'West']
revenue = [3000, 2000, 1700, 2300]

plt.pie(revenue, labels = regions, autopct = '%1.1f%%', colors = ['gold' , 'skyblue', 'lightgreen', 'coral'])
plt.title('Revenue Contribution by Region')

plt.show()