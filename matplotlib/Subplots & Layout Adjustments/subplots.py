# plt.subplot(nrows, ncols, index)

#1
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10, 20, 15, 25]

plt.subplot(1,2,1)      # 1 row, 2 column, 1st position(index)
plt.plot(x,y)
plt.title('Line Chart')

plt.subplot (1,2,2)     # 1 row, 2 column, 2nd position(index)
plt.bar(x,y)
plt.title('Bar Chart')

#2
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10, 20, 15, 25]

plt.subplot(1,2,1)      # 1 row, 2 column, 1st position(index)
plt.plot(x,y)
plt.title('Line Chart')

plt.subplot (1,2,2)     # 1 row, 2 column, 2nd position(index)
plt.bar(x,y)
plt.title('Bar Chart')

# To fit perfectly onto the Canva

plt.tight_layout()
plt.show()


#3
import matplotlib.pyplot as plt

# fig, ax = plt.subplots(nrows, ncols, figsize= (width, height))
fig, ax = plt.subplots(1,2, figsize = (10, 5)) 

x = [1,2,3,4]
y = [10, 20, 15, 25]

ax[0].plot(x,y)
ax[0].set_title('Line Plot')

ax[1].bar(x,y)
ax[1].set_title('Bar Chart')

plt.show()

#4
# Using tight command

import matplotlib.pyplot as plt

# fig, ax = plt.subplots(nrows, ncols, figsize= (width, height))
fig, ax = plt.subplots(1,2, figsize = (10, 5)) 

x = [1,2,3,4]
y = [10, 20, 15, 25]

ax[0].plot(x,y, color = 'blue')
ax[0].set_title('Line Plot')

ax[1].bar(x,y, color = 'green')
ax[1].set_title('Bar Chart')

# To give title to both the charts 
'''  suptitle()  # please note its SUP  '''
fig.suptitle('Compariosn of Bar and Line Graphs')

plt.tight_layout()
plt.show()