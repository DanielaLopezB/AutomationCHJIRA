#Autor: Daniela López Barahona
#seleccionEdit  retorna el código correspondiente para la seleción de Pais y Area responsable del cambio a crear.
#Marzo 2020


def EditCountryArea(typeI,DataI):
    
    #Pais
    if typeI == 'Country':
        if DataI == 'Argentina':
            return "customfield_24329-1"
        if DataI == 'Brazil':
            return "customfield_24329-2"
        if DataI == 'Caribbean':
            return "customfield_24329-3"
        if DataI == 'Chile':
            return "customfield_24329-4"
        if DataI == 'Colombia':
            return "customfield_24329-5"
        if DataI == 'Ecuador':
            return "customfield_24329-6"
        if DataI == 'Peru':
            return "customfield_24329-7"
        if DataI == 'Puerto Rico':
            return "customfield_24329-8"
        if DataI == 'Uruguay':
            return "customfield_24329-9"
        if DataI == 'USA':
            return "customfield_24329-10"
        if DataI == 'Venezuela':
            return "customfield_24329-11"
    #Area
    if typeI == 'Area':
        if DataI == 'Analytics & Reporting':
            return "customfield_24942-1"
        if DataI == 'Broadcast Center': 
            return "customfield_24942-2"
        if DataI == 'Customer Care': 
            return "customfield_24942-3"
        if DataI == 'Digital': 
            return "customfield_24942-4"
        if DataI == 'Finance': 
            return "customfield_24942-5"
        if DataI == 'IT': 
            return "customfield_24942-6"
        if DataI == 'Legal':
            return "customfield_24942-7"
        if DataI == 'Marketing & Programming': 
            return "customfield_24942-8"
        if DataI == 'Operations': 
            return "customfield_24942-9"
        if DataI == 'RH': 
            return "customfield_24942-10"
        if DataI == 'Security': 
            return "customfield_24942-11"