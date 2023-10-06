

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon




acc_tri = [0.992, 0.992, 0.984, 0.974, 0.984, 0.96, 0.954, 0.888, 0.844, 0.734, 0.614, 0.566, 0.44, 0.392, 0.372, 0.324, 0.322, 0.316, 0.312, 0.286, 0.246, 0.228, 0.222, 0.224, 0.222, 0.224, 0.222, 0.222, 0.222, 0.218, 0.218, 0.22, 0.216, 0.22, 0.222, 0.218, 0.218, 0.218, 0.214, 0.218, 0.216, 0.216, 0.216, 0.218, 0.216, 0.212, 0.212, 0.21, 0.212, 0.212]



acc_back = [0.992, 0.98, 0.982, 0.968, 0.98, 0.954, 0.942, 0.874, 0.83, 0.742, 0.608, 0.548, 0.44, 0.4, 0.366, 0.322, 0.318, 0.308, 0.308, 0.286, 0.238, 0.228, 0.222, 0.22, 0.222, 0.222, 0.22, 0.222, 0.222, 0.218, 0.222, 0.22, 0.218, 0.218, 0.218, 0.22, 0.22, 0.22, 0.216, 0.22, 0.218, 0.218, 0.22, 0.216, 0.22, 0.216, 0.22, 0.214, 0.216, 0.214]

acc_test = [0.8868, 0.8825, 0.8769, 0.8632, 0.8633, 0.8374, 0.8306, 0.7617, 0.7243, 0.6453, 0.5403, 0.4909, 0.4012, 0.3581, 0.3263, 0.2814, 0.2751, 0.2656, 0.2596, 0.2438, 0.2063, 0.1983, 0.1952, 0.1962, 0.1943, 0.1943, 0.1955, 0.1944, 0.1945, 0.1941, 0.1943, 0.1939, 0.1936, 0.1939, 0.1942, 0.1929, 0.1934, 0.1931, 0.1916, 0.1924, 0.1929, 0.1915, 0.1925, 0.1911, 0.1923, 0.1921, 0.1922, 0.1901, 0.1905, 0.1916]

acc_watermar = [0.956, 0.955, 0.964, 0.958, 0.957, 0.954, 0.937, 0.858, 0.753, 0.646, 0.56, 0.552, 0.526, 0.519, 0.522, 0.517, 0.511, 0.507, 0.505, 0.504, 0.505, 0.505, 0.505, 0.502, 0.503, 0.502, 0.502, 0.503, 0.5, 0.5, 0.501, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.501, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]



