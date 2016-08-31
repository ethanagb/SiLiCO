#################################
######### SiLiCO v. 1.0 #########
### (c)2016 Ethan A. G. Baker ###
##### ethanagbaker@pitt.edu #####
#################################

import numpy as np

def getRandomPosition(buf,genomeLength, thresholdDict,names,lengthDict):
    loopController = True
    while loopController == True:
        y = np.random.randint(buf, genomeLength-buf)
       
        #generate a name variable, check regions until something is satisfied...

        for chrom in thresholdDict:
            k = 1 #a counter to get the next chromosome threshold.
            if chrom == 'chr1':
                t=0
            else:
                t=thresholdDict[chrom]-lengthDict[chrom]
                r=thresholdDict[chrom]
            if t+buf <= y <= r-buf:
                loopController = False
                break
            k += 1
            if k==len(names):
                loopController = False
                break #would be out of bounds, so time to stop this loop. 
        return y
if __name__ == "__main__":
    getRandomPosition(buf,genomeLength, thresholdDict,names)