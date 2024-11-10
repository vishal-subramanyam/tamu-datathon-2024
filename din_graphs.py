import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
df = pd.read_csv('data/september_2024.csv')

result = df.groupby('Order ID').agg(
    date=('Sent Date', 'first'),
    modifier_count=('Modifier', 'count')
).sort_values(by='date').reset_index()

result['date'] = pd.to_datetime(result['date'])
result['time_interval'] = result['date'].dt.floor('15T').dt.time

result = result.groupby('time_interval').agg(
    count=('Order ID', 'count'),
    total=('modifier_count', 'mean')
).reset_index()

result['time_interval'] = pd.to_datetime(result['time_interval'], format='%H:%M:%S')
result.dtypes

# Set Seaborn style
sns.set(style="whitegrid")

fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot 'count' on the first y-axis
sns.lineplot(data=result, x='time_interval', y='count', ax=ax1, color='tab:blue', marker='o', label='Order Count')
ax1.set_xlabel('Time Interval (hh:mm)')
ax1.set_ylabel('Order Count', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Customize x-axis to show time only
time_fmt = mdates.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(time_fmt)

