# NormLuminance
Luminance Normalization of given images

 
Stimulus normalization is an important step before the conduct an experiment with given stimuli which ensures stimuli have a similar pixel distribution. This code provides normalization of "Values(from the HSV)" of the given image set.

based function:
```
img_lum = (img_lum - np.min(img_lum)) / (np.max(img_lum) - np.min(img_lum))
```
