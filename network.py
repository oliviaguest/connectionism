#! /usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk, gobject, cairo, glib
from gtk import gdk
import gobject
import random as r
import copy as cop
import os
import numpy as np

def Random(max_value, min_value = 0):
  "Random integer from min_value to max_value"
  return int(r.randint(min_value, max_value))
  #return int(round(r.random()*(max_value-min_value) + min_value))
  

  
def div(l, d):
  return [x/d for x in l]

#red = [255, 20, 0]
#red = div(red, 255.0)
red = [1.0, 0.1, 0.2]
blue = [0.0, 0.1, 1.0]
#blue = div(blue,255.0)
#green = [50, 180, 30]
#green = div(green,255.0)
grey = [0.9, 0.9, 0.9]
#purple = [255, 20, 255]
#purple = div(purple,255.0)
#yellow = [255, 200, 10]
#yellow = div(yellow, 255.0)
#cyan = [0, 255, 255]
#cyan = div(cyan, 255.0)
white = [1, 1, 1]
black = [0, 0, 0]

def random_colour():
   colours = [red, blue]
   return colours[Random(len(colours)-1)]
   
def get_resource_path(rel_path):
  dir_of_py_file = os.path.dirname(__file__)
  rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
  abs_path_to_resource = os.path.abspath(rel_path_to_resource)
  return abs_path_to_resource
#Network Globals

padding = 10
    
#height = 60
#width = 60

#ticks = 1

#Layer Globals
living_cost = 0.3
reproduction_energy = 10 #minmum energy value for reproducing
mutation_probability = 5 #per cent
mouth_size = 3 #amount of food that can be eaten in one go
s = 1
d = 0
max_age = 500
death_percent = 0#20
PERCEPTION = 2




#import pygame
#from pygame.locals import *

#pygame.init()
#screen = pygame.display.set_mode((569, 569))
#pygame.display.set_caption("Map")

#background = pygame.Surface(screen.get_size())
#background = background.convert()
#background.fill((255, 255, 255))
#screen.blit(background, (0, 0))


class Unit(object):
  "A unit on the Map"
  global grey
  def __init__(self, x, y, network, width = 10):
    self.x = x
    self.y = y
    #self.unit = pygame.Rect((self.x * 11 + 10, self.y * 11 + 10), (10, 10))
    self.colour = grey
    #self.layer_id = None
    self.width = width
    self.network = network
    self.layer = None


  def Draw(self, cr, width, height): 
    cr.set_source_rgb(self.colour[0], self.colour[1], self.colour[2])
    #cr.rectangle(self.x * 11 + 10, self.y * 11 + 10, 10, 10)
    #cr.rectangle(self.x * (self.width+1) + 10, self.y * (self.width+1)+ 10, self.width, self.width)
    cr.rectangle((width - self.network.width * (self.width+1) - 20) / 2.0 + 10 + (self.x * (self.width+1) ), self.y * (self.width+1)+ 10, self.width, self.width)
    cr.fill()

    
class Layer(object):
  "An organism inhabiting a Unit"
  def __init__(self, id_number, number_of_units, network, unit_width = 10, targets = None, learning_rate = 0.001):
    self.colour = [0.2, 0.1, 0.1]
    self.id_number = id_number
    self.units = []
    self.network = network
    self.unit_width = unit_width
		
    self.targets = np.asarray(targets)
    self.learning_rate = learning_rate
    self.weights = np.random.normal(0.0, 0.001, len(self.self.network.layer[self.id_number-1]))
    self.errors = np.zeros(len(targets[0]))
    for x in xrange(number_of_units):
		unit = Unit(x, self.id_number, self.network, self.unit_width)
		self.units.append(unit)

  def Draw(self, cr, width, height):
    for unit in self.units:
      unit.Draw(cr, width, height)
      
      
  def set_colour(self, colour):
    for unit in self.units:
      unit.colour = colour

