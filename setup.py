from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name = 'hr',
    version = '1.0.0',
    description = 'command line user utility',
    long_description = readme,
    author = 'santosh kaluva',
    author_email = 'skaluva16@gmail.com',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = [],
    entry_points={
        'console_scripts': 'hr=hr.cli:main'
    }
)
