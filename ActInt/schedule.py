from collections import defaultdict
from mesa.time import RandomActivation

class RandomActivationBySpawn(RandomActivation):

  def __init__(self, model):
    super().__init__(model)
    self.agents_by_spawn = defaultdict(dict)

  def add(self, agent):
    self._agents[agent.unique_id] = agent
    agent_class = type(agent)
    self.agents_by_spawn[agent_class][agent.unique_id] = agent

  def remove(self, agent):

    del self._agents[agent.unique_id]

    agent_class = type(agent)
    del self.agents_by_spawn[agent_class][agent.unique_id]

  def step(self, by_spawn = True):

    if by_spawn:
      for agent_class in self.agents_by_spawn:
        self.step_spawn(agent_class)
        self.steps += 1
        self.time += 1
    else:
      super().step()
  
  def step_spawn(self, spawn):

    agent_keys = list(self.agents_by_spawn[spawn].keys())
    self.model.random.shuffle(agent_keys)
    for agent_key in agent_keys:
      self.agents_by_spawn[spawn][agent_key].step()
  
  def get_spawn_count(self, spawn_class):
    return len(self.agents_by_spawn[spawn_class].values())