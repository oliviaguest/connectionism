from math import *
import random 
import time
import numpy
import matplotlib.pyplot as plt

numpy.set_printoptions(formatter={'float': '{: 0.1f}'.format})


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
    self.layers = 2
    
    #If set to True graphs representing the classification permformed by the network will be drawn
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


      plt.draw()
	


      
  def Train_(self, iterations = 10):
       
        x = self.input_units 
        y = self.output_units
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
                        
                    #for i in range(N):    
                      #x[i] = self.patterns[p][i]
                      
                    x[0:N] = self.patterns[p][:]  
                    
                    #y[0] = 0
                    #for i in range(N+1): 
                      #y[0] += x[i] * w[i]
                      
                    y = numpy.dot(x, w)

                    #y[0] = f(y[0])
                    
                    y = vf(y)
                    
                    #error = d[p][0] - y[0]
                    error = d[p] - y

                    #for i in range(N+1): 
                      #w[i] += h * error * x[i]
                      
                    w += h * error * x
                    #print w
                    #print self.weights
                    print  x, '->',  y, ', 'error
        self.Show_Graphs()


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
              print  'input -> output, error'
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
                      
                    print  x, '->',  y, ', 'error
        self.Show_Graphs()
             
  def Run(self):
    x = self.input_units 
    y = self.output_units
    w = self.weights
    h = self.learning_rate
    d = self.targets
    N = len(self.patterns[0])
    P = len(self.patterns)

    while True:
          for p in range(P):
                  for i in range(N):
                    x[i] = self.patterns[p][i]
                  y[0] = 0
                  for i in range(N+1):
                    y[0] += x[i] * w[i]
                  y[0] = f(y[0])

                  error = self.targets[p][0] - f(y[0])

                  #self.Draw()

                  time.sleep(0.5)


Patterns = [
         ##colour, shape, taste
         ##red-yellow, sweet-sour
         [0.1, 0.5], #loquat 
         [0.0, 0.0], #lemon 
         [1.0, 0.8], #red apple 
         [1.0, 0.9], #strawberry 
         #[0.1, 0.0], #loquat 
         #[0.0, 0.2], #lemon 
         #[1.0, 0.5], #red apple 
         #[1.0, 0.0], #strawberry 
        ]

Targets = [
           [1.0], #first target
           [0.0], #targets indicate 
           [0.0], #which class
           [1.0], #a pattern         
          ] #belongs to           
                   

def Main():
  #below this line are things that will be run - above it are just declarations and definitions of classes, etc.
  N = Network(Patterns, Targets, learning_rate = 0.001)

  #N.Graph()

  #N.Train()
  #N.Graph()
  
  N.Train(10)

  
  #N.Run()

  #refresh the screen
  #pygame.display.update()

  #loop to fall into once the main stuff has been done
  #while True:
    #for event in pygame.event.get():
      #if event.type == QUIT:
         #quit()

if __name__ == "__main__":
  Main()