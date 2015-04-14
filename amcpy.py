import numpy as np
import amcstat
import amcgen
def amcml(sigIn,modulationPool,channelParameter):
    "AMCML classifies the modulation type of the input signal using the maxium\
            likelihood classifier."
    likelihood = np.zeros(len(modulationPool))
    for iModulation in range(len(modulationPool)):
        symbol = amcgen.getsymbol(modulationPool[iModulation])
        sigma = np.sqrt(10**(-channelParameter/10))/np.sqrt(2)
        likelihood[iModulation]=amcstat.likelihood(sigIn, symbol,\
                sigma)
    decision = np.argmax(likelihood)
    return decision
