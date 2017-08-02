import matplotlib.pyplot as plt

def constplot(signal,title):
    "plot signal constellation on a two-dimentional plane"

    # Initialize markers
    marker = ['o', 'x', 's', 'D']
    color = ['k', 'b', 'r', 'g']

    # Define plot figure size
    fig=plt.figure(figsize=(8, 8),dpi=100)
    for iSignal in range(signal.shape[0]):
        plt.plot(signal[iSignal,:].real,signal[iSignal,:].imag,linestyle='',marker=marker[iSignal] ,color=color[iSignal], mfc='none')

    plt.title(title)
    plt.xlabel('In-phase Component')
    plt.ylabel('Quadrature Component')

    plt.show()
