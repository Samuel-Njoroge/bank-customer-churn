# **Bank Customer Churn Prediction Model**

## **Problem Statement.**
Rated Bank, a financial institution, aims to solve their challenge of customers churning. Their current architecture entails sending raw data from their on-premises database to Azure Blob Storage.

## Solution
This project implements a machine learning model to predict customer churn for Rated Bank. It utilizes Azure cloud services for data storage, model training, and deployment.

## **Architecture.**
![](https://github.com/Samuel-Njoroge/bank-customer-churn/blob/main/diagrams/Azure_Projects-Machine%20learning.svg)

## **Technology Stack.**
- Data Storage: Bank application database → Azure Blob Storage
- Model Training: Azure Machine Learning Studio
- Model Deployment: Azure ML Endpoint

## **Setup and Installation**
1. Clone this repository
```sh
git clone https://github.com/Samuel-Njoroge/bank-customer-churn
```
3. Install required packages
```sh
pip install -r requirements.txt
```
5. Set up Azure credentials

## **Implementation Process**

All the steps taken can be found [here](https://medium.com/@_NjorogeSamuel/bank-customer-churn-using-azure-machine-learning-c5faee021b5c)

## **Model Performance**

Accuracy: 0.99

## **Deployment**
The model is deployed as an Azure ML Endpoint. Refer [here](https://medium.com/@_NjorogeSamuel/bank-customer-churn-using-azure-machine-learning-c5faee021b5c) for detailed instructions on the process.

## **Skills Learned**

*1. Data Engineering*

- Working with Azure Blob Storage for data management.
- Data preprocessing and cleaning techniques.

*2. Cloud Computing*
- Utilizing Azure services for machine learning workflows..
- Understanding cloud-based data storage and processing.

*3. Machine Learning*
- Developing predictive models for customer churn.
- Feature engineering and selection.

*4. MLOps (Machine Learning Operations)*
- Deploying machine learning models as API endpoints.
- Version control for both data and models.

*5. Domain Knowledge*

- Understanding the banking domain and customer churn factors.
- Translating business requirements into technical solutions.

## **Contributing**
Please, feel free to submit pull requests.

## **License**
This project is licensed under the MIT License.
