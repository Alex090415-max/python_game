class Inventory:
  def __init__(self):
      self.items = []

  def add_item(self, item):
      self.items.append(item)
      print(f"Added {item.name} to inventory.")

  def remove_item(self, item):
      if item in self.items:
          self.items.remove(item)
          print(f"Removed {item.name} from inventory.")
      else:
          print(f"{item.name} not found in inventory.")

  def list_items(self):
      print("Inventory:")
      if not self.items:
          print("Your inventory is empty.")
      for item in self.items:
          print(f"- {item.name}")
