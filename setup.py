from setuptools import setup, find_packages


setup(
    name='pythonConsoleConfigs',
    version='0.9',
    license='Apache License',
    author="Stefanos Grigori",
    author_email='gregorystefanos@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/StefanosGregory/PythonConsoleConfig',
    keywords='Python Console Configuration'
)
