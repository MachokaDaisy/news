from flask import render_template
from . import main

@main.app_errorhandler(404)
def forohfor(error):
    '''
    function to render the 404 error page
    '''
    return render_template('forohfor.html'),404