'''
Decouverte Application Rest

@author: maelle
'''
from bottle import run,get,post,request

animals = [{'name' : 'Dumbo','type':'elephant'},
           {'name' : 'Python','type':'serpent'},
           {'name' : 'Zed','type':'zebre'}
           ]

@get('/animals')
def getAll():
    return {'animals':animals}

@get('/animal/<name>')
def getOne(name):
     
    the_animal = [animal for animal in animals if animal['name']==name]
    
    return {'animal' : the_animal[0]}

@post('/animal')
def addOne():
    new_animal = {'name': request.json.get('name'), 'type':request.json.get('type')}
    animals.append(new_animal)
    return {'animals':animals}


run(reloader=True,debug=True)