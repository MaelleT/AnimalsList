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

run(reloader=True,debug=True)