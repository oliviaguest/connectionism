#! /usr/bin/network python
import pygtk
pygtk.require('2.0')
import gtk, gobject, cairo, glib
from gtk import gdk
import gobject
import random as r
import copy as cop
import os
import numpy as np
import time
import logic


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

# Create a GTK+ widget on which we will draw using Cairo
class Network(gtk.DrawingArea):
    # Draw in response to an expose-event
    __gsignals__ = { "expose-event": "override" }
    # Create the cairo context

      

    
    def __init__(self, width, height, patterns = None, targets = None, learning_rate = 0.005, unit_width = 10):

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
        #self.max_population = self.height * self.width
        #self.initial_population = int(self.max_population/2.0)
        ##print self.window
        ##self.cr = self.window.cairo_create()
        self.current_pattern = 0

        self.input_units =  np.zeros(len(patterns[0])+1)
        self.output_units = np.zeros(len(targets[0]))
        self.hidden_units = np.zeros(1 + 1)
        self.patterns = patterns
        self.targets = np.asarray(targets)
        self.learning_rate = learning_rate
        self.weights = np.random.normal(0.0, 0.001, len(self.input_units))
        self.errors = np.zeros(len(targets[0]))
        self.layers = 2
        
        def f(x):
          if x < 0.0:
            return 0.0
          else:
            return 1.0
          
        self.activation_function = np.vectorize(f) 
        
        self.input_width = len(self.input_units) - 1
        self.output_width = len(self.output_units)
        self.hidden_width = len(self.hidden_units) - 1

        
        #self.layers = []
        self.units_per_layer = [2, 1, 1]
        #for y in xrange(self.height):
            #layer = Layer(y, self.units_per_layer[y], self, unit_width = self.unit_width, output_layer = (y+1 == len(self.units_per_layer)))
            #self.layers.append(layer)
        #self.input_layer = self.layers[0]
        #if self.width == 2:
          #self.output_layer = self.layers[1]
          #self.hidden_layer = None
        #elif self.width == 3:  
          #self.hidden_layer = self.layers[1]
          #self.output_layer = self.layers[2]
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

    def _draw(self):
      cr = self.window.cairo_create()
      cr.set_antialias(cairo.ANTIALIAS_NONE)
      for layer in self.layers:
        #layer.set_colour(np.random.uniform(low=0.0, high=1.0, size=3))
        #layer.Run([1, 0])
        #cr = self.window.cairo_create()
        #cr.set_antialias(cairo.ANTIALIAS_NONE)
        layer.Draw(cr, *self.window.get_size())
        

    def _propagate(self, pattern = 0):
      #output = self.input_layer.Run([1, 1])
      #print output
      #if self.hidden_layer:
        #output = self.hidden_layer.Run(output)
      #output = self.output_layer.Run(output)
      #print output
      x = self.input_units 
      y = self.output_units
      w = self.weights
      h = self.learning_rate
      d = self.targets
      N = len(self.patterns[0])
      P = len(self.patterns)
      p = pattern
      f = self.activation_function
      for i in range(N):
        x[i] = self.patterns[p][i]
        y[0] = 0
        for i in range(N+1):
          y[0] += x[i] * w[i]
        y[0] = f(y[0])

        error = self.targets[p][0] - f(y[0])

        #self.Draw()

        
    def _train(self, pattern = 0):
      x = self.input_units 
      
      h = self.hidden_units 
      
      y = self.output_units
      w = self.weights
      h = self.learning_rate
      d = self.targets
      N = len(self.patterns[0])
      P = len(self.patterns)
      p = pattern
      f = self.activation_function
          
      for i in range(N):    
        x[i] = self.patterns[p][i]
        
      #x[0:2] = self.patterns[p][:]  
      
      y[0] = 0
      for i in range(N+1): 
        y[0] += x[i] * w[i]
        
      #y[0] = np.dot(x, w)
      
      y = f(y)
      print "output unit in Train()", y
      print len(self.output_units)
      self.output_units = y
      #error = d[p][0] - y[0]
      error = d[p] - y

      #for i in range(N+1): 
        #w[i] += h * error * x[i]
        
      w += h * error * x
      #print w
      #print self.weights
      print  x, '->',  y, error
      #time.sleep(1)
      
      
    def Run(self):
      #print 'tick: %s /' % str(self.tick).zfill(len(str(self.ticks))),
      #print '%s' % str(self.ticks).zfill(len(str(self.ticks)))



      #if self.ticks:
        #self.ticks = ticks
      print "tick", self.tick, self.current_pattern, len(self.patterns)

      #self.Propagate(self.current_pattern)
      self._train(self.current_pattern)
      
      if self.current_pattern >= (len(self.patterns)-1):
        self.current_pattern = 0
        self.tick += 1
        
      else: 
        self.current_pattern += 1

      cr = self.window.cairo_create()
      cr.set_antialias(cairo.ANTIALIAS_NONE)
      self.Draw(cr, *self.window.get_size())
  

      if self.running and not self.paused:
        return True
      else:
        return False

    def Train(self):
      #print 'tick: %s /' % str(self.tick).zfill(len(str(self.ticks))),
      #print '%s' % str(self.ticks).zfill(len(str(self.ticks)))

      if self.tick >= self.ticks:
        self.running = False
        return False
      else:
        self.running = True

      #if self.ticks:
        #self.ticks = ticks
      print "tick", self.tick, self.current_pattern, len(self.patterns)

      #self.Propagate(self.current_pattern)
      self._train(self.current_pattern)
      
      if self.current_pattern >= (len(self.patterns)-1):
        self.current_pattern = 0
        self.tick += 1
        
      else: 
        self.current_pattern += 1

      cr = self.window.cairo_create()
      cr.set_antialias(cairo.ANTIALIAS_NONE)
      self.Draw(cr, *self.window.get_size())
  

      if self.running and not self.paused:
        return True
      else:
        return False
      
      
    def Run(self):
      #print 'tick: %s /' % str(self.tick).zfill(len(str(self.ticks))),
      #print '%s' % str(self.ticks).zfill(len(str(self.ticks)))



      #if self.ticks:
        #self.ticks = ticks
      print "tick", self.tick, self.current_pattern, len(self.patterns)

      #self.Propagate(self.current_pattern)
      self._train(self.current_pattern)
      
      if self.current_pattern >= (len(self.patterns)-1):
        self.current_pattern = 0
        self.tick += 1
        
      else: 
        self.current_pattern += 1

      cr = self.window.cairo_create()
      cr.set_antialias(cairo.ANTIALIAS_NONE)
      self.Draw(cr, *self.window.get_size())
  

      if self.running and not self.paused:
        return True
      else:
        return False

    def Propagate(self, pattern = 0):
      #print 'tick: %s /' % str(self.tick).zfill(len(str(self.ticks))),
      #print '%s' % str(self.ticks).zfill(len(str(self.ticks)))

      #if self.tick >= self.ticks:
        #self.running = False
        #return False
      #else:
        #self.running = True

      #if self.ticks:
        #self.ticks = ticks
      #print "tick", self.tick, self.current_pattern, len(self.patterns)

      #self.Propagate(self.current_pattern)
      self._propagate(pattern)
      
      #if self.current_pattern >= (len(self.patterns)-1):
        #self.current_pattern = 0
        #self.tick += 1
        
      #else: 
        #self.current_pattern += 1

      cr = self.window.cairo_create()
      cr.set_antialias(cairo.ANTIALIAS_NONE)
      self.Draw(cr, *self.window.get_size())
  

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

    def Draw(self, cr = None, width = None, height = None):
        #font_size = self.unit_width / 10.0
        if  self.unit_width  < 20:
          font_size = 0
        elif self.unit_width <= 35:
          font_size = 10
        elif  self.unit_width <= 80:
          font_size = 12
        else:
          font_size =  self.unit_width / 10 * 1.5
        
        cr.set_font_size(font_size)
         
        j = 0
        for i in range(self.input_width):
          j = 0
          cr.set_source_rgb(1.0 - self.input_units[i], 1.0 - self.input_units[i], 1.0 - self.input_units[i])
          x = (width - self.input_width * (self.unit_width+1) - 20) / 2.0 + 10 + (i * (self.unit_width+1) )
          y = j * (self.unit_width+1)+ 10
          cr.rectangle(x, y, self.unit_width, self.unit_width)
          cr.fill()
          
          cr.set_source_rgb(self.input_units[i], self.input_units[i], self.input_units[i])
          
          (text_x, text_y, text_width, text_height, text_dx, text_dy) = cr.text_extents(str(self.input_units[i])) 
          
          cr.move_to(self.unit_width/2.0 + x - text_width/2.0, self.unit_width/2.0 + y + text_height/2.0)
          cr.show_text(str(self.input_units[i]))

        j += 1
        for i in range(self.hidden_width):
          print "hidden unit", self.hidden_units[i]
          cr.set_source_rgb(1.0 - self.hidden_units[i], 1.0 - self.hidden_units[i], 1.0 - self.hidden_units[i])
          x = (width - self.output_width * (self.unit_width+1) - 20) / 2.0 + 10 + (i * (self.unit_width+1) )
          y = j * (self.unit_width+1)+ 10
          cr.rectangle(x, y, self.unit_width, self.unit_width)
          cr.fill()
          
          cr.set_source_rgb(self.hidden_units[i], self.hidden_units[i], self.hidden_units[i])

          (text_x, text_y, text_width, text_height, text_dx, text_dy) = cr.text_extents(str(self.hidden_units[i])) 

          cr.move_to(self.unit_width/2.0 + x - text_width/2.0, self.unit_width/2.0 + y + text_height/2.0)
          cr.show_text(str(self.hidden_units[i]))

        j += 1
        for i in range(self.output_width):
          print "output unit", self.output_units[i]
          cr.set_source_rgb(1.0 - self.output_units[i], 1.0 - self.output_units[i], 1.0 - self.output_units[i])
          x = (width - self.output_width * (self.unit_width+1) - 20) / 2.0 + 10 + (i * (self.unit_width+1) )
          y = j * (self.unit_width+1)+ 10
          cr.rectangle(x, y, self.unit_width, self.unit_width)
          cr.fill()
          
          cr.set_source_rgb(self.output_units[i], self.output_units[i], self.output_units[i])

          (text_x, text_y, text_width, text_height, text_dx, text_dy) = cr.text_extents(str(self.output_units[i])) 

          cr.move_to(self.unit_width/2.0 + x - text_width/2.0, self.unit_width/2.0 + y + text_height/2.0)
          cr.show_text(str(self.output_units[i]))


    
    def Reset(self, width, height, unit_width, patterns, targets):
      print self.width, self.height
      self.__init__(width, height, unit_width = unit_width, patterns = patterns, targets = targets)
      print self.width, self.height

      self.redraw_canvas()
      

      
