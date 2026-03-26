from model_part1 import BomberModel
from view import BomberView
from time import sleep

class BomberController:
    def __init__(self, model: BomberModel, view: BomberView) -> None:
        self._model = model
        self._view = view
    
    def run(self):
        model = self._model
        view = self._view

        while not model.is_over:
            view.clear_screen()
            view.print_turn(model.turn)
            view.print_grid(model.grid, model.player)
            action = view.ask_player_movement(model.player.move_set)
            model.player_turn(action)
            explosions = model.bomb_turn()
            view.print_explosion(model.grid, model.player, explosions)
            sleep(1)
            model.next_turn()
        view.lose_message()
    