# Create a GTK+ widget on which we will draw using Cairo
class Network(gtk.DrawingArea):
    # Draw in response to an expose-event
    __gsignals__ = { "expose-event": "override" }
    # Create the cairo context

      

    
    def __init__(self, width, height, unit_width = 10):

	super(Network,self).__init__()
	#global width
	#global height
	self.width = width#*11 + 20 # we want padding on both sides
	self.height = height#*11 +10  #we do not want padding on the bottom due to the way packing is done
	self.set_size_request(self.width*(unit_width+1) + 20 , self.height*(unit_width+1) + 20)
	self.tick = 0
	self.ticks = 0
	#self.coord.append(0)
	#self.connect("expose-event", self.do_expose_event)
	#self.name = name                        
	#gobject.timeout_add(1000,self.draw_loop)
        self.paused = False
        self.running = False
	self.unit_width = unit_width
        self.max_population = self.height * self.width
	self.initial_population = int(self.max_population/2.0)
	##print self.window
	##self.cr = self.window.cairo_create()


	
	self.layers = []
	units = [2, 1, 2, 3, 4, 6]
	for y in xrange(self.height):
	    layer = Layer(y, units[y], self, unit_width = self.unit_width)
	    self.layers.append(layer)

	##Debugging Globals
	#global deaths
        #global offspring_created
	#offspring_created = 0

	  
    def Pause(self):
      self.paused =  not self.paused
      
    def redraw_canvas(self):
      if self.window:
	  alloc = self.get_allocation()
	  rect = gdk.Rectangle(0, 0, alloc.width, alloc.height)
	  self.window.invalidate_rect(rect, True)
	  self.window.process_updates(True)
	  
    def Run(self):
      #print 'tick: %s /' % str(self.tick).zfill(len(str(self.ticks))),
      #print '%s' % str(self.ticks).zfill(len(str(self.ticks)))

      if self.tick >= self.ticks:
	self.running = False
	return False
      else:
	self.running = True

      #if self.ticks:
	#self.ticks = ticks

      self.tick += 1
      for layer in self.layers:
	layer.set_colour(np.random.uniform(low=0.0, high=1.0, size=3))
	cr = self.window.cairo_create()
	cr.set_antialias(cairo.ANTIALIAS_NONE)
	layer.Draw(cr, *self.window.get_size())

      #for i in range(self.max_population):
	#if self.Layers[i] != None:
	  #if self.Layers[i].alive:
	    #cr = self.window.cairo_create()
	    #cr.set_antialias(cairo.ANTIALIAS_NONE)

	    #self.Layers[i].Live(cr)
	    

      if self.running and not self.paused:
	return True
      else:
	return False
    # Handle the expose-event by drawing
    def do_expose_event(self, event):
	cr = self.window.cairo_create()
	cr.set_antialias(cairo.ANTIALIAS_NONE)
	#print "beep"
	

        # Restrict Cairo to the exposed area; avoid extra work
        cr.rectangle(event.area.x, event.area.y, event.area.width, event.area.height)
        #print event.area.x
        #print event.area.y
        #print event.area.width
        #print event.area.height
        cr.clip()
        self.Draw(cr, *self.window.get_size())
        #self.Run(cr)
        #self.Layer_draw(cr)

    def Draw(self, cr, width, height):
	print width,
	print height
      	for layer in self.layers:
		layer.Draw(cr, width, height)
		

	    
    def Reset(self, width, height, unit_width):
      print self.width, self.height
      self.__init__(width, height, unit_width = unit_width)
      print self.width, self.height

      self.redraw_canvas()
      

      
##----------------------------------------------------------------------------------------------------##
      
