import math
from mesa import Agent


#Distance between two points
def get_distance(pos_1, pos_2):
  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2

  return math.sqrt(dx ** 2 + dy ** 2)


class Boxbot(Agent):
  def __init__(self, pos, model, moore = False, package = 0, energy = 0, vision = 0):
    super().__init__(pos, model)
    self.pos = pos
    self.moore = moore
    self.package = package
    self.energy = energy
    self.vision = vision

#Get package
  def get_box(self, pos):
    this_cell = self.model.grid.get_cell_list_contents([pos])
    print("Agents in cell", this_cell)
    for agent in this_cell:
      if type(agent) is Package:
        print(agent)
        print("List",this_cell)
        print("test",this_cell[0].accommodated)
        this_cell[0].accommodated = True
        print("Package found")
        
        return agent
    
  def is_occupied(self, pos):
    this_cell = self.model.grid.get_cell_list_contents([pos])
    return len(this_cell) > 1
    
  def move(self):
    next_moves = self.model.grid.get_neighborhood(self.pos, self.moore, True)
    next_move = self.random.choice(next_moves)
    self.model.grid.move_agent(self, next_move)
 
  def pick(self):
    box_patch = self.get_box(self.pos)
    print(box_patch)
      
  def step(self):
    self.move()
    self.pick()

class Package(Agent):
  def __init__(self, pos, model, accommodated):
    super().__init__(pos, model)
   
    self.accommodated = accommodated
  
  def storage(self):
    storage_position = (0,0)
    self.model.grid.move_agent(self, storage_position)

  def step(self):
    if self.accommodated == True:
      print("Current position")
      print(self.pos)
      self.storage()
      print("New position")
      print(self.pos)
    
    print("Initial parameters:")
    print(self.accommodated)
    
    print(self.pos)