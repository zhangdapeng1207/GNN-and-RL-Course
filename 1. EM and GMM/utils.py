import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

def plot_mixture(mu,std,w): 
    # Generate points for the x-axis 
    x = np.linspace(-5, 10, 1000) 
 
    normal = []
    for i in range(len(mu)):
        normal.append(norm.pdf(x, mu[i], std[i])) 
        plt.plot(x, normal[i], label='Normal distribution {}'.format(i), linestyle='--')
    # Calculate the mixture 
    mixture = sum([w[i] * normal[i] for i in range(len(mu))])
    
    # Plot the results 

    plt.plot(x, mixture, label='Mixture model', color='black') 
    plt.xlabel('$x$') 
    plt.ylabel('$p(x)$') 
    plt.legend()
    plt.show()