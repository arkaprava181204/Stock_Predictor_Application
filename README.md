# Stock_Predictor_Application
I built a Stock Price Prediction App that uses deep learning (LSTM) to analyze historical market data and forecast future prices.  This project took me through the full pipeline: ✔ Data preprocessing ✔ Feature scaling ✔ Time-series sequence creation ✔ LSTM model training ✔ Prediction &amp; visualization
**🚀 Project Overview**

Stock prices are sequential and highly dependent on past trends. In this project, I used a Long Short-Term Memory (LSTM) network, a type of Recurrent Neural Network (RNN), to capture these time-based patterns and predict future values.

**The application:**

1.Preprocesses historical stock data

2.Normalizes the data using MinMax scaling

3.Creates sliding window sequences

4.Trains a deep LSTM model

5.Predicts future stock prices


**🛠️ Technologies Used:**

1.Python

2.Pandas & NumPy

4.Scikit-learn (MinMaxScaler)

5.TensorFlow / Keras

6.Matplotlib

7.Jupyter Notebook

**📊 Model Architecture**

1.The model is a stacked LSTM network:

2.Input Layer

3.LSTM (50 units) + Dropout

4.LSTM (60 units) + Dropout

5.LSTM (80 units) + Dropout

6.LSTM (120 units) + Dropout

7.Dense Output Layer (1 neuron)

This architecture allows the model to learn both short-term and long-term patterns in stock price movements.


**🔄 Data Processing Steps:**

1.Load historical stock data

2.Handle missing values

3.Apply MinMax scaling (0–1)

4.Create sequences of 100 time steps

5.Split data into training and testing sets

6.Train the LSTM model

7.Generate predictions


**📈 Output:**

The model predicts future stock prices and compares them with actual values using visualization, helping to evaluate how well the model has learned market patterns.

Details have also been discussed and sample shown in :- [Sample Video](https://www.linkedin.com/posts/arkaprava-bhattacharya-976926308_deeplearning-lstm-python-activity-7415428945950568448-1p0y?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE5ye-oBQzwSqY_5vmtM-VgYXA4iZCPcIYo)
