from setuptools import setup, find_packages

setup(
    name='getcurrenttime',
    version='0.1',
    description='Retrieves current date and time',
    package_dir={"":"currentdatetime"},
    packages=find_packages(where="currentdatetime")
)