##----------------------------------------------------------------------------------------------------##
      
class Model:

    def If_running(self):
      #print network.running
      self.play.set_sensitive(not self.network.running)   
      self.step.set_sensitive(not self.network.running)   
      return self.network.running
      
    def If_paused(self):
      #print network.running
      self.pause.set_sensitive(self.network.running)
      return False

    def Status_update(self):
      if self.network.running:
        context_id = self.status_bar.get_context_id("Running")
        #print context_id
        text = "Iteration: " +  str(self.network.tick).zfill(len(str(self.network.ticks))) + "/" + str(self.network.ticks).zfill(len(str(self.network.ticks)))
        if self.network.paused:
          text += ", Paused"
        self.status_bar.push(context_id, text)
        return True # we need it to keep updating if the model is running   
      elif not self.network.running:
        if not self.network.paused:
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
        self.network.Pause()
        if self.network.paused:
          self.pause.set_label("Unpause")
        else:
          self.pause.set_label("Pause")
          glib.idle_add(self.network.Run)
          glib.idle_add(self.If_running)
        glib.idle_add(self.Status_update)
          
          
    def Step(self, widget=None, data=None):
      glib.idle_add(self.network.Propagate, self.pattern_spin_button.get_value_as_int())

      
    def Run(self, widget=None, data=None):
      self.network.ticks += self.iterations_spin_button.get_value_as_int()
      if not self.network.running:
        glib.idle_add(self.network.Train)
      glib.idle_add(self.Status_update)
      glib.idle_add(self.If_running)
      glib.idle_add(self.If_paused)

    def Reset(self, widget=None, data=None):
      #[network, play, pause]
      #print 'combobox', self.layer_combobox.get_active_text()
      self.network.Reset(self.width_spin_button.get_value_as_int(), int(self.layer_combobox.get_active_text()), self.unit_width_spin_button.get_value_as_int(), patterns = logic.Patterns, targets = logic.Targets)
      self.pause.set_label('Pause')
      self.pause.set_sensitive(self.network.paused)
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
      
      self.patterns = logic.Patterns
      self.targets = logic.Targets

      # Args are: homogeneous, spacing, expand, fill, padding
      homogeneous = False
      spacing = 0
      expand = False
      fill = False
      padding = 10

      self.hbox = gtk.HBox(homogeneous, spacing)
      self.hbox2 = gtk.HBox(homogeneous, spacing)
      self.vbox = gtk.VBox(homogeneous, spacing)
      self.window.add(self.vbox)

      
      adjustment = gtk.Adjustment(value=1, lower=1, upper=100000000, step_incr=1000, page_incr=10000)
      self.iterations_spin_button = gtk.SpinButton(adjustment, climb_rate=0, digits=0)
      adjustment = gtk.Adjustment(value=2, lower=1, upper=100, step_incr=5, page_incr=5)
      self.width_spin_button = gtk.SpinButton(adjustment, climb_rate=0, digits=0)
      
      self.layer_combobox = gtk.combo_box_new_text()
      for i in range(2, 4):
                self.layer_combobox.append_text(str(i))        
      self.layer_combobox.set_active(0)
      
      adjustment = gtk.Adjustment(value=2, lower=1, upper=100, step_incr=5, page_incr=5)
      self.height_spin_button = gtk.SpinButton(adjustment, climb_rate=0, digits=0)
      adjustment = gtk.Adjustment(value=100, lower=1, upper=100, step_incr=5, page_incr=5)
      self.unit_width_spin_button = gtk.SpinButton(adjustment, climb_rate=0, digits=0)
      
      adjustment = gtk.Adjustment(value=0, lower=0, upper=len(self.patterns)-1, step_incr=1, page_incr=1)
      self.pattern_spin_button = gtk.SpinButton(adjustment, climb_rate=0, digits=0)
    
      # Create a series of buttons with the appropriate settings
      self.play = gtk.Button("Train")
      self.pause = gtk.Button("Pause")
      self.reset = gtk.Button("Reset")
      self.step = gtk.Button("Step")
      
      self.play.connect("clicked", self.Run, None)
      self.pause.connect("clicked", self.Pause, None)
      self.reset.connect("clicked", self.Reset, None)
      self.step.connect("clicked", self.Step, None)
      self.width_spin_button.connect("value_changed", self.Reset)
      self.height_spin_button.connect("value_changed", self.Reset)
      self.unit_width_spin_button.connect("value_changed", self.Reset)
      self.layer_combobox.connect('changed', self.Reset)

      self.network = Network(width = self.width_spin_button.get_value_as_int(), height = 3, unit_width = self.unit_width_spin_button.get_value_as_int(),
                             patterns = self.patterns, targets = self.targets)
      self.network.show()
      self.pause.set_sensitive(self.network.paused)


      self.vbox.pack_start(self.network, True, True, 0)
      self.vbox.pack_start(self.hbox, expand, fill, 3)
      self.vbox.pack_start(self.hbox2, expand, fill, 3)
      self.status_bar = gtk.Statusbar()
      self.vbox.pack_start(self.status_bar, expand, fill, 0)
      self.status_bar.show()
      glib.idle_add(self.Status_update)
      self.hbox.show()
      self.hbox2.show()
      self.vbox.show()
      self.play.show()    
      self.pause.show()
      self.reset.show() 
      self.step.show() 
      self.iterations_spin_button.show()  
      self.width_spin_button.show()
      self.height_spin_button.show()
      self.unit_width_spin_button.show()
      self.pattern_spin_button.show()
      self.layer_combobox.show()
      
      
      self.hbox.pack_start(self.play, expand, fill, padding) 
      self.hbox.pack_start(self.pause, expand, fill, 0)      
      self.hbox.pack_start(self.reset, expand, fill, padding)
     
      label = gtk.Label("Epochs:") 
      label.show()
      self.hbox.pack_start(label, expand, fill, 0)
      self.hbox.pack_start(self.iterations_spin_button, expand, fill, padding)
      
      #label = gtk.Label("Hidden units:") 
      #label.show()
      #self.hbox.pack_start(label, expand, fill, padding)
      #self.hbox.pack_start(self.width_spin_button, expand, fill, 0)
      
      label = gtk.Label("Unit size:") 
      label.show()
      self.hbox.pack_start(label, expand, fill, 0)
      self.hbox.pack_start(self.unit_width_spin_button, expand, fill, padding)
      
      #label = gtk.Label("Number of layers:") 
      #label.show()
      #self.hbox.pack_start(label, expand, fill, padding)
      #self.hbox.pack_start(self.layer_combobox, expand, fill, 0)
      
      self.hbox2.pack_start(self.step, expand, fill, padding)      
      
      label = gtk.Label("Pattern:") 
      label.show()
      self.hbox2.pack_start(label, expand, fill, 0)
      self.hbox2.pack_start(self.pattern_spin_button, expand, fill, padding)
      
      self.quit = gtk.Button("Quit")
      self.quit.connect("clicked", self.destroy, None)
      self.hbox2.pack_end(self.quit, expand, fill, padding)
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
    
