
from poker_game_runner.state import Observation
from poker_game_runner.utils import Range, HandType

"""
  This bot tries to steal the pot with a min raise if everyone checks to it.
  Checks are a sign of a weak hand, so there is a good chance that the player will fold to a raise.
"""


class Bot:
  def get_name(self):
      return "checkmate"
  
  def act(self, obs: Observation):
    if self.is_checked_to_me(obs):
      return obs.get_min_raise() #attempt to steal the pot
    if obs.current_round == 0:
      return 0 # fold preflop, steal later hand
    else:
      return 1 # call and steal later round

  def is_checked_to_me(self, obs:Observation):
    call_actions = [action_info for action_info in obs.get_actions_this_round() if action_info.action == 1]
      
    return len(call_actions) == len(obs.get_active_players())-1