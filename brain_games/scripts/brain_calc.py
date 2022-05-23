#!/usr/bin/env python
from ..main_logic import logic
from ..games.game_calc import calc
from ..games.game_calc import game_question


def main():
    logic(calc, game_question)


if __name__ == '__main__':
    main()
