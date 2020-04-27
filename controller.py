import csv
import os
import hashlib
import toHTML

DirectoryFile = "directory.csv"
CodeLength = 5

# code generation
with open(DirectoryFile, "r") as SourceFile:
	source = csv.reader(SourceFile)
	with open("temp.csv", "w") as WriteFile:
		writer = csv.writer(WriteFile)
		for row in source:
			FirstName = row[0].strip()
			LastName = row[1].strip()
			school = row[3].strip()
			HashBase = hashlib.sha256()
			HashBase.update(bytes(FirstName, encoding = "utf8"))
			HashBase.update(bytes(LastName, encoding = "utf8"))
			code = str(HashBase.hexdigest())[0:CodeLength]
			writer.writerow([FirstName, LastName, code, school])

os.remove(DirectoryFile)
os.rename("temp.csv", DirectoryFile)

# HTML generation
with open(DirectoryFile, "r") as SourceFile:
	source = csv.reader(SourceFile)
	for row in source:
		FirstName = row[0].strip()
		LastName = row[1].strip()
		code = row[2].strip()
		school = row[3].strip()
		toHTML.GenerateHTML(FirstName, LastName, code, school)