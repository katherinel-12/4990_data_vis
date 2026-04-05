import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("bank-full.csv", sep=';')
df['age_group'] = pd.cut(df['age'], bins=range(0, 110, 10),
                         labels=[f'{i}-{i+9}' for i in range(0, 100, 10)])

hierarchies = {
    'Marital > Education > Job': ['marital', 'education', 'job'],
    'Age Group > Marital > Education': ['age_group', 'marital', 'education'],
    'Age Group > Job > Marital': ['age_group', 'job', 'marital'],
    'Education > Job > Marital': ['education', 'job', 'marital'],
}

fig = go.Figure()
for i, (label, path) in enumerate(hierarchies.items()):
    trace = px.sunburst(df, path=path, values='campaign').data[0]
    trace.visible = (i == 0)
    fig.add_trace(trace)

first = list(hierarchies)[0]
fig.update_layout(
    title=dict(
        text=f'Bank Marketing Sunburst — {first}',
        x=0.5,
        xanchor='center',
    ),
    margin=dict(t=100),
    updatemenus=[dict(
        buttons=[dict(
            label=label,
            method='update',
            args=[
                {'visible': [j == i for j in range(len(hierarchies))]},
                {'title.text': f'Bank Marketing Sunburst — {label}'},
            ],
        ) for i, label in enumerate(hierarchies)],
        direction='down', x=0.0, xanchor='left', y=1.15, yanchor='top',
    )],
)
fig.show()
