from flask import Blueprint
app=Blueprint("general",__name__)

@app.route('/')
def main():
    return 'hello word'

@app.route('/about')
def about():
    return 'about us'