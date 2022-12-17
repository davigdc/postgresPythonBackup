from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Davi Carmo',
    author_email='davigdc10@gmail.com',
    description='A utility for backing up PostgresSQL databas',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/davigdc/postgresPythonBackup',
    packages=find_packages('src')
)