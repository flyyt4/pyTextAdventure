#   name:pyTxtxAdventure
#   type:game
import sys, os, random, configparser
from colorama import init, Fore, Back

init()
os.system('cls')

class Game:
    def __init__(self):
        self.initialized = False
        self.command = ""
        self.command_verified = False
        self.last_command = ""
        self.help_command = "help"
        self.commands = ["/help", "/test"]
        self.classes = {
            'swordsman': {
                "damage": 20,
                "ability": ""
            }
        }

class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.level = 1
        self.xp = 0
        self.char_class = char_class
        self.skills = ""
        self.stats = {}

    def print_stats(self):
        print("Estadísticas del jugador:")
        print("Nombre:", self.name)
        print("Clase:", self.char_class)
        print("Nivel:", self.level)
        print("XP:", self.xp)
        print("Habilidades:", self.skills)
        print("Estadísticas:")
        for stat, value in self.stats.items():
            print(f"{stat.capitalize()}: {value}")

    def print_inventory(self):
        print("Inventario del jugador:")
        # TODO: Implementar el inventario del jugador

class Config:
    def __init__(self, file):
        self.file = file
        self.config = configparser.ConfigParser()

    def get_user_config(self):
        if os.path.exists(self.file):
            self.config.read(self.file)
            if 'user' in self.config['DEFAULT'] and 'class' in self.config['DEFAULT']:
                name = self.config['DEFAULT']['user']
                char_class = self.config['DEFAULT']['class']
                while True:
                    player_input = input(Back.BLACK + Fore.WHITE + "  " + name + "  " + Fore.BLACK + Back.RESET + "\ue0b0 " + Fore.WHITE)
                    if player_input != "":
                        break
                return name, char_class
        while True:
            name = input(Back.BLACK + Fore.WHITE + "  " + "¿Cuál es tu nombre?" + "  " + Fore.BLACK + Back.RESET + "\ue0b0 " + Fore.WHITE)
            if name != "":
                break
        print("clases:\nswordsman")
        while True:
            char_class = input(Back.BLACK + Fore.WHITE + "  " + "¿Cuál es tu clase?" + "  " + Fore.BLACK + Back.RESET + "\ue0b0 " + Fore.WHITE)
            if char_class != "":
                break
        self.config['DEFAULT'] = {'user': name, 'class': char_class}
        with open(self.file, 'w') as file:
            self.config.write(file)
        return name, char_class

config = Config('config.ini')
name, char_class = config.get_user_config()
player = Character(name, char_class)
game_inst = Game()

while True:
    try:
        player_input = input(Back.BLACK + Fore.WHITE + "  " + player.name + "  " + Fore.BLACK + Back.RESET + "\ue0b0 " + Fore.WHITE)

        # test command 1arg logic
        if player_input.startswith("/test"):
            # Dividir la entrada en partes
            parts = player_input.split(" ")
            if len(parts) == 3 and parts[2] == "test":
                print("HOLA")
            else:
                print(parts[1])
            continue

        # Verificar si el juego ha sido inicializado
        if not game_inst.init:
            if player_input == "/help":
                print("Bienvenido a pyTxtxAdventure. Para comenzar, inicie el juego con el comando /start.")
            elif player_input.startswith("/start"):
                game_inst.init = True
                print("Bienvenido a la aventura! Escribe /help para ver la lista de comandos.")
            else:
                print(Fore.RED + "[!] Debe inicializar el juego primero con el comando /start.")
                print("Escribe /help para ver la lista de comandos.")
        else:
            # Verificar si el comando ingresado es válido
            if player_input.startswith(game_inst.commands):
                command = player_input
                command_verified = True
                last_command = command
            elif player_input.strip() == "":
                print(" ")
            else:
                print("Entrada inválida. Intente de nuevo.")
                print("Escribe /help para ver la lista de comandos.")

            if command_verified:
                if command == "/help":
                    print("Lista de comandos:")
                    print("/stats: Ver estadísticas del jugador.")
                    print("/inventory: Ver inventario del jugador.")
                    print("/map: Ver mapa de la zona.")
                elif command == "/stats":
                    player.print_stats()
                elif command == "/inventory":
                    player.print_inventory()
                elif command == "/map":
                    print("Mapa de la zona.")
                # Reiniciar el estado del comando
                command = ""
                command_verified = False

    except KeyboardInterrupt:
        print(Fore.GREEN +"\n[!] Saliendo...")
        sys.exit(1)






