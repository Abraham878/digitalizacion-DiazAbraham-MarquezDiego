pokemon = {
    "Nombre": "Pikachu",
    "Tipo": "Electrico",
    "Nivel": 40}

clave = input("Dime una clave: ")

print(pokemon.get(clave,"Esa clave no existe"))