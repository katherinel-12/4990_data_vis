import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sleep_clean.csv", keep_default_na=False)
df = df[df["Sleep Disorder"] != "None"].reset_index(drop=True)

dims = ["Sleep Duration", "Quality of Sleep", "Physical Activity Level",
        "Stress Level", "Heart Rate", "Daily Steps", "Systolic"]

norm = df[dims].copy()
for c in dims:
    norm[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())
norm["Sleep Disorder"] = df["Sleep Disorder"]
agg = norm.groupby("Sleep Disorder")[dims].mean()

colors = {"None": "#1f77b4", "Insomnia": "#ff7f0e", "Sleep Apnea": "#d62728"}

fig = go.Figure()
for grp in agg.index:
    fig.add_trace(go.Bar(
        name=grp, x=dims, y=agg.loc[grp].values,
        marker_color=colors[grp],
    ))
fig.update_layout(
    barmode="stack",
    title="Sleep Health — Stacked Bar Chart (normalized mean per Sleep Disorder)",
    xaxis=dict(tickangle=-20),
    yaxis=dict(title="Stacked normalized mean"),
)
fig.write_image("viz_stacked_bar.png", width=1200, height=600, scale=2)
print("Wrote viz_stacked_bar.png")