class Model:

    def If_running(self):
      #print env.running
      self.play.set_sensitive(not self.env.running)   
      return self.env.running
      
    def If_paused(self):
      #print env.running
      self.pause.set_sensitive(self.env.running)
      return False

    def Status_update(self):
      if self.env.running:
	context_id = self.status_bar.get_context_id("Running")
	#print context_id
	text = "Iteration: " +  str(self.env.tick).zfill(len(str(self.env.ticks))) + "/" + str(self.env.ticks).zfill(len(str(self.env.ticks)))
	if self.env.paused:
	  text += ", Paused"
	self.status_bar.push(context_id, text)
	return True # we need it to keep updating if the model is running   
      elif not self.env.running:
	if not self.env.paused:
	  self.status_bar.remove_all(self.status_bar.get_context_id("Running"))
	  self.status_bar.remove_all(self.status_bar.get_context_id("Ready"))
	  context_id = self.status_bar.get_context_id("Ready")
	  #print context_id
	  text = "Ready"
	  self.status_bar.push(context_id, text)
	return False 
	
    #def Quit(self, widget, data=None):
      ##print 'Byez!'
      #gtk.main_quit()
      
    def Pause(self, widget=None, data=None):
	self.env.Pause()
	if self.env.paused:
	  self.pause.set_label("Unpause")
	else:
	  self.pause.set_label("Pause")
	  glib.idle_add(self.env.Run)
	  glib.idle_add(self.If_running)
	glib.idle_add(self.Status_update)
	  
	  
      
      
    def Run(self, widget=None, data=None):
      self.env.ticks += self.iterations_spin_button.get_value_as_int()
      if not self.env.running:
	glib.idle_add(self.env.Run)
      glib.idle_add(self.Status_update)
      glib.idle_add(self.If_running)
      glib.idle_add(self.If_paused)

    def Reset(self, widget=None, data=None):
      #[env, play, pause]
      print 'combobox', self.layer_combobox.get_active_text()
      self.env.Reset(self.width_spin_button.get_value_as_int(), int(self.layer_combobox.get_active_text()), self.unit_width_spin_button.get_value_as_int())
      self.pause.set_label('Pause')
      self.pause.set_sensitive(self.env.paused)
      glib.idle_add(self.If_running)
      glib.idle_add(self.Status_update)


    def delete_event(self, widget=None, event=None, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.
        #print "delete event occurred"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    def destroy(self, widget=None, data=None):
        #print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
      # create a new window
      self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
      # When the window is given the "delete_event" signal (this is given
      # by the window manager, usually by the "close" option, or on the
      # titlebar), we ask it to call the delete_event () function
      # as defined above. The data passed to the callback
      # function is NULL and is ignored in the callback function.
      self.window.connect("delete_event", self.delete_event)
      # Here we connect the "destroy" event to a signal handler.  
      # This event occurs when we call gtk_widget_destroy() on the window,
      # or if we return FALSE in the "delete_event" callback.
      self.window.connect("destroy", self.destroy)

      #window.set_icon_from_file(get_resource_path("icon.png"))
      #window.connect("delete-event", Quit)
      #window.connect("destroy", Quit)
      self.window.set_title("Network")
      self.window.set_default_size(0, 0) #this si to ensure the window is always the smallest it can be
      self.window.set_resizable(False)
      #window.set_border_width(10)

      # Args are: homogeneous, spacing, expand, fill, padding
      homogeneous = False
      spacing = 0
      expand = False
      fill = False
      padding = 10

      self.hbox = gtk.HBox(homogeneous, spacing)
      self.vbox = gtk.VBox(homogeneous, spacing)
      self.window.add(self.vbox)

      
      self.adjustment = gtk.Adjustment(value=10000, lower=1, upper=100000000, step_incr=1000, page_incr=10000)
      self.iterations_spin_button = gtk.SpinButton(self.adjustment, climb_rate=0, digits=0)
      self.adjustment = gtk.Adjustment(value=2, lower=1, upper=100, step_incr=5, page_incr=5)
      self.width_spin_button = gtk.SpinButton(self.adjustment, climb_rate=0, digits=0)
      
      self.layer_combobox = gtk.combo_box_new_text()
      for i in range(1, 3):
		self.layer_combobox.append_text(str(i))	
      self.layer_combobox.set_active(1)
      
      self.adjustment = gtk.Adjustment(value=2, lower=1, upper=100, step_incr=5, page_incr=5)
      self.height_spin_button = gtk.SpinButton(self.adjustment, climb_rate=0, digits=0)
      self.adjustment = gtk.Adjustment(value=100, lower=1, upper=100, step_incr=5, page_incr=5)
      self.unit_width_spin_button = gtk.SpinButton(self.adjustment, climb_rate=0, digits=0)
    
      # Create a series of buttons with the appropriate settings
      self.play = gtk.Button(label = "Run", stock = gtk.STOCK_EXECUTE)
      self.pause = gtk.Button("Pause")
      self.reset = gtk.Button("Reset")
      
      self.play.connect("clicked", self.Run, None)
      self.pause.connect("clicked", self.Pause, None)
      self.reset.connect("clicked", self.Reset, None)
      self.width_spin_button.connect("value_changed", self.Reset)
      self.height_spin_button.connect("value_changed", self.Reset)
      self.unit_width_spin_button.connect("value_changed", self.Reset)
      self.layer_combobox.connect('changed', self.Reset)

      self.env = Network(width = self.width_spin_button.get_value_as_int(), height = self.height_spin_button.get_value_as_int(), unit_width = self.unit_width_spin_button.get_value_as_int())
      self.env.show()
      self.pause.set_sensitive(self.env.paused)


      self.vbox.pack_start(self.env, True, True, 0)
      self.vbox.pack_start(self.hbox, expand, fill, 10)
      self.status_bar = gtk.Statusbar()
      self.vbox.pack_start(self.status_bar, expand, fill, 0)
      self.status_bar.show()
      glib.idle_add(self.Status_update)
      self.hbox.show()
      self.vbox.show()
      self.play.show()    
      self.pause.show()
      self.reset.show() 
      self.iterations_spin_button.show()  
      self.width_spin_button.show()
      self.height_spin_button.show()
      self.unit_width_spin_button.show()
      self.layer_combobox.show()
      
      self.hbox.pack_start(self.play, expand, fill, padding) 
      self.hbox.pack_start(self.pause, expand, fill, 0)      
      self.hbox.pack_start(self.reset, expand, fill, padding)
      self.hbox.pack_start(self.iterations_spin_button, expand, fill, 0)
      self.hbox.pack_start(self.width_spin_button, expand, fill, padding)
      self.hbox.pack_start(self.height_spin_button, expand, fill, 0)
      self.hbox.pack_start(self.unit_width_spin_button, expand, fill, padding)
      self.hbox.pack_start(self.layer_combobox, expand, fill, 0)
      
      self.quit = gtk.Button("Quit")
      self.quit.connect("clicked", self.destroy, None)
      self.hbox.pack_end(self.quit, expand, fill, padding)
      self.quit.show()
      #print window.get_size()
      self.window.show()
      
      self.window.present()
      #gtk.main()
      # And of course, our main loop.
      #gtk.main()
      # Control returns here when main_quit() is called
      return None
    
    def main(self):
    # All PyGTK applications must have a gtk.main(). Control ends here
    # and waits for an event to occur (like a key press or mouse event).
      gtk.main()
    
    
    
##----------------------------------------------------------------------------------------------------##
# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    model = Model()
    model.main()
    
