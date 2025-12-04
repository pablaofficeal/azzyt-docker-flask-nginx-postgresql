from flask import Flask


app.register_blueprint(bp)
app.register_blueprint(routes.bp)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")