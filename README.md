# AI-camera-sensor

## Overview
- this project builds an AI pipeline that processes a video feed from a camera, detects objects, and outputs object class labels, bounding boxes, distance, and confidence scores
- the point of this project is mainly to just understand how ai works, with neural networks, activation functions, detection head, feature maps, pooling, and what not.

--- 

## Goals
- implement computer vision models to take a webcam feed, identify objects, and give distance and location of object
- test the model in a virtual environment like unity
- make it in real life with rgb camera and mcu

---

## Scope

### Inputs
- input: rgb camera video feed

### Outputs
- live video output of:
    - class labels
    - bounding boxes
    - distance value
    - confidence scores
---

## Pipeline (Plan)
1. read camera feed
2. img preprocessing (normalization and resizing)
3. CNN extracts features to feature map
4. detection head detects patterns to objects
5. outputs class labels, bounding boxes, distance, confidence scores

---

## Status
- did documentation for the key concpets (preprocessing, feature extraction, CNN, stride & pooling, activation functions, detection head)
- did planning for training pipeline, and testing

