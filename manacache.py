# Simple python script to create a list of cards needed.
# Export your collection to the same directory as collection.txt
# Save a decklist as decklist.txt
# Script creates a rental.txt with the cards you need
collectionCards, decklistCards = {}, {}

with open('collection.txt', 'r') as collectionFile, open('decklist.txt', 'r') as deckFile, open('rental.txt', 'w') as rentalFile:
    for line in collectionFile:
      if "Sideboard" not in line:
        collectionCards[line.rstrip().split(" ", 1)[1]] = int(line.split()[0])

    for line in deckFile:
      if "Sideboard" not in line:
        data = line.rstrip().split(" ", 1)
        name, qty = data[1], int(data[0])
        
        if name in decklistCards:
          decklistCards[name] = qty + decklistCards[name]
        else:
          decklistCards[name] = qty

    rentalCards = { k : decklistCards[k] for k in set(decklistCards) - set(collectionCards) }

    for k, v in decklistCards.items():
      rentalFile.write(str(v) + " " + k + "\n")