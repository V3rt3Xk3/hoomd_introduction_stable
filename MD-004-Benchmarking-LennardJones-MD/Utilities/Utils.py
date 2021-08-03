

class SysUtils:

	@staticmethod
	def generateSnaptshotPath(currentPath, fileName):
		# HACK: Generating the savePath

		if (currentPath == ""):
			file_path = "./snapshots/" + fileName
		elif (currentPath != ""):
			file_path = currentPath + '/snapshots/' + fileName

		return file_path
	
	@staticmethod
	def generateSavePathFromUtilities(currentPath, fileName):
		# HACK: Generating the savePath

		if (currentPath == ""):
			file_path = "./../snapshots/" + fileName
		elif (currentPath != ""):
			file_path = currentPath + '/../snapshots/' + fileName

		return file_path

	@staticmethod
	def generateLogPath(currentPath, fileName):
		# HACK: Generating the savePath

		if (currentPath == ""):
			file_path = "./snapshots/" + fileName
		elif (currentPath != ""):
			file_path = currentPath + '/snapshots/' + fileName

		return file_path