#Autor: Daniela López Barahona - EQUIPO PROYECTOS
#creacionCHNormal crea cambios tipo NORMALES en JIRA, teniendo en cuenta los datos diligenciados en un documento excel.
#Junio 2020

# ------------------------ IMPORTS-------------------------------
import time

from seleccionEdit import EditCountryArea

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


#Función CreationCH ejecuta cada uno de los pasos necesarios para crear un cambio normal en JIRA
def CreationCH(dataCH, tasks, countRB):
    try:
        #Datos 
        username = dataCH[0][1]
        password = dataCH[1][1] 
        user = username + '@directvla.com.co'
        nameCH = dataCH[2][1] 

        #Driver 
        driver = webdriver.Chrome("./resources/chromedriver.exe")
        driver.set_window_size(1152, 840)
        
        
        #Abre página Jira
        driver.get("https://directvla.jira.com/projects/CH/board")

        #Confirma que si es la página Login
        assert "Log in to continue - Log in with Atlassian account" in driver.title

        driver.implicitly_wait(20)
        
        #Página Loggging Jira
        driver.find_element_by_id("username").send_keys(user)
        driver.find_element_by_xpath("//*[@id='login-submit']/span/span/span").click()
            
        #Página Loggging Jira-Username/Password
        eleUsername = WebDriverWait(driver, 5).until(
             EC.presence_of_element_located((By.ID, "userid"))
        )
        eleUsername.send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "submit-btn").click()

        time.sleep(10)
        #Click Crear cambio
        eleCreate = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(( By.CSS_SELECTOR, "#createGlobalItem .css-t5emrf"))
        )
        eleCreate.click()
       
        time.sleep(5)   
        #Ingreso datos CH  y su creación
        driver.find_element(By.CSS_SELECTOR, "#issuetype-single-select > .icon").click() #Issue Type
        driver.find_element(By.ID, "issuetype-field").send_keys("Normal Change Request")
        driver.find_element(By.ID, "issuetype-field").send_keys(Keys.ENTER) 
        time.sleep(2)
        driver.find_element(By.ID, "summary").send_keys(nameCH)
        driver.find_element(By.ID, "customfield_25269-2").click()
        driver.find_element(By.ID, "create-issue-submit").click()
        
        #Seleciona y redirecciona al CH creado
        eleSel = WebDriverWait(driver, 5).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".issue-created-key"))
        )
        eleSel.click()

        #Establecer old view
        driver.implicitly_wait(20)
        urlch = driver.current_url
        urlch = urlch + '?oldIssueView=true'  
        driver.get(urlch) 
  
        #Seleciona crear sub.task
        eleSub = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "#opsbar-operations_more > .icon"))
        )
        eleSub.click()
        driver.find_element(By.ID, "create-subtask").click()

        time.sleep(10)
        #Creación de subtareas
        countT = 0
        countP = 1
        numT = len(tasks) - 1
            
        for task,group,typeT,hourS,hourF,descriptionT in tasks:
                
            summaryD = task + " - " + group
            descriptionR = "Ejecutar las tareas descritas en el documento adjunto."    
                    
            time.sleep(8)   
            driver.find_element(By.CSS_SELECTOR, "#issuetype-single-select > .icon").click() #Issue Type
            driver.find_element(By.ID, "issuetype-field").send_keys(task)
            driver.find_element(By.ID, "issuetype-field").send_keys(Keys.ENTER)             
                
            if task == 'Schedule Assessment' or task == 'Technical Assessment' or task == 'Authorization':
                
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR, "#summary").send_keys(summaryD) #Summary
                driver.find_element(By.ID, "description").send_keys(summaryD)
                
                time.sleep(1)

                if task == 'Technical Assessment' : 
                    selAss = Select(driver.find_element_by_id('customfield_24683')) #Assessment Type
                    selAss.select_by_visible_text(typeT)
                    
                if task == 'Schedule Assessment' or task == 'Technical Assessment' :
                    selGroup = Select(driver.find_element_by_id('customfield_25033')) # Owner group selector
                    selGroup.select_by_visible_text(group)
                        
                if task == 'Authorization' :
                    selGroup = Select(driver.find_element_by_id('customfield_25122')) #Owner gruop selector
                    selGroup.select_by_visible_text(group)           
                
            if task == 'Implementation Activity' or task == 'Validation Activity' or task == 'RollBack Activity':
                
                if task == 'Implementation Activity':
                    nameRO = str(countP) + ". RollOut - " + typeT + " - " + group
                    
                if task == 'Validation Activity':
                    nameRO = str(countP) + ". " + task + " - " + group
                    descriptionR = "Validar las tareas desplegadas."
                    
                if task == 'RollBack Activity':
                    nameRO = str(countP) + ". " + task + " - "  + typeT + " - " + group
                    countRB -= 1
                    
                if descriptionT != None :
                    descriptionR = descriptionT
                
                time.sleep(5)
                driver.find_element(By.CSS_SELECTOR, "#summary").send_keys(nameRO) #Summery
                driver.find_element(By.ID, "description").send_keys(descriptionR) #Description
                    
                hourS = hourS.strftime("%d/%b/%y %I:%M %p")
                driver.find_element(By.ID, "customfield_24668").clear() #Start Date
                driver.find_element(By.ID, "customfield_24668").click()
                driver.find_element(By.ID, "customfield_24668").send_keys(hourS)
                    
                hourF = hourF.strftime("%d/%b/%y %I:%M %p")
                driver.find_element(By.ID, "customfield_24667").clear() #Finish Date
                driver.find_element(By.ID, "customfield_24667").click()
                driver.find_element(By.ID, "customfield_24667").send_keys(hourF)
                    
                selGroup = Select(driver.find_element_by_id('customfield_25033')) #Owner gruop selector
                selGroup.select_by_visible_text(group)
                countP += 1         
                
            if countT == 0:
                driver.find_element(By.CSS_SELECTOR, ".qf-create-another").click() #Create another sub-task
            if countRB == 0 and countT == numT:
                driver.find_element(By.CSS_SELECTOR, ".qf-create-another").click() #No Create another sub-task
                    
            countT += 1

            driver.find_element(By.ID, "create-issue-submit").click()  #Create a subtask buttom              

        time.sleep(16)
        #Modifica la opción Edit 
        driver.find_element(By.ID, "action_id_231").click()

        time.sleep(10)
        driver.find_element(By.ID, "description").click() #Description
        driver.find_element(By.ID, "description").send_keys(dataCH[3][1])
            
        selGroup = Select(driver.find_element_by_id('customfield_25033')) # Owner group selector
        selGroup.select_by_visible_text(dataCH[4][1])
            
        sDate = dataCH[5][1].strftime("%d/%b/%y %I:%M %p")
        driver.find_element(By.ID, "customfield_24668").click() # Start date and time
        driver.find_element(By.ID, "customfield_24668").send_keys(sDate)
            
        fDate = dataCH[6][1].strftime("%d/%b/%y %I:%M %p")
        driver.find_element(By.ID, "customfield_24667").click() # End date and time
        driver.find_element(By.ID, "customfield_24667").send_keys(fDate)
            
        ofDate = dataCH[7][1].strftime("%d/%b/%y %I:%M %p")
        driver.find_element(By.ID, "customfield_24775").click() #Outage date from
        driver.find_element(By.ID, "customfield_24775").send_keys(ofDate)
            
        otDate = dataCH[8][1].strftime("%d/%b/%y %I:%M %p")
        driver.find_element(By.ID, "customfield_24776").click() #Outage date to
        driver.find_element(By.ID, "customfield_24776").send_keys(otDate)
            
        typeI = "Country" #Country
        css = EditCountryArea(typeI,dataCH[9][1])
        driver.find_element(By.ID, css).click() 
            
        typeI = "Area" #Impacted Business Area
        css = EditCountryArea(typeI,dataCH[10][1])
        driver.find_element(By.ID, css).click()
            
        selService = Select(driver.find_element_by_id('customfield_24995')) #Service
        selService.deselect_by_visible_text('None')
        selService.select_by_visible_text(dataCH[11][1])      
                
        selApp = Select(driver.find_element_by_id('customfield_24924')) #Application
        selApp.deselect_by_visible_text('None')
        selApp.select_by_visible_text(dataCH[12][1])  
                    
        selIPrac = Select(driver.find_element_by_id('customfield_24654')) #Input Practice
        selIPrac.select_by_visible_text(dataCH[13][1])      
            
        selIT = Select(driver.find_element_by_id('customfield_24685')) #Impact Type
        selIT.select_by_visible_text(dataCH[14][1])
            
        selEnv = Select(driver.find_element_by_id('customfield_24686')) #Environment
        selEnv.select_by_visible_text(dataCH[15][1])
            
        selRisk = Select(driver.find_element_by_id('customfield_24690')) #Risk
        selRisk.select_by_visible_text(dataCH[16][1])
            
        selImp = Select(driver.find_element_by_id('customfield_24687')) #Impac
        selImp.select_by_visible_text(dataCH[17][1])
            
        selUrg = Select(driver.find_element_by_id('customfield_24688')) #Urgency
        selUrg.select_by_visible_text(dataCH[18][1])
            
        selChC = Select(driver.find_element_by_id('customfield_24691')) #Change Category
        selChC.select_by_visible_text(dataCH[19][1])
            
        driver.find_element(By.ID, "customfield_24656").click() #Change Reason
        driver.find_element(By.ID, "customfield_24656").send_keys(dataCH[20][1])
            
        selPA = Select(driver.find_element_by_id('customfield_24655')) #Probability of anomalies
        selPA.select_by_visible_text(dataCH[21][1])
            
        driver.find_element(By.ID, "customfield_24692").click() #Effect of non-implementation
        driver.find_element(By.ID, "customfield_24692").send_keys(dataCH[22][1])
            
        driver.find_element(By.ID, "issue-workflow-transition-submit").click() #Submit información Edit

        driver.implicitly_wait(20)

        url = driver.current_url
        
        estado = "Se creó el cambio correctamente."  

        return estado, url
    
    except Exception as error:
        return "No se creó correctamente el cambio. ", error