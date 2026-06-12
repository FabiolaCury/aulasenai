#Inicializando a playlist antes do laço para não apagar os dados
playlist = ["Velha Infância", "Depois", "Ainda Bem", "My sacrifice", "Someone you loved", "Before you go", "Acróstico", "Waka Waka"]

while True:
    #Exibição do menu de opções
    print("\n" + "=" *30)
    print("     Menu da playlist")
    print("=" *30)
    print("1. Adicionar música")
    print("2. Ver playlist atual")
    print("3. Alterar música por posição")
    print("4. Remover música por nome")
    print("5. Sair do programa")
    print("=" *30)

    #Entrada da opção do usuário
    opcao = input("Ecolha uma opção (1-5): ")
    print("-" *30)

    #---Opção 1: Adicionar ---
    if opcao == "1":
        nova_musica = input("Digite o nome da música para adicionar: ")
        playlist.append(nova_musica)
        print(f"{nova_musica} foi adicionada com sucesso!")

    #---Opção 2: Exibir---
    elif opcao == "2":
        if len(playlist) == 0:
            print("Sua playlist está vazia no momento!")
        else:
            print("---Sua playlist---")
            #O enumerate ajuda a mostrar o índice para o usuário saber como alterar depois
            for  indice, musica in enumerate(playlist):
                print(f"Posição {indice} -> {musica}")

    #---Opção 3: Alterar---
    elif opcao == "3":
            if len(playlist) == 0:
                print("Não há músicas para alterar. A playlist está vazia!")
            else:
                posicao = int(input("Digite o número da posiçao que deseja alterar: "))

                #Validação para garantir que o índice existe na lista
                if 0 <= posicao < len(playlist):
                    musica_antiga = playlist[posicao]
                    nova_musica = input(f"Substituir '{musica_antiga}' por: ")
                    playlist[posicao] = nova_musica
                    print("Música alterada com sucesso!")
                else:
                    print("Posição inválida! Verifique os números na opção 2.")
    #---Opção 4: Remover---
    elif opcao == "4":
        if len(playlist) == 0:
            print("Não há músicas para remover. A playlist está vazia!")
        else:
            musica_remover = input("Digite o nome exato da música que deseja remover: ")

            #Verificamos se o elemento está na lista antes de remover (evita erro)
            if musica_remover in playlist:
                playlist.remove(musica_remover)
                print(f"'{musica_remover}' removida com sucesso!")
            else:
                print("Música não encontrada. Atenção com maiúsculas e minúsculas.")

    #---Opção 5: Sair---
    elif opcao == "5":
        print("Encerrando o sistema de música. Até logo!")
        break #interrompe o laço 'while true' e finaliza o programa

    #---Tratamento de opção inválida---
    else:
        print("Opção inválida! Escolha um número de 1 a 5.")
                 