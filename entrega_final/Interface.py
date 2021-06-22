#Importando biblioteca Threads
from threading import Thread
#Importando biblioteca PSUTIL
import psutil
#Importando biblioteca Tempo
import time
import datetime
from datetime import datetime
#Importando biblioteca MYSQL para conexão com Banco de Dados MySql
import mysql.connector
from mysql.connector import Error
# Bibliotecas Tkinter
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
from tkinter import messagebox
#Biblioteca Matplot
import matplotlib.pyplot
from matplotlib.animation import FuncAnimation
import matplotlib.ticker as plticker
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chamando Janela
root = tk.Tk()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fonte do titulo
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
# Fonte Subtitulo
fontStyle_2 = tkFont.Font(family="Lucida Grande", size=15)
# Fonte topicos
fontStyle_3 = tkFont.Font(family="Lucida Grande", size=10)
# Fonte Dados
fontStyle_4 = tkFont.Font(family="Lucida Grande", size=35)
# Fonte Dados
fontStyle_5 = tkFont.Font(family="Lucida Grande", size=12)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Posicionamento e tamanho: y = linha e x = coluna & widht = largura e height = altura
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tamanho da Janela
root.geometry("750x500")
# Titulo
l1= tk.Label(root, text="Monitoramento De Dados", bg="White", fg="black", font=fontStyle).place(x = 0, y = 5, width=750, height=50)
# Label CPU
l2= tk.Label(root, text="Percentual Uso CPU:", bg="White", fg="black", font=fontStyle_3).place(x = 10, y = 60, width=138, height=20)
# Label RAM
l3= tk.Label(root, text="Percentual Uso RAM:", bg="White", fg="black", font=fontStyle_3).place(x = 158, y = 60, width=138, height=20)
# Label Disco
l3= tk.Label(root, text="Percentual Uso Disco:", bg="White", fg="black", font=fontStyle_3).place(x = 306, y = 60, width=138, height=20)
# Label Bateria
l4= tk.Label(root, text="Porcentagem Bateria:", bg="White", fg="black", font=fontStyle_3).place(x = 454, y = 60, width=138, height=20)
# Label Rede
l5= tk.Label(root, text="Percentual Uso Rede:", bg="White", fg="black", font=fontStyle_3).place(x = 602, y = 60, width=138, height=20)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Valor label CPU
l6= tk.Label(root, text="0%", bg="White", fg="black", font=fontStyle_4)
l6.place(x = 10, y = 80, width=138, height=70)
# Valor label RAM
l7= tk.Label(root, text="0%", bg="White", fg="black", font=fontStyle_4)
l7.place(x = 158, y = 80, width=138, height=70)
# Valor label Disco
l8= tk.Label(root, text="0%", bg="White", fg="black", font=fontStyle_4)
l8.place(x = 306, y = 80, width=138, height=70)
# Valor label Bateria
l9= tk.Label(root, text="0%", bg="White", fg="black", font=fontStyle_4)
l9.place(x = 454, y = 80, width=138, height=70)
# Valor label Rede
l10= tk.Label(root, text="0%", bg="White", fg="black", font=fontStyle_4)
l10.place(x = 602, y = 80, width=138, height=70)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Subtitulo
l11= tk.Label(root, text="Realizar Consulta Dos Dados Monitorados", bg="White", fg="black", font=fontStyle_2).place(x = 10, y = 160, width=380, height=30)
# Label seleção
l12= tk.Label(root, text="Selecionar Campo:", bg="White", fg="black", font=fontStyle_5).place(x = 10, y = 190, width=140, height=20)
#Seleção CAMPO
combo = ttk.Combobox(root, values=["Selecione", "Uso CPU", "Uso RAM", "Uso Disco", "Porcentagem Bateria", "Uso Rede"], state="readonly")
combo.place(x = 10, y = 215 , width=250, height=30)
combo.current(0) #set the selected item
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Label tipo
l12= tk.Label(root, text="Tipo:", bg="White", fg="black", font=fontStyle_5).place(x = 10, y = 250, width=50, height=20)
#Marcador Data
chk_state = tk.BooleanVar()
chk_state.set(False) #set check state
chk = tk.Checkbutton(root, text='Data', var=chk_state)
chk.place(x = 65, y = 250, width=70, height=30)
#Marcador Numeros
chk_numeros = tk.BooleanVar()
chk_numeros.set(False) #set check state
chk = tk.Checkbutton(root, text='Numeros', var=chk_numeros)
chk.place(x = 135, y = 250, width=70, height=30)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Texto METRICAS VALORES
l13 = tk.Label(root, text="Métricas Valores(Preencher Caso Selecionado):", bg="White", fg="black", font=fontStyle_5).place(x = 10, y = 280, width=350, height=20)
# MAIOR
l14 = tk.Label(root, text="Menor:", bg="White", fg="black", font=fontStyle_3).place(x = 10, y = 300, width=50, height=20)
txt1 = tk.Entry(root,width=10)
txt1.place(x = 60, y = 300, width=90, height=20)
# MENOR
l15 = tk.Label(root, text="Maior:", bg="White", fg="black", font=fontStyle_3).place(x = 10, y = 320, width=50, height=20)
txt2 = tk.Entry(root,width=10)
txt2.place(x = 60, y = 320, width=90, height=20)
#Texto METRICAS DATAS
l16 = tk.Label(root, text="Métricas Datas(Preencher Caso Selecionado):", bg="White", fg="black", font=fontStyle_5).place(x = 10, y = 350, width=330, height=20)
ll1 = tk.Label(root, text="Formato(AAAA-MM-DD)", bg="White", fg="black", font=fontStyle_3).place(x = 10, y = 370, width=150, height=20)
# MAIOR
l17 = tk.Label(root, text="Menor:", bg="White", fg="black", font=fontStyle_3).place(x = 10, y = 390, width=50, height=20)
txt3 = tk.Entry(root,width=10)
txt3.place(x = 60, y = 390, width=90, height=20)
# MENOR
l18 = tk.Label(root, text="Maior:", bg="White", fg="black", font=fontStyle_3).place(x = 10, y = 410, width=50, height=20)
txt4 = tk.Entry(root,width=10)
txt4.place(x = 60, y = 410, width=90, height=20)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Subtitulo
l19= tk.Label(root, text="Informaçãoes Atuais do Sistema", bg="White", fg="black", font=fontStyle_2).place(x = 370, y = 400, width=300, height=30)
# Label Status Bateria
l20= tk.Label(root, text="Status Da Bateria:", bg="White", fg="black", font=fontStyle_5).place(x = 370, y = 430, width=130, height=20)
l21= tk.Label(root, text="Null", bg="White", fg="black", font=fontStyle_5)
l21.place(x = 500, y = 430, width=170, height=20)
# Label Duração Bateria
l22= tk.Label(root, text="Duração Da Bateria:", bg="White", fg="black", font=fontStyle_5).place(x = 370, y = 450, width=145, height=20)
l23= tk.Label(root, text="Null", bg="White", fg="black", font=fontStyle_5)
l23.place(x = 515, y = 450, width=155, height=20)
# Label Status Cabo de Rede
l24= tk.Label(root, text="Cabo De Rede:", bg="White", fg="black", font=fontStyle_5).place(x = 370, y = 470, width=110, height=20)
l25= tk.Label(root, text="Null", bg="White", fg="black", font=fontStyle_5)
l25.place(x = 480, y = 470, width=190, height=20)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Configurações de conexão com banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dados_pc"
)

