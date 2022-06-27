import random
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
import csv

df = pd.read_csv('ph_brand.csv')

fig = ff.create_distplot([df['Avg Rating'].tolist()], ['Avg ratings of mobile brands'])
fig.show()

