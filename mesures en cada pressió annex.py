#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('time', '', '#importar galeries\nimport openpyxl\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom metpy.plots import SkewT\nfrom metpy.units import units\nimport seaborn as sns\n\n#Valors a canviar al canviar d\'any:\nestació="Albuquerque"\nany=2022\ndies_febrer=28\nexcel=openpyxl.load_workbook("2022_tfg_Albuquerque.xlsx")#obrim l\'excel\n')


# In[2]:


#pre mirar excel

#aquí miro quantes mesures hi ha de cada pressió per saber si val la pena o no

#fem molts arrays on hi posarem les coordenades en que hi ha cada pressió en el excel
proves700=[]
proves609=[]
proves600=[]
proves500=[]
proves400=[]
proves300=[]
proves200=[]
proves150=[]
proves100=[]
proves50=[]
proves40=[]
proves30=[]
proves20=[]
proves10=[]

#fem un loop
noms_fulls= excel.sheetnames#els noms dels fulls de l'excel
for full in noms_fulls:#loop per fer coses a cada full
    print(full)
    full=excel[full]#obrim el full de l'iteració
    columna=full["B"]#columna de l'excel on hi ha els numerets indicant la pressió

    for celda in columna:#per cada casella de la columna de les pressions
        if celda.value=="700.0":#mira si la pressió és 700hPa
            proves700=np.append(proves700,celda.coordinate)#posa el valor de les coordinades de la cela al array
    #ara segueix el mateix per cada pressió que farem:
    for celda in columna:
        if celda.value=="609.0":
            proves609=np.append(proves609,celda.coordinate)

    for celda in columna:
        if celda.value=="600.0":
            proves600=np.append(proves600,celda.coordinate)

    for celda in columna:
        if celda.value=="500.0":
            proves500=np.append(proves500,celda.coordinate)

    for celda in columna:
        if celda.value=="400.0":
            proves400=np.append(proves400,celda.coordinate)

    for celda in columna:
        if celda.value=="300.0":
            proves300=np.append(proves300,celda.coordinate)

    for celda in columna:
        if celda.value=="200.0":
            proves200=np.append(proves200,celda.coordinate)

    for celda in columna:
        if celda.value=="150.0":
            proves150=np.append(proves150,celda.coordinate)

    for celda in columna:
        if celda.value=="100.0":
            proves100=np.append(proves100,celda.coordinate)

    for celda in columna:
        if celda.value=="50.0":
            proves50=np.append(proves50,celda.coordinate)

    for celda in columna:
        if celda.value=="40.0":
            proves40=np.append(proves40,celda.coordinate)

    for celda in columna:
        if celda.value=="30.0":
            proves30=np.append(proves30,celda.coordinate)

    for celda in columna:
        if celda.value=="20.0":
            proves20=np.append(proves20,celda.coordinate)

    for celda in columna:
        if celda.value=="10.0":
            proves10=np.append(proves10,celda.coordinate)

#contem quants valors tenen les celes i així sabrem quants cops hi ha cada pressió
print("numero de mesures a 700hPa=",len(proves700))
print("numero de mesures a 609hPa=",len(proves609))
print("numero de mesures a 600hPa=",len(proves600))
print("numero de mesures a 500hPa=",len(proves500))
print("numero de mesures a 400hPa=",len(proves400))
print("numero de mesures a 300hPa=",len(proves300))
print("numero de mesures a 200hPa=",len(proves200))
print("numero de mesures a 150hPa=",len(proves150))
print("numero de mesures a 100hPa=",len(proves100))
print("numero de mesures a 50hPa=",len(proves50))
print("numero de mesures a 40hPa=",len(proves40))
print("numero de mesures a 30hPa=",len(proves30))
print("numero de mesures a 20hPa=",len(proves20))
print("numero de mesures a 10hPa=",len(proves10))


# In[3]:


#pre mirar excel

#quantes mesures hi ha per pressió?


noms_fulls= excel.sheetnames#els noms dels fulls de l'excel
quants=[]
quina=[]
for i in np.arange(700.0,850.0,step=1.0):
    provant=[]
    for full in noms_fulls:#loop per fer coses a cada full
        full=excel[full]#obrim el full de l'iteració
        columna=full["B"]#columna de l'excel on hi ha els numerets indicant la pressió
        for celda in columna:
            if celda.value==str(i):
                provant=np.append(provant,celda.coordinate)
    print(i, len(provant))
    quants=np.append(quants,len(provant))
    quina=np.append(quina,i)

plt.plot(quina,quants)
plt.grid()
plt.show

