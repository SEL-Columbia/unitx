from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='unitx',
      version=version,
      description="",
      long_description="""\
      """,
      classifiers=[], 
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite='unitx.test',
      install_requires=[
          # -*- Extra requirements: -*-
        'pyyaml',
      ],
      entry_points={ 
        'console_scripts': 
        ['unitx-start = unitx:run_command_line']
        }
      )
