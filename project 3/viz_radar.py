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

agg = norm.groupby("Sleep Disorder")[dims].mean().reset_index()

fig = go.Figure()
colors = {"None": "#1f77b4", "Insomnia": "#ff7f0e", "Sleep Apnea": "#d62728"}
for _, row in agg.iterrows():
    fig.add_trace(go.Scatterpolar(
        r=[row[c] for c in dims] + [row[dims[0]]],
        theta=dims + [dims[0]],
        fill="toself",
        name=row["Sleep Disorder"],
        line=dict(color=colors[row["Sleep Disorder"]]),
    ))
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
    title="Sleep Health — Radar Chart (mean profile per Sleep Disorder, normalized)",
    showlegend=True,
)
fig.write_image("viz_radar.png", width=900, height=800, scale=2)
print("Wrote viz_radar.png")
