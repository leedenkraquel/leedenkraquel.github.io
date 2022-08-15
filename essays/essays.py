from os import listdir
from parse_md import parse_md
from page import create_page

###
# Name: essays.py
# Author(s): Leeden Raquel
# Description: generates a string that represents the html for the essays page.
###

def create_essays_page (directory):
    essay_page = '<div class="essay_page">'
    essay_files = listdir("essays/")
    essay_page += ''.join(create_essay_cards(directory, essay_files))
    essay_page += "</div>"
    return essay_page

def create_essay_cards (directory, essay_files):
    essay_cards = []
    href = "essays/"
    if "essays/" in directory:
        href = ""
    for essay in essay_files:
        if ".md" in essay:
            essay_obj = parse_md("essays/" + essay)
            essay_card = '<a class="essay_link" href="' + href + essay[:-3] + '.html"><div class="essay_card">'
            essay_card += '<p class="title">' + essay_obj.get_title() + '</p>'
            essay_card += '<p class="date">' + essay_obj.get_date() + '</p>'
            essay_card += '<p class="summary">' + essay_obj.get_summary() + '</p>'
            essay_card += '<div class="labels_section"><p class="label">' + '</p><p class="label">'.join(essay_obj.get_labels()) + '</p>'
            essay_card += '</div></div></a>'
            essay_cards.append((essay_obj.get_date(), essay_card))
            create_about_essay_page('essays/' + essay[:-3] + ".html", essay_obj)
    
    essay_cards = sorted(essay_cards, reverse = True)
    return list(list(zip(*essay_cards))[1])

def create_about_essay_page (directory, essay_obj):
    about_essay_body = essay_obj.to_html()
    create_page(directory, about_essay_body, ["about-essay.css"])