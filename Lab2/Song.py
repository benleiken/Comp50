class Song:
	"""A Song has a Title, Artist, and Album"""
	def __init__ (self, title, artist, album):
		self.title = title
		self.artist = artist
		self.album = album
	def output(self):
		print "Title: \"" + self.title + "\""
		print "Artist: " + self.artist
		print "Album: " + self.album + "\n"
		
if __name__ == "__main__":
	levels = Song("Levels", "Avicii", "Le7els")
	lazers = Song("Destroy Them With Lazers", "Knife Party", "The Knife Party")
	summit = Song("Summit", "Skrillex", "Scary Monsters")
	levels.output()
	lazers.output()
	summit.output()