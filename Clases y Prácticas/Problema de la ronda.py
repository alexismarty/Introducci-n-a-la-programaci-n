LIMITE_CUENTA = 50
LIMITE_PERSONA = 10
sentidoGiro = "horario"
personaActual = 0

for cuenta in range(1,LIMITE_CUENTA + 1):

  if (sentidoGiro == "horario"):

    if (personaActual < LIMITE_PERSONA):
     personaActual = personaActual + 1
    else:
      personaActual = 1

  else:
    if (personaActual > 1):
      personaActual = personaActual - 1
    else:
      personaActual = LIMITE_PERSONA
  
  if (cuenta % 8 == 0):
    if (sentidoGiro == "horario"):
      sentidoGiro = "antihorario"
    else:
      sentidoGiro = "horario"

  if (cuenta % 11 == 0):
    if (sentidoGiro == "horario"):
      personaActual = personaActual + 1
    else:
      personaActual = personaActual - 1

  print ("sentido", sentidoGiro, "persona", personaActual, "cuenta", cuenta)