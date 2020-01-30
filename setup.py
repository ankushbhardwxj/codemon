from setuptools import setup, find_packages

setup(
  name='codemon',
  version='0.0.1',
  author='Ankush Bhardwaj',
  packages=find_packages(),
  install_requires=[
    'watchdog',
    'clint'
  ],
  entry_points={
    'console_scripts': [
      'codemon = codemon.codemon:main'
    ]
  }
)