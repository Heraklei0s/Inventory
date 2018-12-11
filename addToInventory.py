


def addToInventory(inventory, addedItems):
    for v in range(len(addedItems)):
        inventory.setdefault(addedItems[v], 1)
        inventory[addedItems[v]] = inventory[addedItems[v]] + 1
    return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = {'gold coin': 42, 'rope': 1}
        
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)        
        
        
