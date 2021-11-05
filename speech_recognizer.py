# Библиотека для распознования речи
import speech_recognition as sr


def speech_rec(file, transcript):
    """Распознает речь в аудиофайле и переводит её в текст.
    Файлы принимаются только wav. формата."""
    # Объект класса Recognizer для преобразования аудиофайла в текст
    recognizer = sr.Recognizer()
    # Указываем аудиофайл, который переводим в текст
    audiofile = sr.AudioFile(file)

    with audiofile as source:
        # Преобразуем аудиофайл в объект AudioData
        data = recognizer.record(source)
    # Применяем метод recognize_google() к аудиофайлу для преобразования его в текст
    transcript = recognizer.recognize_google(data, key=None)

    return transcript
