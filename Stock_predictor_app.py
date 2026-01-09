import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import streamlit as st
import matplotlib.pyplot as plt

model = load_model('D:\Projects\Data Analytics\Stock predictor\Stock Predictions Model.keras')

st.header('Stock Predictor App')

stock = st.text_input('Enter stock symbol','GOOG')
start = '2015-01-01'
end = '2024-12-31'

data = yf.download(stock,start,end)

st.subheader('Stock Data')
st.write(data)

data_train = pd.DataFrame(data.Close[0:int(len(data)*0.80)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.80):len(data)])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (0,1))

pas_100_days = data_train.tail(100)
data_test = pd.concat([pas_100_days,data_test], ignore_index = True)
data_test_scale = scaler.fit_transform(data_test)

x = []
y = []
for i in range(100,data_test_scale.shape[0]):
    x.append(data_test_scale[i-100:i])
    y.append(data_test_scale[i,0])
x,y = np.array(x), np.array(y)

predict = model.predict(x)

scale = 1/scaler.scale_
predict = predict*scale
y = y*scale

st.subheader('Prediction')
fig = plt.figure(figsize = (10,8))
plt.plot(predict, 'r', label = 'predicted price')
plt.plot(y, 'g', label = 'original price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()
st.pyplot(fig)

