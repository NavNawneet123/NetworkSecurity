'''
The setup.py file is an essemtial part of packaging and distributing 
projects . It is used by setuptools to define the configuration
 of the project , such as its metadata , dependencies and more 
'''
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements 
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read line from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found")
    return requirement_lst
print(get_requirements())  

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Nawneet Kumar",
    author_email="navnawneet.008@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
