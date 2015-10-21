#Block Practical: Connectionist Models and Cognitive Processes

##Course Materials
###1st Week
- Code: [pyceptron.py](https://github.com/oliviaguest/connectionism/raw/master/week1/pyceptron.py)
- Slides: [Part 1: Intro to Programming](https://github.com/oliviaguest/connectionism/raw/master/week1/slides/part_1_slides.pdf), [Part 2: Intro to Networks](https://github.com/oliviaguest/connectionism/raw/master/week1/slides/part_2_slides.pdf)
- Exercises: [Pyceptron](https://github.com/oliviaguest/connectionism/raw/master/week1/exercises/exercises.pdf)

##Reading Materials
- [Essay: A Brief Introduction to Connectionism](http://kimplunkett.org.uk/secondtry/page31/page32/index.html)

###2nd Week
- Code: [network_missing.py](https://github.com/oliviaguest/connectionism/raw/master/week2/network_missing.py)
- Slides: [Part 3: Feedfoward Networks](https://github.com/oliviaguest/connectionism/raw/master/week2/slides/part_3_slides.pdf)
- Exercises: [Backpropagation](https://github.com/oliviaguest/connectionism/raw/master/week2/exercises/exercises.pdf)


##Programming
###Exercises
- [Codecademy](www.codecademy.com)
- [LearnPython.org](http://www.learnpython.org/)
- [Codewars](http://www.codewars.com/)

###Books
- [Learn Python the Hard Way](http://learnpythonthehardway.org/book/)
- [How to Think Like a Computer Scientist: Learning with Python](http://www.openbookproject.net/thinkcs/python/english2e/)
- [Think Python: How to Think Like a Computer Scientist](http://www.greenteapress.com/thinkpython/)

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
