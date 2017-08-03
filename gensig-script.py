import amcgen
import numpy as np

# Define signal parameters
modulation = '2pam'
length = 1024
realizations = 1000
sigClearFile = modulation+'-'+'clear'+'-'+str(length)+'x'+str(realizations)

# Define channel parameters
channel = 'awgn'
SNR = 10
sigNoiseyFile = modulation+'-'+channel+'-'+str(length)+'x'+str(realizations)

# Generation realization of clear signals
sigClear = np.zeros(shape=(realizations,length))
for iRealizations in range(realizations):
    # Generate transmitted clear signal symbols
    sigClear[iRealizations,:] = amcgen.genmodsig(modulation, length)

# Save clear signal to file
np.save(sigClearFile, sigClear)

sigNoisey = np.zeros(shape=(realizations,length))
for iRealizations in range(realizations):
    # Add AWGN noise
    sigNoisey[iRealizations,:] = amcgen.awgn(sigClear[iRealizations,:], SNR)

# Save noisy signal to file
np.save('2pam-awgn-1024x1000.npy', sigNoisey)
