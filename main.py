from test import run_benchmark, run_table
from poker_game_runner.bots import randombot
from example_bots import panic_bot, odds_bot, checkmate, position_bot
import my_bot_dev
import my_bot_master

bots = [panic_bot, odds_bot, checkmate, position_bot, randombot, panic_bot, odds_bot, checkmate, position_bot, my_bot_dev]

#run_table(bots)

run_benchmark(bots, 30)
 
