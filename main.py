meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso", "ROFL": "una respuesta a una broma", "SHEESH": "algo sorprendente"
            
            
    
        
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esta palabra no se encuentra en el diccionario")
