import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv('data/all_data.csv')
sales_per_month = {'2024-04':0, '2024-05':0, '2024-06':0, '2024-07':0, '2024-08':0, '2024-09':0, '2024-10':0}

for i in range(len(df)):
    if (i == len(df) - 1 or df['Order ID'][i] != df['Order ID'][i+1]):
        sales_per_month[df['Sent Date'][i].split(' ')[0][:7]] += 1

df = pd.DataFrame({
    'ds': ['2024-04-01', '2024-05-01', '2024-06-01', '2024-07-01', '2024-08-01', '2024-09-01', '2024-10-01'],
    'y': sales_per_month.values()
})

df['ds'] = pd.to_datetime(df['ds'])
#df.set_index('ds', inplace=True)

model = ExponentialSmoothing(df['y'], trend=None, seasonal=None, damped_trend=False)
model_fit = model.fit()

# Forecast next 12 months
forecast = model_fit.forecast(steps=12)

# Plot the forecast
plt.plot(df['ds'], df['y'], label='Observed Sales')
plt.plot(pd.date_range(df['ds'].iloc[-1], periods=13, freq='M')[1:], forecast, label='Forecasted Sales', linestyle='--')
plt.title('Sales Forecast using Simple Exponential Smoothing')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()




