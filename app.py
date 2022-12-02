# 1. Import Flask
from flask import Flask

# 2. Create an app
app = Flask(__name__)

# 3. Define index route
@app.route('/')
def index():
    return 'Hello world'
# 4. Define the about route
@app.route('about')
def index():
    name = 'Patrick'
    loc = 'New Jersey'

# 5. Define the contact route
@app.route('contact')
def index():
    email = 'ngorahhanzian@gmail.com'

# 6. Define main behavior
if __name__ == '__main_':
        app.run(debug=True)