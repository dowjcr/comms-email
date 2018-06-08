# Downing College JCR Comms Email Generator

## Introduction 
This system is Cameron O'Connor, 2018. It comprises a 'quick and dirty' Python script, which takes data from text files, and produces an
HTML comms email.

## Howto - Files
Data should be placed in text files in the same directory as the script.

### `items.txt`
This file will contain any news items to include in the email. For each section, the first line is the title, and any subsequent lines
make up the body text. Sections should be separated by five equals signs, `=====` . Below is an example of this format:

```
This is a title
This is some body text. The body
text can continue onto multiple lines
like this.
=====
This is another title
And some more body text! This text can be
made <b>bold</b> by using HTML tags, and
a new line can be inserted by using the <br>
tag.
=====
Yet another title
blah...
```

### `intro.txt`
This file will contain the text to include in the introduction section. As before, HTML tags such as `<b>...</b>` and `<br>` may
be inserted here. Below is an example of this format:

```
Hello and welcome to this week's comms!<br>
This is a comms email.
```

### `meme.txt`
The first line of this file should be an absolute link to the meme image. The second line should be the caption of the meme.
Below is an example of this format:

```
https://www.jcr.dow.cam.ac.uk/media/images/...
This is the meme caption.
```

## Howto - Run Script
Open a console window in the same directory as the script. Then run:

```Bash
python emailgen.py
```

A file called `out.html` is created in the same directory.
