from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from agents import Boxbot, Package
from schedule import RandomActivationByBreed

class Warehouse(Model):
  verbose = True

  def __init__(self, height = 5, width = 5, initial_population = 5):

    #Set parameters
    self.height = height
    self.width = width
    self.initial_population = initial_population

    self.schedule = RandomActivationByBreed(self)
    self.grid = MultiGrid(self.height, self.width, torus = False)
    self.datacollector = DataCollector(
      {"Boxbot": lambda m: m.schedule.get_breed_count(Boxbot),
      "Package": lambda m: m.schedule.get_breed_count(Package)}
    )

    #Create package
    for i in range(10):
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      accommodated = False
      package = Package((x, y), self, accommodated)
      self.grid.place_agent(package, (x,y))
      self.schedule.add(package)
      self.datacollector.collect(self)


    #Create agent
    for i in range(self.initial_population):
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      package = self.random.randrange(1, 3)
      energy = self.random.randrange(2,4)
      vision = self.random.randrange(1, 6)
      boxbot = Boxbot((x, y), self, False, package, energy, vision)
      self.grid.place_agent(boxbot, (x,y))
      self.schedule.add(boxbot)

      self.running = True
      self.datacollector.collect(self)

  def step(self):
    self.schedule.step()
    # collect data
    self.datacollector.collect(self)
    if self.verbose:
      print("Data:")
      print([self.schedule.time, self.schedule.get_breed_count(Boxbot)])
  
  def run_model(self, step_count = 200):
    if self.verbose:
      print(
        "Initial bot count:",
        self.schedule.get_breed_count(Boxbot),
      )
    for i in range(step_count):
      self.step()

    if self.verbose:
      print("")
      print(
        "Final bot count:",
        self.schedule.get_breed_count(Boxbot),
      )