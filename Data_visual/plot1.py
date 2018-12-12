import matplotlib.pyplot as plt

squares=[1,4,9,16,25]
input_values=[1,2,3,4,5]
plt.plot(input_values,squares,linewidth=5)
plt.title('square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('square of value',fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.savefig('square_plot1.png',bbox_inches='tight')
plt.figure(2)
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,s=1,edgecolors='None',c=y_values,cmap=plt.cm.Greens)#c='yellow|rgb';映射
plt.axis([0,1100, 0,1100000])
plt.savefig('square_plot.png',bbox_inches='tight')
plt.show()
