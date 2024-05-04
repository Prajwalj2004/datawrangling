import plotly.express as px
import plotly.graph_objects as go
fig=go.Figure(data=[go.Sankey(
        node=dict(
            thickness=5,
            line=dict(
                color='green',
                width=0.1),
            label=['A','B','C','D','E','F'],
            color='blue'),
            link=dict(
                source=[0,6,1,4,2,3],
                target=[2,1,5,2,1,5],
                value=[7,1,3,6,9,4]))])
fig.show()