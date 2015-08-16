from pyceptron import *

''' This file contains the patterns used in the excersises for teaching the network logic '''

#Patterns = [ ## NOT ##
            #[0.0],
            #[1.0],
           #]

#Targets = [
           #[1.0], #first target, corresponds to first pattern
           #[0.0],
         
          #]
          
          
Patterns = [ ## OR ##
            [0.0, 0.0],
            [0.0, 1.0],
            [1.0, 0.0],
            [1.0, 1.0]
           ]

Targets = [
           [0.0], #first target, corresponds to first pattern
           [1.0],
           [1.0],
           [1.0],
         
          ]
          
         
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

N = Network(Patterns, Targets)
N.Graph()

for i in range(5):
	print 'Training cycle:', i
	N.Train(1)
	N.Graph()

N.Show_Graphs()
  

#loop to fall into once the main stuff has been done
#while (1):
  #for event in pygame.event.get():
    #if event.type == QUIT:
      #quit()