
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import matplotlib.pyplot as plt

# -------------------------------------------------------------------------------------------------------------------------- 


def grafico1(df_pasiva): #Creamos un funcion que regresa una grafico
    Plot1 = plt.plot(df_pasiva['TIMESTAMP'],df_pasiva['REND']) #Graficamos el rendimiento atraves del tiempo
    plt.grid(color='r', linestyle='dotted', linewidth=1) #Le damos un poco de formato
    plt.show() #Para que nos muestre el grafico
    
    return (Plot1) #Regresa la variable con un nombre


# -------------------------------------------------------------------------------------------------------------------------- 



def grafico2(df_pasiva): #Creamos un funcion que regresa una grafico
    Plot2 = plt.bar(df_pasiva['TIMESTAMP'],df_pasiva['CAPITAL']) #Graficamos el capital atraves del tiempo
    plt.grid(color='r', linestyle='dotted', linewidth=1) #Le damos un poco de formato
    plt.show() #Para que nos muestre el grafico
    
    return (Plot2)#Regresa la variable con un nombre


# -------------------------------------------------------------------------------------------------------------------------- 



def grafico3(df_pasiva): #Creamos un funcion que regresa una grafico
    Plot3 = plt.plot(df_pasiva['TIMESTAMP'],df_pasiva['REND_ACUM']) #Graficamos el rendimiento acumulado atraves del tiempo
    plt.grid(color='g', linestyle='dotted', linewidth=1) #Le damos un poco de formato
    plt.show() #Para que nos muestre el grafico
    
    return (Plot3)


# -------------------------------------------------------------------------------------------------------------------------- 



def grafico4(df_pasiva_Final): #Creamos un funcion que regresa una grafico
    Plot4 = plt.bar(df_pasiva_Final['Ticker'],df_pasiva_Final['CAPITAL'])  #Visauliza la capital de cada tickers
    plt.grid(color='g', linestyle='dotted', linewidth=1) #Le damos un poco de formato
    plt.show() #Para que nos muestre el grafico
    
    return (Plot4)#Regresa la variable con un nombre



# -------------------------------------------------------------------------------------------------------------------------- 









