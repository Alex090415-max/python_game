class Item:
  def __init__(self, name, description, value):
      self.name = name
      self.description = description
      self.value = value

  def describe(self):
      print(f"{self.name}: {self.description} (Value: {self.value})")


first_aid = Item("First aid", "Restores a large amount of health.", 75)
#add a key item for 'locked doors'

