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

6. Before you can experiment with the code, you'll have to make sure that you have all the libraries and dependencies required to support this project. You will mainly need Python3.7+, PyTorch and its torchvision, OpenCV, and Matplotlib. You can install  dependencies using:
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


#### Syllabus
-  Python Basics
 1. Interpreter and Jupyter Basics
 2. Python Language Basics
 3. Control Flow
 4. Data Structures
 5. Functions, Modules, Packages, Iterators, Generators
 6. Files and the Operating System
 7. Errors and Exception Handling
 8. Database
 9. Other Subjects
 10. Programming Exercises
-  Python for Data Science, Machine Learning, Deep Learning
 1. Python for Data Analysis
    1. NumPy
    2. Pandas
    3. Data Loading, Storage, and File Formats
    4. Data Cleaning and Preparation
    5. Data Wrangling Join, Combine,and Reshape
    6. Plotting and Visualization
    7. Data Aggregation and Group Operations
    8. Time Series
    9. Real World Data Analysis Examples

TODO: Complete syllabus
