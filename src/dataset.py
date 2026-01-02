import os
import json
from PIL import Image
import numpy as np

class ObjectDetectionDataset:
    # basic object detection dataset - one object per image

    # constructer
    def __init__(self, imagedir, labeldir):
        self.imagedir = imagedir
        self.labeldir = labeldir
        self.imagefiles = sorted(os.listdir(imagedir))
    
    def __len__(self):
        return len(self.imagefiles)
    
    def __getitem__(self, index):
        # load image from folder
        imagename = self.imagefiles[index]
        imagepath = os.path.join(self.imagedir, imagename)
        image = Image.open(imagepath).convert("RGB")
        image = np.array(image) / 255.0

        # load label from folder
        labelname = imagename.replace(".jpg", ".json")
        labelpath = os.path.join(self.labeldir, labelname)

        with open(labelpath, "r") as f:
            label = json.load(f)
        
        class_id = label["class_id"]
        boundingbox = np.array(label["bbox"], dtype=np.float32)

        return image, class_id, boundingbox