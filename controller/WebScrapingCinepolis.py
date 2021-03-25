# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver_path = 'C:/Users/Administrador/Downloads/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
# Inicializamos el navegador
driver.get('https://www.cinepolis.com.sv/cartelera/')

#selecciona san salvador
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'input#cityBillboardSearch.el-input__inner')))\
            .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, 
    '/html/body/div[2]/div[1]/div[1]/ul/li[1]')))\
        .click()

        
#selecciona todos los cines
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'input#cinemaBillboardSearch.el-input__inner')))\
            .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, 
    '/html/body/div[3]/div[1]/div[1]/ul/li[1]')))\
        .click()


#Obtenemos titulo
titulo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.billboard-page_content_title')))
#print(titulo.text)       


# ------------------Recorrer Todas las peliculas -------------------------------------
#obtenemos todas las peliculas
listPeliculas = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.row.paddingCard div')))
listIdPeliculas = []
listPeliculasNombreAlt = []
listPeliculasImg = []
listHorarios = []
listHorarioCine = []
nombrePelicula = ""
nombreCine = ""

for element in listPeliculas: #obtenemos los id de cada div de las peliculas
    if(element.get_attribute('id') != ""):
        listIdPeliculas.append(element.get_attribute('id'))

#print(listIdPeliculas)
#cadenaPath = ".row.paddingCard div#" +listIdPeliculas[0] + " div img"
#print(cadenaPath)

#como estan en imagenes vamos a obtener los alt
textoQuitar = "Poster de la película "
textoAsignar = "" 


for element in listIdPeliculas:
    listPeliculasImg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".row.paddingCard div#" + element + " div img")))
    listPeliculasNombreAlt.append(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".row.paddingCard div#" + element + " div img"))).get_attribute('alt').replace(textoQuitar, textoAsignar))

print(listPeliculasNombreAlt)

for element in listIdPeliculas:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".row.paddingCard div#" + element + " div img"))).click()
    listHorarios = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div ul.list-group.list-group-flush li')))
    
    for item in listHorarios:
        nombrePelicula = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.movie-details div h1'))).text
        nombreCine = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'ul.list-group.list-group-flush li div.d-flex div h3'))).text
        listHorarioCine = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'ul.list-group.list-group-flush li div div div')))
        print(listHorarioCine)

    #driver.execute_script("window.history.go(-1)") #retroceder

#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".row.paddingCard div#" + listIdPeliculas[0] + " div img"))).click()




#crear archivo excel
#df = pd.DataFrame({'Cartelera': listPeliculasNombreAlt})
#df.to_csv('cartelera cinepolis.csv', index  = False, encoding = 'utf-8')


#divPelicula = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#getTicket_2856')))
#print(divPelicula.get_attribute('id'))




#misPelis = driver.find_element_by_class_name('paddingCard')

#print(misPelis)















#seleccionar la tercer pelicula 
#WebDriverWait(driver, 10)\    .until(EC.element_to_be_clickable((By.XPATH,     '/html/body/main/div/div/div[5]/section[5]/div/div/div[3]/div[1]/img')))\
        #.click()
#seleccionar dia
#WebDriverWait(driver, 10)\    .until(EC.element_to_be_clickable((By.XPATH,     '/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div/label/div[2]')))\
       # .click()
#seleccionar hora
#WebDriverWait(driver, 10)\
    #.until(EC.element_to_be_clickable((By.XPATH, 
    #'/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div/div[2]/div/label')))\
       # .click()
#selecciona botton "comprar boletos"
#WebDriverWait(driver, 10)\
  #  .until(EC.element_to_be_clickable((By.XPATH, 
  #  '/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[5]/button')))\
     #   .click()

#path de la tabla donde estan los asientos
# /html/body/main/div/div/div[5]/div/div[4]/div/div/div[4]/div/div        

#path del dia
# 
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/label/div[2]
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div/label/div[2]

#path de la hora 
# 
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[1]/div[2]/div[1]/label  doblada
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[1]/div[2]/div[2]/label  doblada
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[2]/div[2]/div   /label     sub

# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[2]/div[2]/div   /div[2]/div[1]/label     dob
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[2]/div[2]/div   /div[2]/div[2]/label     dob
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[2]/div[2]/div   /div[2]/div[3]/label     dob

# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[3]/div[2]/div   /div[2]/div[1]/label     dob
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[3]/div[2]/div   /div[2]/div[2]/label     dob
#                                                                                     /cines       /dob o sub
#                                                                                                                /hora

#path de pelicula

# /html/body/main/div/div/div[5]/section[5]/div/div/div[1]/div[2]/button
# /html/body/main/div/div/div[5]/section[5]/div/div/div[2]/div[2]/button
# /html/body/main/div/div/div[5]/section[5]/div/div/div[9]/div[2]/button
# /html/body/main/div/div/div[5]/section[5]/div/div/div[1]/div[1]/img
