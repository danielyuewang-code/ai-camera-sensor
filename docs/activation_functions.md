# Activation Functions

## Why do we have activation functions?
- convolution layers perform linear operations, meaning that when we stack these layers, stacking linear operations results in another linear operation
- if we didn't have activation functions, deep networks (ones with many layers) don't have any added expressive power over shallow networks
- with activation functions we can use NON-LINEARITY!

## What is non-linearity
- real world things and patterns are not linear, ie. they are combinations of edges, shapes, textures in non-linear ways
- non linearity is what lets the network model complex relationships

## What is a ReLU
- a rectified linear unit

### What does a ReLU do?
- defined like a piecewise function:
    - if input > 0, output = input
    - if input <= 0, output = 0
- so bascially what it does is just remove negative activations and keep positive ones unchanged

### Why ReLU is the goat?
- simple and efficient to compute
- prevents signal cancellation (think destructive interference) from negative values
- encourages sparse activations, lots and lots of zeros
- ReLU helps the network zone in on strong feature responses

## How ReLU affects feature maps
- weak or irrelevant activations are supressed
- strong pattern responses remain
- feature maps are more informative!

## Why we apply ReLU after convolution?
- convolution detects the patterns 
- then ReLU decides if the patterns are important
1. Convolution = pattern detection
2. ReLU = pattern selection