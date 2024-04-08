import random

def choice():
  opciones = ('piedra', 'papel', 'tijera')
  opcion_cpu = random.choice(opciones)
  opcion_jugador = input("escribe piedra papel o tijera? => ").lower()
  if not opcion_jugador in opciones:
    print("digite una opcion correcta")
    return choice()
  print("jugador escoge=> ", opcion_jugador)
  print("cpu escoge=> ", opcion_cpu)
  return opcion_jugador, opcion_cpu
  
def rules(opcion_jugador,opcion_cpu,uw=0, cw=0):
  if opcion_jugador == opcion_cpu:
    print("empate")
  elif (opcion_jugador == "piedra" and opcion_cpu == "tijera") or (opcion_jugador == "tijera" and opcion_cpu == "papel") or (opcion_jugador == "papel" and opcion_cpu == "piedra"):
    print("gana jugardor")
    uw += 1
  else:
    print("gana cpu")
    cw += 1
  return uw, cw


def run_game():
  uw = 0
  cw = 0
  wins = int(input("digite numero de triunfos => "))
  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', cw)
    print('user_wins', uw)
    rounds += 1
    oj, oc= choice()
    uw, cw = rules(oj, oc, uw, cw)
    if uw == wins:
      print('El ganador es la usuario')
      print(f"resultado final jugador {uw} Cpu {cw}")
      break
    if cw == wins:
      print('El ganador es el computadora')
      print(f"resultado final jugador {uw} Cpu {cw}")
      break

run_game()