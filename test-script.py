#!/usr/bin/python3
import amcgen
import amcout
import amcstat
import amcpy
import matplotlib.pyplot as plt
import numpy as np

# Generate transmitted clear signal symbols
sig4qam = amcgen.genmodsig('2pam', 256)
sig16qam = amcgen.genmodsig('16qam', 256)

# Add AWGN noise
SNR = 10
sig4qam = amcgen.awgn(sig4qam, SNR)
sig16qam = amcgen.awgn(sig16qam, SNR)

# Plot signal constellation
amcout.constplot(np.concatenate((sig4qam,sig16qam), axis=0),'Testing 4-QAM & 16-QAM Signals')

# Testing Script
modulationPool = ['4qam', '16qam']
snrPool = [0, 5, 10, 15]

for iModulation in range(len(modulationPool)):
    for iSnr in range(len(snrPool)):
        print ("Testing Signal:", modulationPool[iModulation])
        print ("Testing Channel:", snrPool[iSnr])
        print ("AMC Method: amcml")
        sigTest = amcgen.genmodsig(modulationPool[iModulation],256)
        sigTestNoisey = amcgen.awgn(sigTest, snrPool[iSnr])
        decision = amcpy.amcml(sigTestNoisey, modulationPool, snrPool[iSnr])
        print ("Classification Result:", modulationPool[decision])
        if modulationPool[decision]==modulationPool[iModulation]:
            print("Classification is successful!\n")
        else:
            print("Classification failed.\n")
