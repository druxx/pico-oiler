from microdot_asyncio import Microdot, send_file

app = Microdot()


@app.route('/')
async def index(req):
    return send_file('html/index.html')

@app.route('/<path:path>')
async def static(request, path):
    print(path)
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    if path.endswith('.html') or path.endswith('.js') or path.endswith('.png') or path == 'favicon.ico':
        return send_file('html/' + path)
    else:
        return 'Not found', 404

if __name__ == '__main__':
    app.run()