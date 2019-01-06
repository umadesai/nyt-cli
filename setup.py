from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='nyt-cli',
    version='0.1.0',
    packages=find_packages(),
    description='A command line news tool',
    long_description=readme,
    author='Uma Desai',
    author_email='udesai@olin.edu',
    url='https://github.com/umadesai/nyt-cli'
)
