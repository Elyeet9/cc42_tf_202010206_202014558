from matplotlib import pyplot as plt    
from matplotlib import style    
style.use('ggplot')    

b = []
b1 = []
n_a = npr.randint(50,100)
for i in range(n_a):
  x = npr.randint(1000000)
  y = npr.randint(1000000)
  b.append(x)
  b1.append(y)
c = []
c1 = []
n_e = npr.randint(2500,5000)
for i in range(n_e):
  x = npr.randint(1000000)
  y = npr.randint(1000000)
  c.append(x)
  c1.append(y)

for k in range(1000):
  for j in range(1000):
    if j in b1 and k in b:
      x = [k]
      y = [j]
      plt.scatter(x, y, color='r')
    if j in c1 and k in c:
      x = [k]
      y = [j]
      plt.scatter(x, y, color='b')
    else:
      x = [k]
      y = [j]
      plt.scatter(x, y, color='g')    
    
plt.show()    
