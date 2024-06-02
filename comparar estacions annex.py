#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#convertir la info dels fitxers en matrius array
Albuquerque2022_00nit = np.genfromtxt('Albuquerque2022_00nit.csv', delimiter=',')
Grand_Junction2022_00nit = np.genfromtxt('Grand_Junction2022_00nit.csv', delimiter=',')
Dodge_City2022_00nit = np.genfromtxt('Dodge_City2022_00nit.csv', delimiter=',')

Albuquerque2022_12dia = np.genfromtxt('Albuquerque2022_12nit.csv', delimiter=',')
Grand_Junction2022_12dia = np.genfromtxt('Grand_Junction2022_00nit.csv', delimiter=',')
Dodge_City2022_12dia = np.genfromtxt('Dodge_City2022_12dia.csv', delimiter=',')


# In[3]:


#fer les restes que vulguem
Al_GJ_00=Albuquerque2022_00nit-Grand_Junction2022_00nit
Al_DC_00=Albuquerque2022_00nit-Dodge_City2022_00nit

Al_GJ_12=Albuquerque2022_12dia-Grand_Junction2022_12dia
Al_DC_12=Albuquerque2022_12dia-Dodge_City2022_12dia


# In[4]:


#coses necessàries per després fer les gràfiques
dies=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
mesos=["gener","febrer","març","abril","maig","juny","juliol","agost","setembre","octubre","novembre","desembre"]
mesos_31dies=["gener","març","maig","juliol","agost","octubre","desembre"]
mesos_30dies=["abril","juny","setembre","novembre"]
dies_febrer=28

dates_00=[]
dies_mesos=[0,]
a=0
for mes in mesos:
    if mes in mesos_31dies:
        dimes=31
    elif mes in mesos_30dies:
        dimes=30
    elif mes=="febrer":
        dimes=dies_febrer
    for i in np.arange(0,dimes):
        dates_00.append(mes + " " + dies[i])#per fer l'eix X de les gràfiques amb cada dia
    a+=dimes
    dies_mesos=np.append(dies_mesos,a)
print(dies_mesos)


pressionsTot=[830., 700., 610., 500., 400., 300., 200., 150., 100.,  50.,  30.,  20.]


# In[5]:


#gràfiques amb plot

custom_colors = ["k", "#8E477F","#AD589B" , "#CC6AAC","#E67EBD" ,"#FFA1CE" ,"#FFBDDA","darkgreen","yellowgreen","#00008B","#0000FF","#87CEFA","k"]

#fem un loop per graficar cada pressió
for i in np.arange(0,len(pressionsTot)):
    plt.plot(dates_00,Al_GJ_00[i,:], label=f'{pressionsTot[i]}hPa',color=custom_colors[i])

    #decoració
    plt.title("2022 00 nit diferència Albuquerque - Grand Junction")
    plt.xticks(dies_mesos,rotation=90)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.ylabel("Temperatura (ºC)")

    plt.grid(alpha=0.3)
    plt.show()

for i in np.arange(0,len(pressionsTot)):
    plt.plot(dates_00,Al_DC_00[i,:], label=f'{pressionsTot[i]}hPa',color=custom_colors[i])

    #decoració
    plt.title("2022 00 nit diferència Albuquerque - Dodge City")
    plt.xticks(dies_mesos,rotation=90)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.ylabel("Temperatura (ºC)")

    plt.grid(alpha=0.3)
    plt.show()

    
for i in np.arange(0,len(pressionsTot)):
    plt.plot(dates_00,Al_GJ_12[i,:], label=f'{pressionsTot[i]}hPa',color=custom_colors[i])

    #decoració
    plt.title("2022 12 dia diferència Albuquerque - Grand Junction")
    plt.xticks(dies_mesos,rotation=90)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.ylabel("Temperatura (ºC)")

    plt.grid(alpha=0.3)
    plt.show()
    
for i in np.arange(0,len(pressionsTot)):
    plt.plot(dates_00,Al_DC_12[i,:], label=f'{pressionsTot[i]}hPa',color=custom_colors[i])

    #decoració
    plt.title("2022 12 dia diferència Albuquerque - Dodge City")
    plt.xticks(dies_mesos,rotation=90)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.ylabel("Temperatura (ºC)")

    plt.grid(alpha=0.3)
    plt.show()