def gravando_dados():
    #Buscando porcentagem de uso da CPU
    Uso_CPU_Percentual = psutil.cpu_percent(interval=None)
    #Buscando informações da memoria RAM
    RAM = psutil.virtual_memory()
    RAM_Percentual = RAM.percent
    #Buscando informações do disco
    Disco = psutil.disk_usage('/')
    Disco_Percentual = Disco.percent
    #Buscando informações da bateria
    Bateria = psutil.sensors_battery()
    #Buscando percentual da bateria
    Bateria_Percentual = Bateria.percent 
    #Buscando tempo de duração da bateria
    if str(Bateria.secsleft) == 'BatteryTime.POWER_TIME_UNLIMITED':
        Bateria_Duracao = "Duração Infinita"
    else:
        Bateria_Duracao = (Bateria.secsleft/60)
        Bateria_Duracao = str(Bateria_Duracao) + 'Minutos'
    #Buscando se a bataria está conectado a fonte
    if str(Bateria.power_plugged) == 'False':
        Bateria_Status = "Descarregando"
    else:
        Bateria_Status = "Carregando"
    #Buscando Status de conexão de rede
    Rede = psutil.net_if_stats()['Ethernet']
    if str(Rede.isup) == 'True':
        Conectado_Rede = "Online"
    else:
        Conectado_Rede = "Offline"
    #Enviando dados para o MySql
    mycursor = mydb.cursor()
    sql = 'INSERT INTO dados_coletados(Uso_CPU_Percentual, RAM_Percentual, Disco_Percentual, Bateria_Percentual, Bateria_Duracao, Bateria_Status, Conectado_Rede) VALUES (%s, %s, %s, %s, %s, %s, %s )'
    sql_data = (Uso_CPU_Percentual, RAM_Percentual, Disco_Percentual, Bateria_Percentual, Bateria_Duracao, Bateria_Status, Conectado_Rede)
    mycursor.execute(sql, sql_data)
    mydb.commit()

