from listas import LinkedList

l = LinkedList()
print(f"L esta vacía? {l.is_empty()}")
l.append(10)
l.append(5)
l.append(6)
l.append(20)
l.append(22)

print(f"L está vacía? {l.is_empty()}")

l.transversal()
l.remove(10)
l.transversal()
l.preppend(3)
l.transversal()
print(l.get())
print(l.get(2))
print(l.get(0))
