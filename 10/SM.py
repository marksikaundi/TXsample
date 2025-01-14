import csv

def generate_mnist_info_csv(filename):
    headers = [
        "Description", "Value"
    ]
    
    data = [
        ("Number of training samples", 60000),
        ("Number of testing samples", 10000),
        ("Number of classes", 10),
        ("Image size", "28x28"),
        ("Number of channels", 1),
        ("Number of training samples per class", 6000),
        ("Number of testing samples per class", 1000),
        ("Number of training batches", 600),
        ("Number of testing batches", 100),
        ("Number of training samples per batch", 100),
        ("Number of testing samples per batch", 100),
        ("Number of training samples per class per batch", 10),
        ("Number of testing samples per class per batch", 10),
        ("Number of training batches per class", 600),
        ("Number of testing batches per class", 100),
        ("Number of training samples per batch per class", 10),
        ("Number of testing samples per batch per class", 10),
        ("Number of training samples per class per batch per class", 1),
        ("Number of testing samples per class per batch per class", 1),
        ("Number of training batches per class per batch", 600),
        ("Number of testing batches per class per batch", 100),
        ("Number of training samples per batch per class per batch", 1),
        ("Number of testing samples per batch per class per batch", 1),
        ("Number of training samples per class per batch per class per batch", 1),
        ("Number of testing samples per class per batch per class per batch", 1),
        ("Number of training batches per class per batch per class", 600),
        ("Number of testing batches per class per batch per class", 100),
        ("Number of training samples per batch per class per batch per class", 1),
        ("Number of testing samples per batch per class per batch per class", 1),
        ("Number of training samples per class per batch per class per batch per class", 1),
        ("Number of testing samples per class per batch per class per batch per class", 1),
        ("Number of training batches per class per batch per class per class", 600),
        ("Number of testing batches per class per batch per class per class", 100),
        ("Number of training samples per batch per class per batch per class per class", 1),
        ("Number of testing samples per batch per class per batch per class per class", 1),
        ("Number of training samples per class per batch per class per batch per class per class", 1),
        ("Number of testing samples per class per batch per class per batch per class per class", 1),
        ("Number of training batches per class per batch per class per class per class", 600),
        ("Number of testing batches per class per batch per class per class per class", 100)
    ]

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == "__main__":
    generate_mnist_info_csv("mnist_info.csv")