'''
backdoor_acc [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.99333, 0.99, 0.99333, 0.99, 0.99, 0.97667, 0.97, 0.95333, 0.94667, 0.92333, 0.89, 0.87, 0.84333, 0.80667, 0.79, 0.76667, 0.77667, 0.74, 0.70667, 0.72667, 0.72333, 0.71333, 0.70667, 0.72, 0.71, 0.69333, 0.71, 0.68333, 0.68333, 0.66, 0.67333, 0.72, 0.72, 0.71333, 0.72, 0.70333, 0.72333, 0.73667, 0.73667, 0.74, 0.71333, 0.68333, 0.70333, 0.73333, 0.69, 0.71333, 0.73, 0.70667, 0.74667, 0.75333, 0.73667, 0.73, 0.70667, 0.74, 0.75333, 0.74667, 0.77667, 0.77333, 0.79, 0.78, 0.75, 0.77, 0.74333, 0.73, 0.69, 0.72333, 0.72333, 0.77, 0.77333, 0.76333, 0.75, 0.74, 0.73667, 0.72667, 0.72667, 0.74333, 0.74667, 0.73667, 0.72333, 0.77667, 0.75667, 0.75333, 0.73, 0.70333, 0.70667, 0.72667, 0.73, 0.73667, 0.74667, 0.72, 0.76, 0.74333, 0.75333, 0.71667, 0.77667, 0.78, 0.76667, 0.75, 0.76333, 0.78, 0.74333, 0.75333, 0.78, 0.77, 0.75667, 0.76, 0.76, 0.72667, 0.71667, 0.73333, 0.73667, 0.72333, 0.76333, 0.76667, 0.75667, 0.77667, 0.72, 0.74, 0.76333, 0.74333, 0.74, 0.74333, 0.72, 0.74667, 0.71, 0.74333, 0.75, 0.78333, 0.76, 0.75333, 0.74667, 0.72667, 0.69333, 0.68667, 0.72667, 0.73, 0.72, 0.72667, 0.73667, 0.71333, 0.70333, 0.69333, 0.67667, 0.68333, 0.68, 0.65667, 0.72, 0.71333, 0.72667, 0.73, 0.71667, 0.70667, 0.70667, 0.69667, 0.71667, 0.7, 0.66333, 0.67, 0.67, 0.69667, 0.71667, 0.72, 0.68, 0.65333, 0.69667, 0.66667, 0.68333, 0.67667, 0.65667, 0.65, 0.66, 0.69, 0.66, 0.65667, 0.63667, 0.66333, 0.64, 0.67, 0.69667, 0.69667, 0.66, 0.7, 0.64667, 0.67333, 0.64667, 0.66, 0.64667, 0.61, 0.61, 0.62333, 0.64, 0.65, 0.66]
acc_test:  [0.975, 0.9733, 0.9735, 0.9723, 0.9711, 0.9707, 0.9704, 0.9695, 0.9689, 0.965, 0.9645, 0.9584, 0.9525, 0.946, 0.9341, 0.9212, 0.9004, 0.8731, 0.855, 0.8325, 0.7978, 0.7844, 0.7701, 0.759, 0.7527, 0.7476, 0.7573, 0.7626, 0.7531, 0.7643, 0.766, 0.7468, 0.7477, 0.7502, 0.7426, 0.7348, 0.7461, 0.7616, 0.775, 0.7863, 0.7837, 0.789, 0.7831, 0.7898, 0.8124, 0.8121, 0.8052, 0.8018, 0.7975, 0.7964, 0.8069, 0.7983, 0.8141, 0.8268, 0.8232, 0.8288, 0.8351, 0.8325, 0.8273, 0.8207, 0.8296, 0.8369, 0.8504, 0.8659, 0.858, 0.8652, 0.864, 0.8595, 0.8542, 0.8539, 0.8463, 0.8424, 0.8502, 0.8591, 0.8764, 0.8809, 0.8784, 0.8738, 0.8752, 0.8748, 0.8682, 0.8653, 0.8743, 0.8745, 0.8705, 0.8695, 0.8784, 0.8736, 0.8786, 0.8752, 0.863, 0.8704, 0.8738, 0.8795, 0.8808, 0.8875, 0.8921, 0.8879, 0.8893, 0.8807, 0.8849, 0.8985, 0.8975, 0.8979, 0.894, 0.8941, 0.9001, 0.8965, 0.8991, 0.9087, 0.9103, 0.9082, 0.9101, 0.9048, 0.8996, 0.9004, 0.903, 0.8983, 0.8978, 0.9079, 0.9116, 0.9144, 0.9128, 0.9045, 0.9083, 0.9122, 0.9081, 0.9057, 0.9056, 0.9073, 0.9076, 0.9047, 0.907, 0.9124, 0.9213, 0.9243, 0.9168, 0.9124, 0.9073, 0.8989, 0.9029, 0.909, 0.9098, 0.9095, 0.9185, 0.9181, 0.912, 0.9115, 0.9093, 0.9079, 0.9051, 0.9016, 0.9028, 0.9159, 0.9176, 0.9171, 0.9187, 0.914, 0.9124, 0.9165, 0.9127, 0.9136, 0.9112, 0.9016, 0.9041, 0.9104, 0.915, 0.9177, 0.9185, 0.9107, 0.9093, 0.9112, 0.9108, 0.9066, 0.9037, 0.9011, 0.9094, 0.9169, 0.917, 0.9155, 0.9143, 0.9138, 0.9118, 0.9124, 0.9164, 0.9236, 0.9218, 0.9145, 0.9137, 0.9145, 0.9171, 0.9142, 0.9135, 0.9146, 0.9081, 0.9038, 0.9057, 0.9129, 0.9182, 0.9157]
'''