#Vetores para os dados de tempo e valores
meses = []
valores = []
#Consultas no banco de dados
#% de uso da CPU
def consulta_cpu(menor_val , maior_val, menor_data, maior_data, opcao):
    meses.clear()
    valores.clear()
    try:
        if(opcao == 1):
            consulta_sql = "SELECT Tempo, Uso_CPU_Percentual FROM `dados_coletados` WHERE Uso_CPU_Percentual > " + menor_val + " AND Uso_CPU_Percentual < "+ maior_val
        if(opcao == 2):
            consulta_sql = "SELECT Tempo, Uso_CPU_Percentual FROM `dados_coletados` WHERE Tempo BETWEEN ('"+menor_data+"') AND ('"+maior_data+"')"
        if(opcao == 3):
            consulta_sql = "SELECT Tempo, Uso_CPU_Percentual FROM `dados_coletados` WHERE Tempo BETWEEN ('"+menor_data+"') AND ('"+maior_data+"') AND Uso_CPU_Percentual BETWEEN "+menor_val+" AND "+maior_val
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        if(cursor.rowcount == 0):
            txt_rol.insert(INSERT,"Sem registros encontrados")
        else:
            for linha in linhas:
                txt_rol.insert(INSERT,"\n" +str(linha[0])+" -> "+str(linha[1])+"%")
                meses_vetor = (str(linha[0]))
                meses.append(meses_vetor)
                valores_vetor = (float(linha[1])) 
                valores.append(valores_vetor)
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)

#% de uso do disco
def consulta_disco(menor_val , maior_val, menor_data, maior_data, opcao):
    meses.clear()
    valores.clear()
    try:
        if(opcao == 1):
            consulta_sql = "SELECT Tempo, Disco_Percentual FROM `dados_coletados` WHERE Disco_Percentual > " + menor_val + " AND Disco_Percentual < "+ maior_val
        if(opcao == 2):
            consulta_sql = "SELECT Tempo, Disco_Percentual FROM `dados_coletados` WHERE Tempo BETWEEN ('"+menor_data+"') AND ('"+maior_data+"')"
        if(opcao == 3):
            consulta_sql = "SELECT Tempo, Disco_Percentual FROM `dados_coletados` WHERE Tempo BETWEEN ('"+menor_data+"') AND ('"+maior_data+"') AND Disco_Percentual BETWEEN "+menor_val+" AND "+maior_val
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        if(cursor.rowcount == 0):
            txt_rol.insert(INSERT,"Sem registros encontrados")
        else:
            for linha in linhas:
                txt_rol.insert(INSERT,"\n" +str(linha[0])+" -> "+str(linha[1])+"%")
                meses_vetor = (str(linha[0]))
                meses.append(meses_vetor)
                valores_vetor = (float(linha[1])) 
                valores.append(valores_vetor)
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)

