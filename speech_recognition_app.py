from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from speech_recognizer import speech_rec


app = Flask(__name__)

bootstrap = Bootstrap(app)


# Метод GET для загрузки содержимого с сайта
# Метод POST для получения файла от пользователя и его обработки
@app.route("/", methods=["GET", "POST"])
def index():
    """Отображает домашнюю страницу приложения."""
    transcript = ""
    if request.method == "POST":

        # Если файл не загружен, то вернуть домашнюю страницу
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        # Если у файла нет имени, то вернуть домашнюю страницу
        if file.filename == "":
            return redirect(request.url)

        # Если файл загружен, то перевести речь в текст
        # Файлы обрабатываются только в wav. формате
        if file:
            transcript = speech_rec(file, transcript)

    return render_template("index.html", transcript=transcript)


# Перевод на страницу с ошибкой в случае загрузки файла неправильного формата
@app.errorhandler(ValueError)
def error_file(error):
    return render_template("error_file.html")


if __name__ == '__main__':
    app.run(debug=False)


