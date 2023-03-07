#   name:pyTextAdventur
#   type:gaem

import sys
import os
import random
import json
from colorama import init, Fore, Back

init()
os.system("clear")
os.system("cls")

if not os.path.exists("settings.json"):
    with open("settings.json", "w") as f:
        f.write("""
        {
    "playerName":"",
    "playerClass":""
}
        """)

with open('settings.json', 'r') as settings_json:
    gameSettings = json.load(settings_json)

# variables globales
class game:
    def __init__(self):
        self.init = False
        self.command = ""
        self.commandFerify = False
        self.lastCommand = ""
        self.helpCommand = "help"
        self.commands = ("/help", "/test", "/init")
        self.around = ""
        self.playerClass = ""
        self.classAtack = ""
        self.gameSetings = gameSettings

# pleyer and game logic
class character:
    def __init__(self, name, playerClass, game_inst):
        self.name = name
        self.level = 1
        self.xp = 0
        self.skills = {playerClass: 1}
        self.stats = {"atack": game_inst.classAtack}

game_inst = game()
player = None

defaultClass = {
    "adventurous": {"damege":10}
}

while True:
    try:
        character_name = game_inst.gameSetings['playerName']
        character_class = game_inst.gameSetings['playerClass']

        # ask for player name if it's not already set in the settings
        if not character_name:
            character_name = input(Back.BLACK + Fore.WHITE + "  " + "Cual es el nombre de tu personaje" + Fore.BLACK + Back.RESET + "\ue0b0 " + Fore.WHITE)
            game_inst.gameSetings['playerName'] = character_name

        print(defaultClass)

        # ask for player class if it's not already set in the settings
        if not character_class:
            while True:
                player_class = input(Back.BLACK + Fore.WHITE + "  " + "Cual es tu clase" + Fore.BLACK + Back.RESET + "\ue0b0 " + Fore.WHITE)
                if not any(char.isdigit() for char in player_class) and player_class:
                    game_inst.gameSetings['playerClass'] = player_class
                    break
                else:
                    print(Fore.RED + "[!] La clase no puede contener números.")

        # save settings to file
        with open('settings.json', 'w') as f:
            json.dump(game_inst.gameSetings, f, indent=4)

        # create player instance and start game
        if game_inst.gameSetings['playerName'] and game_inst.gameSetings['playerClass']:
            player = character(character_name, character_class, game_inst)
            game_inst.init = True
            print(Fore.GREEN + "[+] Bienvenido {}!".format(player.name))
            break

    #commands
while True:
    try:
        playerInput = input(Back.BLACK + Fore.WHITE + "  " + (player.name) + "  " + Fore.BLACK + Back.RESET + "\ue0b0 " + Fore.WHITE)

        # test command 1arg logic
        if playerInput.startswith("/test"):
            # Dividir la entrada en partes
            parts = playerInput.split(" ")
            if len(parts) == 3 and parts[2] == "test":
                print("HOLA")
            else:
                print(parts[1])
            continue

        if not game_inst.init:
            if playerInput.startswith("/init"):
                parts = playerInput.split(" ")
                if len(parts) != 3:
                    print(Fore.RED + "[!] Debe proporcionar un nombre y una clase.")
                    print("/init [nombre] class:[nombre de la clase]")
                    continue
                playerClass = parts[2].split(":")[1]
                player = character(parts[1], playerClass, game_inst)
                game_inst.init = True
                print(Fore.GREEN + "[+] Bienvenido {}!".format(player.name))
            elif playerInput == "/help":
                print(game_inst.helpCommand)
            else:
                print(Fore.RED + "[!] Debe inicializar el juego primero con el comando /init.")
                print(game_inst.helpCommand)
        else:
            if playerInput in game_inst.commands:
                command = playerInput
                commandFerify = True
                lastCommand = command
            elif playerInput.strip() == "":
                print(" ")
            else:
                print("Entrada inválida. Intente de nuevo.")
                print(game_inst.helpCommand)

            if commandFerify:
                if command == "/help":
                    print(game_inst.helpCommand)
                if command == "/init":
                    print(Fore.RED + "[!] El juego ya está inicializado.")
                if command == "/around":
                    print(game_inst.around)
                # Reiniciar el estado del comando
                command = ""
                commandFerify = False

    except KeyboardInterrupt:
        print(Fore.GREEN +"\n[!] Saliendo...")
        sys.exit(1)