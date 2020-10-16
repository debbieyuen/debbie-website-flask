from flask import Flask, render_template
from gsheets import Sheets
from csv import reader

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app = Flask(__name__)

sheets = Sheets.from_files('credentials.json', 'storage.json')
url = "INSERT URL HERE"
filename = 'projects.csv'

class Project:
	def __init__(self, name, img_src, desc, category):
		self.name = name
		self.img_src = img_src
		self.desc = desc
		self.category = category
 
global categories
global tags

categories = ["All"]
tags = {"All": "*"}



def init_projects():
	global categories
	global tags

	s = sheets.get(url)
	s.sheets[0].to_csv(filename, encoding='utf-8', dialect='excel')
	projects = []

	with open(filename, 'r') as read_obj:


		csv_reader = reader(read_obj)
		for row in csv_reader:
			# Skip if its the first row
			if(row[0] == "Project Name"):
				continue

			# Row is not well-formed, skip
			if(len(row) < 4):
				continue

			category = row[3]

			if(category not in tags):
				tags[category] = category.lower().replace(" ", "_").replace("/","_")

				categories += [category]

			p = Project(row[0], row[1], row[2], category)
			projects += [p]

	return projects




@app.route("/portfolio")
def projects():
    debbie_projects = init_projects()
    return render_template('projects.html', proj_len=len(debbie_projects), debbie_projects=debbie_projects, categories=categories, tags=tags, cat_len=len(categories))

@app.route("/research")
def research():
    return render_template('research.html')

@app.route("/home")
@app.route('/')
def index():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)