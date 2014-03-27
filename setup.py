#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

requires = [
        'bedup',
]

setup(name='lowmem-bedup',
      version=0.1,
      author='Peter Smit',
      author_email='peter@smitmail.eu',
      url='',
      description='Lowmem bedup',
      packages=['lowmem-bedup'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
      ],
      license="MIT",
      scripts=['lowmem-bedup.py',
               ],
      install_requires=requires,
      )