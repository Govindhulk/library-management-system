from Models.DBDAO import DBDAO

class DAO():
	print("Hii")
	def __init__(self, app):
		self.db = DBDAO(app)
