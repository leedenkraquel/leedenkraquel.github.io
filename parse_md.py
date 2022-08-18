###
# Name: Markdown
# Author(s): Leeden Raquel
# Description: Represents the header and content in a markdown file
###
class Markdown():
	def __init__(self):
		self.layout = ""
		self.type = ""
		self.image = ""
		self.title = ""
		self.permalink = ""
		self.date = ""
		self.labels = []
		self.summary = ""
		self.content = ""
		self.hide = False

	def __str__(self):
		output = "---\n"
		output += "layout: " + self.layout + "\n"
		output += "type: " + self.type + "\n"
		output += "image: " + self.image + "\n"
		output += "title: " + self.title + "\n"
		output += "permalink: " + self.permalink + "\n"
		output += "date: " + self.date + "\n"
		output += "labels: " + ', '.join(self.labels) + "\n"
		output += "summary: " + self.summary + "\n---\n"
		output += self.content
		return output

	def to_html(self):
		return self.content

	def get_layout(self):
		return self.layout

	def get_type(self):
		return self.type

	def get_image(self):
		return self.image

	def get_title(self):
		return self.title

	def get_permalink(self):
		return self.permalink

	def get_date(self):
		return self.date

	def get_labels(self):
		return self.labels

	def get_summary(self):
		return self.summary
	
	def get_hidden(self):
		return self.hide

###
# Author(s): Leeden Raquel
# Inputs:
#  filedir - string that represents the destination of the file
# Description: parses a markdown file to a Markdown object
# Returns:
#  Markdown - an object that has the headers and content as props
###
def parse_md(filedir):
	md_file = open(filedir, "r")
	content = md_file.readlines()
	output = Markdown()
	header_indexes = [i for i in range(len(content)) if "---" in content[i]]
	
	for line in content[header_indexes[0]+1:header_indexes[1]]:
		if "layout" in line:
			output.layout = line.split(":")[1][1:-1]
		elif "type" in line:
			output.type = line.split(":")[1][1:-1]
		elif "image" in line:
			output.image = line.split(":")[1][1:-1]
		elif "title" in line:
			output.title = line.split(":")[1][1:-1]
		elif "permalink" in line:
			output.permalink = line.split(":")[1][1:-1]
		elif "date" in line:
			output.date = line.split(":")[1][1:-1]
		elif "summary" in line:
			output.summary = line.split(":")[1][1:-1]
		elif "hide" in line:
			output.hide = line.split(":")[1][1:-1]
		elif " - " in line:
			output.labels.append(line.split("-")[1][1:-1])
	
	for line in content[header_indexes[1]+1:]:
		if "[" in line:
			anchor_start_indexes = [i for i in range(len(line)) if line[i] == "["]
			anchor_end_indexes = [i for i in range(len(line)) if line[i] == "]"]
			anchor_indexes = [list(a) for a in zip(anchor_start_indexes, anchor_end_indexes)]
			
			for i in range(len(anchor_indexes) -1, -1, -1):
				ref_index = [anchor_indexes[i][1]+1, line.index(")", anchor_indexes[i][1]+1)]
				line = line[:anchor_indexes[i][0]] + "<a class='project_link' href='" + line[ref_index[0]+1:ref_index[1]] + "'>" + line[anchor_indexes[i][0]+1:anchor_indexes[i][1]] + "</a>" + line[ref_index[1]+1:]
		
		if line[0] == "<":
			output.content += line
		elif line[0] == ">":
			output.content += "<p style='margin-left: 40px'>" + line[2:] + "</p>"
		elif line[0] == "#":
			if line[1] == "#":
				if line[2] == "#":
					output.content += "<h3>" + line[2:] + "</h3>"
				else:
					output.content += "<h2>" + line[2:] + "</h2>"
			else:
				output.content += "<h1>" + line[2:] + "</h1>"
		elif line[0] == "\n":
			output.content += ""
		else:
			output.content += "<p>" + line + "</p>"
	
	return output
