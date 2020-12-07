import pandas as pd
import numpy as np
import dash
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output





# bootstrap added
external_stylesheets = [
   {
       'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
       'rel': 'stylesheet',
       'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
       'crossorigin': 'anonymous'
   }
]

app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
server=app.server


city=[
    {'label':'Kolkata', 'value':'kolkata'},{'label':'Agartala', 'value':'agartala'},{'label':'Bangalore','value':'bangalore'},{'label':'Bhubaneswar','value':'bhubaneswar'},
    {'label':'Chennai','value':'chennai'},{'label':'Delhi','value':'delhi'},{'label':'Hyderabad','value':'hyderabad'},{'label':'Indore','value':'indore'},
    {'label':'Jaipur','value':'jaipur'},{'label':'Kanpur','value':'kanpur'},{'label':'Lucknow','value':'lucknow'},
    {'label':'Mumbai','value':'mumbai'},{'label':'Nagpur','value':'nagpur'},{'label':'Nainital','value':'nainital'},{'label':'Noida','value':'noida'},
    {'label':'Pune','value':'pune'},{'label':'Surat','value':'surat'},{'label':'Visakhapatnam','value':'visakhapatnam'}
]


kolkata = pd.read_csv('static/data/kolkata.csv')
agartala = pd.read_csv('static/data/agartala.csv')
bangalore = pd.read_csv('static/data/bangalore.csv')

bhubaneswar = pd.read_csv('static/data/bhubaneswar.csv')
chennai = pd.read_csv('static/data/chennai.csv')
delhi = pd.read_csv('static/data/delhi.csv')

hyderabad = pd.read_csv('static/data/hyderabad.csv')
indore = pd.read_csv('static/data/indore.csv')
jaipur = pd.read_csv('static/data/jaipur.csv')

kanpur = pd.read_csv('static/data/kanpur.csv')
lucknow = pd.read_csv('static/data/lucknow.csv')
mumbai = pd.read_csv('static/data/mumbai.csv')

nagpur = pd.read_csv('static/data/nagpur.csv')
nainital = pd.read_csv('static/data/nainital.csv')
noida = pd.read_csv('static/data/noida.csv')

pune = pd.read_csv('static/data/pune.csv')
surat = pd.read_csv('static/data/surat.csv')
visakhapatnam = pd.read_csv('static/data/visakhapatnam.csv')


app.layout=html.Div([
    html.Div([html.H4('This site is devaloped by Sankha Subhra Mondal')],className='alert alert-warning', role="alert"),
    html.Div([
        html.Div([
 ## dropdown
            html.Div([
                html.Div([
                    html.Img(src='static/img/{}'.format('kolkata.jpg')
                    ,id='city_pic',className='card-img-top',style={'padding':'20px'}),
                    html.Div([
                        html.Div([
                            dcc.Dropdown(id='city_name',options=city)
                        ],className='card-title'),
                    ],style={'padding':'20px'})
                ],className='card',style={'width': '100%;'})
            ],className='row')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([dcc.Graph(id='weather-plot',
                          figure={'data':[go.Bar(y=kolkata['temperature'], x=kolkata['time'], marker={'color': '#ffba83'}, name='Expected', width=np.ones(24) * 0.75),
                                                      go.Scatter(y=kolkata['feels_like'], x=kolkata['time'], marker={'color': '#cfff30'},
                                                                 customdata=np.transpose([kolkata['wind speed'], kolkata['humidity'], kolkata['weather'], kolkata['feels_like'],kolkata['precipitation'],kolkata['time']]),
                                                                 name='Prediction Line',
                                                                 hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                                                            "<b>Humidity :</b>%{customdata[1]}",
                                                                                            "<b>Weather :</b> %{customdata[2]}",
                                                                                            "<b>Feels Like :</b> %{customdata[3]}",
                                                                                            "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                                                            "<b>Time:</b> %{customdata[5]}"]))],
                                  'layout':go.Layout(title='Hourly Weather', xaxis={'title': 'Hours'},
                                                     yaxis={'title': 'Temperature in °C'},xaxis_tickangle=-45,
                                                     font={"size": 15, "color": "White"}, titlefont={"size": 15, "color": "White"},
                                                     paper_bgcolor='#4E5D6C',plot_bgcolor='#4E5D6C')})
                ],className='card-body')
            ],className='card')
        ],className='col-md-9') ## graph
    ],className='row')
],className='container')



