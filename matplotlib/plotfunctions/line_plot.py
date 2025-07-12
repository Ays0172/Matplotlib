import matplotlib.pyplot as plt

month = [1,2,3,4,5,]
sales = [1500, 3000, 2300, 5000, 4400]

plt.plot(month, sales, color = "green", linestyle = "--", linewidth = 2, marker = 'o', label = '2025 Sales data')

plt.xlabel('Months')
plt.ylabel('Sales per month')
plt.title('Monthly Sales Data Report')
plt.legend(loc ='upper left', fontsize = 10)                # plt.legend(loc ='upper left' / 'lower right', fontsize = 12)
plt.grid(color = 'blue', linestyle = ':', linewidth =1)    # plt.grid(color = 'blue', linestyle = ':', linwewidth =1)
plt.xlim(1,4)                                               # Limit x-axis variable
plt.ylim(0,5500)                                            # Limit y-axis variable
plt.xticks([1,2,3,4,5], ['M1', 'M2', 'M3', 'M4', 'M5'])

plt.show()

