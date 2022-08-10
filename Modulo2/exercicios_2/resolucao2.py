def fun1(funcao,*args ,**kwargs):
        return funcao(*args,**kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


exec_func1 = fun1(fala_oi,'Caio')
exec_func2 = fun1(saudacao, 'Caio', 'bom dia')
print(exec_func2)