#% de uso da RAM
def consulta_ram(menor_val , maior_val, menor_data, maior_data, opcao):
    meses.clear()
    valores.clear()
    try:
        if(opcao == 1):
            consulta_sql = "SELECT Tempo, RAM_Percentual FROM `dados_coletados` WHERE RAM_Percentual > " + menor_val + " AND RAM_Percentual < "+ maior_val
        if(opcao == 2):
            consulta_sql = "SELECT Tempo, RAM_Percentual FROM `dados_coletados` WHERE Tempo BETWEEN ('"+menor_data+"') AND ('"+maior_data+"')"
        if(opcao == 3):
            consulta_sql = "SELECT Tempo, RAM_Percentual FROM `dados_coletados` WHERE Tempo BETWEEN ('"+menor_data+"') AND ('"+maior_data+"') AND RAM_Percentual BETWEEN "+menor_val+" AND "+maior_val
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        if(cursor.rowcount == 0):
            txt_rol.insert(INSERT,"Sem registros encontrados")
        else:
            for linha in linhas:
                txt_rol.insert(INSERT,"\n" +str(linha[0])+" -> "+str(linha[1])+"%")
                meses_vetor = (str(linha[0]))
                meses.append(meses_vetor)
                valores_vetor = (float(linha[1])) 
                valores.append(valores_vetor)
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)

#Nivel Bateria
def consulta_bateria(menor_val , maior_val, menor_data, maior_data, opcao):
    meses.clear()
    valores.clear()
    try:
        if(opcao == 1):
            consulta_sql = "SELECT Tempo, Bateria_Percentual FROM `dados_coletados` WHERE Bateria_Percentual > " + menor_val + " AND Bateria_Percentual < "+ maior_val
        if(opcao == 2):
            consulta_sql = "SELECT Tempo, Bateria_Percentual FROM `dados_coletados` WHERE Tempo BETWEEN ('"+menor_data+"') AND ('"+maior_data+"')"
        if(opcao == 3):
            consulta_sql = "SELECT Tempo, Bateria_Percentual FROM `dados_coletados` WHERE Tempo BETWEEN ('"+menor_data+"') AND ('"+maior_data+"') AND Bateria_Percentual BETWEEN "+menor_val+" AND "+maior_val
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        if(cursor.rowcount == 0):
            txt_rol.insert(INSERT,"Sem registros encontrados")
        else:
            for linha in linhas:
                txt_rol.insert(INSERT,"\n" +str(linha[0])+" -> "+str(linha[1])+"%")
                meses_vetor = (str(linha[0]))
                meses.append(meses_vetor)
                valores_vetor = (float(linha[1])) 
                valores.append(valores_vetor)
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)

#Rede
def consulta_rede(menor_data, maior_data):
    try:
        consulta_sql = "SELECT Tempo, Conectado_Rede FROM `dados_coletados` WHERE Tempo BETWEEN ('"+menor_data+"') AND ('"+maior_data+"')"
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        if(cursor.rowcount == 0):
            txt_rol.insert(INSERT,"Sem registros encontrados")
        else:
            for linha in linhas:
                txt_rol.insert(INSERT,"\n" +str(linha[0])+" -> "+str(linha[1]))
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)

#Relação de porcentagem ao tempo de carga/descaraga da bateria
def bateria_rel():
    try:
        consulta_sql = "SELECT COUNT(*) AS 'Descarregando' FROM dados_coletados WHERE Bateria_Status = 'descarregando'"
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            descarga = float(linha[0])
    
        consulta_sql = "SELECT COUNT(*) AS 'Carregando' FROM dados_coletados WHERE Bateria_Status = 'carregando'"
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            carga = float(linha[0])

        total = carga + descarga
        if descarga > 0 :
            por_des = (descarga/total)*100
            print("\nPorcentagem descarregando:" + str(por_des))
        else:
            print("\nPorcentagem descarregando: 0")
        if carga > 0 :
            por_car = (carga/total)*100
            print("\nPorcentagem carregando:" + str(por_car))
        else:
            print("\nPorcentagem carregando: 0")
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)

#Relação ao tempo da conexão/desconexão de rede
def rede_rel():
    try:
        consulta_sql = "SELECT COUNT(*) AS 'Online' FROM dados_coletados WHERE Conectado_rede = 'online'"
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            on = float(linha[0])
    
        consulta_sql = "SELECT COUNT(*) AS 'Offline' FROM dados_coletados WHERE Conectado_rede = 'offline'"
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            off = float(linha[0])

        total = on + off
        if on > 0 :
            por_on = (on/total)*100
            #print("\nPorcentagem online:" + str(por_on))
            return str(por_on)[0:4]
        else:
            #print("\nPorcentagem online: 0")
            return 0
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)

