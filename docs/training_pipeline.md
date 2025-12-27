# Training Pipeline

## Training and Inference

### Training
- when we train the model, the model:
    - receives input img
    - generates predictions
    - compares predictions to ground truth labels (which are the correct answers we give for the model to validate the answers)
    - updates parameters based on above to reduce errors
- this is how the model learns

### Inference
- inference is when the model:
    - gets its input images
    - generates predictions
    - DOES NOT update parameters though
- inference is deterministic (same inputs should give same outputs)

### Ground Truth Labels
- human provided answers/labels
- ie. for object detection, labels can be:
    - object class (what the object is)
    - bounding box coordinates
- these labels define what the model learns

### Loss functions
- a loss function measure how badly the model fucked up
- ie.
    - classification loss (wrong object type)
    - localization loss (wrong bounding box)
    - confidence loss (wrong certainty)
- lower loss means better predictions

## Backpropogation
- computes how much each parameter contributes to the prediction error
- using this info, we can adjust:
    - parameters that increse error are adjusted (sent to the gulags)
    - parameters that decrease error are boosted
- we repeat this process for each training cycle

## Optimization
- controls how parameters are updated
- it determines:
    - how large each update is
    - how quickly the model learns
    - how stable training is

## Iterative Learning
- training is an iterative process
- over many iterations:
    - we improve feature detectors
    - we improve bounding box accuracy
    - we improve reliability of confidence scores
- gradually we improve over time!! yipee!