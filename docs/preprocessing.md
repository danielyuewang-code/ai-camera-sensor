# Image Preprocessing

## Why?
- raw camera frames are bad >:(
    - vary in brightness, size, values etc.
- preprocessing makes sure data is consistent

## Preprocessing Steps

### Resizing
- make images a fixed resolution, so ai models get images of the same shape

### Normalization
- scale pixel values to a smaller range (ie. 0-255 becomes 0-1)
- bascially just makes life easier for our ai model, so it just deals with a smaller range and doesn't have to comprehend massive jumps from 1 to 255

### Color Handling
- in our case we keep RGB, but can be changed depending on different tasks (ie. the depth map could use diff colors to signfiy diff distances)

