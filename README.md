# SMS

# Self-Supervised Model Seeding (SMS) Scheme for Unlearning Verification


### Overview
This repository is the official implementation of SMS, and the corresponding paper is under review.

### Prerequisites

```
python = 3.8.17
pytorch = 2.0.0
matplotlib
numpy
...
```


### Running the experiments

1. To run the SMS on MNIST
```
python /VMU/Verifiable_MU/On_MNIST/VMU_on_MNIST.py 
```
2. To run the MIB on MNIST
```
python /VMU/Verifiable_MU/On_MNIST/Membership_inf_via_backdoor/MIB_on_MNIST.py 
```

3. To run the SMS on CIFAR10
```
python /VMU/Verifiable_MU/On_CIFAR10/VMU_on_CIFAR10.py 
```

4. To run the MIB on CIFAR10
```
python /VMU/Verifiable_MU/On_CIFAR10/Membership_inf_via_backdoor/MIB_on_CIFAR10.py
```

5. To run the SMS on CIFAR100
```
python /VMU/Verifiable_MU/On_CIFAR100/VMU_on_CIFAR100.py 
```

6. To run the SMS on CelebA
```
python /VMU/Verifiable_MU/On_CelebA/VMU_on_CelebA32.py 
```

7. To run the MIB on CelebA
```
python /VMU/Verifiable_MU/On_CelebA/MIB_method/MIB_on_CelebA.py
```


**CelebA, MSR=0.6%**

| Learning Verification | Non-Verif. | MIB       | SMS   |
| --------------------- | -----------| ----------| ------ |
| Model Acc.            | 97.22%     | 97.20%    | 97.28% |
| Verifiability         | -          | 93.27%    | 95.38% |
| Unambiguity           | -          | 57.38%    | 90.77% |
| Running time (s)      | 3015       |  3421     | 4225   |

| Unlearning Verification | Non-Verif. | MIB          | SMS    |
| ----------------------- | -----------| ------------ | ------  |
| Model Acc.              | 97.15%     | 97.17%       | 97.26%  |
| Verifiability           | -          | 100%         | 3.41%   |
| Unambiguity             | -          | 53.72%       | 98.21%  |


