# flask-usul
My flask base of the pillar to build on
Inspired from Rails and cookiecutter-flask (https://github.com/sloria/cookiecutter-flask) (weird I know)

# Workflow
## To change
- change init_db.py
- change app/configuration/config.py

## Blueprints
- Add your blueprint in app/blueprints/blueprint_name (see bellow for details)
- import it in app/__init__.py, in the function configure_blueprints()

## Extenions
- in app/configuration/extensions
- add the standalone extension  object in __init__.py
```python
db = SQLAlchemy()
```
- if needed, add a file with a function importNAME-OF-EXTENSION()
- call this function in app/__init__.py, function configure_extensions(app):
```python
from app.configuration.extensions.database import initDb
initDb(app)
```

# Tree
## app/blueprints
- one blueprint per subfolder
- provided : flask-login, flask-admin

### app/blueprints/blueprint_name
- __init__.py -> create the blueprint (cf app/blueprints/home for translations):
```python
mod = Blueprint('home', __name__, url_prefix="/<lang_code>")
```
- views.py -> views

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
