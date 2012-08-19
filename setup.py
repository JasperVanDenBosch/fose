from setuptools import setup, find_packages
from version import get_git_version


setup(name='fose',
        version=get_git_version(),
        packages=find_packages(),
        test_suite='tests',
        entry_points={
          'console_scripts': ['fose = fose:main',]},
        tests_require='lxml',
        package_data={'fose': ['*.xsd']},
      )

