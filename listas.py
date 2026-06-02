#playlist músicas
import random

playlist = ["music1", "music2", "music3",
            "music4", "music5", "music6", "music7",
              "music8", "music9", "music10"]

print("Essa é sua playlist:\n")

for musicas in playlist:
    print(f"{musicas}")

play = [random.choice(playlist) for _ in range(1)]
print(f"A música que está tocando é: {play}.")