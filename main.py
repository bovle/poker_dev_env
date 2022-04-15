from datetime import datetime
from test import run_benchmark, run_benchmark_parallel, run_table
from poker_game_runner.bots import randombot
from example_bots import panic_bot, odds_bot, checkmate, position_bot
import my_bot

bots = [
    panic_bot,
    odds_bot,
    checkmate,
    position_bot,
    randombot,
    panic_bot,
    odds_bot,
    checkmate,
    position_bot,
    my_bot,
]

# run_table(bots)

run_benchmark_parallel(bots, 200)
