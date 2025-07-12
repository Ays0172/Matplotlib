# plt.bar(x, height, color = 'color_name', width = value, label = 'label_name')

import matplotlib.pyplot as plt

product = ['A', 'B', 'C', 'D']
sales = [1000, 1500, 800, 1200]

plt.bar(product, sales, color = 'orange', label = 'Sales 2025') # use plt.barh (To show horizontal bar)
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title("Product Sales Comparison")
plt.legend()


plt.show()