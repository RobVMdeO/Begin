saludo = '''
Hola, ¿quieres jugar?
> Si
> No
'''
print(saludo)
respuesta1 = str(input("> ")).upper()

afirmativo = 'SI'
negativo = 'NO'

if respuesta1 == afirmativo:
    print("Genial! Me encanta jugar. ¿Te gustan las adivinanzas?")
    respuesta2 = str(input("> ")).upper()
    if respuesta2 == afirmativo:
        print("Te doy 3 oportunidades "
              "para adivinar un número del 0 al 20 "
              "que es par y se halla en el medio de esos dos números")
        intentos = 0
        posintentos = 3
        solucion = "10"
        while intentos < posintentos:
            respuesta3 = str(input("> ")).upper()
            intentos += 1
            if respuesta3 != solucion:
                print(f"Quedan {3-intentos} oportunidades")
            elif respuesta3 == solucion:
                print("Excelente! Te felicito! Gracias por participar!")
                break
        else:
            print('Lo siento. Se acabaron las oportunidades. Intenta de nuevo')
    elif respuesta2 == negativo:
        print("Qué lástima. Es lo que hay (por ahora ;D)")
    else:
        print("No entendí")
elif respuesta1 == negativo:
    print("Qué lástima. Te lo pierdes")
else:
    print("No entendí")
