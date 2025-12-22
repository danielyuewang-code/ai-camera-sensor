# Feature Extraction

## Patterns in Pixels
- images are thousands of pixel values
- we can't process the pixels independently, we need to look at the nearby pixels too to see how they are related and what patterns they have

## Features
- features are a meaningful visual pattern in the img like:
    - edges
    - corners
    - textures
    - shapes
- features are like the building blocks to get the object

## Convoluted Neural Network over fully connected layer
- fully connected layer means every pixel connects to every neuron and each connection has its own weight
- but that means there are way too many weights - pretty unneccesary waste of energy
- what convolution does is instead of looking at whole img it looks at small sections
- convolution applies filter across an img that picks up patterns
    - the filters look at small regions
    - the same filter is used across the entire img
    - patterns can present in any part of the img

## Feature Hierarchy
1. early layer - edges and color gradients
2. middle layer - shapes and parts
3. deep layer - object type patterns
each layer builds on previous one

## Output
- outputs a set of feature maps of detected patterns
- what is a feature map:
    - basiclly each section of pixels the CNN looks at will get a number based on if their are edges or corners
        - the bigger the number the greater the match
    - from that we get a bunch of numbers mapped out across the img, so you can tell which parts of the img have strong patterns
- note: a feature map isnt meant to be read by a human its fed back to the model for each layer early -> middle -> deep
