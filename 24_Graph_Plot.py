import matplotlib.pyplot as plt
print("Input X-Axis values:")
x=list(map(int,input().split(",")))
print("Input Y-Axis values:")
y=list(map(int,input().split(",")))
plt.plot(x,y,marker='o')
plt.show()