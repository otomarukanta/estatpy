#!/usr/bin/env python

from setuptools import setup, find_packages
import os

description = 'A simple python wrapper to access e-Stat API'
long_description = description
if os.path.exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()

setup(name='estatpy',
      version='0.0.1',
      description=description,
      author='otomarukanta',
      author_email='kanta208@gmail.com',
      license='MIT',
      keywords='e-stat wrapper, pandas',
      url='http://github.com/otomarukanta/estatpy',
      packages=find_packages(),

      long_description=long_description,

      install_requires=['pandas'],
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          ]
      )
