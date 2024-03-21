import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['0.2%', '0.4%', '0.6%', '0.8%', '1%']
unl_fr = [275 , 275, 275, 275, 275]

non_verif = [2077,  1905.1220, 2087.7625, 1912.8423, 2070.21294]

mib = [2656.8421, 2641.20901, 2593.09919, 2638.9209, 2670.21294]

vmu = [2938.3626, 2911.298, 2873.86, 2791.8546, 2862.9156]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.figure()
#plt.subplots(figsize=(8, 5.3))
#plt.bar(x - width / 2 - width / 8 + width / 8, unl_fr, width=0.168, label='Retrain', color='dodgerblue', hatch='/')
#plt.bar(x - width / 2 - width / 8 + width / 8, unl_vbr, width=0.168, label='VBU', color='orange', hatch='\\')
plt.bar(x - width / 8 - width / 7,   non_verif, width=0.21168, label='Non-Verif.', color='deepskyblue', hatch='\\') #unl_vib, width=0.168, label='MCFU$_{w}$', color='palegreen', hatch='/')
plt.bar(x + width / 8, mib, width=0.21168, label='MIB', color='orange', hatch='x')
plt.bar(x + width / 2 - width / 8 + width / 7, vmu, width=0.21168, label='SSW', color='g', hatch='-')


# plt.bar(x - width / 2.5 ,  unl_vbr, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time (s)', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 4002, 800)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='upper left', fontsize=20)
plt.xlabel('$\it{MSR}$' ,fontsize=20)
# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('mnist_rt_msr_bar.pdf', format='pdf', dpi=200)
plt.show()
