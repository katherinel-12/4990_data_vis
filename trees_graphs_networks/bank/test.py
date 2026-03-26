import pandas as pd
import plotly.express as px

df = pd.read_csv("test.csv")

print(df.head())

fig = px.sunburst(
    df,
    path=['Region', 'Category', 'Product'],
    values='Sales',
    # color='Sales',
    title='Sales Hierarchy Sunburst Chart'
)

fig.show()