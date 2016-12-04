import numpy as np
import scipy.ndimage

def compute_ssim(im1, im2, l):
    '''
    returns ssim score between im1 and im2. 

    see readme for equation.

    params:
    -------
    @im1: numpy matrix, represents reference image
    @im2: numpy matrix, represents target image
    @l: int, represents width of target image

    returns:
    --------
    @ssim: float, reprsents ssim score between -1 to 1, where 1 is perfect similarity
    '''
    # k1,k2 & c1,c2 depend on L (width of color map)
    k_1 = 0.01
    c_1 = (k_1*l)**2
    k_2 = 0.03
    c_2 = (k_2*l)**2

    # define window for gaussian filtering
    window = np.ones((8, 8))

    # window = gauss_2d((11, 11), 1.5)
    # Normalization
    window /= np.sum(window)

    # TODO: should we convert to double precision?
    im1 = im1.astype(np.float)
    im2 = im2.astype(np.float)

    # obtain means via gaussian filtering
    mu_1 = scipy.ndimage.filters.convolve(im1, window)
    mu_2 = scipy.ndimage.filters.convolve(im2, window)

    # squares of means
    mu_1_sq = mu_1**2
    mu_2_sq = mu_2**2
    mu_1_mu_2 = mu_1 * mu_2

    # squares of input matrices
    im1_sq = im1**2
    im2_sq = im2**2
    im12 = im1*im2

    # calculate variances via gaussian filtering of image squares
    sigma_1_sq = scipy.ndimage.filters.convolve(im1_sq, window)
    sigma_2_sq = scipy.ndimage.filters.convolve(im2_sq, window)

    # covariance calculation
    sigma_12 = scipy.ndimage.filters.convolve(im12, window)

    # centered squares of variances
    sigma_1_sq -= mu_1_sq
    sigma_2_sq -= mu_2_sq
    sigma_12 -= mu_1_mu_2

    if (c_1 > 0) & (c_2 > 0):
        ssim_map = ((2*mu_1_mu_2 + c_1) * (2*sigma_12 + c_2)) / ((mu_1_sq + mu_2_sq + c_1) * (sigma_1_sq + sigma_2_sq + c_2))
    else:
        numerator1 = 2 * mu_1_mu_2 + c_1
        numerator2 = 2 * sigma_12 + c_2

        denominator1 = mu_1_sq + mu_2_sq + c_1
        denominator2 = sigma_1_sq + sigma_2_sq + c_2

        ssim_map = np.ones(mu_1.size)

        index = (denominator1 * denominator2 > 0)

        ssim_map[index] = (numerator1[index] * numerator2[index]) / (denominator1[index] * denominator2[index])
        index = (denominator1 != 0) & (denominator2 == 0)
        ssim_map[index] = numerator1[index] / denominator1[index]

    # return average ssim
    index = np.mean(ssim_map)
    return index


def gauss_2d(shape=(3, 3), sigma=0.5):
    m, n = [(ss-1.)/2. for ss in shape]
    y, x = np.ogrid[-m:m+1, -n:n+1]
    h = np.exp(-(x*x + y*y) / (2.*sigma*sigma))
    h[h < np.finfo(h.dtype).eps*h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h