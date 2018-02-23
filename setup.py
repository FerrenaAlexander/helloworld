
from setuptools import setup, find_packages
setup(
    name="helloworld",
    version="0.1",
    packages=find_packages(),
    author="Alex Ferrena"
    license="GPLv3",
    description="A package to say hi, determine the best type of music, calculate the time since the crab nebula supernova, and peace out politely"
    entry_points={
        'console_scripts': ['helloworld = helloworld.__main__:main']
        },
    classifiers=["Programming Language :: Python :: 3"]
)