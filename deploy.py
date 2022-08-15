from about.about import create_about_me_page
from essays.essays import create_essays_page
from home import create_home_page
from page import create_page
from home import create_home_page
from about.about import create_about_me_page
from projects.projects import create_projects_page

###
# Name: deploy.py
# Author(s): Leeden Raquel
# Description: used by github actions to recreate all static html pages in the website
#  whenever a commit is made
###

create_page("index.html", create_home_page(), ["home.css", "projects/projects.css", "essays/essays.css"])
create_page("projects/index.html", create_projects_page("projects/"), ["projects.css"])
create_page("essays/index.html", create_essays_page("essays/"), ["essays.css"])
create_page("about/index.html", create_about_me_page(), ["about.css"])