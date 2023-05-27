
#Class implementing random generator algorithm		
class RandomGenerator:
	def __init__(self):
		self.bag = []
		self.refill_bag()
	
	def refill_bag(self):
		self.bag = [0,1,2,3,4,5,6]
		random.shuffle(self.bag)
	
	def get_next_piece(self):
		if len(self.bag) == 0:
			self.refill_bag()
		return self.bag.pop(0)
	

#Class for the game's timing events
class GameClock: