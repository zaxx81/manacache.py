# Simple python script to create a list of cards needed.
collectionCards, decklistCards = {}, {}

with open('collection.txt', 'r') as collectionFile, open('decklist.txt', 'r') as deckFile, open('rental.txt', 'w') as rentalFile:
    for line in collectionFile:
      if "Sideboard" not in line:
        collectionCards[line.rstrip().split(" ", 1)[1]] = int(line.split()[0])

    for line in deckFile:
      if "Sideboard" not in line and line not in ['\n', '\r\n']:
        data = line.rstrip().split(" ", 1)
        name, qty = data[1], int(data[0])
        
        if name in decklistCards:
          decklistCards[name] = qty + decklistCards[name]
        else:
          decklistCards[name] = qty

    rentalCards = { k : decklistCards[k] for k in set(decklistCards) - set(collectionCards) }

    for k, v in rentalCards.items():
      rentalFile.write(str(v) + " " + k + "\n")
