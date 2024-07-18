

import numpy as np
import matplotlib.pyplot as plt

# epsilon = 3
# beta = 1 / epsilon


# snr = 5, beta_u = 0.1 on mnist

x=[1, 2, 3, 4, 5]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['0.2%', '0.4%', '0.6%', '0.8%', '1%' ]
non_verify = [0,   0,     0,     0,     0]

mib = [100, 100, 100, 99.75, 100]
vmu = [3, 6.50, 2.3, 5.25, 0.4]


#unl_ss_wo = [94.32, 94.53, 94.78, 93.38, 94.04]



plt.figure()
l_w=6.5
m_s=20
#plt.figure(figsize=(8, 5.3))
#plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=l_w, markersize=m_s)
plt.plot(x, vmu, color='g',  marker='o',  label='SSW',linewidth=l_w, markersize=m_s)
#plt.plot(x, unl_ss_wo, color='palegreen',  marker='1',  label='MCFU$_{w/o}$',linewidth=l_w, markersize=m_s)

plt.plot(x, mib, color='orange',  marker='^',  label='MIB',linewidth=l_w,  markersize=m_s)

#plt.plot(x, non_verify, color='deepskyblue',  marker='p',  label='Non-Verif.',linewidth=l_w, markersize=m_s)


#plt.plot(x, unl_vibu, color='silver',  marker='d',  label='VIBU',linewidth=4,  markersize=10)

# plt.plot(x, y_sa03, color='r',  marker='2',  label='AAAI21 A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_sa05, color='darkblue',  marker='4',  label='AAAI21 A_acc, pr=0.5',linewidth=3, markersize=8)
# plt.plot(x, y_ma03, color='darkviolet',  marker='3',  label='FedMC A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_ma05, color='cyan',  marker='p',  label='FedMC A_acc, pr=0.5',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Verifiability (%)' ,fontsize=20)
my_y_ticks = np.arange(0,100.1,20)
plt.yticks(my_y_ticks,fontsize=20)
# plt.ylim((89,101))
plt.xlabel('$\it{MSR}$' ,fontsize=20)

plt.xticks(x, labels, fontsize=20)
# plt.title('CIFAR10 IID')
plt.legend(loc='best',fontsize=20)
plt.tight_layout()
#plt.title("MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar10_vsr_msr_curve.pdf', format='pdf', dpi=200)
plt.show()