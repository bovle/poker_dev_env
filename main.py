from test import run_benchmark, run_table
from poker_game_runner.bots import foldBot, randombot
from example_bots import panic_bot, odds_bot, checkmate, position_bot

bots = [panic_bot, odds_bot, checkmate, position_bot, randombot, panic_bot, odds_bot, checkmate, position_bot,randombot]

#run_table(bots)

json = run_benchmark(bots, 30)
 
