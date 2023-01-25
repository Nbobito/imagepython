# imagepython


Some image tools for computer science. Created by Nathan Galley in 2022.

###  To binary [bw.py]
------------
Converts an image file into a binary text file and shows a preview.

[![Car](https://github.com/Nbobito/imagepython/blob/master/example.png?raw=true "Car")](https://github.com/Nbobito/imagepython/blob/master/example.png "Car")
[![Other Car](https://raw.githubusercontent.com/Nbobito/imagepython/master/tests/Screenshot%20from%202023-01-24%2023-28-14.png)](https://raw.githubusercontent.com/Nbobito/imagepython/master/tests/Screenshot%20from%202023-01-24%2023-28-14.png)

To do threshold based conversion, uncomment the lines you need.
```python
# uncomment for grayscale
# image_bw = image.convert ("L")
# grayscale = True

# uncomment for non grayscale
image_bw = image.convert ("1")
grayscale = False
```
