from rolls import *
from common import *
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.arange(2, 13, 1)

# Analytical
ax, ay = np.arange(1, 7, 1), np.zeros(11)
for i in range(len(ax)):
    for j in range(len(ax)):
        ay[int(ax[i] + ax[j] - 2)] += 1

ay /= (len(ax) * len(ax))
plt.bar(x, ay, label="Analytic Data")


# Experimental
def estimate_rolls(num_samples, num_bins):
    hold = np.zeros(num_bins)

    for i in range(num_samples):
        roll1, roll2 = roll(1, 6, 2)
        hold[int(roll1 + roll2 - 2)] += 1

    hold /= num_samples
    return hold


numHists = 50
numRolls = 1000
allHists = np.zeros([numHists, len(x)])

for i in range(numHists):
    allHists[i, :] = estimate_rolls(numRolls, len(x))

lower, median, upper = np.zeros(len(x)), np.zeros(len(x)), np.zeros(len(x))
for i in range(len(lower)):
    median[i] = np.median(allHists[:, i])
    lower[i] = median[i] - np.percentile(allHists[:, i], 5)
    upper[i] = np.percentile(allHists[:, i], 95) - median[i]

plt.errorbar(x, median, yerr=[lower, upper], fmt='ko', label='Experimental Data')

plt.title('Comparison of Analytic and Experimental Results of the Sum of Two Dice')
plt.xlabel('Outcomes')
plt.ylabel('Probability of Outcomes')
plt.legend()
plt.xticks(x)
plt.show()
