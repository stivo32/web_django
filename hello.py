def app(environ, start_response):
	data = list()
	for pair in environ['QUERY_STRING'].split('&'):
		print(pair)
		data.append(bytes(pair+'\n', 'utf-8'))
	start_response("200 OK", [("Content-Type", "text/plain")])
	return iter(data)
