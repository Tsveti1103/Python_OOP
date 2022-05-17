from project.player import Player
from project.validator import Validator


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *all_players):
        added_players = []
        for player in all_players:
            if player not in self.players:
                added_players.append(player.name)
                self.players.append(player)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *all_supplys):
        for supply in all_supplys:
            self.supplies.append(supply)

    def sustain(self, player_name, sustenance_type):
        player = Validator.find_by_name(player_name, self.players)
        if player:
            if player.stamina == 100:
                return f"{player_name} have enough stamina."
            sustenance = Validator.find_by_type(sustenance_type, self.supplies)
            if player.stamina + sustenance.energy > 100:
                sustenance.energy = 100 - player.stamina
            player.stamina += sustenance.energy
            a = []
            for i, v in enumerate(self.supplies):
                if v.name == sustenance.name:
                    a.append(i)
            index = a[-1]
            self.supplies.pop(index)
            return f"{player_name} sustained successfully with {sustenance.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = Validator.find_by_name(first_player_name, self.players)
        player_two = Validator.find_by_name(second_player_name, self.players)
        stamina_res = []
        if player_one.stamina == 0:
            stamina_res.append(f"Player {first_player_name} does not have enough stamina.")
        if player_two.stamina == 0:
            stamina_res.append(f"Player {second_player_name} does not have enough stamina.")
        if stamina_res:
            return '\n'.join(stamina_res)
        if player_one.stamina > player_two.stamina:
            first_player, second_player = player_two, player_one
        else:
            first_player, second_player = player_one, player_two
        second_player.stamina -= (first_player.stamina / 2)
        if second_player.stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"
        first_player.stamina -= (second_player.stamina / 2)
        if first_player.stamina <= 0:
            first_player.stamina = 0
            return f"Winner: {second_player.name}"
        if first_player.stamina < second_player.stamina:
            return f"Winner: {second_player.name}"
        else:
            return f"Winner: {first_player.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - 2 * player.age < 0:
                player.stamina = 0
            else:
                player.stamina -= 2 * player.age
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ''
        for player in self.players:
            result += f"{str(player)}\n"
        for supply in self.supplies:
            result += f"{supply.details()}\n"
        return result.strip()



