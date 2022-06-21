from flask import Flask

app = Flask(__name__)

app.secret_key = "making secrets"           # Needs to be added for session; secret_key can be set to anything in the string

# Set database to the name of the schema in MySQL Workbench
database = "lecture_recipes_schema"