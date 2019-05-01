things = []

class thing():
	def __init__(self, loc, mass = 1, xrad = 1, yrad = 1):
		global things
		things += [self]
		
		self.location = loc
		self.gravity = [0, -0.5]
		self.__velocity = [0, 0]
		self.mass = mass
		self.xrad = xrad
		self.yrad = yrad
		self.immobile = False
		self.collidable = True
		self.drag = 0.9

	def thrust(self, vect, two = ''):
		try:
			self.__velocity[0] += vect[0]
			self.__velocity[1] += vect[1]
		except: # Just being nice and making it so you don't *need* an array. thrust(1,2) and thrust([1,2]) will do the same thing.
			self.__velocity[0] += vect
			self.__velocity[1] += two

	def getVelocity(self):
		return self.__velocity

	def __move(self, vect): # Called when ticking to trace collision.
		if not self.collidable: # Things that don't collide don't need tracing.
			self.location[0] += vect[0]
			self.location[1] += vect[1]
			return True

		if self.collision(self.location) != False: # Hopefully prevent clipping crashes
			print("Clipping error!")
			self.location = [self.location[0] - self.__velocity[0], self.location[1] - self.__velocity[1]]
			self.__velocity = [self.__velocity[0] * -1, self.__velocity[1] * -1]
			return False
#			o = self.collision(self.location)
#			if self.location[0] < o.location[0]:
#				if self.__velocity[0] > 0:
#					self.__velocity[0] += 1
#					self.__velocity[0] = self.__velocity[0] * -1
#				else:
#					self.__velocity[0] -= 1
#			elif self.location[0] > o.location[0]:
#				if self.__velocity[0] < 0:
#					self.__velocity[0] -= 1
#					self.__velocity[0] = self.__velocity[0] * -1
#				else:
#					self.__velocity[0] += 1
#			if self.location[1] < o.location[1]:
#				if self.__velocity[1] > 0:
#					self.__velocity[1] += 1
#					self.__velocity[1] = self.__velocity[1] * -1
#				else:
#					self.__velocity[1] -= 1
#			elif self.location[1] > o.location[1]:
#				if self.__velocity[1] < 0:
#					self.__velocity[1] -= 1
#					self.__velocity[1] = self.__velocity[1] * -1
#				else:
#					self.__velocity[1] += 1
#			return
			
		if vect[0] > self.xrad or vect[1] > self.yrad: # If it's moving more than its own size in the tick, trace collision recursively.
			nvec = [vect[0] * 0.5, vect[1] * 0.5]
			if self.__move(nvec):
				if self.__move(nvec):
					return True
				return False
			return False
		
		nloc = [self.location[0] + vect[0], self.location[1] + vect[1]] # Now we actually trace for collision
		if self.collision(nloc) == False: 
			self.location = nloc
			return True
		o = self.collision(nloc) # Now that we know what we're colliding with, it's time to find where we hit.
		minx = nloc[0] - (self.xrad/2)
		maxx = nloc[0] + (self.xrad/2)
		miny = nloc[1] - (self.yrad/2)
		maxy = nloc[1] + (self.yrad/2)
		ominx = o.location[0] - (o.xrad/2)
		omaxx = o.location[0] + (o.xrad/2)
		ominy = o.location[1] - (o.yrad/2)
		omaxy = o.location[1] + (o.yrad/2)
		
		if ominx < maxx and omaxx > minx: # Overlapping on x
			if self.location[0] < o.location[0]:
				nx = o.location[0] - (o.xrad/2+self.xrad/2) # If self is to the left, stop short on the left
			else:
				nx = o.location[0] + (o.xrad/2+self.xrad/2)
		else:
			nx = nloc[0] # If not overlapping, don't stop short
		
		if ominy < maxy and omaxy > miny: # As above, but y
			if self.location[1] < o.location[1]:
				ny = o.location[1] - (o.yrad/2+self.yrad/2)
			else:
				ny = o.location[1] + (o.yrad/2+self.yrad/2)
		else:
			ny = nloc[1]
		
		mm = 1 # Mass ratio as a modifier for the collision
		#self.location = [nx, ny]

		# Let's find a rough vector of collision to bounce from
		if (minx > ominx and maxx < omaxx) or (ominx > minx and omaxx < maxx): # Parallel along x
			nx = 0
		else:
			nx = 1
		
		if (miny > ominy and maxy < omaxy) or (ominy > miny and omaxy < maxy): # Parallel along y
			ny = 0
		else:
			ny = 1
		
		if not o.immobile:
			o.thrust(self.__velocity[0] * mm * nx * 0.5, self.__velocity[1] * mm * ny * 0.5)
		self.thrust(self.__velocity[0] / mm * nx * -0.5, self.__velocity[1] / mm * ny * -0.5)
		return False

	def tickMe(self):
		if self.immobile:
			self.__velocity = [0,0]
			return
		self.thrust(self.gravity)
		self.__move(self.__velocity)
		self.__velocity = [self.__velocity[0] * self.drag, self.__velocity[1] * self.drag]

	def collision(self, loc): # Checks if there would be something collidable overlapping with the object if it were at "loc".
		global things
		
		minx = loc[0] - (self.xrad/2)
		maxx = loc[0] + (self.xrad/2)
		miny = loc[1] - (self.xrad/2)
		maxy = loc[1] + (self.xrad/2)

		for o in things:
			if o != self:
				ominx = o.location[0] - (o.xrad/2)
				omaxx = o.location[0] + (o.xrad/2)
				ominy = o.location[1] - (o.yrad/2)
				omaxy = o.location[1] + (o.yrad/2)

				if ominx < maxx and omaxx > minx and ominy < maxy and omaxy > miny and o.collidable:
					return o
		return False

#ticker = thing([0,0])
#ticker.collidable = False

def tick():
	global things
	#global ticker
	#import math
	for i in things:
		i.tickMe()
		#i.location = [i.location[0] % 80, i.location[1] % 40]
	#s = ""
	#for q in range(40):
	#	for j in range(80):
	#		if ticker.collision([j, q]) == False:
	#			s += " "
	#		else:
	#			s += ticker.collision([j, q]).token
	#	if q != 39:
	#		s += "\n"
	#print(s)
    
