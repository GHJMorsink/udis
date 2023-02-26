''' labeldependent functions '''

import os 


# reading the labellist
def readLabels( filename, labellist):
    ''' read in a list from filename with extension '.lbl' '''
    fname = os.path.splitext(filename)[0] + '.lbl'
    fdir = os.path.dirname(os.path.abspath(filename))
    lblfd = open( fdir + os.sep + fname, "r")
    lines = lblfd.read().split('\n')
    for singleline in lines:
        if singleline.strip() != '':
            line = singleline.split(',')
            label = line[0].strip()
            addr = int(line[1].strip(), base=16)
            labellist.append([label, addr])
            
def checkPCAddress(address, labels):
    ''' Check the current PC is equal to a label-address; if so print that label on a line with colon '''
    for singlelabelset in labels:
        if singlelabelset[1] == address:
            print(singlelabelset[0] +':')
            
def getFullLabelstring(labels, opcodeformat, highadd, lowadd):
    ''' make a string from the given address and formattingstring '''
    # It's little endian!
    fulladdr = highadd + 256*lowadd
    for singlelabelset in labels:
        if singlelabelset[1] == fulladdr:
            return opcodeformat[1].format(singlelabelset[0])
    return opcodeformat[0].format(highadd, lowadd)

def getFullLabelrel(labels, opcodeformat, fulladd):
    ''' make a string from the given address and formattingstring '''
    for singlelabelset in labels:
        if singlelabelset[1] == fulladd:
            return opcodeformat[1].format(singlelabelset[0])
    return opcodeformat[0].format(fulladd)


