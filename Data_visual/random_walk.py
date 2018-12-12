from random import choice
import matplotlib.pyplot as plt

class person():
    def __init__(self,walk_steps,step_distance):
        self.walk_steps=walk_steps
        self.step_distance=step_distance
        self.x=[0]
        self.y=[0]
        self.distances=[]

    def random_walk(self):
          for i in range(1,self.walk_steps):
              x_direction=choice([1,-1])
              y_direction=choice([1,-1])
              x_step_distance=choice(self.step_distance)
              y_step_distance=choice(self.step_distance)
              x=self.x[-1]+x_direction*x_step_distance #下一点的坐标值
              y=self.y[-1]+y_direction*y_step_distance
              self.x.append(x)
              self.y.append(y)

    def show_point(self):
           plt.figure('point')
           plt.title('Random_walk')
           plt.scatter(self.x,self.y,c=range(self.walk_steps),cmap='Reds',s=5,edgecolors='none')
           plt.scatter(self.x[0],self.y[0],s=100,c='yellow')
           plt.scatter(self.x[-1],self.y[-1],s=100,c='pink')
           plt.show()


    def show_distance(self):
         #plt.figure('distance')
         distance=[]
         for i in range(self.walk_steps):
             distance.append(pow(self.x[i]**2+self.y[i]**2,0.5))
         #plt.scatter(range(self.walk_steps),distance,s=5,c=range(self.walk_steps),cmap='Reds')
         #plt.scatter(distance.index(max(distance)),max(distance),s=50,c='red')
         self.distances.append(distance[-1])

walk_steps=5000
step_distance=[0.3,0.3,0.3,0.2,0.2,0.1]
David=person(walk_steps,step_distance)
for i in range(10000):
    David.x=[0]
    David.y=[0]
    David.random_walk()
    David.show_distance()

plt.figure(figsize=(61.8,38.2))
plt.scatter(range(10000),David.distances,s=5,c='red')
plt.savefig('random_walk_distanse.png',bbox_inches='tight')
plt.show()
