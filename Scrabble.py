letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}

print(letter_to_points)

letter_to_points[" "]= 0

def score_words(word):
  point_total = 0
  for letter in word:
    letter = letter.upper()
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_words("brownie")
#print(brownie_points)

players = ["player1", "wordNerd", "Lexi Con", "Prof Reader"]
words = [["blue", "tennis", "exit"], ["earth", "eyes", "machine"], ["eraser", "belly", "husky"], ["zap", "coma", "period"]]
player_to_words = {key:value for key, value in zip(players, words)}
#print(player_to_words)

player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_words(word)
  player_to_points[player] = player_points
  
print(player_to_points)