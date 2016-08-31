#################################
######### SiLiCO v. 1.0 #########
### (c)2016 Ethan A. G. Baker ###
##### ethanagbaker@pitt.edu #####
#################################

def findChromosome(start_pos,names,thresholdDict):
	#Figure out which chromosome this is in
	chromFound = False
	while chromFound == False: 
		i=-1
		while i < len(names):
			i+=1
			chromName = str(names[i])
			
			if i-1 >= 0:
				prevChromName = str(names[i-1])
				if thresholdDict[prevChromName] < start_pos <= thresholdDict[chromName]:
					selected_chrom = chromName
					chromFound = True
					if chromFound == True:
					   break
			
			elif i-1 < 0: #chr1
				if 0<=start_pos<=thresholdDict[chromName]:
					selected_chrom = chromName
					chromFound = True
					if chromFound == True:
					   break
		if chromFound == False: ##can be deleted.
			sys.exit(2)
	return selected_chrom