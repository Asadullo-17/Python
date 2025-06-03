#Lesson-11

#task-1

#step-1
python -m venv myvenv
#step-2
myvenv\Scripts\activate
#step-3
sorce myvenv/bin/activate
#step-4
pip install numpy pandas matplotlib
#step-5
pip list
#step-6
deactivate


#task-2

#1.geometry/ --> package

#__init__.py -->file

from .circle import area as circle_area, perimeter as circle_perimeter

#circle.py --> file

import math

def area(radius):
    return math.pi*radius**2

def perimeter(radius):
    return 2*math.pi*radius

#2.file_operations/ --> package

#__init__.py --> file

from .file_reader import read_file
from .file_writer import write_file


#file_reader.py --> file

def read_file(file_path):
    with open(file_path,'r') as f:
        return f.read()

#file_writer.py -->file

def write_file(file_path,content):
    with open(file_path,'w') as f:
        return f.write(content)
    
    
