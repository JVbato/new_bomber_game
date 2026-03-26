from common_types import Scenario, BombType, BasicMovement
from random import Random

class SolidExplosion:
    def __init__(self, n: int, loc: tuple[int, int]) -> None:
        self._n = n
        self._loc = loc
        self._r = 2
        self._timer = 4
    
    def __str__(self) -> str:
        if self.is_done():
            return "."
        else:
            return str(self._timer)
        
    def is_done(self) -> bool:
        if self._timer <= 0:
            return True
        else:
            return False
        
    def explode(self) -> set[tuple[int, int]]:
        explosion: set[tuple[int, int]] = set()
        for row in range(self._n):
            for col in range(self._n):
                if abs(self._loc[0] - row) + abs(self._loc[1] - col) <= self._r:
                    explosion.add((row, col))
        return explosion
    
    def tick(self) -> None:
        self._timer -= 1
    
class BaseScenario:
    def __init__(self) -> None:
        self._n: int = 5
        self._rng: Random = Random()
        self._bombs: list[type[BombType]] = [SolidExplosion]
        self._gap: int = 2
    
    @property
    def n(self) -> int:
        return self._n
    
    @property
    def bombs(self) -> list[type[BombType]]:
        return self._bombs
    
    @property
    def gap(self) -> int:
        return self._gap

    @property
    def rng(self) -> Random:
        return self._rng


class Player:
    def __init__(self, n: int) -> None:
        self._n = n
        self._loc = (self._n // 2, self._n // 2)
        self._move_set: list[str] = [x.value for x in BasicMovement]

    @property
    def loc(self) -> tuple[int, int]:
        return self._loc
    
    @property
    def move_set(self) -> list[str]:
        return self._move_set
    
    def __str__(self) -> str:
        return "P"
    
    def move(self, wasd: str, grid: list[list[None | BombType]]) -> None:
        if wasd not in {x.value for x in BasicMovement}:
            return
        action = BasicMovement(wasd)
        movement = {BasicMovement.W: (-1, 0), BasicMovement.A: (0, -1), BasicMovement.S: (1, 0), BasicMovement.D: (0, 1)}
        r, c = self._loc
        dr, dc = movement[action]
        
        if self.in_bounds(r + dr, c + dc) and grid[r + dr][c + dc] is None:
            self._loc = r + dr, c + dc
    
    def in_bounds(self, r: int, c: int):
        if 0 <= r < self._n and 0 <= c < self._n:
            return True
        else:
            return False
        

class BomberModel:
    def __init__(self, scenario: Scenario) -> None:
        self._scenario = scenario
        self._n = self._scenario.n
        self._bomb = scenario.bombs
        self._player: Player = Player(self._n)
        self._is_over: bool = False
        self._turn = 1
        self._grid: list[list[BombType | None]] = [[None for _ in range(self._n)] for _ in range(self._n)]
    
    @property
    def is_over(self) -> bool:
        return self._is_over

    @property
    def turn(self) -> int:
        return self._turn

    @property
    def player_loc(self) -> tuple[int, int]:
        return self._player.loc
    
    def player_turn(self, action: str) -> None:
        self._player.move(action, self._grid)
    
    def bomb_turn(self) -> set[tuple[int, int]]:
        explosions: set[tuple[int, int]] = set()
        rng = self._scenario.rng
        #tick all bombs
        for r in range(self._n):
            for c in range(self._n):
                curr_cell = self._grid[r][c]
                if curr_cell:
                    curr_cell.tick()

                    if curr_cell.is_done():
                        explosions = explosions | curr_cell.explode()
                        self._grid[r][c] = None

       #plant new bomb if in gap
        if self._turn % self._scenario.gap == 0:
            i, j = rng.randrange(0, self._n), rng.randrange(0, self._n)
            if not self._grid[i][j]:
                self._grid[i][j] = rng.choice(self._bomb)(self._n, (i, j))
        
        if self.player_loc in explosions:
            self._is_over = True
        return explosions
    
    def next_turn(self) -> None:
        self._turn += 1
    
    @property
    def grid(self) -> list[list[None | BombType]]:
        return self._grid
    
    @property
    def player(self) -> Player:
        return self._player
    

    




    
