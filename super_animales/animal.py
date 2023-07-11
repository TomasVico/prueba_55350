class Animal:
    def __init__ (self,nombre,especie):
        self.nombre= nombre
        self.especie= especie

    def __str__(self):
        print(f'El {self.nombre} es de la especie {self.especie}')