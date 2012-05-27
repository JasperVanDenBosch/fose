from setuptools import setup, find_packages
from version import get_git_version


setup(name='fose',
      version=get_git_version(),
      packages=find_packages(),
        test_suite='tests',
      )

