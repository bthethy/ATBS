inv = {'rope': 1, 'gold coin': 42, 'dagger': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    """Function to display the inventory the game player has"""
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total = item_total + v

    print('Total number of items: ' + str(item_total) + '\n')

def addToInventory(inventory, addedItems):
    """Function to add newly found items to the existing inventory"""
    for item in addedItems:
        # item is not in list, so add it
        if item not in inventory:
           inventory[item] = 1 
        # item is in list, so increment existing key value
        else: 
          inventory[item] = inventory[item] + 1 

    return inventory


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)