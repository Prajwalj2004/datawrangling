import plotly.express as px
df =px.data.iris()
fig=px.line(df,x='species',y='petal_width')
fig.show()
