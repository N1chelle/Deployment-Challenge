
import pandas as pd
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt

df = pd.read_csv('steam_games.csv')
plt.figure(figsize=(12,8))
g = df['is_free'].value_counts().plot(kind='pie', legend=True, autopct='%1.1f%%',explode=(0, 0.2), shadow=True, startangle=0)
