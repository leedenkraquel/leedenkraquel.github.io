from os import listdir
from parse_md import parse_md
from page import create_page

###
# Name: projects.py
# Author(s): Leeden Raquel
# Description: generates a string that represents the html for the projects page.
###

def create_projects_page (directory):
    project_page = '<div class="project_page">'
    project_files = listdir("projects/")
    project_page += ''.join(create_project_cards(directory, project_files))
    project_page += "</div>"
    return project_page

def create_project_cards (directory, project_files):
    project_cards = []
    href = "projects/"
    if "projects/" in directory:
        href = ""
    for project in project_files:
        if ".md" in project:
            project_obj = parse_md("projects/" + project)
            project_card = '<a class="project_link" href="' + href + project[:-3] + '.html"><div class="project_card">'
            project_card += '<p class="title">' + project_obj.get_title() + '</p>'
            project_card += '<p class="date">' + project_obj.get_date() + '</p>'
            project_card += '<img class="cover_image" src="' + '../' * directory.count("/") + project_obj.get_image() + '" />'
            project_card += '<div class="project_card_overlay"><p class="summary">' + project_obj.get_summary() + '</p>'
            project_card += '<p class="label">' + '</p><p class="label">'.join(project_obj.get_labels()) + '</p>'
            project_card += '</div></div></a>'
            project_cards.append((project_obj.get_date(), project_card))
            create_about_project_page('projects/' + project[:-3] + ".html", project_obj)
    
    project_cards = sorted(project_cards, reverse = True)
    return list(list(zip(*project_cards))[1])

def create_about_project_page (directory, project_obj):
    about_project_body = '<h1>' + project_obj.get_title() + '</h1>'
    about_project_body += project_obj.to_html()
    create_page(directory, about_project_body, ["about-project.css"])