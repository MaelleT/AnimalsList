'''
Decouverte Application Rest

@author: maelle
'''
from bottle import run,get

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


run(reloader=True,debug=True)