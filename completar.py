# Completa la cancion

incompleta = '\nCompleta la canción\n\nHoy voy a hablarte de mis ____1____\n' \
             'Que me vieron _____2____\n' \
             'Desde el ___3___ que se hizo rey\n' \
             'Hasta la princesa que rompió la ______4_____\n' \
             'Si me _____5______ a mí, de ellos _____6_____\n'

print(incompleta)
respuesta = input('¿Te animas a intentarlo? > ').upper()

if respuesta == 'SI':
    palabra1 = input('Palabra 1:')
    palabra2 = input('Palabra 2:')
    palabra3 = input('Palabra 3:')
    palabra4 = input('Palabra 4:')
    palabra5 = input('Palabra 5:')
    palabra6 = input('Palabra 6:')

    completada = '\n¿Esto te parece correcto?\n\n' \
                 f'Hoy voy a hablarte de mis {palabra1}\n'\
                 f'Que me vieron {palabra2}\n'\
                 f'Desde el {palabra3} que se hizo rey\n'\
                 f'Hasta la princesa que rompió la {palabra4}\n'\
                 f'Si me {palabra5} a mí, de ellos {palabra6}\n'

    print(completada)
    respuesta2 = input('>').upper()

    if respuesta2 == 'SI':
        print('Pues te felicito por intentarlo!')
    elif respuesta2 == 'NO':
        print('Vamos de nuevo! Presiona el botón verde!')
    else:
        print('No entendì')
elif respuesta == 'NO':
    print('Ahhhh :(')
else:
    print('No entendì')
