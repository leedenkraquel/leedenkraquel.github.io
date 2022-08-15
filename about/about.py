import json

###
# Name: about.py
# Auhtor(s): Leeden Raquel
# Description: generates a string that represents the html for the about me page. The about me page
#  should show a resume about me, skills, experience, and awards
###

def create_about_me_page ():
    about_page = '''
        <img class="profile_picture" src="../images/profile-picture.jpg" alt="headshot" />
        <h1>About</h1>
        <p class="about_body">My name is Leeden. I am a student at the University of Hawaii at Manoa. I currently study Computer Science with a focus on Data Science and will be earning my B.S. in the upcoming Fall 2022 term. I have a passion for development in machine learning, application development, and software engineering. In my free time I enjoy playing tabletop games, cooking, and coding up fun projects.</p>
        <div class="hr"></div>
        <h2>Experience</h2>
    '''
    about_page += get_experience("about/experience.json")

    about_page += '''<div class="hr"></div>
        <h2>Skills</h2>
    '''
    about_page += get_skills("about/skills.json")

    about_page += '''<div class="hr"></div>
        <h2>Education</h2>
    '''
    about_page += get_education("about/education.json")

    about_page += '''<div class="hr"></div>
        <h2>Volunteering</h2>
    '''
    about_page += get_volunteer("about/volunteer.json")

    about_page += '''<div class="hr"></div>
        <h2>Awards</h2>
    '''
    about_page += get_awards("about/awards.json")

    return about_page

def get_experience (directory):
    experience_file = open(directory, "r")
    experience_json = json.load(experience_file)
    experience_output = '<div class="experience section">'
    
    for experience in experience_json.get("experience"):
        experience_output += '<h3 class="title">' + experience.get("position") + ', ' + experience.get("company") + '</h3>'
        experience_output += '<p class="date">' + experience.get("startDate") + ' - ' + experience.get("endDate") + '</p>'
        experience_output += '<a class="website" href="' + experience.get("website") + '">' + experience.get("website") + '</a>'
        if len(experience.get("highlights")) > 0:
            experience_output += '<ul class="highlights">'
            experience_output += '<li>' + '</li><li>'.join(experience.get("highlights")) + '</li>'
            experience_output += '</ul>'

    experience_output += '</div>'
    return experience_output

def get_skills (directory):
    skills_file = open(directory, "r")
    skills_json = json.load(skills_file)
    skills_output = '<div class="skills section">'
    
    for skill in skills_json.get("skills"):
        skills_output += '<h3 class="title">' + skill.get("name") + '</h3>'
        skills_output += '<p class="summary">' + skill.get("summary") + '</p>'
        if len(skill.get("keywords")) > 0:
            skills_output += '<ul class="highlights">'
            skills_output += '<li>' + '</li><li>'.join(skill.get("keywords")) + '</li>'
            skills_output += '</ul>'

    skills_output += '</div>'
    return skills_output

def get_education (directory):
    edu_file = open(directory, "r")
    edu_json = json.load(edu_file)
    edu_output = '<div class="education section">'
    
    for education in edu_json.get("education"):
        edu_output += '<h3 class="title">' + education.get("institution") + '</h3>'
        edu_output += '<p class="date">' + education.get("startDate") + ' - ' + education.get("endDate") + '</p>'
        edu_output += '<p class="summary">' + education.get("studyType") + ', ' + education.get("area") + '</p>'
        if len(education.get("courses")) > 0:
            edu_output += '<ul class="highlights">'
            edu_output += '<li>' + '</li><li>'.join(education.get("courses")) + '</li>'
            edu_output += '</ul>'

    edu_output += '</div>'
    return edu_output

def get_volunteer (directory): 
    vol_file = open(directory, "r")
    vol_json = json.load(vol_file)
    vol_output = '<div class="volunteering section">'
    
    for volunteer in vol_json.get("volunteer"):
        vol_output += '<h3 class="title">' + volunteer.get("organization") + ': ' + volunteer.get("position") + '</h3>'
        vol_output += '<p class="date">' + volunteer.get("date") + '</p>'
        vol_output += '<a class="website" href="' + volunteer.get("website") + '">' + volunteer.get("website") + '</a>'
        vol_output += '<p class="summary">' + volunteer.get("summary") + '</p>'
        if len(volunteer.get("highlights")) > 0:
            vol_output += '<ul class="highlights">'
            vol_output += '<li>' + '</li><li>'.join(volunteer.get("highlights")) + '</li>'
            vol_output += '</ul>'

    vol_output += '</div>'
    return vol_output

def get_awards (directory): 
    award_file = open(directory, "r")
    award_json = json.load(award_file)
    award_output = '<div class="awards section">'
    
    for award in award_json.get("awards"):
        award_output += '<h3 class="title">' + award.get("awarder") + ': ' + award.get("title") + '</h3>'
        award_output += '<p class="date">' + award.get("date") + '</p>'
        award_output += '<a class="website" href="' + award.get("website") + '">' + award.get("website") + '</a>'
        award_output += '<p class="summary">' + award.get("summary") + '</p>'

    award_output += '</div>'
    return award_output