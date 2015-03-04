# flask-usul
My flask base of the pillar to build on
Inspired from Rails and cookiecutter-flask (https://github.com/sloria/cookiecutter-flask) (weird I know)

# Tree
## app/blueprints
- one blueprint per subfolder
- auth with flask-login and flask-admin already configured
## app/configuration
### extensions
- __init__.py :  standalone extension object declaration
- each file should contain an initSOMETHING(app) function to be called when app will be created
### various config files
- config : available in app.config
- constants : standalone config info, enum declarations, etc

## app/models
- one file per model

## app/templates
- do as you wish

## app/translations
- for babel
