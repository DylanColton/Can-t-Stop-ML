import matplotlib.pyplot as plt
import intelligence
import numpy as np
import Graphs
import board

gameBoard = board.Board(1)
randomPlayer = intelligence.RandomPlayer()
greedyPlayer = intelligence.GreedyPlayer()

numTrials, numGames, numRounds = 10, 20, 50
confidence = 95


randoX, randoY, randoLow, randoMed, randoUpp, randoFullData = Graphs.gain_data(numTrials, numGames, numRounds,
                                                                               randomPlayer, confidence)
greedX, greedY, greedLow, greedMed, greedUpp, greedFullData = Graphs.gain_data(numTrials, numGames, numRounds,
                                                                               greedyPlayer, confidence)

plt.figure(figsize=(13, 6))
w = 0.35

randoMedBar = randoMed / (numTrials * numRounds * numGames)
randoLowBar = randoLow / (numTrials * numRounds * numGames)
randoUppBar = randoUpp / (numTrials * numRounds * numGames)

greedMedBar = greedMed / (numTrials * numRounds * numGames)
greedLowBar = greedLow / (numTrials * numRounds * numGames)
greedUppBar = greedUpp / (numTrials * numRounds * numGames)

# Random Player
randoBar = plt.bar(randoX[:50]-w/2, randoMedBar[:50], w, label="Random")
randoBar = plt.errorbar(randoX[:50]-w/2, randoMedBar[:50], yerr=[randoLowBar[:50], randoUppBar[:50]], fmt='none',
                        ecolor='k', label="Random Error")
# Greedy Player
greedBar = plt.bar(greedX[:50]+w/2, greedMedBar[:50], w, label="Greedy")
greedBar = plt.errorbar(greedX[:50]+w/2, greedMedBar[:50], yerr=[greedLowBar[:50], greedUppBar[:50]], fmt='none',
                        label="Greedy Error")

if len(greedX[:50]) < len(randoX[:50]):
    plt.xticks(randoX[:50])
else:
    plt.xticks(greedX[:50])
plt.title("Comparison of Random and Greedy Strategies")
plt.xlabel("Number of Turns to Win")
plt.ylabel("Probability of Winning in this Number of Turns")
plt.legend()
plt.savefig("Random vs Greedy labelled.png")
plt.show()

plt.figure(figsize=(13, 6))
w = 0.35

# Random Player
randoBar = plt.bar(randoX[:50]-w/2, randoMedBar[:50], w, label="Random")
randoBar = plt.errorbar(randoX[:50]-w/2, randoMedBar[:50], yerr=[randoLowBar[:50], randoUppBar[:50]], fmt='none',
                        ecolor='k', label="Random Error")
# Greedy Player
greedBar = plt.bar(greedX[:50]+w/2, greedMedBar[:50], w, label="Greedy")
greedBar = plt.errorbar(greedX[:50]+w/2, greedMedBar[:50], yerr=[greedLowBar[:50], greedUppBar[:50]], fmt='none',
                        label="Greedy Error")

plt.xlabel("Number of Turns to Win")
plt.ylabel("Probability of Winning in this Number of Turns")
plt.legend()
plt.savefig("Random vs Greedy.png")
plt.show()

hold = []
for i in range(len(randoY)):
    hold.append(np.round(randoY[i]))

randoBoxData = []

for i in range(len(randoX)):
    for j in range(int(hold[i])):
        randoBoxData.append(randoX[i])

randoLB, randoUB = Graphs.get_lower_and_upper(randoBoxData)
randoLQ, randoMed, randoUQ = np.percentile(randoBoxData, 25), np.median(randoBoxData), np.percentile(randoBoxData, 75)
randoMean, randoMode = np.mean(randoBoxData), np.argmax(np.bincount(randoBoxData))
randoRange, randoIQR = randoUB - randoLB, randoUQ - randoLQ

randoData = [randoLB, randoLQ, randoMed, randoUQ, randoUB, randoRange, randoIQR, randoMean, randoMode]

hold = []
for i in range(len(greedY)):
    hold.append(np.round(greedY[i]))

greedBoxData = []

for i in range(len(greedX)):
    for j in range(int(hold[i])):
        greedBoxData.append(greedX[i])

greedLB, greedUB = Graphs.get_lower_and_upper(greedBoxData)
greedLQ, greedMed, greedUQ = np.percentile(greedBoxData, 25), np.median(greedBoxData), np.percentile(greedBoxData, 75)
greedMean, greedMode = np.mean(greedBoxData), np.argmax(np.bincount(greedBoxData))
greedRange, greedIQR = greedUB - greedLB, greedUQ - greedLQ

greedData = [greedLB, greedLQ, greedMed, greedUQ, greedUB, greedRange, greedIQR, greedMean, greedMode]

# Random Player
plt.title("Random Player")
plt.xlabel("Number of Turns")
plt.boxplot(randoBoxData, vert=False, showfliers=False, labels=["Random"])
plt.savefig("RandomBox.png")
plt.show()

# Greedy Player
plt.title("Greedy Player")
plt.xlabel("Number of Turns")
plt.boxplot(greedBoxData, vert=False, showfliers=False, labels=["Greedy"])
plt.savefig("GreedyBox.png")
plt.show()

# Comparison
plt.title("Comparison of Random and Greedy Players")
plt.xlabel("Number of Turns to Win")
plt.boxplot([randoBoxData, greedBoxData], labels=["Random", "Greedy"], vert=False, showfliers=False)
plt.savefig("Random vs Greedy Box.png")
plt.show()

randoFile = open("../stoof/randomdata.csv", "w")

randoFile.write("Frequency of Number of Turns to Win \n")
randoFile.write("lower bound, lower quartile, median, upper quartile, upper bound, range, inter-quartile range, mean, "
                "mode\n")
for i in range(len(randoData)):
    randoFile.write(str(randoData[i]))
    if i < len(randoData) - 1:
        randoFile.write(", ")

randoFile.write("\n\nNumber of Turns, ")
for i in range(len(randoX)):
    randoFile.write(str(randoX[i]))
    if i < len(randoX) - 1:
        randoFile.write(", ")
randoFile.write("\nNumber Of Wins, ")
for i in range(len(randoY)):
    randoFile.write(str(randoY[i]))
    if i < len(randoY) - 1:
        randoFile.write(", ")
randoFile.close()

greedFile = open("../stoof/greedydata.csv", "w")
greedFile.write("Frequency of Number of Turns to Win \n")
greedFile.write("lower bound, lower quartile, median, upper quartile, upper bound, range, inter-quartile range, mean, "
                "mode\n")
for i in range(len(greedData)):
    greedFile.write(str(greedData[i]))
    if i < len(greedData) - 1:
        greedFile.write(", ")

greedFile.write("\n\nNumber of Turns, ")
for i in range(len(greedX)):
    greedFile.write(str(greedX[i]))
    if i < len(greedX) - 1:
        greedFile.write(", ")
greedFile.write("\nNumber Of Wins, ")
for i in range(len(greedY)):
    greedFile.write(str(greedY[i]))
    if i < len(greedY) - 1:
        greedFile.write(", ")
greedFile.close()
