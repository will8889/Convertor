from  flask import Flask, redirect, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from os.path import join,isfile
from os import remove,listdir,stat
import time
import git

from conversion_methods import video_conversion as vc
from conversion_methods import audio_conversion as ac
from conversion_methods import image_conversion as ic
from conversion_methods import file_conversion as fc

UPLOAD_FOLDER = "/home/convertorapp/Convertor/uploads"
OUTPUT_FOLDER = "/home/convertorapp/Convertor/output"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER
SUPPORTED_VIDEO_EXTENSIONS = {'mp4', 'mkv', 'mov', 'avi', 'wmv', 'flv'}
SUPPORTED_AUDIO_EXTENSIONS = {'mp3', 'wav', 'ogg', 'flac', 'mp4'}
SUPPORTED_IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'tiff', 'png', 'bmp', 'eps'}
SUPPORTED_DOCUMENT_EXTENSIONS = {'docx', 'pdf'}

def video_is_supported(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in SUPPORTED_VIDEO_EXTENSIONS

def audio_is_supported(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in SUPPORTED_AUDIO_EXTENSIONS

def image_is_supported(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in SUPPORTED_IMAGE_EXTENSIONS

def document_is_supported(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in SUPPORTED_DOCUMENT_EXTENSIONS

@app.route("/")
@app.route("/video", methods=["GET", "POST"])
def video_upload():
    if request.method == "POST":
        file = request.files['file']
        if 'file' not in request.files:
            print('No file')
            return redirect(request.url)
        if file.filename == '':
            print('No filename')
            return redirect(request.url)
        if not (file and video_is_supported(file.filename)):
            print('Invalid video extension')
            return redirect(request.url)

        target_format = str(request.form.get("format"))
        if target_format == 'Output format':
            print('No target')
            return redirect(request.url)

        else:
            print('Video converted')
            filename = secure_filename(file.filename)
            file.save(join(app.config['UPLOAD_FOLDER'], filename))

            convertor = vc.VideoConvertor(app.config['UPLOAD_FOLDER'], app.config["OUTPUT_FOLDER"])

            converted_filename = convertor.convert(filename, target=target_format)
            converted = True
            return render_template("index.html", converted=converted, converted_filename=converted_filename)
    return render_template("index.html")

@app.route("/audio", methods=["GET", "POST"])
def audio_upload():
    if request.method == "POST":
        file = request.files['file']
        if 'file' not in request.files:
            print('No file')
            return redirect(request.url)
        if file.filename == '':
            print('No filename')
            return redirect(request.url)
        if not (file and audio_is_supported(file.filename)):
            print('Invalid audio extension')
            return redirect(request.url)

        target_format = str(request.form.get("format"))
        if target_format == 'Output format':
            print('No target')
            return redirect(request.url)
        else:
            print('Audio converted')
            filename = secure_filename(file.filename)
            file.save(join(app.config['UPLOAD_FOLDER'], filename))

            convertor = ac.AudioConvertor(app.config['UPLOAD_FOLDER'], app.config["OUTPUT_FOLDER"])
            converted_filename = convertor.convert(filename, target=target_format, bitrate="high")
            converted = True
            return render_template("audio.html", converted=converted, converted_filename=converted_filename)
    return render_template("audio.html")

@app.route("/image", methods=["GET", "POST"])
def image_upload():
    if request.method == "POST":
        file = request.files['file']
        if 'file' not in request.files:
            print('No file')
            return redirect(request.url)
        if file.filename == '':
            print('No filename')
            return redirect(request.url)
        if not (file and image_is_supported(file.filename)):
            print('Invalid image extension')
            return redirect(request.url)

        target_format = str(request.form.get("format"))
        if target_format == 'Output format':
            print('No target')
            return redirect(request.url)
        else:
            print('Image converted')
            filename = secure_filename(file.filename)
            file.save(join(app.config['UPLOAD_FOLDER'], filename))
            convertor = ic.ImageConvertor(app.config['UPLOAD_FOLDER'], app.config["OUTPUT_FOLDER"])
            converted_filename = convertor.convert(filename,target = target_format)
            converted = True
            return render_template("image.html", converted=converted, converted_filename=converted_filename)
    return render_template("image.html")

@app.route("/document", methods=["GET", "POST"])
def document_upload():
    if request.method == "POST":
        file = request.files['file']
        if 'file' not in request.files:
            print('No file')
            return redirect(request.url)
        if file.filename == '':
            print('No filename')
            return redirect(request.url)
        if not (file and document_is_supported(file.filename)):
            print('Invalid document extension')
            return redirect(request.url)
        else:
            print('Document converted')
            filename = secure_filename(file.filename)
            file.save(join(app.config['UPLOAD_FOLDER'], filename))

            convertor = fc.convert(app.config['UPLOAD_FOLDER'], app.config["OUTPUT_FOLDER"],filename)
            converted_filename = convertor
            converted = True
            return render_template("document.html", converted=converted, converted_filename=converted_filename)
    return render_template("document.html")



@app.route('/download/<filename>')
def download_file(filename):
    now = time.time()

    for i in listdir(app.config['OUTPUT_FOLDER']):
        i = join(app.config['OUTPUT_FOLDER'],i)
        if stat(i).st_mtime < now - 600:
            if isfile(i):
                remove(i)

    for i in listdir(app.config['UPLOAD_FOLDER']):
        i = join(app.config['UPLOAD_FOLDER'],i)
        if stat(i).st_mtime < now - 600:
            if isfile(i):
                remove(i)
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('path/to/git_repo')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
        
if __name__ == "__main__":
    app.run(debug=True)