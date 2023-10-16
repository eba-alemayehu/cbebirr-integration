
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.18'
DESCRIPTION = 'CBEBirr integration'
LONG_DESCRIPTION = 'This package is a helper package with telebirr integration.'

# Setting up
setup(
    name="cbebirr",
    version=VERSION,
    author="Eba Alemayehu",
    author_email="<ebaalemayhu3@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['xmltodict', 'requests'],
    keywords=['python', 'cbebirr', 'payment', 'ethiopia', 'CBE', 'Commercial bank of Ethiopia'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)