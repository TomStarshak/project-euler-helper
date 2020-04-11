from setuptools import setup

setup( name = 'euler_helper',
      url = 'https://github.com/TomStarshak/project-euler-helper',
      author = 'Tom Starshak',
      author_email = 'starshak@gmail.com',
      version = '0.1',
      description = 'Helper functions for Project Euler',
      packages = ['euler_helper'],
      install_requires=['math'],
      license='MIT',
      long_description=open('README.md').read())
