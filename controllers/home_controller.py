

def route(app):

    @app.route("/contact")
    def contact():
        return "Contact Us via Email: ryan@email.com or by Phone: (555) 555-5555"
