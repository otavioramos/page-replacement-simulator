sequencia_referencia = [0, 3, 5, 6, 7, 8, 8, 9, 4, 1, 2, 4, 5,
                        6, 7, 9, 0, 0, 1, 2, 3, 4, 5, 6, 6, 8,
                        1, 1, 2, 5, 1, 9, 0, 9, 9, 4, 5, 9, 1, 3]

memoria_virtual = []
separador = "======================================================"
indice_de_substituicao = [0,3,1,2]


def inicio_do_programa():
    contador_indice_sub = 0
    execucoes = 1
    print(separador)
    print(">>>>>SIMULADOR DE SUBSTITUIÇÃO DE PÁGINAS<<<<<")
    print(separador)
    input("Tecle ENTER para iniciar")
    print("A sequência de referência utilizada é a seguinte:")
    print(str(sequencia_referencia))
    print("O tamanho da memória virtual é 4. Isto é, suas posições vão de 0 à 3.")
    input("Tecle ENTER para começarmos a simulação, passando a sequência mostrada acima para o algoritmo.")
    print("")
    print(separador)
    verifica_paginas_memoriav(contador_indice_sub, execucoes)


def verifica_paginas_memoriav(cont, exec):
    print(">>>>>>>>>>>>>>>>INICIANDO O ALGORITMO!<<<<<<<<<<<<<<<<")
    print(separador)
    falta_de_paginas = 0
    for pagina in sequencia_referencia:
        if exec <= 9:
            print(">>>>>>>>>>>>>>>>>>>>>>EXECUÇÃO "+ str(exec) +"<<<<<<<<<<<<<<<<<<<<<<")
        else:
            print(">>>>>>>>>>>>>>>>>>>>>EXECUÇÃO " + str(exec) + "<<<<<<<<<<<<<<<<<<<<<<")
        if cont >= 4:
            cont = 0
        print("Página que será procurada na memória: " + str(pagina))
        if pagina in memoria_virtual:
            print("Página encontrada!")
            print("")
            print("Memória Virtual: " + str(memoria_virtual))
            print(separador)
        else:
            print("Falta de página :(")
            falta_de_paginas += 1

            if len(memoria_virtual) < 4:
                memoria_virtual.append(pagina)
                print("Inserindo a página na memória virtual")
                print("")
                print("Memória Virtual: " + str(memoria_virtual))
                print(separador)
            else:
                print("Memória virtual cheia")
                print("Executando o algoritmo e fazendo a substituição de página")
                algoritmo(memoria_virtual, pagina, indice_de_substituicao[cont])
                print(separador)
                cont += 1
        exec += 1
    exibe_falta_de_paginas(falta_de_paginas)


def algoritmo(mmu, pag, indice):
    print("Substituindo a posição: " + str(indice))
    print("")
    print("         0  1  2  3")
    print("Antes:  " + str(mmu))
    mmu[indice] = pag
    print("Depois: "+ str(mmu))


def exibe_falta_de_paginas(falta_pag):
    print("")
    print("A número de falta de páginas durante a execução foi de: " + str(falta_pag) + " páginas")
    print("")
    print(separador)


inicio_do_programa()
