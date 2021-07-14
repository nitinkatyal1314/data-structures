import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.2.1'
PACKAGE_NAME = 'py-ds'
AUTHOR = 'Nitin Katyal'
AUTHOR_EMAIL = 'nitinkatyal1314@gmail.com'
URL = 'https://github.com/nitinkatyal1314/data-structures'

LICENSE = 'MIT License'
DESCRIPTION = 'Ready to use data structures'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = []

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      python_requires=">=3.6",
      include_package_data=True,
      zip_safe=False,
      packages=find_packages()
)