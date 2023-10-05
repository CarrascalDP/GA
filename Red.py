#Red
from pomegranate import*
from pomegranate import Node
# pip install pomegranate

Pregunta_1 = Node(DiscreteDistribution({
    "si": 0.5,
    "no": 0.5
}), name="Pregunta_1")


Pregunta_2 = Node(DiscreteDistribution({
    "fuerte": 0.5,
    "suave": 0.5
}), name="Pregunta_2")

Pregunta_3 = Node(DiscreteDistribution({
    "hobby": 0.5,
    "pasatiempo": 0.5
}), name="Pregunta_3")

# Nodo de Mantenimiento está condicionado por la lluvia
Estrategia = Node(ConditionalProbabilityTable([
    ["si","fuerte","hobby","gusta",0.6],
    ["si","fuerte","hobby","desaprueba",0.4],

    ["si","fuerte","pasatiempo","gusta",0.5],
    ["si","fuerte","pasatiempo","desaprueba",0.5],

    ["si","suave","hobby","gusta",0.7],
    ["si","suave","hobby","desaprueba",0.3],

    ["si","suave","pasatiempo","gusta",0.9],
    ["si","suave","pasatiempo","desaprueba",0.1],

    ["no","fuerte","hobby","gusta",0.8],
    ["no","fuerte","hobby","desaprueba",0.2],

    ["no","fuerte","pasatiempo","gusta",0.4],
    ["no","fuerte","pasatiempo","desaprueba",0.6],

    ["no","suave","hobby","gusta",0.7],
    ["no","suave","hobby","desaprueba",0.3],

    ["no","suave","pasatiempo","gusta",0.8],
    ["no","suave","pasatiempo","desaprueba",0.2]
], [Pregunta_1.distribution,Pregunta_2.distribution,Pregunta_3.distribution]), name="Estrategia")

Accion = Node(ConditionalProbabilityTable([
    ["si","fuerte","hobby","gusta",0.5],
    ["si","fuerte","hobby","desaprueba",0.5],

    ["si","fuerte","pasatiempo","gusta",0.6],
    ["si","fuerte","pasatiempo","desaprueba",0.4],

    ["si","suave","hobby","gusta",0.7],
    ["si","suave","hobby","desaprueba",0.3],

    ["si","suave","pasatiempo","gusta",0.9],
    ["si","suave","pasatiempo","desaprueba",0.1],

    ["no","fuerte","hobby","gusta",0.6],
    ["no","fuerte","hobby","desaprueba",0.4],

    ["no","fuerte","pasatiempo","gusta",0.5],
    ["no","fuerte","pasatiempo","desaprueba",0.5],

    ["no","suave","hobby","gusta",0.8],
    ["no","suave","hobby","desaprueba",0.2],

    ["no","suave","pasatiempo","gusta",0.9],
    ["no","suave","pasatiempo","desaprueba",0.1]
], [Pregunta_1.distribution,Pregunta_2.distribution,Pregunta_3.distribution]), name="Accion")

Deporte = Node(ConditionalProbabilityTable([
    ["si","fuerte","hobby","gusta",0.7],
    ["si","fuerte","hobby","desaprueba",0.3],

    ["si","fuerte","pasatiempo","gusta",0.2],
    ["si","fuerte","pasatiempo","desaprueba",0.8],

    ["si","suave","hobby","gusta",0.5],
    ["si","suave","hobby","desaprueba",0.5],

    ["si","suave","pasatiempo","gusta",0.1],
    ["si","suave","pasatiempo","desaprueba",0.9],

    ["no","fuerte","hobby","gusta",0.8],
    ["no","fuerte","hobby","desaprueba",0.2],

    ["no","fuerte","pasatiempo","gusta",0.5],
    ["no","fuerte","pasatiempo","desaprueba",0.5],

    ["no","suave","hobby","gusta",0.8],
    ["no","suave","hobby","desaprueba",0.2],

    ["no","suave","pasatiempo","gusta",0.1],
    ["no","suave","pasatiempo","desaprueba",0.9]
], [Pregunta_1.distribution,Pregunta_2.distribution,Pregunta_3.distribution]), name="Deporte")


#Modelo Final
modelo_2 = BayesianNetwork()
modelo_2.add_states(Pregunta_1)
modelo_2.add_states(Pregunta_2)
modelo_2.add_states(Pregunta_3)
modelo_2.add_states(Estrategia)
modelo_2.add_states(Accion)
modelo_2.add_states(Deporte)

# Conexiones
modelo_2.add_edge(Pregunta_1, Estrategia)
modelo_2.add_edge(Pregunta_2, Estrategia)
modelo_2.add_edge(Pregunta_3, Estrategia)
modelo_2.add_edge(Pregunta_1, Accion)
modelo_2.add_edge(Pregunta_2, Accion)
modelo_2.add_edge(Pregunta_3, Accion)
modelo_2.add_edge(Pregunta_1, Deporte)
modelo_2.add_edge(Pregunta_2, Deporte)
modelo_2.add_edge(Pregunta_3, Deporte)
modelo_2.bake()
print("Bien")