from src.dataset import ObjectDetectionDataset

def main():
    dataset = ObjectDetectionDataset("data/images", "data/labels")

    print("length - ", len(dataset))

    image, class_id, bbox = dataset[0]

    print("Image shape - ", image.shape)
    print("class id - ", class_id)
    print("bbox -", bbox)

if __name__ == "__main__":
    main()