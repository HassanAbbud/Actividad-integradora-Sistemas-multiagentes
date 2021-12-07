
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule

from agents import Boxbot, Package
from model import Warehouse

def agent_portrayal(agent):
  
  if agent is None:
    return
  
  portrayal = {}

  if type(agent) is Boxbot:

    portrayal["Shape"] = "resources/boxbot.jpg"
    portrayal["scale"] = 0.5
    portrayal["Layer"] = 1
  
  elif type(agent) is Package:

   
      portrayal["Color"] = "#D6F5D6"
      portrayal["Shape"] = "resources/package.png"
      portrayal["Filled"] = "true"
      portrayal["Layer"] = 0
      portrayal["w"] = 1
      portrayal["h"] = 1

  return portrayal
  
canvas_element = CanvasGrid(agent_portrayal, 5, 5, 500, 500)
chart_element = ChartModule([{"Label": "Boxbot", "Color": "#AA0000"}])

server = ModularServer(
    Warehouse, [canvas_element, chart_element], "Simulation"
    
)

server.port = 8887 # 
server.launch()