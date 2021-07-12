from setuptools import setup, find_packages
 
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Education",
  "Operating System :: Microsoft :: Windows :: Windows 10",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.9"
]
 
setup(
  name="gratient",
  version="0.1",
  description="This modules allows you print gratient texts.",
  long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
  url="https://github.com/venaxyt/gratient",  
  author="Venax",
  author_email="venaxumofficial@gmail.com",
  license="MIT",
  keywords="gratient",
  classifiers=classifiers,
  packages=["gratient"]
)
