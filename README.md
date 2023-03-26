# Materials for Python tutorials: From basics to Machine Learning, Data Science, and Deep Learning applications.

This repo provides a series of Python tutorials (Jupyter Notebooks) from basics to Machine Learning, Data Science, and Deep Learning applications.

## Preparing the environment
**Note**: I have tested codes on __Linux__. It can surely be run on Windows and Mac with some little changes.

1. Clone the repository, and navigate to the downloaded folder.
```
git clone https://github.com/iamirmasoud/python_tutorial_material.git
cd python_tutorial_material
```

2. Create (and activate) a new environment, named `coding_env` with Python 3.7. If prompted to proceed with the install `(Proceed [y]/n)` type y.

	```shell
	conda create . n coding_env python=3.7
	source activate coding_env
	```
	
	At this point your command line should look something like: `(coding_env) <User>:python_tutorial_material <user>$`. The `(coding_env)` indicates that your environment has been activated, and you can proceed with further package installations.

6. Before you can experiment with the code, you'll have to make sure that you have all the libraries and dependencies required to support this project. You can install dependencies using:
```
pip install . r requirements.txt
```

7. Navigate back to the repo. (Also, your source environment should still be activated at this point.)
```shell
cd python_tutorial_material
```

8. Open the directory of notebooks, using the below command. You'll see all the project files appear in your local environment; open the first notebook and follow the instructions.
```shell
jupyter notebook
```

9. Once you open any of the project notebooks, make sure you are in the correct `coding_env` environment by clicking `Kernel > Change Kernel > coding_env`.

## Useful Books:

- [Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/)
- [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems 2nd Edition](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646)
- [Python Data Science Handbook: Essential Tools for Working with Data](https://www.amazon.com/Python-Data-Science-Handbook-Essential-ebook/dp/B01N2JT3ST/)


## Syllabus


### Python Basics
This directory contains fundamental Python concepts that beginners need to learn. It consists of the following subdirectories:

#### 1-Interpreter and Jupyter Basics
This section covers the basics of the Python interpreter, the Jupyter Notebook, and how to write Python code in both.

#### 2-Python Language Basics
This section covers Python data types, operators, expressions, and control flow statements.

#### 3-Control Flow
This section covers Python's control flow statements, including if statements, while loops, and for loops.

#### 4-Data Structures
This section covers Python's built-in data structures, such as lists, tuples, dictionaries, and sets.

#### 5-Functions, Modules, Packages, Iterators, Generators
This section covers functions, modules, packages, iterators, and generators in Python.

#### 6-Files and the Operating System
This section covers how to work with files and directories in Python.

#### 7-Errors and Exception Handling
This section covers how to handle errors and exceptions in Python.

#### 8-Database
This section covers how to work with databases in Python using SQLite and SQLAlchemy.

#### 9-Other Subjects
This section covers advanced Python concepts, such as OOP, decorators, and more.

### Python for Data Science, Machine Learning, and Deep Learning

This directory contains resources for using Python for data science, machine learning, and deep learning. It consists of the following subdirectories:

#### Python for Data Analysis

This section covers the NumPy and Pandas libraries, data cleaning and preparation, data wrangling, plotting and visualization, and more.

#### Python for Data Science

This section covers IPython, NumPy, and other libraries used in data science, including debugging and profiling techniques.

#### Hands-On Machine Learning with Sklearn and Tensorflow

This section covers the basics of machine learning, including artificial neural networks, deep neural nets, and convolutional neural networks, using Scikit-Learn and TensorFlow.

#### Deep Learning
This section covers deep learning techniques using Keras and PyTorch.


