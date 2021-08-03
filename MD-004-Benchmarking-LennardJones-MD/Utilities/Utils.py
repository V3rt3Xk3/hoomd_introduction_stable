import pandas

class PandasUtility:

    @staticmethod
    def to_csv(currentPath, fileName, dataFrame):
        # HACK: Gathering the Company names for the web crawler.

        if (currentPath == ""):
            file_path = "./" + fileName
        elif (currentPath != ""):
            file_path = currentPath + '/' + fileName

        dataFrame.to_csv(file_path, sep="\t", encoding="utf-8", index=False)

        return

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