from matplotlib import pyplot as plt
import seaborn as sns

spell = 'Flash Heal'

ranks = [1,2,3,4,5,6,7]
cast_time = 1.5
amount = {1:[202,247],2:[269,325],3:[339,406],4:[414,492],5:[534,633],6:[662,783],7:[828,975]} # each key is the spell rank while each list value is the range of the amount healed
mana = [125,155,185,215,265,315,380]
results = dict()

def downranking(rank, spellpower):
    spc = spellpower * 1.5 / 3.5
    x = sum(amount.get(rank)) / len(amount.get(rank))
    heal = x + spc
    return heal
x = downranking(1, 300)

for i in amount:
    results[i] = {'mana':mana[i - 1]}
    results[i].update({'input':sum(amount[i]) / len(amount[i])})
    results[i].update({'output':[results[i]['input'] + (sp * 100 * 1.5 / 3.5) for sp in range(10) ]})
    results[i].update({'me_rating':[m / results[i]['mana'] for m in results[i]['output']]})
print(results)

thing = [results[i]['input'] / results[i]['mana'] for i in results]
x = [results[x]['mana'] for x in results]
y = [results[x]['input'] for x in results]

plt.plot([i + 1 for i in range(len(thing))], thing)
plt.title("Base Spell vs. Mana")
plt.xlabel('Spell Rank')
plt.ylabel("Mana Efficiency")
plt.grid(b=True)
plt.legend()
plt.show()
plt.show()


for i in results:
    plt.plot(results[i]['output'], label = 'Rank {}'.format(i))
plt.title("Healing + Coefficient vs. Spellpower")
plt.xlabel('Spellpower 1e-2')
plt.ylabel("Healing")
plt.grid(b=True)
plt.legend()
plt.show()

for i in results:
    plt.plot(results[i]['me_rating'], label = 'Rank {}'.format(i))
plt.title("Mana vs. Spellpower")
plt.xlabel('Spellpower 1e-2')
plt.ylabel("Mana Efficiency")
plt.grid(b=True)
plt.legend()
plt.show()

for i in results:
    plt.plot(results[i]['me_rating'], results[i]['output'], label = 'Rank {}'.format(i))
plt.title("Healing + Coefficient vs. Mana")
plt.xlabel('Mana Efficiency')
plt.ylabel("Healing")
plt.grid(b=True)
plt.legend()
plt.show()