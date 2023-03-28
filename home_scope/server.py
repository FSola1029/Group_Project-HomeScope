from flask_app import app
from flask_app.controllers import homes, users
from flask_app.models import home, user

if __name__=="__main__":
    app.run(debug=True,port=5001)
