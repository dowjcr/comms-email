# DOWNING COLLEGE JCR COMMS EMAIL GENERATOR
# Cameron O'Connor (2018)
# --------------------------------------
# === SUMMARY ===
# Takes data passed in correct format and generates an HTML email.
# Output saved in "out.html" in same subdirectory.
# The intention was for this to be self-contained - hence the liberal
# use of HTML and CSS snippets below. Please don't judge me.
# --------------------------------------
# === HOW TO USE ===
# Please place all news items in a file named "items.txt" in this directory.
# The introduction should be placed in a file named "intro.txt", also in
# this directory. You may also paste a URL to the 'meme of the week',
# with the caption on a new line, in meme.txt".
# --------------------------------------

import datetime
now = datetime.datetime.now()

CSS = """
<style>
  @import url(https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic);
  body{
    padding:0px;
  }
  #container{
    width:auto;
    display:block;
    margin:auto;
    padding:0;
    padding-top:0px;
    padding-bottom: 20px;
    margin-top:0px;
    margin-bottom: 20px;
    box-shadow: 0px 0px 30px 0px rgba(0,0,0,0.75);
    background-color:white;
  }
  #header{
    height:170px;
    display:block;
    width:auto;
    background-color:#7F0056
  }
  #header .img{
    margin:0;
    padding:0;
    z-index:1;
  }

  #picture-frame{
    display:block;
    padding:10px;
    text-align:center;
  }

  #picture-frame img {
    border:10px solid white;
    box-shadow: 0px 0px 30px 0px rgba(0,0,0,0.75);
    width: auto;
  }

  p {
    margin:50px;
    margin-top:0px;
    margin-bottom:10px;
    font-family: Lato;
    background-color:white
  }
  hr {
    border-style: solid;
    border-color: #aaa;
    margin-left: 50px;
    margin-right: 50px;
    margin-top:20px;
    width:auto;
  }

  h1 {
    color: purple;
    font-weight:bold;
    font-family: Lato;
    margin-bottom:10px;
  }
  h2 {
    color: purple;
    padding-left:50px;
    font-weight:bold;
    font-family: Lato;
    margin-bottom:10px;
  }
  h3{
    font-weight: bold;
    font-family: Lato;
    color: purple;
    padding-top:50px;
    padding-left:50px;
  }
  h4{
    font-weight: bold;
    font-family: Lato;
    padding-left:50px;
    margin-bottom: 5px;
  }
</style>"""
preamble = """
<table
  border="0px" cellpadding="20px" cellspacing="0" width="100%">
  <tbody>
    <tr>
      <td>
        <div id="container">"""
afterword = """
        </div>
      </td>
    </tr>
  </tbody>
</table>"""
header = """
<div id="header" align="center" style="background-color:#7F0056">
<img src="https://www.jcr.dow.cam.ac.uk/storage/app/media/dowjcrwhite.png" alt="Downing JCR" width="70" height="80" 
    style="Margin-top: 20px"/>%s</div>
"""
meme = """

  <h2>Meme of the Week</h2>
  <div id="picture-frame" style="display: block;padding: 10px;text-align: center;" align="center"> 
    <img alt="Meme of the week" width=400; height=400; 
      src="%s"
      style="border: 10px solid white; box-shadow: 0px 0px 30px
      0px rgba(0, 0, 0, 0.75);"> 
  </div>
  <p style="text-align:center"> <br><i>%s</i></p>
"""

# Data stored in items.txt in same directory.
file = open("items.txt", "r")
lines = file.readlines()
file.close()

# Splits into sections
titles = []
bodies = [""]
count = 0
title = True
for l in lines:
    l = l.replace("\n", " ")
    l = l.replace("\r", "")
    if l == "===== ":
        count += 1
        title = True
    elif title:
        titles.append(l)
        title = False
        bodies.append("")
    else:
        bodies[count] += l

# Generates header & introduction section.
introfile = open("intro.txt", "r")
intro = introfile.read()
out = open("out.html", "w")
out.write(CSS)
out.write(preamble)
date = now.strftime("%d/%m/%Y")
out.write(header % """<h1 style="color:white; margin-top: 10px">JCR Comms %s</h1>""" % date)
out.write("<br><br><p>" + intro + "<br><br></p>")

# Generates the "meme of the week" section.
memefile = open("meme.txt", "r")
memedata = memefile.readlines()
for i in range(0, len(memedata)):
    memedata[i] = memedata[i].replace("\n", "")
    memedata[i] = memedata[i].replace("\r", "")
out.write(meme % (memedata[0], memedata[1]))

# Generates the "in this week's email" section.
out.write("<h2>In this week's email...</h2>")
for i in range(0, len(titles)):
    out.write("""<p> <a href="#anchor%s">%s. %s</a>""" % ((i+1), (i+1), titles[i]))

# Generates the main text sections.
for i in range(0, len(titles)):
    out.write("""<div id="anchor%s"><p style="padding-left:50px">""" % (i+1))
    out.write("<h3>" + str(i+1) + ". " + titles[i] + "</h3>")
    out.write("<p>" + bodies[i] + "</p>")
    out.write("</p></div>")

# Finishes up.
out.write(afterword)
out.close()