@app.callback(Output('city_pic','src'),Output('weather-plot','figure'),[Input('city_name','value')])
def update_graph(type):
    if type == 'kolkata':
        return 'static/img/{}.jpg'.format('kolkata'),{'data':[go.Bar(y=kolkata['temperature'], x=kolkata['time'], marker={'color': '#ffba83'}, name='Expected', width=np.ones(24) * 0.75),
                                                      go.Scatter(y=kolkata['feels_like'], x=kolkata['time'], marker={'color': '#cfff30'},
                                                                 customdata=np.transpose([kolkata['wind speed'], kolkata['humidity'], kolkata['weather'], kolkata['feels_like'],kolkata['precipitation'],kolkata['time']]),
                                                                 name='Prediction Line',
                                                                 hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                                                            "<b>Humidity :</b>%{customdata[1]}",
                                                                                            "<b>Weather :</b> %{customdata[2]}",
                                                                                            "<b>Feels Like :</b> %{customdata[3]}",
                                                                                            "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                                                            "<b>Time:</b> %{customdata[5]}"]))],
                                  'layout':go.Layout(title='Hourly Weather', xaxis={'title': 'Hours'},
                                                     yaxis={'title': 'Temperature in °C'},xaxis_tickangle=-45,
                                                     font={"size": 15, "color": "White"}, titlefont={"size": 15, "color": "White"},
                                                     paper_bgcolor='#4E5D6C',plot_bgcolor='#4E5D6C')}

    elif type == 'agartala':
        return 'static/img/{}.jpg'.format('agartala'), {'data': [
            go.Bar(y=agartala['temperature'], x=agartala['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=agartala['feels_like'], x=agartala['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [agartala['wind speed'], agartala['humidity'], agartala['weather'], agartala['feels_like'],
                            agartala['precipitation'], agartala['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
                                                       'layout': go.Layout(title='Hourly Weather',
                                                                           xaxis={'title': 'Hours'},
                                                                           yaxis={'title': 'Temperature in °C'},
                                                                           xaxis_tickangle=-45,
                                                                           font={"size": 15, "color": "White"},
                                                                           titlefont={"size": 15, "color": "White"},
                                                                           paper_bgcolor='#4E5D6C',
                                                                           plot_bgcolor='#4E5D6C')}
    elif type == 'bangalore':
        return 'static/img/{}.jpg'.format('bangalore'), {'data': [
            go.Bar(y=bangalore['temperature'], x=bangalore['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=bangalore['feels_like'], x=bangalore['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [bangalore['wind speed'], bangalore['humidity'], bangalore['weather'], bangalore['feels_like'],
                            bangalore['precipitation'], bangalore['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}

    if type == 'bhubaneswar':
        return 'static/img/{}.jpg'.format('bhubaneswar'), {'data': [
            go.Bar(y=bhubaneswar['temperature'], x=bhubaneswar['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=bhubaneswar['feels_like'], x=bhubaneswar['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [bhubaneswar['wind speed'], bhubaneswar['humidity'], bhubaneswar['weather'], bhubaneswar['feels_like'],
                            bhubaneswar['precipitation'], bhubaneswar['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
                                                       'layout': go.Layout(title='Hourly Weather',
                                                                           xaxis={'title': 'Hours'},
                                                                           yaxis={'title': 'Temperature in °C'},
                                                                           xaxis_tickangle=-45,
                                                                           font={"size": 15, "color": "White"},
                                                                           titlefont={"size": 15, "color": "White"},
                                                                           paper_bgcolor='#4E5D6C',
                                                                           plot_bgcolor='#4E5D6C')}
    elif type == 'chennai':
        return 'static/img/{}.jpg'.format('chennai'), {'data': [
            go.Bar(y=chennai['temperature'], x=chennai['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=chennai['feels_like'], x=chennai['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [chennai['wind speed'], chennai['humidity'], chennai['weather'],chennai['feels_like'],
                            chennai['precipitation'], chennai['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}

    elif type == 'delhi':
        return 'static/img/{}.jpg'.format('delhi'), {'data': [
            go.Bar(y=delhi['temperature'], x=delhi['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=delhi['feels_like'], x=delhi['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [delhi['wind speed'], delhi['humidity'], delhi['weather'],
                            delhi['feels_like'],delhi['precipitation'], delhi['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}

    if type == 'hyderabad':
        return 'static/img/{}.jpg'.format('hyderabad'), {'data': [
            go.Bar(y=hyderabad['temperature'], x=hyderabad['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=hyderabad['feels_like'], x=hyderabad['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [hyderabad['wind speed'], hyderabad['humidity'], hyderabad['weather'], hyderabad['feels_like'],
                            hyderabad['precipitation'], hyderabad['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
                                                       'layout': go.Layout(title='Hourly Weather',
                                                                           xaxis={'title': 'Hours'},
                                                                           yaxis={'title': 'Temperature in °C'},
                                                                           xaxis_tickangle=-45,
                                                                           font={"size": 15, "color": "White"},
                                                                           titlefont={"size": 15, "color": "White"},
                                                                           paper_bgcolor='#4E5D6C',
                                                                           plot_bgcolor='#4E5D6C')}
    elif type == 'indore':
        return 'static/img/{}.jpg'.format('indore'), {'data': [
            go.Bar(y=indore['temperature'], x=indore['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=indore['feels_like'], x=indore['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [indore['wind speed'], indore['humidity'], indore['weather'], indore['feels_like'],
                            indore['precipitation'], indore['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}
    elif type == 'jaipur':
        return 'static/img/{}.jpg'.format('jaipur'), {'data': [
            go.Bar(y=jaipur['temperature'], x=jaipur['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=jaipur['feels_like'], x=jaipur['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [jaipur['wind speed'], jaipur['humidity'], jaipur['weather'], jaipur['feels_like'],
                            jaipur['precipitation'], jaipur['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}
    elif type == 'kanpur':
        return 'static/img/{}.jpg'.format('kanpur'), {'data': [
            go.Bar(y=kanpur['temperature'], x=kanpur['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=kanpur['feels_like'], x=kanpur['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [kanpur['wind speed'], kanpur['humidity'], kanpur['weather'], kanpur['feels_like'],
                            kanpur['precipitation'], kanpur['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}
    elif type == 'lucknow':
        return 'static/img/{}.jpg'.format('lucknow'), {'data': [
            go.Bar(y=lucknow['temperature'], x=lucknow['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=lucknow['feels_like'], x=lucknow['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [lucknow['wind speed'], lucknow['humidity'], lucknow['weather'], lucknow['feels_like'],
                            lucknow['precipitation'], lucknow['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}

    elif type == 'mumbai':
        return 'static/img/{}.jpg'.format('mumbai'), {'data': [
            go.Bar(y=mumbai['temperature'], x=mumbai['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=mumbai['feels_like'], x=mumbai['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [mumbai['wind speed'], mumbai['humidity'], mumbai['weather'], mumbai['feels_like'],
                            mumbai['precipitation'], mumbai['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}
    elif type == 'nagpur':
        return 'static/img/{}.jpg'.format('nagpur'), {'data': [
            go.Bar(y=nagpur['temperature'], x=nagpur['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=nagpur['feels_like'], x=nagpur['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [nagpur['wind speed'], nagpur['humidity'], nagpur['weather'], nagpur['feels_like'],
                            nagpur['precipitation'], nagpur['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}
    elif type == 'nainital':
        return 'static/img/{}.jpg'.format('nainital'), {'data': [
            go.Bar(y=nainital['temperature'], x=nainital['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=nainital['feels_like'], x=nainital['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [nainital['wind speed'], nainital['humidity'], nainital['weather'], nainital['feels_like'],
                            nainital['precipitation'], nainital['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}
    elif type == 'noida':
        return 'static/img/{}.jpg'.format('noida'), {'data': [
            go.Bar(y=noida['temperature'], x=noida['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=noida['feels_like'], x=noida['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [noida['wind speed'], noida['humidity'], noida['weather'], noida['feels_like'],
                            noida['precipitation'], noida['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}
    elif type == 'pune':
        return 'static/img/{}.jpg'.format('pune'), {'data': [
            go.Bar(y=pune['temperature'], x=pune['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=pune['feels_like'], x=pune['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [pune['wind speed'], pune['humidity'], pune['weather'], pune['feels_like'],
                            pune['precipitation'], pune['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}

    elif type == 'surat':
        return 'static/img/{}.jpg'.format('surat'), {'data': [
            go.Bar(y=surat['temperature'], x=surat['time'], marker={'color': '#ffba83'}, name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=surat['feels_like'], x=surat['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [surat['wind speed'], surat['humidity'], surat['weather'], surat['feels_like'],
                            surat['precipitation'], surat['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}
    elif type == 'visakhapatnam':
        return 'static/img/{}.jpg'.format('visakhapatnam'), {'data': [
            go.Bar(y=visakhapatnam['temperature'], x=visakhapatnam['time'], marker={'color': '#ffba83'},
                   name='Expected',
                   width=np.ones(24) * 0.75),
            go.Scatter(y=visakhapatnam['feels_like'], x=visakhapatnam['time'], marker={'color': '#cfff30'},
                       customdata=np.transpose(
                           [visakhapatnam['wind speed'], visakhapatnam['humidity'], visakhapatnam['weather'],
                            visakhapatnam['feels_like'],
                            visakhapatnam['precipitation'], visakhapatnam['time']]),
                       name='Prediction Line',
                       hovertemplate="<br>".join(["<b>Wind Speed :</b> %{customdata[0]}",
                                                  "<b>Humidity :</b>%{customdata[1]}",
                                                  "<b>Weather :</b> %{customdata[2]}",
                                                  "<b>Feels Like :</b> %{customdata[3]}",
                                                  "<b>Precipitation Chance:</b> %{customdata[4]}",
                                                  "<b>Time:</b> %{customdata[5]}"]))],
            'layout': go.Layout(title='Hourly Weather',
                                xaxis={'title': 'Hours'},
                                yaxis={'title': 'Temperature in °C'},
                                xaxis_tickangle=-45,
                                font={"size": 15, "color": "White"},
                                titlefont={"size": 15, "color": "White"},
                                paper_bgcolor='#4E5D6C',
                                plot_bgcolor='#4E5D6C')}

if __name__=="__main__":
    app.run_server()
