# python_tutorial_material
Materials for my Python tutorials. From basics to Machine Learning, Data Science, and Deep Learning applications.

## Preparing the environment
**Note**: I have tested codes on __Linux__. It can surely be run on Windows and Mac with some little changes.

1. Clone the repository, and navigate to the downloaded folder.
```
git clone https://github.com/iamirmasoud/python_tutorial_material.git
cd python_tutorial_material
```

2. Create (and activate) a new environment, named `coding_env` with Python 3.7. If prompted to proceed with the install `(Proceed [y]/n)` type y.

	```shell
	conda create -n coding_env python=3.7
	source activate coding_env
	```
	
	At this point your command line should look something like: `(coding_env) <User>:python_tutorial_material <user>$`. The `(coding_env)` indicates that your environment has been activated, and you can proceed with further package installations.

6. Before you can experiment with the code, you'll have to make sure that you have all the libraries and dependencies required to support this project. You will mainly need Python3.7+, PyTorch and its torchvision, OpenCV, and Matplotlib. You can install  dependencies using:
```
pip install -r requirements.txt
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

#### TODO: Add syllabus