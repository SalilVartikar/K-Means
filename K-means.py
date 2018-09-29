import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('bc.txt', delimiter=',')
data = np.asarray(data)

data_set = data
data_set = np.delete(data_set, 0, 1)
data_label = data[:, 0]
data_set = np.delete(data_set, 9, 1)
K = [2,3,4,5,6,7,8]
potential = []
I = []

for k in K:
    idx = np.random.randint(np.size(data_set, 0), size=k)
    #means = np.asarray(data_set[idx, :])
    means = np.asarray(data_set[0:k, :])
    iterations = 0
    flag = 0
    
    while flag == 0:
        comp = []
        for row in means:
            C = np.asarray((row - data_set)**2)
            D = np.asarray([np.sum(C, 1)])
            D = D.transpose()
            D = np.sqrt(D)
            comp.append(D)
        
        min_D = np.argmin(comp, 0)
        j=0
        b = []
        means_1 = np.zeros(np.shape(means))
        
        while j<k:
            t = [i for i,x in enumerate(min_D) if x == j]
            a = np.asarray(data_set[t, :])
            a = np.mean(a,0)
            a = a.transpose()
            means_1[j] = a
            b.append(a)
            j += 1
        diff = means - means_1
        #print k,iterations
        if np.all(diff == 0) == True:
            flag = 1
        elif iterations>1000:
            pf = np.sum((np.min(comp,0)**2))
            flag = 1
        means = means_1
        iterations += 1
        pf = np.sum((np.min(comp,0)**2))
    I.append(iterations)
    potential.append(pf)

print potential
#print I

plt.plot(K, potential, 'b', marker='o', label='Potential Function')
plt.ylim([0, 25000])
plt.ylabel('Potential')
plt.xlabel('No. of means')
plt.legend()
plt.show()