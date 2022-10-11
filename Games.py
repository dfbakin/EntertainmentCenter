import Media


class Games(Media):
	# TODO
	# change *args to explicitly stated arguments or kwargs
	def __init__(self, *args, platforms: list = None, has_multiplayer: bool):
		super.__init__(*args)
		if platforms is None:
			platforms = []
		self.platforms = platforms
		self.has_multiplayer = has_multiplayer

	@property
	def platforms(self):
		return self.platforms

	@platforms.setter
	def platforms(self, new_platforms: list):
		if not isinstance(new_platforms, list):
			raise TypeError("Platforms must be a list of strings.")
		self._platforms = new_platforms

	@property
	def has_multiplayer(self):
		return self.has_multiplayer

	@has_multiplayer.setter
	def has_multiplayer(self, new_has_multiplayer: bool):
		if not isinstance(new_has_multiplayer, bool):
			raise TypeError("Has_multiplayer must be of boolean type.")
		self._has_multiplayer = new_has_multiplayer
