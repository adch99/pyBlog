# Blog #
--------
This projects seeks to implement a blog using
Python with web.py for backend. Markdown support
is provided for formatting the content as this
project does not use JS, JQuery or any other such
frontend mechanisms. SQL too is not used.

## Functionality ##
The following functions are offered:
* Adding an article of text
* Removing an article
* Editing an article **(to be added later)**

## Content Type ##
The content can currently include only text with a title.
Functionality for posting pictures will be added later.

## Storage ##
Options for storing posts:
* Save as plain ASCII text file
* Save as Pickled Python object

## Security ##
To prevent against SQL-injection style attacks, Markdown
is used to treat the post content.
