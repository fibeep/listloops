songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0], songs[2])
print(songs[1:3])

songs[2] = "Kings Never Die"

songs.extend(["Do I Wanna Know", "Victorious"])

del songs[0]
print(songs)


animals = ["Snake", "Shark", "Horse"]
animals.append("Dog")
print(animals[2])
del animals[0]

for animal in animals:
    print(animal)