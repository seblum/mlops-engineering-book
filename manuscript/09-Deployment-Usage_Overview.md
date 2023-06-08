
# Development on the custom platform

The ML platform aims to enable the full development cycle of ML algorithms within DevOps and MLOps principles. This includes to enable development within a sophisticated IDE such as VSCode, as well as incorporating best practices like Gitflow, automation by CI/CD, and the containerization of code. Whereas the previous chapter explained the ML platform itself and its deployment, this chapter illustrates the workflow of developing ML models on the platform. Thus, a use case has been selected and implemented such that it integrates each of the previous mentioned principles and best practices.

## Use Case 

The exemplary use case *CNN for skin cancer detection* is based on a dataset from [Kaggle](https://www.kaggle.com/code/fanconic/cnn-for-skin-cancer-detection) and has been chosen to implement a use case leveraging a Deep Learning model, as well as its data quality which requires little to no data exploration and preprocessing.

### Data 

The dataset from [Kaggle](https://www.kaggle.com/code/fanconic/cnn-for-skin-cancer-detection) utilized in this project is obtained from the ISIC (International Skin Image Collaboration) Archive. It consists of 1800 images depicting benign moles and 1497 images representing malignant moles that have already been classified. The primary objective of this use case is to develop a model capable of visually classifying moles as either benign or malignant.

All the images in the dataset have been uniformly resized to a lower resolution of 224x224x3 RGB. Additionally, the dataset has already been cleaned and divided into a train set and a test set. This allows for a straightforward implementation that focuses on the crucial aspects of this tutorial, which involve putting machine learning into production and leveraging workflow management and model tracking tools. The data is also conveniently sorted based on the two types, namely benign and malignant.

```bash
data
│
└── train
│   │
│   └── benign
│   │   ...
│   │   
│   └── malignant
│       ...
│
└── test
│   │
│   └── benign
```

The dataset is kept in an AWS S3 Bucket, which was deployed on the pre-existing ML Platform. The deployment of the Bucket was accomplished using an Infrastructure-as-a-Code (IaaC) script, and the dataset was uploaded to the Bucket at the same time. To enable the ML pipeline to interact with AWS for data retrieval and storage, a custom utils script in the code base provides the necessary functionality.


<!-- Deep Learning --> 
