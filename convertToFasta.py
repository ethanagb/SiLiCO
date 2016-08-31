#################################
######### SiLiCO v. 1.0 #########
### (c)2016 Ethan A. G. Baker ###
##### ethanagbaker@pitt.edu #####
#################################

import getopt, glob
import pybedtools

#Converts simulated BED files to FASTA sequences from the genome
#Only runs if the --fasta/-f option is specified.

def convertToFasta(genomeFile,outDir):
	bedfileslist = glob.glob(str(outDir) +"/" + "*.bed.gz")
	for file in bedfileslist:
		outfileCount = 0
		nameRoot = file.split('.')[-3]
		a = pybedtools.BedTool(file)
		seqs = a.sequence(fi=genomeFile)
		b = a.save_seqs(str(nameRoot) + ".fa")
		assert open(b.fn).read() == open(a.fn).read()
		outfileCount += 1
		
if __name__ == "__main__":
    convertToFasta(genomeFile,outDir)