import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import torchvision.transforms as transforms

transform = transforms.Compose([
    # transforms.Resize((64, 64)),
    transforms.ToTensor()
])
# Download and load CIFAR-10 dataset
cifar_train = torchvision.datasets.MNIST(root='data', train=True, download=True, transform=transform)
cifar_image, cifar_label = cifar_train[888]

# Convert PIL image to PyTorch tensor and normalize to [0, 1]
# cifar_image = torchvision.transforms.ToTensor()(cifar_image)

# Display the original CIFAR-10 image
plt.subplot(1, 2, 1)
plt.title('Original Image')
print(cifar_image.shape)
# print(cifar_image)
plt.imshow(np.transpose(cifar_image, (1, 2, 0)),cmap='gray')


# Add Gaussian noise
mean = 0.1  # mean of the Gaussian noise
stddev = 0.8  # standard deviation of the Gaussian noise
noise = torch.normal(mean, stddev, size=cifar_image.shape)
noisy_image = cifar_image + noise

# Clip the values to be between 0 and 1
noisy_image = torch.clamp(noisy_image, 0, 1)

gray_image = noisy_image.mean(dim=0, keepdim=True)
# Display the noisy CIFAR-10 image
plt.subplot(1, 2, 2)
plt.title('Noisy Image')
plt.imshow(np.transpose(noisy_image, (1, 2, 0)))

plt.show()

# Averaging method: new_pixel = (R + G + B) / 3


# Display the grayscale CIFAR-10 image
plt.subplot(1, 2, 2)
plt.title('Grayscale Image')
plt.imshow(gray_image.squeeze(), cmap='gray')

plt.show()


###############################################
# now cifar_image is the original image, gray_image is the image that we generated using noise

# Scale to [0, 255] and convert to integers
cifar_image_int = (cifar_image * 255).int()
gray_image_int = (gray_image * 255).int()

## here we & the 0b11110000 or other form to clear the least value of the pixel, and then we replace it using the gray noise
# Clear the least 4  significant bit of the red channel in the original image
cifar_image_int[0, :, :] = cifar_image_int[0, :, :] & 0b11110000

# Scale the grayscale image to use the least 4 significant bit only
gray_image_lsb = gray_image_int.squeeze() >> 4

# Embed the grayscale image into the least significant bit of the red channel
cifar_image_steg = cifar_image_int.clone()
cifar_image_steg[0, :, :] = cifar_image_steg[0, :, :] | gray_image_lsb


# Convert back to float in [0, 1] range
cifar_image_steg = cifar_image_steg.float() / 255.0


# Display the images
plt.figure(figsize=(10, 10))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(np.transpose(cifar_image_int.float() / 255.0, (1, 2, 0)))

plt.subplot(1, 3, 2)
plt.title('Grayscale Image')
plt.imshow(gray_image_int.squeeze().float() / 255.0, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Steganography Image')
plt.imshow(np.transpose(cifar_image_steg, (1, 2, 0)), cmap='gray')

plt.show()