# Função do botão ATUALIZAR para atualizar os valores
def atualizar():
    #Inserindo porcentagem no label de uso da CPU
    Uso_CPU_Percentual = psutil.cpu_percent(interval=None)
    l6.configure(text=str(Uso_CPU_Percentual) + "%")
    #Inserindo informações no label da memoria RAM
    RAM = psutil.virtual_memory()
    RAM_Percentual = RAM.percent
    l7.configure(text=str(RAM_Percentual) + "%")   
    #Inserindo informações no label do disco
    Disco = psutil.disk_usage('/')
    Disco_Percentual = Disco.percent
    l8.configure(text=str(Disco_Percentual) + "%")   
    #Inserindo informações no label da bateria
    Bateria = psutil.sensors_battery()
    Bateria_Percentual = Bateria.percent 
    l9.configure(text=str(Bateria_Percentual) + "%")
    #Inserindo informações no label da Rede
    temp = rede_rel()
    l10.configure(text=str(temp) + "%")
    #Buscando se a bataria está conectado a fonte
    if str(Bateria.power_plugged) == 'False':
        Bateria_Status = "Descarregando"
    else:
        Bateria_Status = "Carregando"
    l21.configure(text=str(Bateria_Status))
    #Buscando tempo de duração da bateria
    if str(Bateria.secsleft) == 'BatteryTime.POWER_TIME_UNLIMITED':
        Bateria_Duracao = "∞"
    else:
        Bateria_Duracao = (Bateria.secsleft/60)
        Bateria_Duracao = str(Bateria_Duracao) + 'Minutos'
    l23.configure(text=str(Bateria_Duracao)[0:5]+ ' Minutos')
    #Buscando Status de conexão de rede
    Rede = psutil.net_if_stats()['Ethernet']
    if str(Rede.isup) == 'True':
        Conectado_Rede = "Online"
    else:
        Conectado_Rede = "Offline"
    l25.configure(text=str(Conectado_Rede))

#Função do botão Buscar
def buscar():
    #Checagem dos campos
    if(str(chk_state.get()) == "False" and str(chk_numeros.get()) == "False"):
        messagebox.showerror('ERRO', 'Verifique o preenchimento do campos TIPOS!')
    if(str(chk_state.get()) == "True" and (txt3.get()=="" or txt4.get()=="")):
        messagebox.showerror('ERRO', 'Verifique o preenchimento do campos de DATA!')
    if(str(chk_numeros.get()) == "True" and (txt1.get()=="" or txt2.get()=="")):
        messagebox.showerror('ERRO', 'Verifique o preenchimento do campos VALORES!')
    if(str(chk_numeros.get()) == "True" and combo.get() == "Uso Rede"):
        messagebox.showerror('ERRO', 'Não é possivel buscar por numeros em USO DE REDE!')
    if(combo.get() == "Selecione"):
        messagebox.showerror('ERRO', 'Verifique a SELEÇÃO DO CAMPO!')
    #Pegando os dados dos campos valor e data
    menor_val = txt1.get()
    maior_val = txt2.get()
    menor_data = txt3.get()
    maior_data = txt4.get()
    #Verificando campo e Buscando dados 
    if(combo.get() == "Uso CPU"):
        txt_rol.delete (1.0, END)
        if(str(chk_state.get()) == "False" and str(chk_numeros.get()) == "True"):
            consulta_cpu(menor_val, maior_val, menor_data, maior_data, 1)
        if(str(chk_state.get()) == "True" and str(chk_numeros.get()) == "False"):
            consulta_cpu(menor_val, maior_val, menor_data, maior_data, 2)
        if(str(chk_state.get()) == "True" and str(chk_numeros.get()) == "True"):
            consulta_cpu(menor_val, maior_val, menor_data, maior_data, 3)
    if(combo.get() == "Uso RAM"):
        txt_rol.delete (1.0, END)
        if(str(chk_state.get()) == "False" and str(chk_numeros.get()) == "True"):
            consulta_ram(menor_val, maior_val, menor_data, maior_data, 1)
        if(str(chk_state.get()) == "True" and str(chk_numeros.get()) == "False"):
            consulta_ram(menor_val, maior_val, menor_data, maior_data, 2)
        if(str(chk_state.get()) == "True" and str(chk_numeros.get()) == "True"):
            consulta_ram(menor_val, maior_val, menor_data, maior_data, 3)
    if(combo.get() == "Uso Disco"):
        txt_rol.delete (1.0, END)
        if(str(chk_state.get()) == "False" and str(chk_numeros.get()) == "True"):
            consulta_disco(menor_val, maior_val, menor_data, maior_data, 1)
        if(str(chk_state.get()) == "True" and str(chk_numeros.get()) == "False"):
            consulta_disco(menor_val, maior_val, menor_data, maior_data, 2)
        if(str(chk_state.get()) == "True" and str(chk_numeros.get()) == "True"):
            consulta_disco(menor_val, maior_val, menor_data, maior_data, 3)
    if(combo.get() == "Porcentagem Bateria"):
        txt_rol.delete (1.0, END)
        if(str(chk_state.get()) == "False" and str(chk_numeros.get()) == "True"):
            consulta_bateria(menor_val, maior_val, menor_data, maior_data, 1)
        if(str(chk_state.get()) == "True" and str(chk_numeros.get()) == "False"):
            consulta_bateria(menor_val, maior_val, menor_data, maior_data, 2)
        if(str(chk_state.get()) == "True" and str(chk_numeros.get()) == "True"):
            consulta_bateria(menor_val, maior_val, menor_data, maior_data, 3)
    if(combo.get() == "Uso Rede"):
        txt_rol.delete (1.0, END)
        if(str(chk_state.get()) == "True" and str(chk_numeros.get()) == "False"):
            consulta_rede(menor_data, maior_data)

