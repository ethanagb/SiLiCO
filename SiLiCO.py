#################################
######### SiLiCO v. 1.0 #########
### (c)2016 Ethan A. G. Baker ###
##### ethanagbaker@pitt.edu #####
#################################

import sys, getopt, os
from splitGenomeFasta import splitGenomeFasta
from getRandomPosition import getRandomPosition
from findChromosome import findChromosome
from generateChrDist import generateChrDist
from simulateReads import simulateReads
from convertToFasta import convertToFasta

def main(argv):
	####################
	#SET DEFAULT VALUES#
	####################
	global mean, outfileName, std, desired_cov,y
	outfileName = '.'
	mean = 10000
	std = 2050
	desired_cov = 8 
	trialCount = 1
	FASTA_MODE = False
	SEQ_MODE = 1 #1=PacBio, 2=Nanopore
	SEQ_MODES_CALLED = 0

	#################
	#PARSE ARGUMENTS#
	#################
	try:
		opts, args = getopt.getopt(argv,"i:o:m:s:c:fhpn",["genome=","outdir=","mean_read_length=","standard_dev=", "coverage=","trials=","help","fasta","version","contact","citation","pacbio","nanopore"])
	except getopt.GetoptError:
		print("\n#############################################################################\n## SiLiCO: Simulator of Long Read Sequencing in PacBio and Oxford Nanopore ##\n#############################################################################")
		print("\nUsage: python SiLiCO.py -i </path/to/genome> -o </path/to/outDir> -m <mean read length> -s <standard dev of read lengths> -c <coverage> -t <trials> [-f] \n")
		print("\n" + "[ FILE I/O ]\n")
		print("-i, --infile=<str>, REQ" + '\t\t\t' + "Input genome fasta file. See README for formatting requirments.")
		print("-o, --output=<str>, OPT" + '\t\t\t' + "Output directory for results. Default = Current directory")
		print("\n" + "[ DISTRIBUTION PARAMETERS ]\n")
		print("-m, --mean_read_length=<int>, OPT" + '\t' + "Mean read length for in-silico read generation. Default = 10000 bp")
		print("-s, --standard_dev=<int>, OPT" + '\t\t' + "Standard deviation of in-silico reads. Default = 2050")
		print("-c, --coverage=<int>, OPT" + '\t\t' + "Desired genome coverage of in-silico sequencing. Default = 8")
		print("--trials=<int>, OPT" + '\t\t\t' + "Number of trials. Default = 1 \n")
		print("[ MODES ] \n")
		print("-f, --fasta, OPT \t\t\tFASTA Mode. When present, converts bed files to FASTA sequences using the provided reference genome.")
		print("-n, --nanopore, \t\t\tGenerate Oxford Nanopore data. Calculates a gamma distribution.")
		print("-p, --pacbio, \t\t\t\tGenerate PacBio data. Calculates a log normal distribution. Default mode if none specified.")
		print("\n[ DOCUMENTATION ] \n")
		print("-h, --help" + '\t\t\t\t' + "Display this message.")
		print("--version" + '\t\t\t\t' + "What version of SiLiCO are you using?")
		print("--contact" + '\t\t\t\t' + "Report a bug or get more help.")
		print("--citation" + "\t\t\t\t" + "View the citation for SiLiCO.")
		print("\nSee README.md for additional documentation.")
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h',"--help"):
			print("\n#############################################################################\n## SiLiCO: Simulator of Long Read Sequencing in PacBio and Oxford Nanopore ##\n#############################################################################")
			print("\nUsage: python SiLiCO.py -i </path/to/genome> -o </path/to/outDir> -m <mean read length> -s <standard dev of read lengths> -c <coverage> -t <trials> [-f] \n")
			print("\n" + "[ FILE I/O ]\n")
			print("-i, --infile=<str>, REQ" + '\t\t\t' + "Input genome fasta file. See README for formatting requirments.")
			print("-o, --output=<str>, OPT" + '\t\t\t' + "Output directory for results. Default = Current directory")
			print("\n" + "[ DISTRIBUTION PARAMETERS ]\n")
			print("-m, --mean_read_length=<int>, OPT" + '\t' + "Mean read length for in-silico read generation. Default = 10000 bp")
			print("-s, --standard_dev=<int>, OPT" + '\t\t' + "Standard deviation of in-silico reads. Default = 2050")
			print("-c, --coverage=<int>, OPT" + '\t\t' + "Desired genome coverage of in-silico sequencing. Default = 8")
			print("--trials=<int>, OPT" + '\t\t\t' + "Number of trials. Default = 1 \n")
			print("[ MODES ] \n")
			print("-f, --fasta, OPT \t\t\tFASTA Mode. When present, converts bed files to FASTA sequences using the provided reference genome.")
			print("-n, --nanopore, \t\t\tGenerate Oxford Nanopore data. Calculates a gamma distribution.")
			print("-p, --pacbio, \t\t\t\tGenerate PacBio data. Calculates a log normal distribution. Default mode if none specified.")
			print("\n[ DOCUMENTATION ] \n")
			print("-h, --help" + '\t\t\t\t' + "Display this message.")
			print("--version" + '\t\t\t\t' + "What version of SiLiCO are you using?")
			print("--contact" + '\t\t\t\t' + "Report a bug or get more help.")
			print("--citation" + "\t\t\t\t" + "View the citation for SiLiCO.")
			print("\nSee README.md for additional documentation.")
			sys.exit(2)
		elif opt in ("-i","--genome"):
			infileName = arg
			if os.path.exists(infileName) == False:
				raise IOError("The genome file you've specified does not exist.")
				sys.exit(2)
		elif opt in ("-o","--outdir"):
			outfileName = arg
			if os.path.isdir(outfileName) ==True:
				pass
			elif os.path.isdir(outfileName) == False:
				print("Making the out directory...")
				os.mkdir(outfileName)
		elif opt in ("-m", "--mean_read_length"):
			mean = int(arg)
		elif opt in ("-s", "--standard_dev"):
			std = int(arg)
		elif opt in ("-c", "--coverage"):
			desired_cov = int(arg)
		elif opt in ("-t", "--trials"):
			trialCount = int(arg)
		elif opt in ("-f", "--fasta"):
			FASTA_MODE = True
		elif opt in ("-p", "--pacbio"):
			SEQ_MODE = 1
			SEQ_MODES_CALLED += 1
		elif opt in ("-n", "--nanopore"):
			SEQ_MODE = 2
			SEQ_MODES_CALLED += 1
		elif opt == "--version":
			print("\nSiLiCO v. 1.0.0")
			sys.exit(2)
		elif opt == "--contact":
			print("\nReport bugs on the GitHub repo: \nhttps://www.github.com/ethanagbaker/SiLiCO")
			sys.exit(2)
		elif opt == "--citation":
			print("\nIf you use SiLiCO in your research please cite it as follows: \n")
			print("[Citation Placeholder]:")
			print("Ethan Alexander Garcia Baker, Mendivil Ramos, O., McCombie, W.R., \"SiLiCO:A Simulator for Long Read Sequencing in PacBio and Oxford Nanopore\". Bioinformatics. [Date]")
			print("\nSiLiCO is made freely available under the GNU GPL 3.0 license.")
			print("This software may be freely modified and (re)distributed, but you must make your modifications freely available and cite SiLiCO.\nView LICENSE.txt or http://choosealicense.com/licenses/gpl-3.0/ for more information.")
			print("(c) 2016")
			sys.exit(2)

	######################
	#Execute SiLiCO steps#
	######################

	#Ensure that only one sequence mode has been specified
	if SEQ_MODES_CALLED > 1:
		raise Exception ("Error: You have specified both PacBio and Oxford Nanopore modes. Select exactly one. Omitting sequencing mode parameter will run SiLiCO in PacBio mode.")
		sys.exit(2)

	#Split the input genome to chromosomal fasta files and return the sorted list of chromosome names.
	print("Preparing the genome file.")
	try:
		names = splitGenomeFasta(infileName)
	except UnboundLocalError:
		print("Error: You have not specified an input genome. --help for usage instructions.")
		print("Exiting...")
		sys.exit(2)
	print("Done!")

	#Generate a distribution of chromosome lenghts in the provided genome.
	print("Generating a genome index file...")
	generateChrDist(names) 
	print("Done!")

	#Generate simulated reads
	if SEQ_MODE == 1:
		print("Generating simulated reads in PacBio mode...")
	elif SEQ_MODE == 2:
		print("Generating simulated reads in Oxford Nanopore mode...")
	simulateReads(infileName,outfileName,mean,std,desired_cov,trialCount,names, SEQ_MODE)
	print("Done!")

	#If -f/--fasta flag is found, convert to fasta file using the reference genome.
	if FASTA_MODE == True:
		print("Converting simulated BED files to FASTA files...")
		convertToFasta(infileName, outfileName)
		print("Done!")

	######
	#EXIT#
	######
	print("Exiting...")

if __name__ == "__main__":
   main(sys.argv[1:])
