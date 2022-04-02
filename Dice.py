import random as rnd
class Dice:
  """Creates a pair of six sided dice with a roll method"""
  face1 = None
  face2 = None

  def roll(self):
    self.face1 = rnd.randrange(1, 7)
    self.face2 = rnd.randrange(1, 7)
    return [self.face1, self.face2]
