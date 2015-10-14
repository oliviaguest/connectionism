from math import *
import random 
import time
import numpy
import matplotlib.pyplot as plt

numpy.set_printoptions(formatter={'float': '{: 0.1f}'.format})

Patterns = [ ## Something meaningless ##
            [0.0, 0.0],
            [1.0, 0.4],
            [0.7, 0.0],
            [1.0, 0.8],
            [0.0, 0.1],
            [0.9, 0.0],
            [1.0, 1.0],
            [1.0, 0.5],
           ]

Targets = [
           [1.0],
           [0.0],
           [1.0], 
           [0.0],
           [1.0], 
           [0.0],
           [1.0], 
           [0.0],
         
          ]
def get_angle(x1, y1, x2, y2):
  dx = x2 - x1
  dy= y2 - y1  
  return atan2(dy,dx)

def f(x):
  if x < 0.0:
    return 0.0
  else:
    return 1.0
  
vf = numpy.vectorize(f)  
      

class Network(object):
  "The network itself!"
  def __init__(self, patterns, targets,  learning_rate = 0.001, height = 600, width = 600, graphs = False): 

    # Initialising network
    self.input_units =  numpy.ones(len(patterns[0])+1)
    self.output_units = numpy.zeros(len(targets[0]))
    self.patterns = patterns
    self.targets = numpy.asarray(targets)
    self.learning_rate = learning_rate
    self.weights = numpy.ones(len(self.input_units))
    self.weights = numpy.random.normal(0.0, 0.001, len(self.input_units))
    self.errors = numpy.zeros(len(targets[0]))
    self.learning_rate = learning_rate

    #If set to True graphs representing the classification performed by the network will be drawn
    self.graphs = graphs
  
  def Show_Graphs(self):
      if self.graphs:
          plt.show()

 
  def Graph(self):
      plt.figure()
      line_x = []
      line_y = [] 
      colour = {1: 'ro', 0: 'bs'}
      
      if len(self.patterns[0]) == 2:
        line_x = [2, -2]
        line_y = numpy.zeros(2)
        line_y[0] = (-self.weights[2] - self.weights[0] * line_x[0]) / self.weights[1]
        line_y[1] = (-self.weights[2] - self.weights[0] * line_x[1]) / self.weights[1]
        
        for i, sub_x in enumerate(self.patterns):
          plt.plot(sub_x[0], sub_x[1], colour[self.targets[i][0]])
          
          
      elif len(self.patterns[0]) == 1:
        line_x = numpy.zeros(2)
        line_y = [-2, 2]
        line_x[0] = -self.weights[1] / self.weights[0]
        line_x[1] = -self.weights[1] / self.weights[0]
        #line_x[1] = (- self.weights[0] * line_x[1]) / self.weights[1]
        
        for i, sub_x in enumerate(self.patterns):
          plt.plot(sub_x[0], 0, colour[self.targets[i][0]])
                   
      plt.axis([-1, 2, -1, 2])
      plt.plot(line_x, line_y, 'k-')
      plt.xlabel('First feature of x')
      plt.ylabel('Second feature of x')

      plt.draw()
      

  def Train(self, iterations = 10):
        x = self.input_units 
        y = self.output_units[0]
        w = self.weights
        h = self.learning_rate
        d = self.targets
        N = len(self.patterns[0])
        P = len(self.patterns)

        for t in range(iterations):
              print 'Training cycle:', t
              print  'input -> output error'
              self.Graph()
              for p in range(P):
                        
                    for i in range(N):    
                      x[i] = self.patterns[p][i]
                                        
                    y = 0
                    
                    for i in range(N+1): 
                      y += x[i] * w[i]
                      
                    y = f(y)
                                       
                    error = d[p][0] - y

                    for i in range(N+1): 
                      w[i] += h * error * x[i]
                      
                    print  x, '->',  y, ', ', error
        self.Show_Graphs()
             
             
  def Run(self):
    x = self.input_units 
    y = self.output_units[0]
    w = self.weights
    h = self.learning_rate
    d = self.targets
    N = len(self.patterns[0])
    P = len(self.patterns)

    while True:
          for p in range(P):
                  for i in range(N):
                    x[i] = self.patterns[p][i]
                  y = 0
                  for i in range(N+1):
                    y += x[i] * w[i]
                  y = f(y)

                  error = d[p][0] - y

                  print  'input -> output error'
                  print  x, '->',  y, ', ', error

                  time.sleep(0.5)

    


def Main():
  #below this line are things that will be run - above it are just declarations and definitions of classes, etc.
  N = Network(Patterns, Targets, learning_rate = 0.001, graphs=False)
  #create a Network called N
  
  N.Train(iterations = 10)
  #Ask N to Train itself using the Patterns and Targets given above
  
  #N.Run()
  #Run N to see what/if it has learned


if __name__ == "__main__":
  Main()
