from logic import *

# Define los símbolos para las características de los videojuegos
Plataformas = ["PC", "Play"]
Multijugador = ["Si", "No"]
Precio = ["Gratis", "Pago"]

# Crea una lista de símbolos para cada categoría
plataformas_symbols = [Symbol(plataforma) for plataforma in Plataformas]
multijugador_symbols = [Symbol(multijugador) for multijugador in Multijugador]
precio_symbols = [Symbol(precio) for precio in Precio]

# Combina todos los símbolos en una lista
symbols =   plataformas_symbols + multijugador_symbols + precio_symbols

# Inicializa una base de conocimiento vacía
knowledge = And()
Lista=[]
# Define una función para verificar el conocimiento
def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            Lista.append(symbol)

# Pide al usuario que proporcione las características deseadas
print("Bienvenido al recomendador de videojuegos. Por favor, proporciona las características que deseas:")

# Pregunta sobre la plataforma preferida
plataforma = int(input("¿En qué plataforma quieres jugar? (PC, PlayStation): "))
if plataforma==1:
    plataforma="PC"
if plataforma==2:
    plataforma="Play"
if plataforma in Plataformas:
    knowledge.add(Symbol(plataforma))
else:
    print("Respuesta no válida.")

# Pregunta sobre la preferencia de multijugador
multijugador = int(input("¿Prefieres juegos multijugador? (Si, No): "))
if multijugador==1:
    multijugador="Si"
if multijugador==2:
    multijugador="No"
if multijugador in Multijugador:
    knowledge.add(Symbol(multijugador))
else:
    print("Respuesta no válida.")

# Pregunta sobre el rango de precio
precio = int(input("¿Qué rango de precio estás dispuesto a pagar? (Gratis, Pago): "))
if precio==1:
    precio="Gratis"
if precio==2:
    precio="Pago"
if precio in Precio:
    knowledge.add(Symbol(precio))
else:
    print("Respuesta no válida.")

# Verifica el conocimiento actual
print("\nConocimiento actual:")
check_knowledge(knowledge)
# Ahora puedes buscar juegos que cumplan con los requisitos proporcionados por el usuario en tu base de datos
# Define las reglas lógicas para asociar respuestas con subcategorías
reglas_subcategorias = {
    And(Symbol("PC"), Symbol("No"), Symbol("Pago")): "Subcategoría 1",
    And(Symbol("PC"), Symbol("No"), Symbol("Gratis")): "Subcategoría 2",
    And(Symbol("PC"), Symbol("Si"), Symbol("Pago")): "Subcategoría 3",
    And(Symbol("PC"), Symbol("Si"), Symbol("Gratis")): "Subcategoría 4",
    And(Symbol("Play"), Symbol("No"), Symbol("Pago")): "Subcategoría 5",
    And(Symbol("Play"), Symbol("No"), Symbol("Gratis")): "Subcategoría 6",
    And(Symbol("Play"), Symbol("Si"), Symbol("Pago")): "Subcategoría 7",
    And(Symbol("Play"), Symbol("Si"), Symbol("Gratis")): "Subcategoría 8",
    # Agrega más reglas según tus necesidades
}

# Función para determinar la subcategoría basada en las respuestas y la base de conocimiento
def determinar_subcategoria(knowledge, reglas_subcategorias):
    for condicion, subcategoria in reglas_subcategorias.items():
        if model_check(knowledge, condicion):
            return subcategoria
    return "Sin subcategoría"

# Determina la subcategoría asociada
subcategoria_asociada = determinar_subcategoria(knowledge, reglas_subcategorias)

