class Room:
  def __init__(self, name, description):
      self.name = name
      self.description = description
      self.connections = {}

  def connect_room(self, direction, room):
      self.connections[direction] = room

  def get_details(self):
      print(f"Room: {self.name}")
      print(f"Description: {self.description}")
      print("Connections: ", list(self.connections.keys()))


hallway = Room("Hallway", "A central hallway with doors leading to various rooms.")
kitchen = Room("Kitchen", "A room with cooking appliances and a strong smell of spices.")
dining_room = Room("Dining Room", "A room with a large table and chairs for dining.")
upstairs_hallway = Room("Upstairs Hallway", "A narrow hallway with doors leading to bedrooms and bathrooms.")
bedroom = Room("Bedroom", "A cozy bedroom with a bed and a wardrobe.")
bathroom = Room("Bathroom", "A small bathroom with a shower and sink.")


hallway.connect_room("kitchen", kitchen)
hallway.connect_room("dining room", dining_room)
hallway.connect_room("upstairs", upstairs_hallway)
kitchen.connect_room("hallway", hallway)
dining_room.connect_room("hallway", hallway)
upstairs_hallway.connect_room("hallway", hallway)
upstairs_hallway.connect_room("bedroom", bedroom)
upstairs_hallway.connect_room("bathroom", bathroom)
bedroom.connect_room("upstairs hallway", upstairs_hallway)
bathroom.connect_room("upstairs hallway", upstairs_hallway)
