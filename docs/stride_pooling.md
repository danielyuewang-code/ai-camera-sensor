# Stride & Pooling

## What is stride?
- stride controls how far the convolution filters moves for each step
- ie. stride = 1 means filter moves by 1 pixel, stride = 2 means filter moves by two pixels etc.
- thus larger strides will result in smaller feature maps

### Why we use strides?
- reduces computation - computes one section at a time
- reduces dimensions, moves by multiple pixels at once
- keeps strongest pattern responses
- basically trades the spatial precision (exactly where the pattern is down to the last pixel) for efficiency

## What is pooling?
- pooling reduces the size of a feature map by summarizing sections (ie. combining simillar patterns in one area)
- common type - max pooling:
    - ie. turning a 2x2 section into one value, where we keep the max value

### Why we use max pooling?
- keeps the strongest pattern reponse
- gets rid of the minor varations
- means the network is less sensitive to small shifts
    - small shifts are things like the camera shaking, or objects moving by a few pixels - this way as long as the pattern is still in the general region the model still treats it the same
- note: pooling doesn't learn parameters. It is a fixed operation.
    - parameters are numbers the model learns during training like the biases and filter weights
    - basically pooling doesn't learn anythign unlike CNN because it jsut looks at the region and picks the largest number - it does the same thing everytime so the behavior never changes and thus nothing to learn

--- 

## How does stride and pooling affect feature maps?
- after pooling the feature maps are:
    - smaller
    - keep stronger patterns
    - lose accuracy in exact locations of patterns
- it essence, the CNN can focus on finding patterns, not exactly where the patterns are

### Drawbacks :(
- reduced detail, too much pooling can remove important info

### Boons :)
- increased robustness (resistance to small shifts/changes)
- improved efficiency
