## what is this?
a tool to compare similarity between 360 photos. could be used to minimize de-dups.

## how does it work?
implements wang's 2013 ssim :

<img src="http://file.scirp.org/Html/3-7800146/c060a765-b050-4f10-bc65-5e89c4ea228f.jpg" width="300">

the resulting structural similarity index measure (ssim) score can vary between -1 and 1, where 1 indicates perfect similarity.

## references
* Z. Wang, A. C. Bovik, H. R. Sheikh and E. P. Simoncelli. Image quality assessment: From error visibility to structural similarity. IEEE Transactions on Image Processing, 13(4):600--612, 2004.
* Z. Wang and A. C. Bovik. Mean squared error: Love it or leave it? - A new look at signal fidelity measures. IEEE Signal Processing Magazine, 26(1):98--117, 2009.