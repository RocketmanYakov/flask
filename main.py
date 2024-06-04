from flask import Flask
import random

app = Flask(__name__)

flist = ["Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
         "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
         "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
         "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo"]

@app.route("/")
def hello_world():
    return f'<h1>Hola! En esta pagina podrás encontrar datos aleatorios sobre la dependencia tecnológica en el enlace a continuación:</h1><a href="/random_fact">¡Ver un dato aleatorio!</a><a href="/pass_gen">¿Quieres una contraseña completamente aleatoria? ¡Entra aquí!</a>'

@app.route("/random_fact")
def ran_fact():
    return f'<p>{random.choice(flist)}</p>'

@app.route("/pass_gen")
def pass_gen():
    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    return f'<p>"Tu contraseña se ha generado exitosamente:{(random.choice(caracteres) for i in range(10))}</p>'

app.run(debug=True)