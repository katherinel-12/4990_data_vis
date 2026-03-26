import pandas as pd 
import plotly.express as px 

df = pd.read_csv("bank-full.csv", sep=';')

print(df.head())

fig = px.sunburst(
    df,
    path=['marital', 'education', 'job'],
    values='campaign',
    # color='campaign',
    title='Sunburst Chart'
)

fig.show()

# hierarchical or textual 