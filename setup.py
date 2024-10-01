#it will help me build my application as a package
from setuptools import find_packages, setup
# find_packages() will automatically discover all packages and subpackages
# in the directory where setup.py is located.
# __init__.py is required to make Python treat the directories as containing packages
# This file can be empty, or it can contain valid Python code
from typing import List

Hyphen = '-e .'
def get_requirements(path:str) -> List[str]:
    requirements = []
    with open(path) as f:
        requirements = f.readlines()
        requirements =  [line.replace("\n","") for line in requirements] 
        if Hyphen in requirements:
            requirements.remove(Hyphen)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Hichem',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)