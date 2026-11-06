pokemon = {
    "Nombre": "Charmander",
    "Tipo": "Fuego",
    "Nivel": 25}



if "Charmander" in pokemon.values():
    print("Charmander esta en el diccionario")
else:
    print("Charmander no esta en el diccionario")

if "Tipo" in pokemon:
    print("El tipo de pokemon es:",pokemon["Tipo"])
else:
    print("tipo no esta dentro del diccionario")