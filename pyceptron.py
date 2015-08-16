from math import *
import random 
#import copy as cop
import time
import numpy
#import pygame
#from pygame.locals import *
import matplotlib.pyplot as plt

numpy.set_printoptions(formatter={'float': '{: 0.1f}'.format})


def get_angle(x1, y1, x2, y2):
  dx = x2 - x1
  dy= y2 - y1  
  return atan2(dy,dx)

#preset colours
#magenta = [255, 0, 255]
black = [0, 0 , 0]
white = [255, 255 , 255]
#f = lambda x: 0.0 if x < 0.0 else 1.0
def f(x):
  if x < 0.0:
    return 0.0
  else:
    return 1.0
  
vf = numpy.vectorize(f)  

class Network(object):
  "The network itself!"
  def __init__(self, patterns, targets,  learning_rate = 0.001, height = 600, width = 600): 

    #Initialise pygame
    #pygame.init()
    #self.screen = pygame.display.set_mode((width, height))
    #pygame.display.set_caption("Pyceptron")
    #self.background = pygame.Surface(self.screen.get_size())
    #self.background = self.background.convert()
    #self.background.fill([200, 200, 200])
    #self.screen.blit(self.background, (0, 0))

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
  
    # GUI stuff
    #self.radius = int( height/ (3* max(len(self.input_units), len(self.output_units)) ))
    #self.x_spacing = int(self.radius*1.5)
    #self.y_spacing = int(self.radius*1.5)
    #self.x_offset = int((width - (self.layers - 1) * (self.x_spacing + self.radius)) / 2.0)
    #self.input_units_x =  numpy.ones(len(self.patterns[0]))
    #self.input_units_y =  numpy.ones(len(self.patterns[0]))
    #self.output_units_x =  numpy.ones(len(self.output_units))
    #self.output_units_y =  numpy.ones(len(self.output_units))
    
    #for i in range(len(self.patterns[0])):
      #y_offset = int((height - ((len(self.patterns[0])-1) * (self.y_spacing + self.radius))) / 2.0)
      #self.input_units_x[i] = 0 * (self.x_spacing+self.radius) + self.x_offset     # constant represents what layer they are on
      #self.input_units_y[i] = i * (self.y_spacing+self.radius)  + y_offset

    #for i in range(len(self.output_units)):
      #y_offset = int((height - ((len(self.output_units)-1) * (self.y_spacing + self.radius))) / 2.0)
      #self.output_units_x[i] = 1 * (self.x_spacing+self.radius) + self.x_offset    # constant represents what layer they are on
      #self.output_units_y[i] = i * (self.y_spacing+self.radius)  + y_offset

    # More GUI stuff
    #self.screen.blit(self.background, (0, 0))
    #for i in range(len(self.patterns[0])):

      #x1 = self.input_units_x[i]
      #y1 = self.input_units_y[i]
      #x2 = self.output_units_x[0]
      #y2 = self.output_units_y[0]
      #r1 = self.radius
      #r2 = self.radius
      #a = get_angle(x1, y1, x2, y2)
      #pygame.draw.line(self.screen, black, (x1 + r1 * cos(a),  y1 + r1 * sin(a)), (x2 - r2 * cos(a), y2 - r2 * sin(a)), 1)
      #pygame.draw.circle(self.screen, black, (int(x1), int(y1)), self.radius, 2)

    #for i in range(len(self.output_units)):
      #x2 = self.output_units_x[i]
      #y2 = self.output_units_y[i]
      #pygame.draw.circle(self.screen, black, (int(x2), int(y2)), self.radius, 2)
      
    #pygame.display.update()
    
    # Graphing stuff
    #self.graph_x = []
    #self.graph_y = []
    #if (len(self.patterns[0])) < 3:
      #for i, sub_x in enumerate(self.patterns):
        #self.graph_x.append(sub_x[0])
        #if len(sub_x) == 2:
          #self.graph_y.append(sub_x[1])
    #self.line = plt.plot(1, 1, 'k-')
    #plt.ion() 
  def Show_Graphs(self):
          plt.show()

 
  def Graph(self):
      #self.line.pop(0).remove()
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
      
      #time.sleep(0.1)
      #plt.pause(0.0001)  
      plt.draw()
	
  #def Draw(self):
    ## GUI stuff
    
    #for event in pygame.event.get():
      #if event.type == QUIT:
        #quit()
        #pygame.display.update()
        
    #for i in range(len(self.input_units)-1):

      #x1 = self.input_units_x[i]
      #y1 = self.input_units_y[i]
      #x2 = self.output_units_x[0]
      #y2 = self.output_units_y[0]
      #r1 = self.radius
      #r2 = self.radius

      #rect = pygame.Rect(int(x1)-25, int(y1)-20, 50, 40)
      #pygame.draw.rect(self.screen, [200, 200, 200], rect, 0)
      #font=pygame.font.Font(None,50)
      #text=font.render(str(self.input_units[i]), 1,black)
      #self.screen.blit(text, (int(x1)-25, int(y1)-20))
      #pygame.display.update(rect)
          
          
    #for i in range(len(self.output_units)):
      #x2 = self.output_units_x[i]
      #y2 = self.output_units_y[i]
      #rect = pygame.Rect(int(x2)-25, int(y2)-20, 60, 40)
      #pygame.draw.rect(self.screen, [200, 200, 200], rect, 0)
      #font=pygame.font.Font(None,50)
      #text=font.render(str(self.output_units[i]), 1,black)
      #self.screen.blit(text, (int(x2)-25, int(y2)-20))
      #pygame.display.update(rect)


      
  def Train(self, iterations = 10):
       
        x = self.input_units 
        y = self.output_units
        w = self.weights
        h = self.learning_rate
        d = self.targets
        N = len(self.patterns[0])
        P = len(self.patterns)

        for t in range(iterations):
              for p in range(P):
                        
                    #for i in range(N):    
                      #x[i] = self.patterns[p][i]
                      
                    x[0:2] = self.patterns[p][:]  
                    
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
                    print  x, '->',  y, error



             
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
         #colour, shape, taste
         #red-yellow, big-small, sweet-sour
         #[0.1, 0.0, 0.2], #loquat 
         #[0.0, 0.2, 0.0], #lemon 
         #[1.0, 0.5, 0.8], #red apple 
         #[1.0, 0.0, 0.9], #strawberry 
         [0.1, 0.0], #loquat 
         [0.0, 0.2], #lemon 
         [1.0, 0.5], #red apple 
         [1.0, 0.0], #strawberry 
        ]

Targets = [
           [1.0], #first target
           [1.0], #targets indicate 
           [0.0], #which class
           [0.0], #a pattern         
          ] #belongs to           
                   

def Main():
  #below this line are things that will be run - above it are just declarations and definitions of classes, etc.
  N = Network(Patterns, Targets)

  #N.Graph()

  #N.Train()
  #N.Graph()
  
  for i in range(5):
    print 'Training cycle:', i
    N.Train(1)
    N.Graph()
  N.Show_Graphs()
  
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