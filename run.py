from Book_Flask import create_app

app = create_app()


if __name__ == '__main__':
	app.run(debug = True)