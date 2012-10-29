import bottle


@bottle.route("/")
def home_page():
    return bottle.template("hello_world",
        username="German", things=xrange(20))


@bottle.route('/testpage')
def test_page():
    return "This is a test page"

bottle.debug(True)
bottle.run(host='localhost', port=8080)
