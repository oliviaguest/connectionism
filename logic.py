from pyceptron import *

''' This file contains the patterns used in the excersises for teaching the network logic '''

Patterns = [ ## NOT ##
            [0.0],
            [1.0],
           ]

Targets = [
           [1.0], #first target, corresponds to first pattern
           [0.0],
         
          ]
          
          
#Patterns = [ ## OR ##
            #[0.0, 0.0],
            #[0.0, 1.0],
            #[1.0, 0.0],
            #[1.0, 1.0]
           #]

#Targets = [
           #[0.0], #first target, corresponds to first pattern
           #[1.0],
           #[1.0],
           #[1.0],
         
          #]
          
         
#Patterns = [ ## AND ##
            #[0.0, 0.0],
            #[0.0, 1.0],
            #[1.0, 0.0],
            #[1.0, 1.0]
           #]

#Targets = [
           #[0.0], #first target, corresponds to first pattern
           #[0.0],
           #[0.0],
           #[1.0],
         
          #]  
          
#Patterns = [ ## XOR ##
          #[0.0, 0.0],
          #[0.0, 1.0],
          #[1.0, 0.0],
          #[1.0, 1.0]
          #]

#Targets = [
           #[0.0], #first target, corresponds to first pattern
           #[1.0],
           #[1.0],
           #[0.0],
         
          #] 
          
   
     
     
def Main():
  #below this line are things that will be run - above it are just declarations and definitions of classes, etc.
  N = Network(Patterns, Targets, learning_rate = 0.001)

  #N.Graph()

  #N.Train()
  #N.Graph()
  
  N.Train(10)
  

if __name__ == "__main__":
  Main()
#loop to fall into once the main stuff has been done
#while (1):
  #for event in pygame.event.get():
    #if event.type == QUIT:
      #quit()