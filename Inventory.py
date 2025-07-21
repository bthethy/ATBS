stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
bonus_stuff = {'magic potion': 1, 'flaming sword': 1, 'invisibility cloak': 2}

def displayInventory(inventory, inventory_name = 'inventory'):
    """Function to display the inventory the game player has"""
    print(f"{inventory_name}")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total = item_total + v

    print('Total number of items: ' + str(item_total) + '\n')

displayInventory(stuff, "Player's inventory:")
displayInventory(bonus_stuff, "Bonus inventory:")