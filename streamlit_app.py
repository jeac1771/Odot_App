# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:11:56 2023

@author: jalvarez
"""

## streamlit run ODOT_dashboard.py

import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
from io import BytesIO
import requests

st.set_page_config(layout = 'wide')
#plot_odot(file_dominio, file_ancho, file_angle)

def filtrado_data(str_dominio, filter_data):

    '''
    Input
        - str_dominio(str): ingresa nombre dominio como Dom4
        - filter_data (dataframe): ingresa dataframe

    Output: 
        - berma_dis_s (list)
        - filter_pd (list)
        - total_nr_datas (list)
    '''

    if str_dominio == 'Dom4':
        filter_data1 = filter_data[filter_data['Berm width m']==8.8].reset_index()
        filter_data2 = filter_data[filter_data['Berm width m']==9.2].reset_index()
        filter_data3 = filter_data[filter_data['Berm width m']==10.1].reset_index()
        filter_data4 = filter_data[filter_data['Berm width m']==10.6].reset_index()
        filter_data5 = filter_data[filter_data['Berm width m']==11.6].reset_index()
        filter_data6 = filter_data[filter_data['Berm width m']==12.6].reset_index()
        berma_dis1 = round(filter_data1['Berm width m'][0],2)
        berma_dis2 = round(filter_data2['Berm width m'][0],2)
        berma_dis3 = round(filter_data3['Berm width m'][0],2)
        berma_dis4 = round(filter_data4['Berm width m'][0],2)
        berma_dis5 = round(filter_data5['Berm width m'][0],2)
        berma_dis6 = round(filter_data6['Berm width m'][0],2)
        total_nr_data1 = int(360/filter_data1['Slope dir'][1])
        total_nr_data2 = int(360/filter_data2['Slope dir'][1])
        total_nr_data3 = int(360/filter_data3['Slope dir'][1])
        total_nr_data4 = int(360/filter_data4['Slope dir'][1])
        total_nr_data5 = int(360/filter_data5['Slope dir'][1])
        total_nr_data6 = int(360/filter_data6['Slope dir'][1])
        berma_dis_s = [berma_dis1, berma_dis2, berma_dis3, berma_dis4, berma_dis5, berma_dis6]
        filter_pd = [filter_data1, filter_data2, filter_data3, filter_data4, filter_data5, filter_data6]
        total_nr_datas = [total_nr_data1, total_nr_data2, total_nr_data3, total_nr_data4, total_nr_data5, total_nr_data6]
        iter_subplots = 6

    elif str_dominio == 'Dom5':
        filter_data1 = filter_data[filter_data['Berm width m']==8.8].reset_index()
        filter_data2 = filter_data[filter_data['Berm width m']==9.2].reset_index()
        filter_data3 = filter_data[filter_data['Berm width m']==10.6].reset_index()
        filter_data4 = filter_data[filter_data['Berm width m']==11.3].reset_index()
        filter_data5 = filter_data[filter_data['Berm width m']==12.6].reset_index()
        berma_dis1 = round(filter_data1['Berm width m'][0],2)
        berma_dis2 = round(filter_data2['Berm width m'][0],2)
        berma_dis3 = round(filter_data3['Berm width m'][0],2)
        berma_dis4 = round(filter_data4['Berm width m'][0],2)
        berma_dis5 = round(filter_data5['Berm width m'][0],2)
        total_nr_data1 = int(360/filter_data1['Slope dir'][1])
        total_nr_data2 = int(360/filter_data2['Slope dir'][1])
        total_nr_data3 = int(360/filter_data3['Slope dir'][1])
        total_nr_data4 = int(360/filter_data4['Slope dir'][1])
        total_nr_data5 = int(360/filter_data5['Slope dir'][1])
        berma_dis_s = [berma_dis1, berma_dis2, berma_dis3, berma_dis4, berma_dis5]
        filter_pd = [filter_data1, filter_data2, filter_data3, filter_data4, filter_data5]
        total_nr_datas = [total_nr_data1, total_nr_data2, total_nr_data3, total_nr_data4, total_nr_data5]
        iter_subplots = 5

    else:
        filter_data1 = filter_data[filter_data['Berm width m']==8.8].reset_index()
        filter_data2 = filter_data[filter_data['Berm width m']==9.2].reset_index()
        filter_data3 = filter_data[filter_data['Berm width m']==10.1].reset_index()
        filter_data4 = filter_data[filter_data['Berm width m']==10.6].reset_index()
        filter_data5 = filter_data[filter_data['Berm width m']==11.3].reset_index()
        filter_data6 = filter_data[filter_data['Berm width m']==12.6].reset_index()
        berma_dis1 = round(filter_data1['Berm width m'][0],2)
        berma_dis2 = round(filter_data2['Berm width m'][0],2)
        berma_dis3 = round(filter_data3['Berm width m'][0],2)
        berma_dis4 = round(filter_data4['Berm width m'][0],2)
        berma_dis5 = round(filter_data5['Berm width m'][0],2)
        berma_dis6 = round(filter_data6['Berm width m'][0],2)
        total_nr_data1 = int(360/filter_data1['Slope dir'][1])
        total_nr_data2 = int(360/filter_data2['Slope dir'][1])
        total_nr_data3 = int(360/filter_data3['Slope dir'][1])
        total_nr_data4 = int(360/filter_data4['Slope dir'][1])
        total_nr_data5 = int(360/filter_data5['Slope dir'][1])
        total_nr_data6 = int(360/filter_data6['Slope dir'][1])
        berma_dis_s = [berma_dis1, berma_dis2, berma_dis3, berma_dis4, berma_dis5, berma_dis6]
        filter_pd = [filter_data1, filter_data2, filter_data3, filter_data4, filter_data5, filter_data6]
        total_nr_datas = [total_nr_data1, total_nr_data2, total_nr_data3, total_nr_data4, total_nr_data5, total_nr_data6]
        iter_subplots = 6
        

    return berma_dis_s, filter_pd, total_nr_datas, iter_subplots

def plot_odot_plotly_unico(file_dominio, file_ancho, file_angle, data_base, ODOT_panel):
    
    filter_data = data_base[data_base['Dominio']==file_dominio].copy()
    filter_data = filter_data[filter_data['Berm width m'] == file_ancho]
    filter_data = filter_data[filter_data['Bench angle'] == file_angle]

    berma_dis = round(filter_data['Berm width m'][0],2)
    total_nr_datas = int(360/filter_data['Slope dir'][1])
    total_nr_data = total_nr_datas
    filtrado = filter_data.copy()

    if file_angle == 70:
        ODOT = 9.53
    elif file_angle == 75:
        ODOT = 8.81
    elif file_angle == 80:
        ODOT = 7.77


    fig = go.Figure()

    banco = []
    banco.clear()
    berma_diseno = []
    berma_diseno.clear()


    if ODOT_panel == 'Si':
        ## revisamos cada dipdir de cada angulo de revisión
        for i in range(0, total_nr_data):
            banco.append(filtrado['Spill width m'][i]) ## linea roja
            perdida_berma = filtrado['Berm width m'][i] - filtrado['80% Berm widths > (m)'][i]
            berma_diseno_req = max(ODOT, filtrado['Spill width m'][i]) + perdida_berma
            berma_diseno.append(berma_diseno_req) #barras azules

            ## completamos los valores inciales de los 360° para cerrar la curva
            banco.append(filtrado['Spill width m'][0]) ## linea roja
            perdida_berma = filtrado['Berm width m'][0] - filtrado['80% Berm widths > (m)'][0]
            berma_diseno_req = max(ODOT, filtrado['Spill width m'][0]) + perdida_berma
            berma_diseno.append(berma_diseno_req) #barras azules
    else:
        for i in range(0, total_nr_data):
            banco.append(filtrado['Spill width m'][i]) ## linea roja
            perdida_berma = filtrado['Berm width m'][i] - filtrado['80% Berm widths > (m)'][i]
            berma_diseno_req = filtrado['Spill width m'][i] + perdida_berma
            berma_diseno.append(berma_diseno_req) #barras azules

            ## completamos los valores inciales de los 360° para cerrar la curva
            banco.append(filtrado['Spill width m'][0]) ## linea roja
            perdida_berma = filtrado['Berm width m'][0] - filtrado['80% Berm widths > (m)'][0]
            berma_diseno_req = filtrado['Spill width m'][0] + perdida_berma
            berma_diseno.append(berma_diseno_req) #barras azules

    ## graficamos cada curva
    #########################################################################

    frequencies = banco #datos guardados línea roja
    theta = np.arange(0, 360 + int(filtrado['Slope dir'][1]), int(filtrado['Slope dir'][1])) #angulos roseta


    ## Grafica asociada a las barras azules, correspondiente a la berma de diseño
    fig.add_trace(go.Barpolar(
        r=berma_diseno,
        theta=theta,
        width=5,
        marker_color="deepskyblue",
        marker_line_color="deepskyblue",
        marker_line_width=2,
        opacity=0.8))

    ## Grafica asociada a la línea roja, correspondiente al Largo de Derrame
    fig.add_trace(go.Scatterpolar(
        name = "Largo de Derrame",
        r = frequencies,
        theta = theta, line=dict(color = 'red')))

    ## ODOT
    x = np.arange(0,365,5)
    theta_odot = x
    R1 = np.ones(73)*ODOT
    fig.add_trace(go.Scatterpolar(
        name = "ODOT",
        r = R1,
        theta = theta_odot, line=dict(color = 'darkgreen')))

    ## Berma_diseno (Sblock)
    x = np.arange(0,365,5)
    theta_b_dis = x
    R1 = np.ones(73)*berma_dis
    fig.add_trace(go.Scatterpolar(
        name = "Berma de Diseño",
        r = R1,
        theta = theta_b_dis, line=dict(color = 'darkorange')))


    ## Actualización de Layout
    fig.update_layout(template=None, height=600, width=1000, title_text="Diseño Banco Berma",
    showlegend = False,
    polar = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
        tickfont_size=8,
        rotation=-90, # start position of angular axis
        direction="clockwise"
    ),
    radialaxis = dict(range=[0, 20])
    ))

    ## Graficamos
    st.plotly_chart(fig, use_container_width=True)

## Funcion para generar grafica con plotly
def plot_odot_plotly_LD(file_dominio, file_angle):
    
  filter_data = data_base[data_base['Dominio']==file_dominio]
  filter_data = filter_data[filter_data['Bench angle']==file_angle]
  
  if file_dominio == 'Dominio 1':
      str_dominio = 'Dom1'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)

  elif file_dominio == 'Dominio 2':
      str_dominio = 'Dom2'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)
  
  elif file_dominio == 'Dominio 3':
      str_dominio = 'Dom3'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)
  
  elif file_dominio == 'Dominio 4':
      str_dominio = 'Dom4'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)
  
  elif file_dominio == 'Dominio 5':
      str_dominio = 'Dom5'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)
  
  if file_angle == 70:
    ODOT = 9.53
  elif file_angle == 75:
    ODOT = 8.81
  elif file_angle == 80:
    ODOT = 7.77
  
  if str_dominio == 'Dom5':
    fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'polar'}]*3]*2, subplot_titles=("Berma 8.8 [m]", 
                                                                                        "Berma 9.2 [m]", 
                                                                                        "Berma 10.6 [m]", 
                                                                                        "Berma 11.3 [m]", 
                                                                                        "Berma 12.6 [m]",
                                                                                        " "))
  elif str_dominio == 'Dom4':
    fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'polar'}]*3]*2, subplot_titles=("Berma 8.8 [m]", 
                                                                                        "Berma 9.2 [m]",
                                                                                        "Berma 10.1 [m]", 
                                                                                        "Berma 10.6 [m]", 
                                                                                        "Berma 11.6 [m]", 
                                                                                        "Berma 12.6 [m]"))
  else:
    fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'polar'}]*3]*2, subplot_titles=("Berma 8.8 [m]", 
                                                                                        "Berma 9.2 [m]", 
                                                                                        "Berma 10.1 [m]", 
                                                                                        "Berma 10.6 [m]", 
                                                                                        "Berma 11.3 [m]", 
                                                                                        "Berma 12.6 [m]"))
  total_nr_ids = 0
  
  
  ## iteramos por cada subplot
  for k in range(iter_subplots):
  
    banco = []
    banco.clear()
    berma_diseno = []
    berma_diseno.clear()
  
    total_nr_data = total_nr_datas[total_nr_ids]
    filtrado = filter_pd[total_nr_ids]
    berma_dis = berma_dis_s[total_nr_ids]
    total_nr_ids += 1
  
    if ODOT_panel == 'Si':
      ## revisamos cada dipdir de cada angulo de revisión
      for i in range(0, total_nr_data):
        banco.append(filtrado['Spill width m'][i]) ## linea roja
        perdida_berma = filtrado['Berm width m'][i] - filtrado['80% Berm widths > (m)'][i]
        berma_diseno_req = max(ODOT, filtrado['Spill width m'][i]) + perdida_berma
        berma_diseno.append(berma_diseno_req) #barras azules
    
      ## completamos los valores inciales de los 360° para cerrar la curva
      banco.append(filtrado['Spill width m'][0]) ## linea roja
      perdida_berma = filtrado['Berm width m'][0] - filtrado['80% Berm widths > (m)'][0]
      berma_diseno_req = max(ODOT, filtrado['Spill width m'][0]) + perdida_berma
      berma_diseno.append(berma_diseno_req) #barras azules
    else:
      for i in range(0, total_nr_data):
        banco.append(filtrado['Spill width m'][i]) ## linea roja
        perdida_berma = filtrado['Berm width m'][i] - filtrado['80% Berm widths > (m)'][i]
        berma_diseno_req = filtrado['Spill width m'][i] + perdida_berma
        berma_diseno.append(berma_diseno_req) #barras azules
    
      ## completamos los valores inciales de los 360° para cerrar la curva
      banco.append(filtrado['Spill width m'][0]) ## linea roja
      perdida_berma = filtrado['Berm width m'][0] - filtrado['80% Berm widths > (m)'][0]
      berma_diseno_req = filtrado['Spill width m'][0] + perdida_berma
      berma_diseno.append(berma_diseno_req) #barras azules
      
  
    ## salvamos el Rajo, el dominio y salvamos el IRA, ancho de berma diseño, angulo de banco
    IRA = int(filtrado['Interramp Angle'][0])
    Rajo = 'ESS'
    Dominio = filtrado.iloc[:, 2][0][:4]
  
    ## graficamos cada curva
    #########################################################################
    
    max_radio = max(filtrado['Berm width m'][0], max(berma_diseno)) + 1.9 #maximo radio en la roseta
    frequencies = banco #datos guardados línea roja
    theta = np.arange(0, 360 + int(filtrado['Slope dir'][1]), int(filtrado['Slope dir'][1])) #angulos roseta
    width = np.radians(5) #ancho roseta
    
    ## Aca definimos a que grid corresponde cada roseta
    if k == 0:
      a = 1
      b = 1
    elif k == 1:
      a = 1
      b = 2
    elif k == 2:
      a = 1
      b = 3
    elif k == 3:
      a = 2
      b = 1
    elif k == 4:
      a = 2
      b = 2
    elif k == 5:
      a = 2
      b = 3
  
    ## Grafica asociada a las barras azules, correspondiente a la berma de diseño
    fig.add_trace(go.Barpolar(
        r=berma_diseno,
        theta=theta,
        width=5,
        marker_color="deepskyblue",
        marker_line_color="deepskyblue",
        marker_line_width=2,
        opacity=0.8), a, b)
    
    ## Grafica asociada a la línea roja, correspondiente al Largo de Derrame
    fig.add_trace(go.Scatterpolar(
      name = "Largo de Derrame",
      r = frequencies,
      theta = theta, line=dict(color = 'red')), a, b)
  
    ## ODOT
    x = np.arange(0,365,5)
    theta_odot = x
    R1 = np.ones(73)*ODOT
    fig.add_trace(go.Scatterpolar(
      name = "ODOT",
      r = R1,
      theta = theta_odot, line=dict(color = 'darkgreen')), a, b)
    
    ## Berma_diseno (Sblock)
    x = np.arange(0,365,5)
    theta_b_dis = x
    R1 = np.ones(73)*berma_dis
    fig.add_trace(go.Scatterpolar(
      name = "Berma de Diseño",
      r = R1,
      theta = theta_b_dis, line=dict(color = 'darkorange')), a, b)
  
  ## Actualización de Layout
  fig.layout.annotations[0].update(y=1.05)
  fig.layout.annotations[2].update(y=1.05)
  fig.layout.annotations[1].update(y=1.05)
  fig.layout.annotations[3].update(y=0.41)
  fig.layout.annotations[4].update(y=0.41)
  fig.layout.annotations[5].update(y=0.41)

  ## Actualización de Layout
  fig.update_layout(template=None, height=600, width=1000, title_text="Diseño Banco Berma - Berma de diseño",
  showlegend = False,
  polar = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size=8,
      rotation=-90, # start position of angular axis
      direction="clockwise"
    ),
    radialaxis = dict(range=[0, 20])
  ),
  polar2 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 20])
  ),
  polar3 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 20])
  ),
  polar4 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 20])
  ),
  polar5 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 20])
  ),
  polar6 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 20])
  ))
  
  ## Graficamos
  st.plotly_chart(fig, use_container_width=True)

def plot_odot_plotly_unico_LD(file_dominio, file_ancho, file_angle, data_base, ODOT_panel, nombre_gr):
    
  filter_data = data_base[data_base['Dominio']==file_dominio].copy()
  filter_data = filter_data[filter_data['Berm width m'] == file_ancho]
  filter_data = filter_data[filter_data['Bench angle'] == file_angle].reset_index()

  berma_dis = round(filter_data['Berm width m'][0],2)
  total_nr_datas = int(360/filter_data['Slope dir'][1])
  total_nr_data = total_nr_datas
  filtrado = filter_data.copy()

  if file_angle == 70:
      ODOT = 9.53
  elif file_angle == 75:
      ODOT = 8.81
  elif file_angle == 80:
      ODOT = 7.77


  fig = go.Figure()

  banco = []
  banco.clear()
  berma_diseno = []
  berma_diseno.clear()

  # print(total_nr_data)
  if ODOT_panel == 'Si':
      ## revisamos cada dipdir de cada angulo de revisión
      for i in range(0, total_nr_data):
        banco.append(filtrado['Spill width m'][i]) ## linea roja
        perdida_berma = filtrado['Berm width m'][i] - filtrado['80% Berm widths > (m)'][i]
        berma_diseno_req = max(ODOT, filtrado['Spill width m'][i]) + perdida_berma
        berma_diseno.append(berma_diseno_req) #barras azules

      ## completamos los valores inciales de los 360° para cerrar la curva
      banco.append(filtrado['Spill width m'][0]) ## linea roja
      perdida_berma = filtrado['Berm width m'][0] - filtrado['80% Berm widths > (m)'][0]
      berma_diseno_req = max(ODOT, filtrado['Spill width m'][0]) + perdida_berma
      berma_diseno.append(berma_diseno_req) #barras azules
  else:
      for i in range(0, total_nr_data):
        banco.append(filtrado['Spill width m'][i]) ## linea roja
        perdida_berma = filtrado['Berm width m'][i] - filtrado['80% Berm widths > (m)'][i]
        berma_diseno_req = filtrado['Spill width m'][i] + perdida_berma
        berma_diseno.append(berma_diseno_req) #barras azules

      ## completamos los valores inciales de los 360° para cerrar la curva
      banco.append(filtrado['Spill width m'][0]) ## linea roja
      perdida_berma = filtrado['Berm width m'][0] - filtrado['80% Berm widths > (m)'][0]
      berma_diseno_req = filtrado['Spill width m'][0] + perdida_berma
      berma_diseno.append(berma_diseno_req) #barras azules

    ## graficamos cada curva
    #########################################################################

  frequencies = banco #datos guardados línea roja
  theta = np.arange(0, 360 + int(filtrado['Slope dir'][1]), int(filtrado['Slope dir'][1])) #angulos roseta
  # print(theta)

    ## Grafica asociada a las barras azules, correspondiente a la berma de diseño
  fig.add_trace(go.Barpolar(
      r=berma_diseno,
      theta=theta,
      width=5,
      marker_color="deepskyblue",
      marker_line_color="deepskyblue",
      marker_line_width=2,
      opacity=0.8))

    ## Grafica asociada a la línea roja, correspondiente al Largo de Derrame
  fig.add_trace(go.Scatterpolar(
      name = "Largo de Derrame",
      r = frequencies,
      theta = theta, line=dict(color = 'red')))

  ## ODOT
  x = np.arange(0,365,5)
  theta_odot = x
  R1 = np.ones(73)*ODOT
  fig.add_trace(go.Scatterpolar(
      name = "ODOT",
      r = R1,
      theta = theta_odot, line=dict(color = 'darkgreen')))

  # Berma_diseno (Sblock)
  x = np.arange(0,365,5)
  theta_b_dis = x
  R1 = np.ones(73)*berma_dis
  fig.add_trace(go.Scatterpolar(
      name = "Berma de Diseño",
      r = R1,
      theta = theta_b_dis, line=dict(color = 'darkorange')))

  nombre_gr = f'CB={file_angle}º, B={file_ancho}[m], {file_dominio}'
  # Actualización de Layout
  fig.update_layout(template=None, height=600, width=1000, title_text= nombre_gr,
    showlegend = False,
    polar = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
        tickfont_size=8,
        rotation=-90, # start position of angular axis
        direction="clockwise"
    ),
    radialaxis = dict(range=[0, 20])
    ))

    ## Graficamos
  st.plotly_chart(fig, use_container_width=True)

def plot_PoF_plotly_LD(file_dominio, file_angle):
  filter_data = data_base[data_base['Dominio']==file_dominio]
  filter_data = filter_data[filter_data['Bench angle']==file_angle]
  
  if file_dominio == 'Dominio 1':
      str_dominio = 'Dom1'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)

  elif file_dominio == 'Dominio 2':
      str_dominio = 'Dom2'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)
  
  elif file_dominio == 'Dominio 3':
      str_dominio = 'Dom3'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)
  
  elif file_dominio == 'Dominio 4':
      str_dominio = 'Dom4'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)
  
  elif file_dominio == 'Dominio 5':
      str_dominio = 'Dom5'
      berma_dis_s, filter_pd, total_nr_datas, iter_subplots = filtrado_data(str_dominio, filter_data)
  
  if file_angle == 70:
    ODOT = 9.53
  elif file_angle == 75:
    ODOT = 8.81
  elif file_angle == 80:
    ODOT = 7.77
  
  if str_dominio == 'Dom5':
    fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'polar'}]*3]*2, subplot_titles=("Berma 8.8 [m]", 
                                                                                        "Berma 9.2 [m]", 
                                                                                        "Berma 10.6 [m]", 
                                                                                        "Berma 11.3 [m]", 
                                                                                        "Berma 12.6 [m]",
                                                                                        " "))
  elif str_dominio == 'Dom4':
    fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'polar'}]*3]*2, subplot_titles=("Berma 8.8 [m]", 
                                                                                        "Berma 9.2 [m]",
                                                                                        "Berma 10.1 [m]", 
                                                                                        "Berma 10.6 [m]", 
                                                                                        "Berma 11.6 [m]", 
                                                                                        "Berma 12.6 [m]"))
  else:
    fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'polar'}]*3]*2, subplot_titles=("Berma 8.8 [m]", 
                                                                                        "Berma 9.2 [m]", 
                                                                                        "Berma 10.1 [m]", 
                                                                                        "Berma 10.6 [m]", 
                                                                                        "Berma 11.3 [m]", 
                                                                                        "Berma 12.6 [m]"))
  total_nr_ids = 0
  
  
  ## iteramos por cada subplot
  for k in range(iter_subplots):
  
    banco = []
    banco.clear()
    berma_diseno = []
    berma_diseno.clear()
  
    total_nr_data = total_nr_datas[total_nr_ids]
    filtrado = filter_pd[total_nr_ids]
    berma_dis = berma_dis_s[total_nr_ids]
    total_nr_ids += 1
  

    for i in range(0, total_nr_data):
      banco.append(filtrado['Spill width m'][i]) ## linea roja
      perdida_berma = filtrado['Berm width m'][i] - filtrado['80% Berm widths > (m)'][i]
      berma_diseno_req = filtrado['Spill width m'][i] + perdida_berma
      berma_diseno.append(filtrado['PF berm crest %'][i] ) #barras azules
  
    ## completamos los valores inciales de los 360° para cerrar la curva
    banco.append(filtrado['Spill width m'][0]) ## linea roja
    perdida_berma = filtrado['Berm width m'][0] - filtrado['80% Berm widths > (m)'][0]
    berma_diseno_req = filtrado['Spill width m'][0] + perdida_berma
    berma_diseno.append(filtrado['PF berm crest %'][0]) #barras azules
      
  
    ## salvamos el Rajo, el dominio y salvamos el IRA, ancho de berma diseño, angulo de banco
    IRA = int(filtrado['Interramp Angle'][0])
    Rajo = 'ESS'
    Dominio = filtrado.iloc[:, 2][0][:4]
  
    ## graficamos cada curva
    #########################################################################
    
    max_radio = max(filtrado['Berm width m'][0], max(berma_diseno)) + 1.9 #maximo radio en la roseta
    frequencies = banco #datos guardados línea roja
    theta = np.arange(0, 360 + int(filtrado['Slope dir'][1]), int(filtrado['Slope dir'][1])) #angulos roseta
    width = np.radians(5) #ancho roseta
    
    ## Aca definimos a que grid corresponde cada roseta
    if k == 0:
      a = 1
      b = 1
    elif k == 1:
      a = 1
      b = 2
    elif k == 2:
      a = 1
      b = 3
    elif k == 3:
      a = 2
      b = 1
    elif k == 4:
      a = 2
      b = 2
    elif k == 5:
      a = 2
      b = 3
  
    ## Grafica asociada a las barras azules, correspondiente a la berma de diseño
    fig.add_trace(go.Barpolar(
        r=berma_diseno,
        theta=theta,
        name = 'PoF',
        width=5,
        marker_color="purple",
        marker_line_color="purple",
        marker_line_width=2,
        opacity=0.8), a, b)
  
  ## Actualización de Layout
  fig.layout.annotations[0].update(y=1.05)
  fig.layout.annotations[2].update(y=1.05)
  fig.layout.annotations[1].update(y=1.05)
  fig.layout.annotations[3].update(y=0.41)
  fig.layout.annotations[4].update(y=0.41)
  fig.layout.annotations[5].update(y=0.41)

  ## Actualización de Layout
  fig.update_layout(template=None, height=600, width=1000, title_text="Diseño Banco Berma - Probabilidad de Falla",
  showlegend = False,
  polar = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size=8,
      rotation=-90, # start position of angular axis
      direction="clockwise"
    ),
    radialaxis = dict(range=[0, 60])
  ),
  polar2 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 60])
  ),
  polar3 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 60])
  ),
  polar4 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 60])
  ),
  polar5 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 60])
  ),
  polar6 = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
      tickfont_size = 8,
      rotation = -90,
      direction = "clockwise"
    ),
    radialaxis = dict(range=[0, 60])
  ))
  
  ## Graficamos
  st.plotly_chart(fig, use_container_width=True)

def plot_PoF_plotly_unico(file_dominio, file_ancho, file_angle, data_base, ODOT_panel, nombre_gr):
  filter_data = data_base[data_base['Dominio']==file_dominio].copy()
  filter_data = filter_data[filter_data['Berm width m'] == file_ancho]
  filter_data = filter_data[filter_data['Bench angle'] == file_angle].reset_index()

  berma_dis = round(filter_data['Berm width m'][0],2)
  total_nr_datas = int(360/filter_data['Slope dir'][1])
  total_nr_data = total_nr_datas
  filtrado = filter_data.copy()

  fig = go.Figure()

  banco = []
  banco.clear()
  berma_diseno = []
  berma_diseno.clear()


  for i in range(0, total_nr_data):
    banco.append(filtrado['Spill width m'][i]) ## linea roja
    perdida_berma = filtrado['Berm width m'][i] - filtrado['80% Berm widths > (m)'][i]
    berma_diseno_req = filtrado['Spill width m'][i] + perdida_berma
    berma_diseno.append(filtrado['PF berm crest %'][i]) #barras azules

  ## completamos los valores inciales de los 360° para cerrar la curva
  banco.append(filtrado['Spill width m'][0]) ## linea roja
  perdida_berma = filtrado['Berm width m'][0] - filtrado['80% Berm widths > (m)'][0]
  berma_diseno_req = filtrado['Spill width m'][0] + perdida_berma
  berma_diseno.append(filtrado['PF berm crest %'][0]) #barras azules

    ## graficamos cada curva
    #########################################################################

  frequencies = banco #datos guardados línea roja
  theta = np.arange(0, 360 + int(filtrado['Slope dir'][1]), int(filtrado['Slope dir'][1])) #angulos roseta
  # print(theta)

  ## Grafica asociada a las barras azules, correspondiente a la berma de diseño
  fig.add_trace(go.Barpolar(
      r=berma_diseno,
      name = 'PoF',
      theta=theta,
      width=5,
      marker_color="purple",
      marker_line_color="purple",
      marker_line_width=2,
      opacity=0.8))

  nombre_gr = f'CB={file_angle}º, B={file_ancho}[m], {file_dominio}'
  # Actualización de Layout
  fig.update_layout(template=None, height=600, width=1000, title_text= nombre_gr,
    showlegend = False,
    polar = dict(bgcolor = "oldlace",
    radialaxis_tickfont_size = 8,
    angularaxis = dict(
        tickfont_size=8,
        rotation=-90, # start position of angular axis
        direction="clockwise"
    ),
    radialaxis = dict(range=[0, 60])
    ))

    ## Graficamos
  st.plotly_chart(fig, use_container_width=True)

# Aqui dejaré el Frontend
def load_data(file):
  df = pd.read_csv(file, delimiter = ';')
  return df
uploaded_file = st.sidebar.file_uploader('Seleccione un archivo')

if uploaded_file is not None:
   
  RB_derrame_pof = st.sidebar.radio("Seleccione análisis", ('Berma de diseño', 'PoF'))


  Rosetas = st.sidebar.text('Rosetas')
  file_dominio = st.sidebar.selectbox('Seleccione Dominio: ', ('Dominio 1', 'Dominio 2', 'Dominio 3', 'Dominio 4', 'Dominio 5'), key = 'file_dominio')
  # file_ancho = st.sidebar.selectbox('Seleccione Ancho de Berma (m): ', (8.8, 9.2, 10.1, 10.6, 11.3, 11.6, 12.6))
  file_ancho = 8.8
  ODOT_panel = st.sidebar.selectbox('Seleccionar ODOT: ', ('Si', 'No'), key = 'ODOT_panel')
  file_angle = st.sidebar.selectbox('Seleccione Ángulo Cara de Banco (°): ', (70, 75, 80), key = 'file_angle')

  st.sidebar.text(' ')
  st.sidebar.text(' ')
  st.sidebar.text('----------------------------------')
  st.sidebar.text(' ')
  st.sidebar.text(' ')
  st.sidebar.text('Gráfico 1')
  file_dominio1 = st.sidebar.selectbox('Seleccione Dominio1: ', ('Dominio 1', 'Dominio 2', 'Dominio 3', 'Dominio 4', 'Dominio 5'), key = 'file_dominio1')
  # file_ancho = st.sidebar.selectbox('Seleccione Ancho de Berma (m): ', (8.8, 9.2, 10.1, 10.6, 11.3, 11.6, 12.6))
  if file_dominio1 == 'Dominio 5':
    file_ancho1 = st.sidebar.selectbox('Seleccione Ancho de Berma (m): ', (8.8, 9.2, 10.6, 11.3, 12.6), key = 'file_ancho1')
  elif file_dominio1 == 'Dominio 4':
    file_ancho1 = st.sidebar.selectbox('Seleccione Ancho de Berma (m): ', (8.8, 9.2, 10.1, 10.6, 11.6, 12.6), key = 'file_ancho1')
  else:
    file_ancho1 = st.sidebar.selectbox('Seleccione Ancho de Berma (m): ', (8.8, 9.2, 10.1, 10.6, 11.3, 12.6), key = 'file_ancho1')

  ODOT_panel1 = st.sidebar.selectbox('Seleccionar ODOT: ', ('Si', 'No'), key = 'ODOT_panel1')
  file_angle1 = st.sidebar.selectbox('Seleccione Ángulo Cara de Banco (°): ', (70, 75, 80),  key = 'file_angle1')

  st.sidebar.text('\n\n')
  st.sidebar.text('Gráfico 2')
  file_dominio2 = st.sidebar.selectbox('Seleccione Dominio: ', ('Dominio 1', 'Dominio 2', 'Dominio 3', 'Dominio 4', 'Dominio 5'), key = 'file_dominio2')
  # file_ancho = st.sidebar.selectbox('Seleccione Ancho de Berma (m): ', (8.8, 9.2, 10.1, 10.6, 11.3, 11.6, 12.6))
  if file_dominio2 == 'Dominio 5':
    file_ancho2 = st.sidebar.selectbox('Seleccione Ancho de Berma (m): ', (8.8, 9.2, 10.6, 11.3, 12.6), key = 'file_ancho2')
  elif file_dominio2 == 'Dominio 4':
    file_ancho2 = st.sidebar.selectbox('Seleccione Ancho de Berma (m): ', (8.8, 9.2, 10.1, 10.6, 11.6, 12.6), key = 'file_ancho2')
  else:
    file_ancho2 = st.sidebar.selectbox('Seleccione Ancho de Berma (m): ', (8.8, 9.2, 10.1, 10.6, 11.3, 12.6), key = 'file_ancho2')
  ODOT_panel2 = st.sidebar.selectbox('Seleccionar ODOT: ', ('Si', 'No'), key = 'ODOT_panel2')
  file_angle2 = st.sidebar.selectbox('Seleccione Ángulo Cara de Banco (°): ', (70, 75, 80), key = 'file_angle2')

  data_base = load_data(uploaded_file)

  col1, col2, col3 = st.columns(3)
  with col2:
    
    #url = 'https://github.com/jeac1771/Odot_App/blob/main/logos/SRK_logo01.png'
    #image = Image.open(requests.get(url, stream=True).raw)
    image = Image.open('./logos/SRK_logo01.png')
    st.image(image, width=300)

  if RB_derrame_pof == 'Berma de diseño':
    plot_odot_plotly_LD(file_dominio, file_angle)

    col1, col2 = st.columns(2)
    with col1:
      plot_odot_plotly_unico_LD(file_dominio1, file_ancho1, file_angle1, data_base, ODOT_panel1, 'Gráfico 1')
    with col2:
      plot_odot_plotly_unico_LD(file_dominio2, file_ancho2, file_angle2, data_base, ODOT_panel2, 'Gráfico 2')

  elif RB_derrame_pof == 'PoF':
    plot_PoF_plotly_LD(file_dominio, file_angle)
    col1, col2 = st.columns(2)
    with col1:
      plot_PoF_plotly_unico(file_dominio1, file_ancho1, file_angle1, data_base, ODOT_panel1, 'Gráfico 1')
    with col2:
      plot_PoF_plotly_unico(file_dominio2, file_ancho2, file_angle2, data_base, ODOT_panel2, 'Gráfico 2')
