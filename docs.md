---
layout: page
title: Documentation
subtitle: how to use SiLiCO
permalink: /docs/
---

Formatting Requirements
---
Input genome fasta should be a chromosomal assembly with header lines in the style >chr1, >chr2.

Usage Instructions
---
python SiLiCO.py -i </path/to/genome> [-o </path/to/outDir> -m <mean read length> -s <standard dev of read lengths> -c <coverage> -t <trials>]

Parameters
---

**[ FILE I/O ]**

-i, --infile=<str>, REQ	Input genome fasta file. See README for formatting requirments

o, --output=<str>, OPT**			Output directory for results. Default = Current directory

**[ DISTRIBUTION PARAMETERS ]**

-m, --mean_read_length=<int>, OPT	Mean read length for in-silico read generation. Default = 10000 bp

-s, --standard_dev=<int>, OPT		Standard deviation of in-silico reads. Default = 2050

-c, --coverage=<int>, OPT		Desired genome coverage of in-silico sequencing. Default = 8

--trials=<int>, OPT			Number of trials. Default = 1 

**[ MODES ]**

-f, --fasta, OPT 			FASTA Mode. When present, converts bed files to FASTA sequences using the provided reference genome.

-n, --nanopore, OPT 		Generate Oxford Nanopore data. Calculates a gamma distribution.

-p, --pacbio, OPT 			Generate PacBio data. Calculates a log normal distribution. Default mode if none specified.

**[ DOCUMENTATION ]**

-h, --help				Display this message.

--version	  			What version of SiLiCO are you using?

--contact				Report a bug or get more help.

--citation				View the citation for SiLiCO.



