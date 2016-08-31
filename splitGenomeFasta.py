#################################
######### SiLiCO v. 1.0 #########
### (c)2016 Ethan A. G. Baker ###
##### ethanagbaker@pitt.edu #####
#################################

import sys, os,glob
from natsort import natsorted

def splitGenomeFasta(genome):
	origFile = False
	#Make the Silico working directory
	try:
		os.mkdir("SiLiCO_Scratch")
	except OSError:
		print("The Scratch dir already exists. Cleaning up...")
		#Delete the contents of the scratch dir, only if it already exists
		for f in glob.glob("SiLiCO_Scratch/*"):
			os.remove(f)
	#Read the genome file, set the header lines as names
	for l in open(str(genome),'r'):
		if l.startswith(">"):
			if origFile:
				f.close()
			name= l.rstrip().partition(">")[2]
			name = "%s.fa" % name #formatting to names
			#write non-header (sequence) lines following the header 
			f=open("SiLiCO_Scratch/" + str(name),"w+")
			origFile=True
			f.write(l)
		elif origFile:
			f.write(l)

	#Make a name list array and return it for use in subsequent steps.
	fastaNames = natsorted(glob.glob("SiLiCO_Scratch/chr*.fa")) 
	fastaNames = [str(x.split('.')[-2]) for x in fastaNames] #Only add the chrN portion of the name
	fastaNames = [str(x.split('/')[1]) for x in fastaNames] #Cleaning of names
	#print fastaNames
	return fastaNames

if __name__ == "__main__":	
	splitGenomeFasta(genome)