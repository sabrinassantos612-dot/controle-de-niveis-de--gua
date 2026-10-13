from colorama import Fore, Style
niveldeagua=[
    "nível 1 - Muito baixo (critico)",
    "nível 2 - baixo",
    "nível 3 - Médio",
    "nível 4 - Alto",
    "nível 5 - Muito Alto(alerta)"
] 
def exibir_alerta(indice):
    mensagem=niveldeagua[indice]
    
    if indice == 0: 
     print(Fore.RED + mensagem)

    elif indice == 1:
     print(Fore.YELLOW + mensagem)

    elif indice == 2:
     print(Fore.GREEN + mensagem)

    elif indice == 3:
     print(Fore.CYAN + mensagem)

    elif indice == 4:
     print(Fore.BLUE + mensagem)



exibir_alerta(0)
exibir_alerta(1)
exibir_alerta(2)
exibir_alerta(3)
exibir_alerta(4)

print(Style.RESET_ALL)

  
  

    


