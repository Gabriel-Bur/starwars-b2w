import requests

def getAllPlanets():
    allplanets = []
        
    for page in range(1,8):
        response = requests.get("https://swapi.co/api/planets/?page="+str(page))
        data = response.json()
        for result in data['results']:
            allplanets.append(result)
        
            
    return allplanets

def getCountPlanets(name):
    
    allPlanets = getAllPlanets()
    
    
    for p in allPlanets:
        if p['name']==name:
            return len(p['films'])