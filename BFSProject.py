import pandas as pd
import heapq    

class Juego():
    def __init__(self, nombre, categoria, plataforma, multijugador, precio, metrica):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.plataforma = plataforma    
        self.multijugador = multijugador
        self.metrica = metrica  

    def __gt__(self, otro_nodo):
        return self.metrica > otro_nodo.metrica

class Frontera():
    def __init__(self):
        self.frontera = []

    def empty(self):
        return (len(self.frontera) == 0)

    def add(self, nodo):                                                                                             
        #Se agrega un nodo a la frontera, manteniendo los nodos ordenados por su num de descargas                     
        heapq.heappush(self.frontera, (nodo.metrica, nodo))  

    def eliminar(self):
        _, nodo = heapq.heappop(self.frontera)                                                                       
        return nodo  
        

class JuegosBFS():
    def __init__(self, ruta_archivo):
        
        self.juegos = pd.read_excel(ruta_archivo)
        # Recorrer la fila número 2 (índice 1)
        #fila_especifica = df.iloc[1]  # Utiliza iloc para acceder por índice
        #columna_especifica = df['Precio']  
        #for valor in columna_especifica:
            #print(valor)
        self.explorado=set()
    def buscar(self, criterios):
        start = Juego(nombre=None, categoria=None, plataforma=None, multijugador=None, precio=None, metrica = None)
        frontera = Frontera()
        frontera.add(start)

        juegos_encontrados = []

        while not frontera.empty():
            nodo = frontera.eliminar()
            # Verifica si el juego en el nodo cumple con los criterios
            if self.cumple_criterios(nodo, criterios):
                juegos_encontrados.append(nodo.nombre)

            # Expande el nodo para explorar juegos vecinos
            for nuevo in self.obtener_juegos_vecinos(criterios[0],self.juegos):
                    #print(nuevo[2])
                    hijo = Juego(nombre=nuevo[0], categoria=nuevo[1], plataforma=nuevo[2], multijugador=nuevo[3], precio=nuevo[4], metrica=int(nuevo[5]))
                    frontera.add(hijo)
                    #print("-------------")
                    #print(nuevo)
                    
        return juegos_encontrados

    def cumple_criterios(self, juego, criterios):

        if(criterios[1] == "Subcategoría 1"):
            if juego.categoria == criterios[0] and juego.plataforma == "PC" and juego.multijugador == "No" and juego.precio == "Pago":
                return True
        if(criterios[1] == "Subcategoría 2"):
            if juego.categoria == criterios[0] and juego.plataforma == "PC" and juego.multijugador == "No" and juego.precio == "Gratis":
                return True
        
        if(criterios[1] == "Subcategoría 3"):
            if juego.categoria == criterios[0] and juego.plataforma == "PC" and juego.multijugador == "Si" and juego.precio == "Pago":
                return True
        if(criterios[1] == "Subcategoría 4"):
            if juego.categoria == criterios[0] and juego.plataforma == "PC" and juego.multijugador == "Si" and juego.precio == "Gratis":
                return True

        if(criterios[1] == "Subcategoría 5"):
            if juego.categoria == criterios[0] and juego.plataforma == "PLAY" and juego.multijugador == "No" and juego.precio == "Pago":
                return True
        if(criterios[1] == "Subcategoría 6"):
            if juego.categoria == criterios[0] and juego.plataforma == "PLAY" and juego.multijugador == "No" and juego.precio == "Gratis":
                return True
        if(criterios[1] == "Subcategoría 7"):
            if juego.categoria == criterios[0] and juego.plataforma == "PLAY" and juego.multijugador == "Si" and juego.precio == "Pago":
                return True

        if(criterios[1] == "Subcategoría 8"):
            if juego.categoria == criterios[0] and juego.plataforma == "PLAY" and juego.multijugador == "Si" and juego.precio == "Gratis":
                return True
            
        return False

   

    def obtener_juegos_vecinos(self, cat, Datos):
        cont=0
        filas_coincidentes = []
        for _, row in Datos.iterrows():
            if row['Categoria'] == cat and tuple(row) not in self.explorado:
                #print("va_")
                self.explorado.add(tuple(row))
                cont+=1
                filas_coincidentes.append(row)
                if  cont==2:
                    break
        return filas_coincidentes


