import csv

nombre_csv = 'Libros.csv'

class Libro:
    def __init__(self,id, titulo, genero, ISBN, editorial,autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores
        
    def leer_archivo(self):
        pass
    
    def listar_libro(self):
        pass
    
    def agregar_libro(self):
        lista_libro = [self.id,self.titulo,self.genero,self.ISBN,self.editorial,self.autores]
        
        with open(nombre_csv,'a',newline='') as nuevo_libro:
            #Pase el objeto del archivo CSV a la función writer()
            objeto_libro = csv.writer(nuevo_libro)
            #Pase los datos de la lista_libro como argumento a la función writerow()
            objeto_libro.writerow(lista_libro)
            #cerrando 
            nuevo_libro.close()
            
        
    
    def eliminar_libro(self):
        pass
    
    def buscar_libro_ISBN(self,isbn):
        self.isbn = isbn
        with open(nombre_csv,'r') as archivo:
            for linea in archivo:
                #quitamos los espacios en blanco con rstrip()
                linea = linea.rstrip()
                nueva_lista = linea.split(",")
                if self.isbn == nueva_lista[3]:     
                    print(nueva_lista[1])       
    
    def buscar_libro_titulo(self,titulos):
        self.titulos = titulos
        with open(nombre_csv,'r') as archivo:
            for linea in archivo:
                #quitamos los espacios en blanco con rstrip()
                linea = linea.rstrip()
                nueva_lista = linea.split(",")
                if self.titulos == nueva_lista[1]:     
                    print(nueva_lista[4]) 
    
    def ordenar_titulo(self):
        pass
    
    def buscar_libro2(self):
        pass
    
    def buscar_libro3(self):
        pass
    
    def editar_libro(self):
        print("probando git merge")
        pass
    
    def guardar_libro(self):
        pass
    

libro1 = Libro("5","el señor de los anillos2","accion","12349","tiburones","yohana")
#libro1.agregar_libro()
#libro1.buscar_libro_ISBN("12348")
libro1.buscar_libro_titulo("el señor de los anillos2")