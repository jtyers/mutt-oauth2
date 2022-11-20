import pathlib
from setuptools import setup
from setuptools import find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mutt-oauth2",
    version="0.0.1",
    description="Mutt OAUTH2 script",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jtyers/mutt-oauth2",
    author="Jonny Tyers",
    author_email="jonny@jonnytyers.co.uk",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "mutt-oauth2 = mutt_oauth2.main:main",
        ]
    },
)
