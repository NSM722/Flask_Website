# A Coffee shop website built in Flask

### Installation
It's recommended to use the latest version of Python. Flask supports Python 3.7 and newer. Dependecies are available in the requirements.txt file.
### Virtual environments
Use a virtual environment to manage the dependencies for your project, both in development and in production. Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages. Python comes bundled with the venv module to create virtual environments.
#### Create an environment
The following commands are for Windows OS so create a project folder and a venv folder within:
```python
mkdir myproject
cd myproject
py -3 -m venv venv 
```
#### Activate the environment
```python
venv\Scripts\activate
```
Your shell prompt will change to show the name of the activated environment.
#### Install Flask
Within the activated environment, use the following command to install Flask:
```python
$ pip install Flask
```







