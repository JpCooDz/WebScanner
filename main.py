import os
import platform
import colorama
from colorama import Fore, Style
from scanner import exibir_dados_do_site_e_portas_abertas

colorama.init(autoreset=True)

def display_menu():
    """
    Displays the main menu with options.
    """
    texto_verde = """
          _   ____     ____    ___     ___    ____    _____
         | | |  _ \\   / ___|  / _ \\   / _ \\  |  _ \\  |__  /
      _  | | | |_) | | |     | | | | | | | | | | | |   / / 
     | |_| | |  __/  | |___  | |_| | | |_| | | |_| |  / /_ 
      \\___/  |_|      \\____|  \\___/   \\___/  |____/  /____|
    """
    print(f"{Fore.GREEN}{texto_verde}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}__________________________________________________{Style.RESET_ALL}")
    print("1. Iniciar Scanner")
    print("2. Sair")
    print(f"{Fore.CYAN}__________________________________________________{Style.RESET_ALL}")

def clear_screen():
    """
    Clears the terminal screen.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def display_scanner_screen():
    """
    Displays the scanner screen.
    """
    scanner_text = f"""
{Fore.YELLOW}  #####    ####     ####    #####    #####     ####    ######
 ##       ##  ##       ##   ##  ##   ##  ##   ##  ##    ##  ##
  #####   ##        #####   ##  ##   ##  ##   ######    ##
      ##  ##  ##   ##  ##   ##  ##   ##  ##   ##        ##
 ######    ####     #####   ##  ##   ##  ##    #####   ####{Style.RESET_ALL}
"""
    print(scanner_text)


def main():
    """
    Runs the main loop for the program.
    """
    while True:
        clear_screen()  # Limpa a tela
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            clear_screen()  # Limpa a tela antes de exibir o scanner
            display_scanner_screen()  # Exibe o scanner
            input("Pressione ENTER para continuar...")
            site_url = input("Digite o link do site a ser verificado: ")
            exibir_dados_do_site_e_portas_abertas(site_url)
            input("Pressione ENTER para continuar...")
        elif choice == "2":
            print(f"{Fore.BLUE}Até logo!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Opção inválida. Por favor, escolha novamente.{Style.RESET_ALL}")

# Execute the main function only when the script is run directly
if __name__ == "__main__":
    main()
