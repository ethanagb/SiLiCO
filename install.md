---
layout: page
title: Installing SiLiCO
subtitle: 
permalink: /install/
---

Requirements
---
SiLiCO is compatible with Python 2.7.11 or higher and Python 3.5 or higher.

SiLiCO requires the following dependencies, which are installed during setup:

+ [numpy](http://www.numpy.org/)
+ [pybedtools](https://pythonhosted.org/pybedtools/)*
+ [natsort](http://pythonhosted.org/natsort/)

*pybedtools relies on the pysam package. The latest version of pysam (0.9.1.3) is problematic on OS X systems. SiLiCO installs pysam v.0.8.4 to avoid this, but installing other packages that install pysam may update it to the latest version. If you encounter a `Symbol not found: _hfile_plugin_init_libcurl` error when running SiLiCO, downgrade pysam with `pip install pysam==0.8.4`. 

Installation
---
Once you've downloaded the source code, unpack SiLiCO, build, and install it.

+ `tar -xvzf SiLiCO-1.0.0.tar.gz`
+ `cd SiLiCO-1.0.0`
+ `python setup.py build`
+ `python setup.py install`

