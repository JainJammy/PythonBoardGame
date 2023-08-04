import random
class BoardGame:
    def __init__(self,num_players):
        self.num_players=num_players
        self.players={f"Player{i}":1000 for i in range(1,num_players+1)}
        self.bank_balance=5000
        self.hotels={
            'Sliver':{'value':200,'rent':50},
            'Gold':{'value':300,'rent':150},
            'Platinum':{'value':500,'rent':300}
        }
        self.player_positions = {player_name: 0 for player_name in self.players}

    def move_players(self,player_name,steps):
        current_position = self.player_positions[player_name]
        new_position = (current_position + steps) % len(cells)
        self.player_positions[player_name] = new_position

    def handle_jail(self,player_name):
        fine_amount = 150
        self.players[player_name] -= fine_amount
        self.bank_balance += fine_amount

    def handle_lottery(self,player_name):
        lottery_value = 200
        self.players[player_name] += lottery_value
        self.bank_balance -= lottery_value

    def handle_hotel(self,player_name,hotel_type):
        hotel_info = self.hotels[hotel_type]
        hotel_value = hotel_info['value']
        if self.players[player_name] >= hotel_value:
            self.players[player_name] -= hotel_value
            self.bank_balance += hotel_value
            self.player_positions[player_name] = hotel_type
    def get_asset_value(self,player_name):
        owned_hotel = self.player_positions[player_name]
        return self.hotels[owned_hotel]['value']
    def play(self,cells,dice_output):
        assert len(cells)==len(dice_output)
        for i,player_name in enumerate(self.players):
            player_index=i % len(cells)
            current_cell=cells[player_index]
            dice_roll=dice_output[player_name]
            print(f"{player_name} rolled {dice_roll}")
            if current_cell=="J":
                self.handle_jail(player_name)
            elif current_cell=="L":
                self.handle_lottery(player_name)
            elif current_cell=="H":
                hotel_type=input(f"{player_name},choose hotel type(Sliver Gold Platinum)")      
                self.handle_hotel(player_name,hotel_type)
            self.move_players(player_name,dice_roll)
    def print_player_balances(self):
        for player_name,balance in self.players.items():
            print(f"{player_name} balance:{balance} and asset of amount {self.get_asset_value(player_name)}")
    def print_bank_balance(self):
        print(f"Bank Balance:{self.bank_balance}")         
if __name__ == "__main__":
    cells="JHLHELHLHJ"
    dice_output=[2,2,1,4,4,2,4,4,2,2]
    game=BoardGame(3)
    game.play(cells,dice_output)
    game.print_player_balances()
    game.print_bank_balance()