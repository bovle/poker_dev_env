from os import sep
import time
from poker_game_runner.runner import play_tournament_table
import json
from multiprocessing import Manager, Pool, Process, Queue, cpu_count

PROCESS_COUNT = cpu_count() - 2


def run_benchmark(bots, run_count):
    bot_instances = [b.Bot() for b in bots]
    data = [{"name": b.get_name(), "wins": 0} for b in bot_instances]
    for i in range(run_count):
        res, _ = play_tournament_table(bot_instances, 1000)
        data[res[0]["id"]]["wins"] += 1
        # print(chr(27) + "[2J")
        print("--- " + str(i + 1) + "/" + str(run_count) + " ---")
        [print(d) for d in sorted(data, key=lambda x: x["wins"], reverse=True)]
    return data


def add_victory(data, r):
    data[r[0]["id"]]["wins"] += 1


def local_run_tournament(q: Queue, bot_instances):
    res, _ = play_tournament_table(bot_instances, 1000)
    q.put(res)


def run_benchmark_parallel(bots, run_count):

    start_time = time.time()

    bot_instances = [b.Bot() for b in bots]
    data = [{"name": b.get_name(), "wins": 0} for b in bot_instances]
    m = Manager()
    q = m.Queue()

    with Pool(processes=PROCESS_COUNT) as pool:
        args = [(q, bot_instances) for _ in range(run_count)]
        pool.starmap(local_run_tournament, args)

    while not q.empty():
        res = q.get()
        data[res[0]["id"]]["wins"] += 1

    print(f"--- {run_count} ---")
    [print(d) for d in sorted(data, key=lambda x: x["wins"], reverse=True)]

    duration = time.time() - start_time
    duration_pr_sim = round(duration / run_count, 5)
    print(f"-----------------------------------------")
    print(f"Simulation took {duration_pr_sim} seconds pr. round")
    print(f"Using {PROCESS_COUNT} processes")
    print(f"--- {round(duration, 2)} seconds ---")

    return data


def run_table(bots):
    bot_instances = [b.Bot() for b in bots]

    res, details = play_tournament_table(
        bot_instances, 1000, use_timeout=False, console_output=True
    )

    return json.dumps(details)