#Função do botão Gerar Gráficos
def gerar_graficos():
    figure, ax = matplotlib.pyplot.subplots(figsize=(12,6))
    matplotlib.pyplot.plot(meses, valores)
    loc = plticker.MultipleLocator(base=50.0) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    matplotlib.pyplot.show()

#Vetores para dados do gráfico de tempo real
x = []
y = []
w = []
a = []
label = 'true'
#Função do botão Gráficos em tempo real
def tempo_real():
    global label
    label = 'true'
    figure, ax = matplotlib.pyplot.subplots(figsize=(12,6))
    #Loop para gráfico de tempo real
    def func_animate(i):
        x.append(psutil.cpu_percent(interval=None))
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = str(data_e_hora_atuais.strftime('%H:%M:%S'))
        y.append(data_e_hora_em_texto)
        matplotlib.pyplot.plot(y, x, label = "CPU", color="blue")
        RAM = psutil.virtual_memory()
        w.append(RAM.percent)
        matplotlib.pyplot.plot(y, w, label = "RAM", color="green")
        Disco = psutil.disk_usage('/')
        a.append(Disco.percent)
        matplotlib.pyplot.plot(y, a, label = "Disco", color="black")
        #Definindo Label das linhas para uma única vez 
        global label
        if(label == 'true'):
            label = 'false'
            matplotlib.pyplot.legend()
        matplotlib.pyplot.pause(1)
    ani = FuncAnimation(figure, func_animate, frames=10, interval=50)
    loc = plticker.MultipleLocator(base=10.0) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    matplotlib.pyplot.show()

# Preencher Valores automaticamente
atualizar()
# Caixa de Texto com barra de rolagem
txt_rol = scrolledtext.ScrolledText(root,width=40,height=10)
txt_rol.place(x = 400, y = 185, width=325, height=200)
txt_rol.insert(INSERT, 'Resultados da Busca:')
# Botão Refresh
Button1 = tk.Button(root, text="Atualizar Valores", command=atualizar, bg="Black", fg="white")
Button1.place(x = 602, y = 150, width=138, height=30)
# Botão Buscar
Button1 = tk.Button(root, text="Buscar", command=buscar, bg="Black", fg="white")
Button1.place(x = 10, y = 450, width=100, height=30)
# Botão Gerar Gráficos
Button1 = tk.Button(root, text="Gerar Gráficos", command=gerar_graficos, bg="Black", fg="white")
Button1.place(x = 120, y = 450, width=100, height=30)
# Botão Gerar Gráficos Em Tempo Real
Button1 = tk.Button(root, text="Gráficos Tempo Real", command=tempo_real, bg="Black", fg="white")
Button1.place(x = 230, y = 450, width=120, height=30)
#Chamando Interface Tkinter
root.mainloop()

#Loop de leitura infinito
tempo_leitura = 1
while (tempo_leitura == 1):
    #Chamados todas as Threads para coleta e salvamento de dados
    Thread(gravando_dados())
    #Parando o código por 5 minutos
    time.sleep(5*60)