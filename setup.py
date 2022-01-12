# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst"), "rb") as stream:
    readme = stream.read().decode("utf8")


setup(
    long_description=readme,
    name="pnums",
    version="0.0.5",
    description="A library that encodes coordinates so neural networks can use them better.",
    python_requires="==3.*,>=3.6.0",
    project_urls={"repository": "https://github.com/simleek/pnums"},
    author="SimLeek",
    author_email="simulator.leek@gmail.com",
    license="MIT",
    packages=["pnums"],
    package_data={},
    install_requires=["numpy>=1.16.1", "scipy==1.*,>=1.4.1"],
    extras_require={
        "dev": [
            "black==18.*,>=18.3.0.a0",
            "coverage==4.*,>=4.5.0",
            "mock==3.*,>=3.0.0",
            "mypy==0.*,>=0.740.0",
            "pydocstyle==4.*,>=4.0.0",
            "pytest==5.2.1",
            "sphinx==2.*,>=2.2.0",
            "tox==3.*,>=3.14.0",
            "tox-gh-actions==0.*,>=0.3.0",
            "typing==3.7.4.1",
        ]
    },
)
