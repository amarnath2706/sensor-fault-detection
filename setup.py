from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return a list of requirements
    """
    requirement_list:List[str] = []
    return requirement_list 

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Amar",
    author_email="amarnath.arjsd@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements(), # additional packages we need to install through requirements.txt file
)