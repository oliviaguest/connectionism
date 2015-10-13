#Block Practical: Connectionist Models and Cognitive Processes

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

##Online Courses
- [Machine Learning](https://www.coursera.org/learn/machine-learning/) by Andrew Ng
- [Neural Networks for Machine Learning](https://www.coursera.org/course/neuralnets) by Geoffrey Hinton
- 
##Installing Python 

###Windows Users

This is a little tricky:

1. Install Python: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi

2. Install matplotlib, numpy, and scipy using pip. Specifically you need to download from here http://www.lfd.uci.edu/~gohlke/pythonlibs/ the following:
a. matplotlib-1.4.3-cp27-none-win32.whl
b. numpy-1.10.0b1+mkl-cp27-none-win32.whl
c. scipy-0.16.0-cp27-none-win32.whl
This requires you to be in the Scripts folder of the Python27 installation. So the command prompt for me looks like:
C:\Python27\Scripts>pip install NAME_OF_WHEEL_FILE.whl
For all three of those you need to run a pip command like above.  

3. Install pygtk: http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/pygtk-all-in-one-2.24.2.win32-py2.7.msi

4. To check that everything works, open network.py and see if it runs (it should open a small window with some black and white boxes and some buttons down the bottom): https://www.dropbox.com/s/diynw3xqdyz8ox7/network.py?dl=1
