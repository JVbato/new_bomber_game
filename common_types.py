from enum import StrEnum, auto
from typing import Protocol
from random import Random

#class infos for view
class BombInfo(Protocol):
    def __str__(self) -> str:
        ...

class PlayerInfo(Protocol):
    def __str__(self) -> str:
        ...
    
    @property
    def loc(self) -> tuple[int, int]:
        ...

    @property
    def move_set(self) -> list[str]:
        ...

# normal Protocols
class BombType(BombInfo, Protocol):
    def __init__(self, n: int, loc: tuple[int, int]) -> None:
        ...
    
    def __str__(self) -> str:
        ...
     
    def is_done(self) -> bool:
        ...
        
    def explode(self) -> set[tuple[int, int]]:
        ...
    
    def tick(self) -> None:
        ...

class Scenario(Protocol):
    def __init__(self) -> None:
        ...
    
    @property
    def n(self) -> int:
        ...
    
    @property
    def bombs(self) -> list[type[BombType]]:
        ...
    
    @property
    def gap(self) -> int:
        ...
    
    @property
    def rng(self) -> Random:
        ...

class Player(PlayerInfo, Protocol):
    @property
    def loc(self) -> tuple[int, int]:
        ...

    @property
    def move_set(self) -> list[str]:
        ...

    def __str__(self) -> str:
        ...
    
    def move(self, wasd: str, grid: list[list[None | BombType]]) -> None:
        ...

#enums
class Moveset(Protocol):
    key: object
    value: str

class BasicMovement(StrEnum):
    W = auto()
    A = auto()
    S = auto()
    D = auto()
    