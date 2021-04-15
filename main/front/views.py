from flask import render_template
from ..front import front

@front.route('/', methods=['GET'])
def index():
    """Returns the applications index pages."""
    return render_template('index.html')

@front.route('/marketing', methods=['GET'])
def marketing():
    """Returns the applications index pages."""
    return render_template('marketing.html')

@front.route('/development', methods=['GET'])
def development():
    """Returns the applications index pages."""
    return render_template('development.html')

@front.route('/automation', methods=['GET'])
def analytics():
    """Returns the applications index pages."""
    return render_template('automation.html')




