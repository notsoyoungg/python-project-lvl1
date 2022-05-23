#!/usr/bin/env python
from ..main_logic import logic
from ..games.game_progression import game
from ..games.game_progression import game_question


def main():
    logic(game, game_question)


if __name__ == '__main__':
    main()
