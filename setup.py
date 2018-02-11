from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='colorcalendar',
    version='1.0.0',
    description='A calendar for command-line in Linux',
    url='https://github.com/houluy/calendar',
    author='Houlu',
    author_email='houlu8674@bupt.edu.cn',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='calendar, colorful',
    install_requires=[
        'colorline>=1.0.2',
    ],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'colorcalendar = colorcalendar.main:main',
        ],
    }
)
