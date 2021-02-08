
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Laboratorio1                                                                               -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: PiedrasAyala95                                                                              -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/PiedrasAyala95/MyST_LAB1_APA                                         -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

from data import archivos, data_archivos
from functions import fecha1,Activos,yahoo,cierre,fecha2,p_adj_close,precios,Activo_No
from functions import passivo,peso,pasiva_2,dinero,operaciones,dataframe_pasiva
from visualizations import grafico1,grafico2,grafico3,grafico4


archivos = archivos #Mandamos a llamar la lista de archivos
data_archivos = data_archivos #Mandamos a llamar un diccionario donde contenemos todo  los archivos limpios
i_fechas = fecha1(archivos) #Mandamos a llamar una lista de fechas que la usaremos para otras funciones
global_tickers = Activos(archivos,data_archivos) #Manda a llamar todos los tickers unicos que tenemos en todos los archvios
Data_Yahoo = yahoo(global_tickers) #Manda a llamar una funcion donde descargamos los historicos de las acciones
Close = cierre(Data_Yahoo,global_tickers) #Manda a llamar una funcion donde contenemos unicamente el cierre de todas las acciones
Fechas_list = fecha2(Close,i_fechas) #Manda a llamar otra lista de fechas
Precio_Adj_Close = p_adj_close(Close,Fechas_list) #Manda a llamar una funcion donde contenemos unicamente el adj_close de todas las acciones
precios = precios(Precio_Adj_Close) #Manda a llamar una funcion donde contenemos unicamente el precio de todas las acciones
k = 1000000 #capital inicial
c = 0.00125 # comisiones por transaccion
List_Activos = Activo_No() # Manda a allmar una funcion donde tenemos una lista de activos que no queremos o necesitamos 
pasiva_p = passivo(k) #Mnada a llamr un diccionario 
Datos_Peso = peso(data_archivos,archivos,List_Activos) #Manda a llamar una funcion donde obtenemos los pesos % de cada activo
df_pasiva_Final = pasiva_2(Datos_Peso) #Manda a llamar una funcion donde nos ayudara a mantener los datos para futuras operacioenes
Dinero = dinero(df_pasiva_Final,precios,Fechas_list,k,c) #Nos regresa un numero 
df_operaciones = operaciones(df_pasiva_Final) #Mandamos a llamar un dataframe donde tenemos las columnas requeridas para las operaciones
df_pasiva = dataframe_pasiva(Fechas_list,precios,df_pasiva_Final,pasiva_p,Dinero,df_operaciones) #Mnadamos a llamar un dataframe donde contiene las operaciones de la pasiva
Plot1 = grafico1(df_pasiva) #Visauliza el comportamiento del rendimiento atraves del tiempo
Plot2 = grafico2(df_pasiva) #Visauliza el comportamiento de la capital atraves del tiempo
Plot3 = grafico3(df_pasiva) #Visauliza el comportamiento del rendimiento_acumulado atraves del tiempo
Plot4 = grafico4(df_pasiva_Final) #Visauliza la capital de cada tickers