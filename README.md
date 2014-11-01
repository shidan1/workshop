# Workshop

Workshop in compile-time techniques for detecting Javascript exploits.

### Short description of our implementation

We created learning machine based on an SVM [(Support Vector Machine)](http://en.wikipedia.org/wiki/Support_vector_machine) using an RBF [(Radial Basis Function)](http://en.wikipedia.org/wiki/Radial_basis_function_kernel) kernel. The machine analyzes a large number of scripts, both malicious and benign, and uses this information to determine if a given script is malicious or not.

Users can add more scripts to the machine's script database to better improve performance and classification.

The machine uses dozens of features based on academic papers and our research.

We concentrated on features regarding the visibilty of the code and characters distrubtion, such as entropy, n-Grams and more.


### Prerequisites and Installation 

* <u>Prerequisites</u>: You must have **python 3.3** or higher installed on your machine.

* <u>Installation</u>: To install, extract all the files into one folder.
<br>Make sure that you have the following packages in your folder:
	1. Project
	2. libsvm-3.18
	3. ply-3.4
	4. slimit-master

**Please note:** Windows may delete malicious files when running the program. We recommend using a mac or disabling any protection software before installation.

### How to use

<u>Run instructions</u>: To run the program, open a Console, go to the **Project** package folder and type:

`>> python3 UserInterface.py`


We created a nice and simple user interface that allows the user to paste scripts or load them from an existing file.

An empty text editor will open. Paste the code into the editor or load it by clicking on *File > Open*.

<br>
To analyaze the given script, click on *File > Detect Malicious Code*. 

After the program will finish analyzing the script, a message will appear with the results.

<br>
To add your script to the learning machine's script database:

 - <u>For malicious script:</u> Click on *File > Add this Malicious Code to the Learning Machine* 

 - <u>For proper script:</u> Click on *File > Add this Proper Code to the Learning Machine* 

** Please note: ** Before loading a new script, use the *Edit > Clear all* or the *File > New* functions. Otherwise the scripts will be concatenated.

### About us

Daniel Strokovsky - <strokovsky@gmail.com>
<br>
Idan Sharon - <idansharonx@gmail.com>

