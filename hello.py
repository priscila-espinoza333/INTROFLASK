#primero debemos ejecutar el pipenv install flask
#luego pipenv shell
#luego py (nombre del archivor).py py hello.py


from flask import Flask  # Aca estoy importanto flask para crear una aplicación web

app = Flask(__name__) # aqui estoy creando una nueva instancia de la calse Flask llamada app

@app.route('/') # el decoador '@' asocia esa ruta con la funcion que vamos a tener inmediatamente  
def hola_mundo ():
    return 'Hola Mundo!'

@app.route('/hola/<nombre>') # para mi ruta /hola/__________ cualquier cosa despues de  /hola/ se va a pasar como variable nombre
def hola(nombre):
    return f'<h1>Hola {nombre}, cómo estás?</h1>' # la f nos permite que con las llaves poner el nombre de la variable de forma más sencilla
    #tambien puedo utilizar la etiquetas directamente aqui 









if __name__ =="__main__": # esto asegura que el archivo se esta ejecutando directamente y o de un modulo diferente
    app.run(debug=True) # esto ejecuta la aplicación
