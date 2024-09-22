# Open Glossary
A simple open source glossary system generated from markdown files - but not a static site.

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