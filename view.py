from common_types import BombInfo, PlayerInfo
from typing import Sequence

class BomberView:
    def print_grid(self, grid: Sequence[Sequence[None | BombInfo]], player: PlayerInfo):
        str_grid = [[str(cell) if cell is not None else "." for cell in row] for row in grid]
        str_grid[player.loc[0]][player.loc[1]] = str(player)
        for row in str_grid:
            print(" ".join(row))
    
    def print_explosion(self, grid: Sequence[Sequence[None | BombInfo]], player: PlayerInfo, explosions: set[tuple[int, int]]):
        str_grid = [[str(cell) if cell is not None else "." for cell in row] for row in grid]
        str_grid[player.loc[0]][player.loc[1]] = str(player)
        for i, j in explosions:
            str_grid[i][j] = "*"
        for row in str_grid:
            print(" ".join(row))

    def ask_player_movement(self, moveset: list[str]) -> str:
        print("Moves: ", end="")
        print(", ".join(moveset))

        action = input("- ").lower().strip()
        return action
    
    def print_turn(self, turn: int):
        print(f"TURN {turn}")

    def lose_message(self):
        print("GG you lost")
    
    def clear_screen(self):
        print("\033c", end="")