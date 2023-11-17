import re

# Dicionário mapeando expressões regulares a identificadores de intenção
intent_dict = {
    r"\b(?:(?:[Aa]tualizar)|(?:[Mm]udar)|(?:[Cc]artão)|(?:[Cc]artão de crédito)|(?:[Cc]rédito)|(?:[Pp]agamento)|(?:[Dd]esatualizado))": "atualizar",

    r"\b(?:(?:[Ss]tatus)|(?:[Pp]edido)|(?:[Mm]eu pedido)|(?:[Rr]astrear)|(?:[Oo]nde)|(?:[Ee]stá)|(?:[Ee]ntrega)|(?:[Cc]onsultar))": "pedido",

}

action_dict = {
    "atualizar": "Para atualizar acesse o menu e clique em atualizar.",
    "pedido": "Para saber sobre o pedido, acesse o menu e clique em pedido"

}

# Classe principal para o nó do chatbot
class ChatBotNode():
    def __init__(self):
        while True:  # Loop infinito para manter a solicitação de comandos
            print("Caso queira encerrar o programa digite 'sair' \n", end=" ")
            command = input("Digite o seu comando: ")
            if command.lower() == 'sair':  # Verifica a condição de saída
                exit()
            #looping para verificar o comando
            for key, value in intent_dict.items():
                pattern = re.compile(key)
                groups = pattern.findall(command)
                # se achou algo, printa
                if groups:
                    if value == "atualizar":
                        print(action_dict[value])
                    if value == "pedido":
                        print(action_dict[value])
                        

# Função principal para executar o nó do chatbot
def main(args=None):

    ChatBotNode()

if __name__ == '__main__':
    main()