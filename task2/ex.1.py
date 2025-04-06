# Let us define the list with names:
queue = ["Matti", "Riikka", "Antti", "Jenni", "Anu", "Ville", "Jarno"]
# Time t + 1: The first person in the queue leaves after paying for their purchases
queue.pop(0)
print(f'ex1: {queue}')
# Time t + 2: Ville recruits Anni to queue on his behalf
queue[queue.index('Ville')] = "Anni"
print(f'ex2: {queue}')
# Time t + 3: Jarno leaves, tired of the constant waiting
queue.pop(queue.index('Jarno'))
print(f'ex3: {queue}')
# Time t + 4: Marjo joins the end of the queue
queue.append("Marjo")
print(f'ex4: {queue}')
# Time t + 5: As a gentleman, Antti lets the two people behind him go ahead of him
queue.pop(queue.index('Antti'))
queue.append("Antti")
print(f'ex5: {queue}')
