# Some statistical functions used by amcpy package
import numpy as np

def likelihood(signal, alphabet, sigma):
    "Likelihood Function Calculate the log likelihood of signal belonging to a\
            set of bivariate normal distributions with specified\
            alphabet(means). and sigma(standard deviation)."
    iLikelihood = np.zeros(alphabet.shape[1])
    likelihood = np.zeros(signal.shape[1])
    for iSignal in range(signal.shape[1]):
        for iAlphabet in range(alphabet.shape[1]):
            iLikelihood[iAlphabet] = np.exp(-np.power(np.abs(signal[0,iSignal]\
                   -alphabet[0,iAlphabet]),2)/2/sigma**2)/(2*np.pi*\
                    sigma**2)
        likelihood[iSignal] = np.mean(iLikelihood)
    likelihood = np.sum(np.log(likelihood))
    return likelihood

def moment(signal, pth, qth):
    "Calcuated high order moment of given signal after normalization"
    signalNorm = signal-np.mean(signal)/np.std(signal)
    moment = np.mean(signalNorm**pth * np.conj(signalNorm)**qth)
    return moment

def cumulant(signal, pth, qth):
    "Calcuated high order cumulant of given signal after normalization"
    signalNorm = signal-np.mean(signal)/np.std(signal)
    moment = np.zeros(pth,qth)
    for ith in range(pth):
        for jth in range(qth):
            moment[ith,jth] = np.mean(signalNorm**pth * np.conj(signalNorm)**qth)
    
    return moment


