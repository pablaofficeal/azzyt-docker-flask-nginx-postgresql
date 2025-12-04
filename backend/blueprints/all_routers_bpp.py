from routers.home.main_home_bpp import home_bpp

def register_all_routers_bpp(app):
    app.register_blueprint(home_bpp)