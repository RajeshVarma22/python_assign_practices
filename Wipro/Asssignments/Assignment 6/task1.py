footballPlayers = ["Eve", "Tom", "Richard", "Peter"]
volleyballPlayers = ["Jack", "Hugh", "Peter", "Sam"]
basketballPlayers = ["Eve", "Richard", "Jessica", "Sam", "Michael"]

basketballPlayersSet = set(basketballPlayers).difference(set(footballPlayers).union(set(volleyballPlayers)))

print(basketballPlayersSet)