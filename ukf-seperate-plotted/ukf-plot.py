from plotly.graph_objs import *
import pandas as pd
import math

my_cols=['t','est_px','est_py','a','b','c','d','e','meas_px','meas_py','gt_px','gt_py','gt_vx','gt_vy']
with open('output3.txt') as f:
    table_ekf_output = pd.read_table(f, sep='\t', header=None, names=my_cols, lineterminator='\n')
    
#table_ekf_output

import plotly.offline as py
from plotly.graph_objs import *


#estimations
trace1 = Scatter(
    x=table_ekf_output['est_px'],
    y=table_ekf_output['est_py'],
    xaxis='x2',
    yaxis='y2',
    name='KF- Estimate',
)

#Measurements
trace2 = Scatter(
    x=table_ekf_output['meas_px'],
    y=table_ekf_output['meas_py'],
    xaxis='x2',
    yaxis='y2',
    name = 'Measurements (Sensor)',
    mode = 'markers'
)

#Measurements
trace3 = Scatter(
    x=table_ekf_output['gt_px'],
    y=table_ekf_output['gt_py'],
    xaxis='x2',
    yaxis='y2',
    name = 'Ground Truth (Exact)',
)

data = [trace1, trace2, trace3]

layout = Layout(
    xaxis2=dict(
   
        anchor='x2',
        title='px'
    ),
    yaxis2=dict(
    
        anchor='y2',
        title='py'
    )
)

fig = Figure(data=data, layout=layout)
py.iplot(fig, filename= 'EKF')