# In[6]:


mitj_Al_GJ_00=[]
mitj_Al_DC_00=[]
mitj_Al_GJ_12=[]
mitj_Al_DC_12=[]

with open("Albuquerque-Grand_Junction_00nit.txt", 'w') as file:
    file.write("A les 00 de la nit:" + "\n")
    file.write("Si restem les temperatures de Grand Juction a les d'Alburquerque la mitjana d'aquesta resta a diferents pressions és:" + "\n")
    for i in np.arange(0,len(pressionsTot)):
        pre=pressionsTot[i]
        mitj=np.nanmean(Al_GJ_00[i,:])
        mitj_Al_GJ_00=np.append(mitj_Al_GJ_00, mitj)
        file.write(f"a {pre} ="+ str(mitj) + "ºC" + "\n")


with open("Albuquerque-Dodge_city_00nit.txt", 'w') as file:
    file.write("A les 00 de la nit:" + "\n")
    file.write("Si restem les temperatures de Dodge City a les d'Alburquerque la mitjana d'aquesta resta a diferents pressions és:" + "\n")
    for i in np.arange(0,len(pressionsTot)):
        pre=pressionsTot[i]
        mitj=np.nanmean(Al_DC_00[i,:])
        mitj_Al_DC_00=np.append(mitj_Al_DC_00, mitj)
        file.write(f"a {pre} ="+ str(mitj) + "ºC" + "\n")
        
with open("Albuquerque-Grand_Junction_12dia.txt", 'w') as file:
    file.write("A les 12 del dia:" + "\n")
    file.write("Si restem les temperatures de Grand Juction a les d'Alburquerque la mitjana d'aquesta resta a diferents pressions és:" + "\n")
    for i in np.arange(0,len(pressionsTot)):
        pre=pressionsTot[i]
        mitj=np.nanmean(Al_GJ_12[i,:])
        mitj_Al_GJ_12=np.append(mitj_Al_GJ_12, mitj)
        file.write(f"a {pre} ="+ str(mitj) + "ºC" + "\n")


with open("Albuquerque-Dodge_city_12dia.txt", 'w') as file:
    file.write("A les 12 del dia:" + "\n")
    file.write("Si restem les temperatures de Dodge City a les d'Alburquerque la mitjana d'aquesta resta a diferents pressions és:" + "\n")
    for i in np.arange(0,len(pressionsTot)):
        pre=pressionsTot[i]
        mitj=np.nanmean(Al_DC_12[i,:])
        mitj_Al_DC_12=np.append(mitj_Al_DC_12, mitj)
        file.write(f"a {pre} ="+ str(mitj) + "ºC" + "\n")
    

plt.plot(np.array(pressionsTot, dtype=float),mitj_Al_GJ_00)
plt.title("Mitjana a cada pressió de Al-GJ a les 00 de la nit")
plt.xlabel("Pressions (hPa)")
plt.ylabel("Temperatura (ºC)")
plt.grid(alpha=0.3)
plt.show()

plt.plot(np.array(pressionsTot, dtype=float),mitj_Al_DC_00)
plt.title("Mitjana a cada pressió de Al-DC a les 00 de la nit")
plt.xlabel("Pressions (hPa)")
plt.ylabel("Temperatura (ºC)")
plt.grid(alpha=0.3)
plt.show()

plt.plot(np.array(pressionsTot, dtype=float),mitj_Al_GJ_12)
plt.title("Mitjana a cada pressió de Al-GJ a les 12 del migdia")
plt.xlabel("Pressions (hPa)")
plt.ylabel("Temperatura (ºC)")
plt.grid(alpha=0.3)
plt.show()

plt.plot(np.array(pressionsTot, dtype=float),mitj_Al_DC_12)
plt.title("Mitjana a cada pressió de Al-DC a les 12 del migdia")
plt.xlabel("Pressions (hPa)")
plt.ylabel("Temperatura (ºC)")
plt.grid(alpha=0.3)
plt.show()

