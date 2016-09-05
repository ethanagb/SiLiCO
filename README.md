
#SiLiCO: Simulator of Long Read Sequencing in PacBio and Oxford Nanopore 


###Installation
---
If you've downloaded the source code, unpack SiLiCO, build, and install it.

+ `tar -xvzf SiLiCO-1.0.0.tar.gz`
+ `cd SiLiCO-1.0.0`
+ `python setup.py build`
+ `python setup.py install`

###Requirements
---
SiLiCO is compatible with Python 2.7.11 or higher and Python 3.5 or higher.

SiLiCO requires the following dependencies, which are installed during setup:

+ [numpy](http://www.numpy.org/)
+ [pybedtools](https://pythonhosted.org/pybedtools/)*
+ [natsort](http://pythonhosted.org/natsort/)

*pybedtools relies on the pysam package. The latest version of pysam (0.9.1.3) is problematic on OS X systems. SiLiCO installs pysam v.0.8.4, to avoid this, but installing other packages that install pysam may update it to the latest version. If you encounter a `Symbol not found: _hfile_plugin_init_libcurl` error when running SiLiCO, downgrade pysam with `pip install pysam==0.8.4`. 




###Usage Instructions
---

```
python SiLiCO.py -i </path/to/genome> [-o </path/to/outDir> -m <mean read length> -s <standard dev of read lengths> -c <coverage> -t <trials> -f]

[ FILE I/O ]

-i, --infile=<str>, REQ			Input genome fasta file. See README for formatting requirments**.
-o, --output=<str>, OPT			Output directory for results. Default = Current directory

[ DISTRIBUTION PARAMETERS ]

-m, --mean_read_length=<int>, OPT	Mean read length for in-silico read generation. Default = 10000 bp
-s, --standard_dev=<int>, OPT		Standard deviation of in-silico reads. Default = 2050
-c, --coverage=<int>, OPT		Desired genome coverage of in-silico sequencing. Default = 8
--trials=<int>, OPT			Number of trials. Default = 1 

[ MODES ] 

-f, --fasta, OPT 			FASTA Mode. When present, converts bed files to FASTA sequences using the provided reference genome.
-n, --nanopore, OPT 		Generate Oxford Nanopore data. Calculates a gamma distribution.
-p, --pacbio, OPT 			Generate PacBio data. Calculates a log normal distribution. Default mode if none specified.

[ DOCUMENTATION ] 

-h, --help				Display this message.
--version				What version of SiLiCO are you using?
--contact				Report a bug or get more help.
--citation				View the citation for SiLiCO.
```
---
###Formatting Requirements

---
Input genome fasta should ideally be a chromosomal assembly with header lines in the style >chr1, >chr2.


###About SiLiCO
---

If you use SiLiCO in your research please cite it as follows: 

[Citation Placeholder]:

`Ethan Alexander Garcia Baker, Mendivil Ramos, O., McCombie, W.R., "SiLiCO:A Simulator for Long Read Sequencing in PacBio and Oxford Nanopore". Bioinformatics. [Date]`

SiLiCO is made freely available under the GNU GPL 3.0 license.
This software may be freely modified and (re)distributed, but you must make your modifications freely available and cite SiLiCO.

View LICENSE.txt or [http://choosealicense.com/licenses/gpl-3.0/](http://choosealicense.com/licenses/gpl-3.0/) for more information.

---

(c) 2016 Ethan Alexander García Baker

<img src="https://www.cshl.edu/images/stories/about_us/logos/cshllogo_standard_RGB.png" alt="cshl logo" width="259"> 

![pitt_logo](http://www.communications.pitt.edu/images/shared/pitt.gif)
