print()
print("Programa de Pergunta e Resposta como uma Prova (Escreva Apenas a Letra Certa)")
print()


questoes = {
    'Questao1':{
        'pergunta': 'Quando o Caio NASCEU?',
        'respostas': {'a':'2006', 'b':'2005','c': '2004', 'd': '2007',},
        'resposta_certa': 'c'},
    'Questao2':{
        'pergunta': 'Quando o Felipe NASCEU?',
        'respostas': {'a':'2006', 'b':'2005','c': '2004', 'd': '2007',},
        'resposta_certa': 'd'},

    'Questao3':{
        'pergunta': 'Comida Favorita do Caio?',
        'respostas': {'a':'trigo', 'b':'alface','c': 'pizza', 'd': 'hamburguer',},
        'resposta_certa': 'b'},

    'Questao4':{
        'pergunta': 'Quando a Lizzy NASCEU?',
        'respostas': {'a':'2015', 'b':'2012','c': '2017', 'd': '2016',},
        'resposta_certa': 'd'},
    
    'Questao5':{
        'pergunta': 'Quando o Felipe lava o louça?',
        'respostas': {'a':'depois de ir no banheiro', 'b':'feio','c': 'nunca', 'd': 'quase nunca',},
        'resposta_certa': 'a'},
}

nota = 0

for qk , qv in questoes.items():
    print(f'{qk} : {qv["pergunta"]}')
   
    print('Respostas:')
    for rk , rv in qv['respostas'].items():
        print(f'[{rk}] = {rv}')

    resposta_usuario = input('Digite sua Resposta: ')

    if resposta_usuario.lower() == qv['resposta_certa']:
        nota += 1
        print()
    else:
        print(f'(Errou!!! a Resposta Correta era : {qv["resposta_certa"]})')
        print()


quant_q = len(questoes)
porc = nota / quant_q * 100
if  porc < 60:
        print(f'Você Não Conhece Seus Filhos, Sua Porcetagem de Acerto foi: {porc}')
else:
    print(f'Parabens ! Você fez o Minimo, Sua Porcetagem de Acerto foi:  {porc}')


