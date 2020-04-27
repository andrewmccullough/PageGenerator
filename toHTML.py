import xlrd


def GenerateHTML(FirstName, LastName, OutputFilename, school, GeneralMessageFile = "messages/all.xlsx"):
	PageTemplate = """
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>For {0}, from Detachment 890</title>
	    <link rel="stylesheet" href="styles/{1}.css">
	</head>
	<body>
	    <div id="top-splash">
	        <h1>Hi, {2}!</h1>
	    </div>
	    <div id="background-info">
	        <p>Since the school year ended so abruptly, we didn&rsquo;t get the opportunity to say goodbye to all of our graduating cadets. We wanted to let you know how much we&rsquo;ve appreciated your friendship, mentorship, and hard work over the years, and to wish you the best as you start your careers after commissioning. Read the notes from the first-, second-, and third-year classes below!</p>
	        {3}
	    </div>
	    <div id="main">
	        <div id="container">
	            <div id="general-messages">
	                <h1>Messages for the Class of 2020</h1>
					{4}
	            </div>
	            {5}
	        </div>
	    </div>
	</body>
	</html>
	"""

	# process general messages
	GeneralMessages = """"""
	book = xlrd.open_workbook(GeneralMessageFile)
	worksheet = book.sheet_by_index(0)
	for entry in range(worksheet.nrows):
		sender = worksheet.cell(entry, 0).value
		body = worksheet.cell(entry, 1).value

		BodyParsed = body.split("\n")
		paragraphs = """"""
		for paragraph in BodyParsed:
			if len(paragraph) > 1:
				ParagraphTemplate = """<p>{0}</p>"""
				paragraphs += ParagraphTemplate.format(paragraph)

		MessageTemplate = """
			<div class="message">
	            <div class="body">
	                {0}
	            </div>
	            <p class="sender">{1}</p>
	        </div>
		"""

		GeneralMessages += MessageTemplate.format(paragraphs, sender)

	# process personal messages
	PersonalMessages = """"""
	book = xlrd.open_workbook("messages/" + LastName.lower() + ".xlsx")
	worksheet = book.sheet_by_index(0)
	if worksheet.nrows > 0:
		for entry in range(worksheet.nrows):
			sender = worksheet.cell(entry, 0).value
			body = worksheet.cell(entry, 1).value

			BodyParsed = body.split("\n")
			paragraphs = """"""
			for paragraph in BodyParsed:
				if len(paragraph) > 1:
					ParagraphTemplate = """<p>{0}</p>"""
					paragraphs += ParagraphTemplate.format(paragraph)

			MessageTemplate = """
				<div class="message">
		            <div class="body">
		                {0}
		            </div>
		            <p class="sender">{1}</p>
		        </div>
			"""

			PersonalMessages += MessageTemplate.format(paragraphs, sender)
		PersonalMessagesSection = """
	        <div id="personal-messages">
                <h1>Messages for you</h1>
				{0}
	        </div>
		"""
		PersonalMessagesSection = PersonalMessagesSection.format(PersonalMessages)
		Navigation = """
			<ul>
	            <li><a href="#general-messages">Messages for the Class of 2020</a></li>
	            <li><a href="#personal-messages">Messages for you</a></li>
	        </ul>
		"""
	else:
		PersonalMessagesSection = """"""
		Navigation = """"""

	f = open("outputs/" + OutputFilename + ".html", "w")
	f.write(PageTemplate.format(FirstName + " " + LastName, school.lower(), FirstName, Navigation, GeneralMessages, PersonalMessagesSection))
	f.close()
