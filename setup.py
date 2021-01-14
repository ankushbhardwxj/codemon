from setuptools import setup,find_packages

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setup(
  name='codemon',
  version='0.0.4',
  author='Ankush Bhardwaj',
  author_email='ankush.bhardwaj0@gmail.com',
  description='CLI tool to ace competitive programming contests',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/ankingcodes/codemon',
  packages=find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  install_requires=[
    'watchdog',
    'clint',
    'stdiomask', 
    'requests',
    'bs4'
  ],
  entry_points={
    'console_scripts': [
      'codemon = codemon.codemon:main'
    ]
  }
)
