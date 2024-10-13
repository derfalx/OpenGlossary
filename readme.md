# Open Glossary
A simple open source glossary system generated from markdown files - but not a static site.

**Why not static?** 
Good question. While this could be a simple static site generator for glossaries, it is planned to provide a proper search
functionality. While it could be possible to implement this in a static-site-way, it is planned to be implemented in a 
dynamic application way by now.

## Features
 - [x] Minimal Viable Product (MVP) glossary entries
 - [x] MVP menu structuring
 - [x] MVP additional pages
 - [x] MVP docker based deployment
 - [x] MVP markdown to sqlite3 parsing functionality
 - [ ] CLI to parse Markdown to sqlite3
 - [ ] Additional properties per glossary entry
 - [ ] Search functionality
 - [ ] Proper documentation


## Configuration
```json
{
  "title": "App-Title",
  "icon": { # Controls the title icon on the top left of the page
    # By now only the type 'text' is supported. The Icon on the top left will be simply the text provided in the
    # 'text' property
    "type": "text",
    "text": "App"
  },
  "menu": { # Controls additional elements in the main menu
    # Each key represents the name of a menu entry. The according value describes the referenced page.
    # If it is a string starting with underscore ('_') a page from the database will be referenced.
    # Else it will be interpreted as URL and simply put into an <a> tag    
    "About": "_about",
    "Links": "_links"
  },
  # URL of the database to use with sqlalchemy
  "SQLALCHEMY_DATABASE_URI": "sqlite:////app/glossary.db"
}
```