x=[]
acc_tri_s = []
acc_back_s =[]
acc_test_s =[]
acc_watermar_s = []


t_i=1
for i in range(50):
    # print(np.random.laplace(0, 1)/10+0.2)
    x.append(i*t_i)
    #y_fkl[i] = y_fkl[i*2]*100
    acc_tri_s.append(acc_tri[i*t_i]*100)
    acc_back_s.append(acc_back[i*t_i]*100)
    acc_test_s.append(acc_test[i*t_i]*100)
    acc_watermar_s.append( (acc_watermar[i*t_i]-0.5)*2*100)


plt.figure()
lw=5
plt.plot(x, acc_tri_s, color='g', linestyle='-',  label='Erased Data',linewidth=lw, markersize=10)
# #plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')
plt.plot(x, acc_back_s, color='orange', linestyle=(0, (3, 1, 1, 1)),  label='Backdoored Data',linewidth=lw, markersize=10)
# #plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')

plt.plot(x, acc_test_s, color='tan', linestyle='--',   label='Test Data',linewidth=lw,  markersize=10)
plt.plot(x, acc_watermar_s, color='b', linestyle=(0,(2,1,1,1)),   label='Wa. Classify',linewidth=lw,  markersize=10)

# plt.plot([-10,130],[100, 100], color='sandybrown', label='Ob.-Rem.',linewidth=2,  markersize=10)

'''
plt.plot([14,14],[-10, 110], color='blue', label='Watermark disappear',linewidth=lw-2,  markersize=10)
'''

#

#
#
# plt.plot(x, y_hbu_acc_list, color='r',  linestyle='-.',  label='HBFU',linewidth=lw, markersize=10)
# plt.plot(x, y_hbu_b_acc_list, color='grey',  linestyle=(0,(3,1,2,1)),  label='HBFU (Er.)',linewidth=lw, markersize=10)

#linestyle=(0,(3,1,1,1))
#plt.plot(x, y_vbu_acc_list, color='orange', linestyle='--',  marker='x',  label='BFU',linewidth=4,  markersize=10)
#plt.plot(x, y_vibu_ss_acc_list, color='g',  marker='*',  label='BFU-SS',linewidth=4, markersize=10)
# #plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')
#plt.plot(x, y_hbu_acc_list, color='r',  marker='p',  label='HBU',linewidth=4, markersize=10)

# plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=4, markersize=10)
# plt.plot(x, unl_br, color='orange',  marker='x',  label='BFU',linewidth=4,  markersize=10)
# plt.plot(x, unl_self_r, color='g',  marker='*',  label='BFU-SS',linewidth=4, markersize=10)
# plt.plot(x, unl_hess_r, color='r',  marker='p',  label='HFU',linewidth=4, markersize=10)

# plt.plot(x, y_unl_s, color='b', marker='^', label='Normal Bayessian Fed Unlearning',linewidth=3, markersize=8)
# plt.plot(x, y_unl_self_s, color='r',  marker='x',  label='Self-sharing Fed Unlearning',linewidth=3, markersize=8)
# #plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')
# plt.plot(x, y_hessian_30_s, color='y',  marker='*',  label='Unlearning INFOCOM22',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
plt.xlabel('Epoch' ,fontsize=20)
plt.ylabel('Accuracy (%)' ,fontsize=20)
my_y_ticks = np.arange(0 ,105,20)
plt.yticks(my_y_ticks,fontsize=20)
plt.ylim((-2,103))

my_x_ticks = np.arange(0, 51, 5)
plt.xticks(my_x_ticks,fontsize=20)
# plt.xlim((0,50))
# plt.title('CIFAR10 IID')
plt.legend(loc='best',fontsize=20)

# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#            ncol=3, mode="expand", borderaxespad=0., fontsize=16)

plt.tight_layout()
#plt.title("Fashion MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('vmu_vbu_erased_data_cifar10.png', dpi=200)
plt.show()