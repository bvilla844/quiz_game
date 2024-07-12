import time
import sys

print("Hola! Me llamo Brayan y te doy la bienvenida a mi juego de Quiz_game!")
user_name = input("Cual es tu nombre : ")

playing = input(f"Hola! {user_name} Quieres jugar mi juego? Si/No: ").lower()

if playing != "si":
    quit()

print("Okay! Juguemos :)")
print("-"*70)
print(
    "Quiz_game es un juego de preguntas de cultura general en el que cuentas con 1 minuto para responder la mayor cantidad de preguntas, al final te dare tu score..")
print("-"*70)
print("-"*70)
print("MUCHA SUERTE EMPECEMOS!! 😉😆")
print("-"*70)
score = 0
start_time = time.time()
time_out = 60


def check_time():
    done_time = time.time() - start_time
    if done_time >= time_out:
        print("se acabo el tiempo 😔😔 ")
        print(f"tu puntuación final es {score} de 100 ")
        time.sleep(10)
        sys.exit()


question = input(
    "¿Qué monumento histórico de Estados Unidos se encuentra en la isla de Liberty Island en Nueva York? : ")
check_time()
if question.lower().strip() in ["la estatua de la libertad" , "estatua de la libertad"]:
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

question = input("¿En qué ciudad europea puedes encontrar el Arco del Triunfo, construido por Napoleón Bonaparte? : ")
check_time()
if question.lower() == "paris":
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

question = input(
    "¿Cuál es el antiguo anfiteatro romano que se encuentra en el centro de Roma y es famoso por sus luchas de gladiadores? : ")
check_time()
if question.lower() in ["el coliseo", "coliseo"]:
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

question = input("¿Cuál es el país más grande del mundo en términos de área? : ")
check_time()
if question.lower() == "rusia":
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

question = input(
    "¿Cuál es la molécula de gas que los seres vivos inhalan para obtener energía durante la respiración? : ")
check_time()
if question.lower() == "oxigeno":
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

question = input("¿Qué famoso científico desarrolló la teoría de la relatividad? : ")
check_time()
if question.lower() in ["albert einstein", "einstein"]:
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

question = input("¿Qué proceso natural convierte la luz solar en energía química en las plantas? : ")
check_time()
if question.lower() in ["fotosintesis", "fotosíntesis"]:
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

question = input(
    "¿Qué imperio conquistó gran parte de Europa, Asia y África en el siglo XIII bajo el liderazgo de Genghis Khan? : ")
check_time()
if question.lower() in ["mongol", "imperio mongol", "el imperio mongol"]:
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

question = input("¿En qué continente se encuentra Egipto? : ")
check_time()
if question.lower() == "africa":
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

question = input("¿Cuál es el país que se extiende a lo largo de dos continentes, Europa y Asia? : ")
check_time()
if question.lower() in ["turquia", "turquía"]:
    print('Correcto!')
    score += 10
    print(f"tu puntuación es ->{score}")
else:
    print('Incorrecto!')
    score += 0
    print(f"tu puntuación es -> {score}")

print(f"tu puntuación final es {score} de 100 ")
