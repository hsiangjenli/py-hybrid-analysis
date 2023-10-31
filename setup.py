from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = [item for item in f.read().split('\n') if item]

setup(

    author='Hsiang-Jen Li',
    author_email='hsiangjenli@gmail.com',

    name='pyHybridAnalysis',
    version='0.0.0',
    url='https://github.com/hsiangjenli/py-hybrid-analysis',

    description='Using python to access Hybrid Analysis API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['pyhybridanalysis'],
    install_requires=requirements,
)