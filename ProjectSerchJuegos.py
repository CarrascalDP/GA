#PROJECT
from Red import modelo_2
###############Menú###########################

P1 = int(input("Prefieres 1.Intensidad  2.Planificar Movimientos "))
P2 = int(input("Dificultad 1.Moderado  2.Fuerte: "))
P3 = int(input("1.Pasa tiempo  2.hobby: "))

if P1==1:
    P1 = "si"
if P1==2:
    P1 = "no"


if P2==1:
    P2 = "suave"
if P2==2:
    P2 = "fuerte"


if P3==1:
    P3 = "pasatiempo"
if P3==2:
    P3 = "pasatiempo"


evidencia = {
        "Pregunta_1": P1,
        "Pregunta_2": P2,
        "Pregunta_3": P3,
    }

predicciones = modelo_2.predict_proba([evidencia])

max_probabilidad = 0.0
categoria_max_probabilidad = ""

for nodo, prediccion in zip(modelo_2.states, predicciones[0]):

    if isinstance(prediccion, str):
        print(f" {nodo.name}: {prediccion}")
    else:
        print(f"{nodo.name}")
        for valor, probabilidad in prediccion.parameters[0].items():
            print(f"       {valor}: {probabilidad:.2f}")

    if nodo.name == "Estrategia":
        # Itera a través de las predicciones del nodo "desicion"
        for valor, probabilidad in prediccion.parameters[0].items():
            if valor == "gusta":
                #print("gusta: ",probabilidad)
                if probabilidad > max_probabilidad:
                    max_probabilidad = probabilidad
                    categoria_max_probabilidad = "Estrategia"

    if nodo.name == "Accion":
        # Itera a través de las predicciones del nodo "desicion"
        for valor, probabilidad in prediccion.parameters[0].items():
            if valor == "gusta":
                #print("gusta: ",probabilidad)
                if probabilidad > max_probabilidad:
                    max_probabilidad = probabilidad
                    categoria_max_probabilidad = "Accion"
        
    if nodo.name == "Deporte":
        # Itera a través de las predicciones del nodo "desicion"
        for valor, probabilidad in prediccion.parameters[0].items():
            if valor == "gusta":
                #print("gusta: ",probabilidad)
                if probabilidad > max_probabilidad:
                    max_probabilidad = probabilidad
                    categoria_max_probabilidad = "Accion"


from Logica_Project import subcategoria_asociada
Lista_Criterios = []
Lista_Criterios.append(categoria_max_probabilidad)
Lista_Criterios.append(subcategoria_asociada)
#print(Lista_Criterios)

from BFSProject import*
Objeto = JuegosBFS('Lista_Juegos.xlsx') 
ListaF=Objeto.buscar(Lista_Criterios)
print("Según tus elecciones te puedo recomendar los siguientes juegos")
for i in ListaF:
    print("----> ",i)