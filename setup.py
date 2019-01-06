from setuptools import setup


with open('README.md') as f:
    readme = f.read()

setup(
    name='nyt-cli',
    version='0.1.0',
    py_modules=['nyt_cli'],
    description='A command line news tool',
    long_description=readme,
    author='Uma Desai',
    author_email='udesai@olin.edu',
    url='https://github.com/umadesai/nyt-cli'
)
