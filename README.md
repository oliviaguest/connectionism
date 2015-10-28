#Block Practical: Connectionist Models and Cognitive Processes

##Course Materials
###1st Week
- Code: [pyceptron.py](https://github.com/oliviaguest/connectionism/raw/master/week1/pyceptron.py)
- Slides: [Part 1: Intro to Programming](https://github.com/oliviaguest/connectionism/raw/master/week1/slides/part_1_slides.pdf), [Part 2: Intro to Networks](https://github.com/oliviaguest/connectionism/raw/master/week1/slides/part_2_slides.pdf)
- Exercises: [Pyceptron](https://github.com/oliviaguest/connectionism/raw/master/week1/exercises/exercises.pdf)


###2nd Week
- Code: [network_missing.py](https://github.com/oliviaguest/connectionism/raw/master/week2/network_missing.py), [network_hints.py](https://github.com/oliviaguest/connectionism/raw/master/week2/network_hints.py), [network.py](https://github.com/oliviaguest/connectionism/raw/master/week2/network.py)
- Slides: [Part 3: Feedfoward Networks](https://github.com/oliviaguest/connectionism/raw/master/week2/slides/part_3_slides.pdf)
- Exercises: [Backpropagation](https://github.com/oliviaguest/connectionism/raw/master/week2/exercises/exercises.pdf)

###3rd Week
- Code: [network.py](https://github.com/oliviaguest/connectionism/raw/master/week3/network_missing.py)
- Slides: [Part 4: Replicating a Model](https://github.com/oliviaguest/connectionism/raw/master/week3/slides/part_4_slides.pdf)
- Exercises: [Replication of Tyler et al. (2000)](https://github.com/oliviaguest/connectionism/raw/master/week3/exercises/exercises.pdf)
- Tyler, L. K., Moss, H. E., Durrant-Peatfield, M. R., & Levy, J. P. (2000). **[Conceptual structure and the structure of concepts: A distributed account of category-specific deficits](https://github.com/oliviaguest/connectionism/raw/master/week3/tyler_2000.pdf)**. *Brain and language*, 75(2), 195-231.


##Reading Materials
- [Essay: A Brief Introduction to Connectionism](http://kimplunkett.org.uk/secondtry/page31/page32/index.html)


##Programming
###Exercises
- [Codecademy](www.codecademy.com)
- [LearnPython.org](http://www.learnpython.org/)
- [Codewars](http://www.codewars.com/)

###Books
- [Learn Python the Hard Way](http://learnpythonthehardway.org/book/)
- [How to Think Like a Computer Scientist: Learning with Python](http://www.openbookproject.net/thinkcs/python/english2e/)
- [Think Python: How to Think Like a Computer Scientist](http://www.greenteapress.com/thinkpython/)

##Inspiration
- [Numpy Tutorial](http://www.python-course.eu/numpy.php)
- [Matplotlib Examples](http://matplotlib.org/1.4.0/examples/index.html)
- [A Primer on Scientific Programming with Python](https://hplgit.github.io/scipro-primer/slides/index.html)
- [Scipy Lecture Notes](http://www.scipy-lectures.org)
- [The Glowing Python](http://glowingpython.blogspot.co.uk/): This blog has various examples of interesting code to play with and give you ideas for your own projects.

##Online Courses
- [Machine Learning](https://www.coursera.org/learn/machine-learning/) by Andrew Ng
- [Neural Networks for Machine Learning](https://www.coursera.org/course/neuralnets) by Geoffrey Hinton

##Installing Python 

###Windows Users

This is a little tricky:

1. Install Python: [download from here](https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi)

2. Install matplotlib, numpy, and scipy using pip. Specifically you need to download the following from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/):
 - matplotlib-1.4.3-cp27-none-win32.whl
 - numpy-1.10.0b1+mkl-cp27-none-win32.whl
 - scipy-0.16.0-cp27-none-win32.whl
 
 This requires you to be in the Scripts folder of the Python27 installation. And to use the windows command prompt. For me this looks like:
```
C:\Python27\Scripts>pip install NAME_OF_WHEEL_FILE.whl
```
For all three of those you need to run a pip command like above.  

3. Install PyGTK: [download from here](http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/pygtk-all-in-one-2.24.2.win32-py2.7.msi)

4. To check that everything works, open network.py and see if it runs without any errors.

###Mac Users

I finally managed to do this on my mac. Use [Homebrew](http://brew.sh/) to install matplotlib, numpy, scipy, pygtk.

###Linux Users

Use your favourite package manager to install matplotlib, numpy, scipy, pygtk.
