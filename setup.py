import os
from setuptools import setup

def read(fname):
      return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
      name='neolinearalgebra',
      version='0.1.6',
      author='Sajid Sarker',
      author_email='sajid.sarker@gmail.com',
      description='NEO Linear Algebra package for Matrix Manipulation.',
      license='MIT',
      keywords='linear algebra matrix vector math',
      packages=['neolinearalgebra'],
      long_description=read('README.md'),
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3'
      ],
      zip_safe=False
)
