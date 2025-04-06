import random


class Item:
    """
    Represents an item in the game with a name and value.
    """

    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def get_name(self):
        """Returns the item's name."""
        return self.__name

    def get_value(self):
        """Returns the item's value."""
        return self.__value

    def __str__(self):
        """String representation of the item."""
        return f"{self.__name} costs {self.__value} gold."


class Character:
    """
    Represents a player or NPC in the game with gold and a backpack.
    """

    def __init__(self, name, gold):
        self.__name = name
        self.__gold = gold
        self.__backpack = []  # Holds items

    def get_name(self):
        return self.__name

    def get_gold(self):
        return self.__gold

    def get_backpack(self):
        return self.__backpack

    def add_gold(self, amount):
        """Adds gold to the character's balance."""
        self.__gold += amount

    def subtract_gold(self, amount):
        """Reduces gold if the character has enough."""
        if self.__gold >= amount:
            self.__gold -= amount
            return True
        return False

    def add_item(self, item):
        """Adds an item to the backpack."""
        self.__backpack.append(item)

    def remove_item(self, item):
        """Removes an item from the backpack, if present."""
        if item in self.__backpack:
            self.__backpack.remove(item)
            return True
        return False

    def show_backpack(self):
        """Displays contents of the backpack."""
        return "The backpack is empty." if not self.__backpack else ", ".join(str(item) for item in self.__backpack)

    def __str__(self):
        return f"{self.__name} has {self.__gold} gold and carries: {self.show_backpack()}"


class NPC(Character):
    """
    Represents an NPC shopkeeper with inventory.
    """

    def __init__(self, name="Shopkeeper"):
        super().__init__(name, gold=1000)
        self.__shop_inventory = []

    def add_item_to_shop(self, item):
        self.__shop_inventory.append(item)

    def show_shop_inventory(self):
        return "The shop is empty." if not self.__shop_inventory else ", ".join(
            str(item) for item in self.__shop_inventory)

    def get_shop_inventory(self):
        return self.__shop_inventory


class Shop:
    """
    A shop where players can buy, sell, or gamble for items.
    """

    def __init__(self, shopkeeper):
        self.__shopkeeper = shopkeeper

    def buy_item(self, player, item_name):
        """Handles purchasing an item from the shop."""
        for item in self.__shopkeeper.get_shop_inventory():
            if item.get_name() == item_name:
                if player.get_gold() >= item.get_value():
                    player.subtract_gold(item.get_value())
                    player.add_item(item)
                    self.__shopkeeper.get_shop_inventory().remove(item)
                    print(f"{player.get_name()} bought {item.get_name()} for {item.get_value()} gold.")
                else:
                    print("Not enough gold.")
                return
        print("Item not found in shop.")

    def sell_item(self, player, item_name):
        """Handles selling an item to the shop at half price."""
        for item in player.get_backpack():
            if item.get_name() == item_name:
                player.add_gold(item.get_value() // 2)
                player.remove_item(item)
                self.__shopkeeper.get_shop_inventory().append(item)
                print(f"{player.get_name()} sold {item.get_name()} for {item.get_value() // 2} gold.")
                return
        print("Item not found in backpack.")

    def gamble(self, player, desired_item_name):
        """Allows the player to gamble an item for another item in the shop."""
        if not player.get_backpack():
            print("Backpack is empty! Cannot gamble.")
            return

        desired_item = next(
            (item for item in self.__shopkeeper.get_shop_inventory() if item.get_name() == desired_item_name), None)
        if not desired_item:
            print("The desired item is not in the shop.")
            return

        lost_item = random.choice(player.get_backpack())  # Lose a random item
        player.remove_item(lost_item)

        if random.random() < 0.5:
            player.add_item(desired_item)
            self.__shopkeeper.get_shop_inventory().remove(desired_item)
            print(f"{player.get_name()} won the gamble and received {desired_item.get_name()}!")
        else:
            print(f"{player.get_name()} lost the gamble and lost {lost_item.get_name()}.")

    @staticmethod
    def generate_random_item():
        """Generates a random item for the shop."""
        items = [Item("Health Potion", 10), Item("Magic Scroll", 50), Item("Iron Armor", 200)]
        return random.choice(items)


# Test cases
if __name__ == "__main__":
    player = Character("Player", 100)
    shopkeeper = NPC("Old Merchant")
    shop = Shop(shopkeeper)

    shopkeeper.add_item_to_shop(Item("Stone Sword", 50))
    shopkeeper.add_item_to_shop(Item("Stone Shield", 30))

    player.add_item(Item("Wooden Stick", 10))
    player.add_item(Item("Old Helmet", 15))

    print(player)
    print("Shop Inventory:", shopkeeper.show_shop_inventory())

    shop.buy_item(player, "Stone Sword")
    print(player)

    shop.sell_item(player, "Old Helmet")
    print(player)

    shop.gamble(player, "Stone Shield")
    print(player)

    random_item = Shop.generate_random_item()
    print(f"Randomly generated item: {random_item}")
