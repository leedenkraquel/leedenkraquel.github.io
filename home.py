from os import listdir
from parse_md import parse_md
from projects.projects import create_project_cards
from essays.essays import create_essay_cards

###
# Name: page.py
# Auhtor(s): Leeden Raquel
# Description: generates a string that represents the html for the home page. The home page should
#  display a header with my name followed by a preview of my projects and essays
###

def create_home_page ():
    project_files = listdir("projects/")
    essay_files = listdir("essays/")

    home_page = '''
        <div>
            <h1 class="centered about_header">Leeden Raquel</h1>
            <p class="centered about_body">Software Developer</p>
        </div>
        <div class="hr"></div>
        <h2>Projects</h2>
        <div class="project_section">
    '''
    
    home_page += ''.join(create_project_cards("", project_files)[:3])

    home_page += '''
        </div>
        <a class="see_more" href="projects/">See more...</a>
        <div class="hr"></div>
        <h2>Essays</h2>
        <div class="essay_section">
    '''

    home_page += ''.join(create_essay_cards("", essay_files)[:3])

    home_page += '''</div>
        <a class="see_more" href="essays/">See more...</a>
        <div class="hr"></div>
    '''
    return home_page