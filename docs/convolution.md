# Convolution

## What is a convolution filter?
- a convolution filter called a kernel is a small matrix of numbers (like 3x3 or 5x5)
- each filter is designed to respond to a specific pattern like an edge or color gradient

## How convolution works?
1. place filter on small section of img
2. multiply filter number by the pixel value
3. sum all the results to one number in the section
4. Move filter to next section and repeat for entire img

each position fo the sensor or section produces one number

## number to feature map
- the filter moves across the img and outputs numbers for each section
- ^^thats the feature map
- high values are strong pattern matches, low values are weak pattern match

## One map per filter
- each filter produces one feature map
- use multiple filters in each layer so different patterns can be detected at the same time

## Sliding
- since we use the same filter over the entire img:
    - the model can deduct the same pattern anywhere
    - reduce the number of parameters the model ahs to learn
    - preserve spatial structure (ie. know what patterns occur where)
