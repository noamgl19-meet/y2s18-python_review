# Write your solutions for 1.5 here!
class Superheros:
	def __init__(self, name,superpower, strengh):
		self.name = name
		self.superpower = superpower
		self.strengh = strengh
	def name_strengh(self):
		print("the name of the superhero is: " + self.name +",his strengh level is: "+str(self.strengh))
	def save_civilian(self, work):
		if work > self.strengh:
			print("not enough power :(")	
		else:
			self.strengh -= work
			print("the amount of strengh left in your hero is "+str(self.strengh))
			
hero = Superheros("noam", "flying", 11)
hero.name_strengh()
hero.save_civilian(2)