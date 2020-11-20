# encoding: utf-8

from flask import Flask, render_template
from gsheets import Sheets
from csv import reader

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app = Flask(__name__)

sheets = Sheets.from_files('credentials.json', 'storage.json')
url = "https://docs.google.com/spreadsheets/d/1glsAF033cPecjG_TH76uhLktSrpUWUHJymdSrWRNoQM/edit#gid=0"
filename = 'projects.csv'
projects_filename = 'projects_images.csv'
videos_filename = 'project_videos.csv'

class Project:
	def __init__(self, name, img_src, overlay_desc, main_desc, authors, github, paper, youtube, problem, results, future, role, video, category):
		self.name = name
		self.img_src = img_src
		self.overlay_desc = overlay_desc
		self.main_desc = main_desc
		self.authors = authors
		self.github = github
		self.paper = paper 
		self.youtube = youtube 
		self.problem = problem
		self.results = results
		self.future = future
		self.role = role 
		self.video = video 
		self.category = category

		#Images of each project
		self.images = None  
		self.images_len = 0 

		#Videos of each project
		self.videos = None
		self.videos_len = 0

 
global categories
global tags
global projects_dict 

categories = ["All"]
tags = {"All": "*"}
projects_dict = {}


#Code that fetches portfolio projects from excel document
def init_projects():
	global categories
	global tags

	cat = set()

	s = sheets.get(url)
	s.sheets[0].to_csv(filename, encoding='utf-8', dialect='excel')
	s.sheets[1].to_csv(projects_filename, encoding='utf-8', dialect='excel')
	s.sheets[2].to_csv(videos_filename, encoding='utf-8', dialect='excel')

	projects = []

	with open(filename, 'r') as read_obj:


		csv_reader = reader(read_obj)
		for row in csv_reader:
			# Skip if its the first row
			if(row[0] == "Project Name"):
				continue

			# Row is not well-formed, skip
			if(len(row) < 13):
				continue

			category = row[13:]
			meta_tag = []
			# print(row)
			for c in category:
				if(c not in tags):
					tags[c] = c.lower().replace(" ", "_").replace("/","_")
				meta_tag += [tags[c]]
				cat.add(c)

			problem_text = row[8]
			if(problem_text):
			    problem_paragraphs = problem_text.split('\n')
			else: 
				problem_paragraphs = []
				

			main_desc_text = row[3]
			if(main_desc_text):
			    main_desc_paragraphs = main_desc_text.split('\n')
			else: 
				main_desc_paragraphs = []

			result_text = row[9]
			if(result_text):
			    result_paragraphs = result_text.split('\n')
			else: 
				result_paragraphs = []

			role_text= row[11]
			if(role_text):
			    role_paragraphs = role_text.split('\n')
			else: 
				role_paragraphs = []

			future_text= row[10]
			if(future_text):
			    future_paragraphs = future_text.split('\n')
			else: 
				future_paragraphs = []


			for i in range(len(main_desc_paragraphs)):
				main_desc_paragraphs[i] = main_desc_paragraphs[i].strip()
				# print(result_paragraphs[i])

			for i in range(len(result_paragraphs)):
				result_paragraphs[i] = result_paragraphs[i].strip()
				
			p = Project(row[0], row[1], row[2], main_desc_paragraphs, row[4], row[5],
			row[6], row[7], problem_paragraphs, result_paragraphs, future_paragraphs, role_paragraphs, row[12], " ".join(meta_tag))

			projects_dict[p.name] = p
			projects += [p]

	with open(projects_filename, 'r') as read_obj:
		csv_reader = reader(read_obj)
		for row in csv_reader:
			if(row[0] == "Project Name"):
				continue
			if(row[0] in projects_dict):
				projects_dict[row[0]].images = row[1:]

	with open(videos_filename, 'r') as read_obj:
		csv_reader = reader(read_obj)
		for row in csv_reader:
			if(row[0] == "Project Name"):
				continue

			if(row[0] in projects_dict):
				projects_dict[row[0]].videos = row[1:]
	



	categories = ["All"] + list(cat)
	return projects

@app.route('/portfolio/<project_title>')
def show_project(project_title):
	# p = project_title.lower().replace(" ", "_") + '.html'
	print(projects_dict[project_title].results)
	return render_template("project_template.html", project=projects_dict[project_title])



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
	# app.jinja_env.filters['split_space'] = split_space
    app.run(debug=True)