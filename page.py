###
# Name: page.py
# Auhtor(s): Leeden Raquel
# Description: every page in the site is created by this script. It 
#  adds the navbar and the footer to each page
###

subdirectory = ""

def write_header (page, stylesheets):
    page.write('''
        <head>
            <title>Leeden R | Portfolio</title>
            <link rel="stylesheet" href="''' + subdirectory + '''styles.css" />''')

    for stylesheet in stylesheets:
        page.write('<link rel="stylesheet" href="' + stylesheet + '" />')

    page.write('''
            <link rel="icon" type="image/x-icon" href="''' + subdirectory + '''images/favicon.png" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        </head>
    ''')
    return page

def write_navbar (page):
    page.write('''
        <div class="navbar">
            <a class="menu_obj" href="#"><img class="inverted menu_button" src="''' + subdirectory + '''images/menu.png" alt="menu button" /></a>
            <a class="navbar_obj" href="/">Home</a>
            <a class="navbar_obj" href="/projects/">Projects</a>
            <a class="navbar_obj" href="/essays/">Essays</a>
            <a class="navbar_obj" href="/about/">About Me</a>
        </div>
    ''')
    return page

def write_body (page, body):
    page.write('<div class="site_body">')
    page.write(body)
    page.write('</div>')
    return page

def write_footer (page):
    page.write('''
        <div class="footer">
            <div class="footer_col">
                <a class="sitemap_obj" href="/">Home</a>
                <a class="sitemap_obj" href="/projects/">Projects</a>
                <a class="sitemap_obj" href="/essays/">Essays</a>
                <a class="sitemap_obj" href="/about/">About Me</a>
            </div>
            <div class="footer_col">
                <a href="https://github.com/leedenkraquel"><img class="inverted footer_icon" src="''' + subdirectory + '''images/github.png" alt="github logo" /></a>
                <a href="https://www.linkedin.com/in/leeden-raquel-398309183/"><img class="inverted footer_icon" src="''' + subdirectory + '''images/linkedin.png" alt="linkedin logo" /></a>
            </div>
            <div class="footer_col">
                <p>Quote</p>
            </div>
        </div>
    ''')
    return page

def create_page (directory, body, stylesheets = []):
    global subdirectory
    subdirectory = "../" * directory.count("/")
    page_html = open(directory, "w")
    page_html.write('<!-- THIS FILE IS PROGRAMATICALLY GENERATED, CHANGES TO THIS .html FILE WILL NOT SAVE-->')
    page_html = write_header(page_html, stylesheets)
    page_html.write('<body><div class="background_image">')
    page_html = write_navbar(page_html)
    page_html = write_body(page_html, body)
    page_html = write_footer(page_html)
    page_html.write('</div></body>')