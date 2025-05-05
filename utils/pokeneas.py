import random

pokeneas = [
        {
            "id": 1,
            "nombre": "Bulbasur",
            "altura": "0,7m",
            "habilidad": "Espesura",
            "imagen": "https://pokeneass.s3.us-east-1.amazonaws.com/bulbasur.png",
            "frase": "La verdadera fuerza crece con paciencia, como una semilla que se convierte en bosque.",
        },
        {
            "id": 2,
            "nombre": "Charmander",
            "altura": "0,6m",
            "habilidad": "Mar Llamas",
            "imagen": "https://pokeneass.s3.us-east-1.amazonaws.com/charmander.png",
            "frase": "El fuego que arde dentro de ti puede iluminar el camino o consumirlo todo; elige tu llama con sabiduria.",
        },
        {
            "id": 3,
            "nombre": "Squirtle",
            "altura": "0,5m",
            "habilidad": "Torrente",
            "imagen": "https://pokeneass.s3.us-east-1.amazonaws.com/squirtle.png",
            "frase": "La calma es más poderosa que la tormenta; quien fluye como el agua se adapta y vence.",
        },
        {
            "id": 4,
            "nombre": "Pidgeot",
            "altura": "1,5m",
            "habilidad": "Vista Lince",
            "imagen": "https://pokeneass.s3.us-east-1.amazonaws.com/pidgeot.png",
            "frase": "La libertad no se encuentra en el vuelo, sino en tener el valor de elevarse por encima del miedo.",
        },
        {
            "id": 5,
            "nombre": "Pikachu",
            "altura": "0,4m",
            "habilidad": "Elec. Estatica",
            "imagen": "https://pokeneass.s3.us-east-1.amazonaws.com/pikachu.png",
            "frase": "A veces, lo más pequeño en apariencia contiene la energia para cambiarlo todo.",
        },
        {
            "id": 6,
            "nombre": "Greninja",
            "altura": "1,5m",
            "habilidad": "Torrente",
            "imagen": "https://pokeneass.s3.us-east-1.amazonaws.com/greninja.png",
            "frase": "La sombra y el silencio son armas del sabio que lucha sin ser visto.",
        },
        {
            "id": 7,
            "nombre": "Lucario",
            "altura": "1,2m",
            "habilidad": "Fuerza Mental",
            "imagen": "https://pokeneass.s3.us-east-1.amazonaws.com/lucario.png",
            "frase": "Escucha el aura del mundo, y entenderás que la justicia nace del equilibrio entre fuerza y compasion.",
        },
        {
            "id": 8,
            "nombre": "Luxray",
            "altura": "1,4m",
            "habilidad": "Intimidacion",
            "imagen": "https://pokeneass.s3.us-east-1.amazonaws.com/luxray.png",
            "frase": "Ver a traves de la oscuridad no es un don, sino el deber de quien busca la verdad, aunque duela.",
        },
    ]

def get_pokenea():
    return random.choice(pokeneas)