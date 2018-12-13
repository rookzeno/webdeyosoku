from flask import Flask, jsonify, abort, make_response,render_template,url_for,request,redirect,send_file
import os.path
from imagenet import imagenet
from PIL import Image
import io
import qrcode as qr
import base64

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/send',methods = ['post'])
def posttest():
    img_file = request.files['img_file']
    fileName = img_file.filename
    root, ext = os.path.splitext(fileName)
    ext = ext.lower()
    gazouketori = set([".jpg", ".jpeg", ".jpe", ".jp2", ".png", ".webp", ".bmp", ".pbm", ".pgm", ".ppm",
                      ".pxm", ".pnm",  ".sr",  ".ras", ".tiff", ".tif", ".exr", ".hdr", ".pic", ".dib"])
    if ext not in gazouketori:
        return render_template('index.html',massege = "対応してない拡張子です",color = "red")
    print("success")
    try:
        bunrui = imagenet(img_file)
        name, desc, score =  bunrui.deep()
    except:
        return render_template('index.html',massege = "解析出来ませんでした",color = "red")
    buf = io.BytesIO()
    image = Image.open(img_file)
    image.save(buf, 'png')
    qr_b64str = base64.b64encode(buf.getvalue()).decode("utf-8")
    qr_b64data = "data:image/png;base64,{}".format(qr_b64str)
    return render_template('kekka.html',namae = desc ,kaku = score,img = qr_b64data)

@app.route('/kekka')
def kekka():
    return render_template('kekka.html')

# エラーハンドリング
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run()
