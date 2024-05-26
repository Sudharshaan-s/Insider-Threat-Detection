# Insider Threat Detection

This project focuses on detecting insider threats within a company's network using the Isolation Forest algorithm. By analyzing various log data such as device logs, email logs, file logs, logon logs, and HTTP logs, we aim to identify anomalous behavior that may indicate potential insider threats.

## Introduction

Insider threats are malicious activities performed by individuals within an organization. These threats can lead to significant security breaches and data loss. This project leverages machine learning, specifically the Isolation Forest algorithm, to detect such threats by identifying anomalous patterns in log data.

## Dataset

The dataset includes logs from various sources:

- **Device logs:** Track device connections and disconnections.
- **Email logs:** Record email activities including recipients and whether emails are sent to external addresses.
- **File logs:** Monitor file access and transfers.
- **Logon logs:** Capture login and logout activities.
- **HTTP logs:** Record web browsing activities.

## Links
  ftp://ftp.sei.cmu.edu/pub/cert-data/r4.2.tar.bz2
  https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=508099

## Modeling

The Isolation Forest algorithm is employed to detect anomalies. The process involves:

1. **Data Preparation:** Vectorizing the user activity data based on the engineered features.
2. **Training and Testing Split:** Dividing the data into training and testing sets.
3. **Model Training:** Training the Isolation Forest model on the training data.
4. **Anomaly Detection:** Using the model to score and identify anomalies in the data.

## Results

The model's performance is evaluated by examining the distribution of anomaly scores for both normal and threat data. Histograms are used to visualize these scores, and a cutoff threshold is defined to classify data points as anomalies.

## Dependencies

- Python 3.7+
- pandas
- numpy
- scikit-learn
- matplotlib

To run the insider threat detection system:
Clone the repository
```bash
git clone https://github.com/your-repo/insider-threat-detection.git
```
Install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Contributing

We welcome contributions to enhance this project. Please fork the repository and submit pull requests with your improvements.
