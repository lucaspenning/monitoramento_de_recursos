#Importando biblioteca Threads
from threading import Thread
#Importando biblioteca PSUTIL
import psutil
#Importando biblioteca Tempo
import time
#Importando biblioteca MYSQL para conexão com Banco de Dados MySql
import mysql.connector
from mysql.connector import Error

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
    
#Consultas no banco de dados
#% de uso da CPU
def consulta_cpu():
    try:
        consulta_sql = "SELECT Tempo, Uso_CPU_Percentual FROM `dados_coletados` WHERE Uso_CPU_Percentual > 80"
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print("Número total de registros retornados: ", cursor.rowcount)

        print("\nMostrando os dados cadastrados com uso = 80")
        for linha in linhas:
            print("Data:", linha[0])
            print("CPU %:",linha[1], "\n")
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
#% de uso do disco
def consulta_disco():
    try:
        consulta_sql = "SELECT Tempo, Disco_Percentual FROM `dados_coletados` WHERE Disco_Percentual > 70"
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print("Número total de registros retornados: ", cursor.rowcount)

        print("\nMostrando os dados cadastrados com uso Disco > 70")
        for linha in linhas:
            print("Data:", linha[0])
            print("Disco %:",linha[1], "\n")
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
#Uso máximo e minimo de RAM nos ultimos dois dias
def uso_min_max_ram_2_dias():
    try:
        consulta_sql = "SELECT MIN(RAM_Percentual), MAX(RAM_Percentual) FROM dados_coletados WHERE tempo BETWEEN NOW() - INTERVAL 2 DAY AND NOW()"
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        print("\nMostrando os dados cadastrados uso de RAM maximo e minimo nos ultimos 2 dias")
        for linha in linhas:
            print("Minimo_RAM:", linha[0])
            print("Maximo_RAM:",linha[1], "\n")
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
#Nivel abaixo de 30% da bateria
def bateria_abaixo_30():
    try:
        consulta_sql = "SELECT TEMPO, Bateria_Percentual FROM `dados_coletados` WHERE Bateria_Percentual < 30"
        cursor = mydb.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        
        print("Número total de registros retornados com menos de 30 de carga: ")
        for linha in linhas:
            print("Data:", linha[0])
            print("Bateria %:",linha[1], "\n")
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
            print("\nPorcentagem online:" + str(por_on))
        else:
            print("\nPorcentagem online: 0")

        if off > 0:
            por_off = (off/total)*100
            print("\nPorcentagem offline:" + str(por_off))
        else:
            print("\nPorcentagem offline: 0")
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)


#Loop de leitura infinito
tempo_leitura = 1
while (tempo_leitura == 1):
    #Chamados todas as Threads para coleta e salvamento de dados
    Thread(gravando_dados())
    #Consultado uso do Disco
    Thread(consulta_disco())
    #Consultando uso da CPU 
    Thread(consulta_cpu())
    #Consultando uso minimo e maximo de RAM nos ultimos 2 dias
    Thread(uso_min_max_ram_2_dias())
    #Consultando Tempo que a bateria obteve um % < 30
    Thread(bateria_abaixo_30())
    #Consultando porcentagem de carga/descarga da bateria
    Thread(bateria_rel())
    #Consultando porcentagem de online/offline do cabo de rede
    Thread(rede_rel())
    #Parando o código por 5 minuto
    time.sleep(5*60)
