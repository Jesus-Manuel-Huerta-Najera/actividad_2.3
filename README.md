# actividad_2.3
Análisis, limpieza, entrenamiento y despliegue

#instructions

#image
'''bash
docker build -t regresion_lineal:v0.1 .
'''
#container
'''bash
docker run -it -p 8080:8080 -v "$PWD"/code/:/home/code/ --name gitpod_rl1 -h rl1 regresion_lineal:v0.1
'''