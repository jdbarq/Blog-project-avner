from app import app, db  # import our Flask app
import os
import sys
import views
import models
from entries.blueprint import entries
app.register_blueprint(entries, url_prefix='/entries')

#runs the application 

app.run(
    
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    
    )
    





if __name__ == '__main__':
    app.run()
    


