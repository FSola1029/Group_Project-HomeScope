from flask import Flask
app = Flask(__name__, static_url_path='/')

app.secret_key = "Beefcake Cartman"
app.config['CLOUDINARY_CLOUD_NAME'] = "dggzaweqo"
app.config['CLOUDINARY_API_KEY'] = "679358338584312"
app.config['CLOUDINARY_API_SECRET'] = "F-RCHPq88AX3DXYo3V6cSGjqhOQ"
