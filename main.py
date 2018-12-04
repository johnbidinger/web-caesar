from flask import Flask, request 
from caesar import rotate_string
app = Flask(__name__)

app.config['DEBUG'] = True

# page_header = """
# <!DOCTYPE html>
# <html>
#     <head>
#         <title>FlickList</title>
#     </head>
#     <body>
#         <h1>FlickList</h1>
# """

# page_footer = """
#     </body>
# </html>
# """
form = """
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <!-- Create your form here -->

        <form method="POST" >
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0"><br>
            
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit form">
        </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot_value = request.form['rot']
    text_value = request.form['text']
    encrypted = rotate_string(text_value, int(rot_value))
    # new_text = "<h1>" + encrypted + "</h1>"
    return form.format(encrypted)

app.run()

