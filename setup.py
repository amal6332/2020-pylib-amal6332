from setuptools import find_packages
from setuptools import setup

setup(
    name='awesome',
    version='0.1.0',
    description='',
    url='ttps://github.com/USER/REPO',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=['numpy'],
    entry_points={'console_scripts': ['hello = awesome.module:hello']},
    zip_safe=False
)
