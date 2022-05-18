#!/usr/bin/env python
from ..main_logic import main
from ..games.game_even import game
from ..games.game_even import game_question


def script():
    main(game, game_question)


if __name__ == '__main__':
    script()
