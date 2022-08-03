import setuptools
from setuptools import setup
import os


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


long_description = read("README.md")

setup(
    name='pythonConsoleConfigs',
    description="Python Console Configuration",
    long_description=long_description,
    version='0.9.4',
    license='Apache License',
    author="Stefanos Grigori",
    author_email='gregorystefanos@gmail.com',
    packages=setuptools.find_packages(),
    url='https://github.com/StefanosGregory/PythonConsoleConfig',
    keywords=['Python', 'Console', 'Configuration', 'Font', 'Color', 'Highlight', 'Style']
)
