import os
from flask import Flask, redirect, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename, send_from_directory

app = Flask(__name__)
# app.config['IMAGE_UPLOADS'] = os.path.dirname(os.path.realpath(__file__)) + '/uploads' 

@app.route("/", methods = ['GET'])
def index():
	return render_template('index_main.html')


@app.route("/upload", methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':
		img = request.files['file']
		
		img_ext = img.filename.rsplit('.', 1)[1].lower()
		if img_ext == 'pdf':
			print("Can't upload PDF")
			return render_template('index_main.html')

		filename = secure_filename(img.filename)
		base_Dir = os.path.abspath(os.path.dirname(__file__)) + '/uploads'
		img.save(os.path.join(base_Dir, filename))
		return render_template('index_main.html', filename=filename)

	return render_template('index_main.html')


@app.route("/visualize/<filename>")
def visualize(filename):
	base_Dir = os.path.abspath(os.path.dirname(__file__)) + '/uploads'
	environ = request.environ
	return send_from_directory(base_Dir, filename, environ)
	# return redirect(url_for('upload', filename = base_Dir + filename), code=301)


if __name__ == '__main__':
	app.run(debug=False)
