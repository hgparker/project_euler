from collections import Counter

straights = {
  (1, 2, 3, 4, 5),
  (2, 3, 4, 5, 6),
  (3, 4, 5, 6, 7),
  (4, 5, 6, 7, 8),
  (5, 6, 7, 8, 9),
  (6, 7, 8, 9, 10),
  (7, 8, 9, 10, 11),
  (8, 9, 10, 11, 12),
  (9, 10, 11, 12, 13),
  (10, 11, 12, 13, 14),
  (1, 11, 12, 13, 14),
  (1, 2, 12, 13, 14),
  (1, 2, 3, 13, 14),
  (1, 2, 3, 4, 14)
}


def get_rank(vals, suits):
  """Return comparable tuple for card given parallel []'s vals and suits"""

  sorted_val_freqs = sorted(Counter(vals).values())

  cs = Counter(suits)
  val_val = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
  }

  sorted_val_vals = sorted(val_val[val] for val in vals)
  # royal flush
  if len(cs) == 1 and sorted_val_vals == [10, 11, 12, 13, 14]:
    return 10, -1, tuple(sorted_val_vals[::-1])
  
  # straight flush
  if len(cs) == 1 and tuple(sorted_val_vals) in straights:
    return 9, sorted_val_vals[0], tuple(sorted_val_vals[::-1])
  
  # four of a kind
  if sorted_val_freqs == [1, 4]:
    return 8, sorted_val_vals[2], tuple(sorted_val_vals[::-1]) # b/c must be part of four

  # full house
  if sorted_val_freqs == [2, 3]:
    return 7, sorted_val_vals[2], tuple(sorted_val_vals[::-1]) # (3,) can't tie and must be in [2]
  
  # flush
  if len(cs) == 1:
    return 6, -1, tuple(sorted_val_vals[::-1])

  # straight
  if tuple(sorted_val_vals) in straights:
    return 5, sorted_val_vals[0], tuple(sorted_val_vals[::-1])
  
  # three of a kind
  if sorted_val_freqs == [1, 1, 3]:
    return 4, sorted_val_vals[2], tuple(sorted_val_vals[::-1]) # must be in [2]
  
  ### double check this
  # two pairs
  if sorted_val_freqs == [1, 2, 2]:
    pair_vals = []
    for k in range(len(sorted_val_vals)-1):
      if sorted_val_vals[k] == sorted_val_vals[k+1]:
        pair_vals.append(sorted_val_vals[k])
    pair_vals.sort(reverse=True)
    return 3, pair_vals, tuple(sorted_val_vals[::-1]) # always highest of pairs

  # one pair
  if sorted_val_freqs == [1, 1, 1, 2]:
    for k in range(len(sorted_val_vals)-1):
      if sorted_val_vals[k] == sorted_val_vals[k+1]:
        return 2, sorted_val_vals[k], tuple(sorted_val_vals[::-1])
  
  # high card
  return 1, sorted_val_vals[-1], tuple(sorted_val_vals[::-1])

def score_hand(hand):
  vals, suits = [], []
  for card in hand:
    vals.append(card[0])
    suits.append(card[1])
  rank = get_rank(vals, suits)  
  return rank

player1_wins = 0

def process(s):
  global player1_wins
  decomposed = s.split(" ")
  hand1, hand2 = decomposed[:5], decomposed[5:] 
  hand1_score, hand2_score = score_hand(hand1), score_hand(hand2)
  print(f"hand1_score = {hand1_score}")
  print(f"hand2_score = {hand2_score}")
  if hand1_score > hand2_score:
    player1_wins += 1

###

s = input()
while s != "":
  process(s)
  s = input()

print(f"player1_wins = {player1_wins}")