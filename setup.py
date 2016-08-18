from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    project_license = f.read()

setup(
    name='NAME',
    version='0.1',
    description='My Project',
    long_description=readme,
    author='Austin Keller',
    author_email='atkeller@uw.edu',
    url='https://github.com/austinkeller/myproject',
    license=project_license,
    packages=find_packages(exclude=('tests', 'docs'))
)
