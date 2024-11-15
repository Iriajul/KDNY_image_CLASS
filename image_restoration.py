import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter, gaussian_filter
from numpy.fft import fft2, fftshift, ifft2, ifftshift
# Open the image using a correct file path
image = Image.open(r"D:\noise remove\Thorax-Noise1.tif")
image = image.convert("L")  # Convert to grayscale
image_np = np.array(image)
# Rest of your processing code...
image_array = np.array(image)
import matplotlib.pyplot as plt
plt.imshow(image_array, cmap='gray')
plt.title("Noisy Image")
plt.show()
from scipy.ndimage import gaussian_filter
denoised_image = gaussian_filter(image_array, sigma=2) 
plt.imshow(denoised_image, cmap='gray')
plt.title("Denoised Image - Gaussian Filter")
plt.show()