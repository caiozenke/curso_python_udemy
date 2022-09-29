import json as j


pessoas ={
    'Pessoa 1' : {
        'Nome:' : 'Caio',
        'idade' : 19
    },
    'Pessoa 2' : {
        'Nome:' : 'Julius',
        'idade' : 22
    },
}

# transformar para json

pessoas_json = j.dumps(pessoas , indent=True)

#Ler o Arquivo Json 
def abrir_json():
    with open('pessoas.json' , '+w') as pj:
        pj.write(pessoas_json)

def ler_json():
    with open('pessoas.json' , 'r') as pj:
        d1_json = pj.read()
        d1_json = j.loads(d1_json) #transformar em dict
        #print(d1_json)
    
    for k, v in d1_json.items():
        print(f'{k}')
        for atributos,i in v.items():
            print(atributos,i)


#abrir_json()
ler_json()
