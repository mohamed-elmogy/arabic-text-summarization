from app import app
from flask import render_template, url_for, flash
from app.forms import VoiceForm, DocumentForm, TxtForm, OcrForm
import speech_recognition as sr
from transformers import pipeline
import math
import docx
import requests
import json

Abstractive_output_dir = "results-arabart-finetuned-squad-accelerate"
Abstractive_summarizer = pipeline("summarization", model=Abstractive_output_dir)
Recognizer = sr.Recognizer()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home page',
                           legend='Home Page')


@app.route('/abstractive')
def Abstractive_summarization():
    header = "Abstractive Summarization"
    return render_template('Abstractive_summarization.html', title='Abstractive Summarization',
                           legend='Abstractive Summarization', header=header)


@app.route('/extractive')
def Extractive_summarization():
    header = "Extractive Summarization"
    return render_template('Extractive_summarization.html', title='Extractive Summarization',
                           legend='Extractive Summarization', header=header)


@app.route('/abstractive/voice', methods=['GET', 'POST'])
def Abstractive_voice():
    header = "Abstractive voice summarization"
    form = VoiceForm()
    summary = ''
    if form.validate_on_submit():
        record = form.file.data
        audio_file = sr.AudioFile(record)
        text = voice_recognizer(audio_file)
        percent = float(form.slider.data) / 100
        max_length = len(text.split())
        min_length = math.ceil(percent * len(text.split()))
        summary = Abstractive_summarizer(text, max_length=max_length, min_length=min_length)[0]["summary_text"]
        flash('your voice has been summarized', 'success')
    return render_template('voice.html', title='Abstractive Voice Summary',
                           form=form, legend='Voice Summary', summary=summary, header=header)


@app.route('/extractive/voice', methods=['GET', 'POST'])
def Extractive_voice():
    header = "Extractive voice summarization"
    form = VoiceForm()
    summary = ''
    if form.validate_on_submit():
        record = form.file.data
        audio_file = sr.AudioFile(record)
        text = voice_recognizer(audio_file)
        percent = float(form.slider.data) / 100
        max_length = len(text.split())
        min_length = math.ceil(percent * len(text.split()))
        summary = Abstractive_summarizer(text, max_length=max_length, min_length=min_length)[0]["summary_text"]
        flash('your voice has been summarized', 'success')
    return render_template('voice.html', title='Extractive Voice Summary',
                           form=form, legend='Voice Summary', summary=summary, header=header)


@app.route('/abstractive/docx', methods=['GET', 'POST'])
def Abstractive_docx():
    header = "Abstractive document summarization"
    form = DocumentForm()
    summary = ''
    if form.validate_on_submit():
        file = form.document.data
        text = docx_preprocess(file)
        percent = float(form.slider.data) / 100
        for para in text:
            max_length = len(para.split())
            min_length = math.ceil(percent * len(para.split()))
            summary = summary + Abstractive_summarizer(para, max_length=max_length, min_length=min_length)[0][
                "summary_text"]
        flash('your document has been summarized', 'success')
    return render_template('Docx.html', title='Abstractive docx Summary',
                           form=form, legend='Document Summary', summary=summary, header=header)


@app.route('/extractive/docx', methods=['GET', 'POST'])
def Extractive_docx():
    header = "Extractive document summarization"
    form = DocumentForm()
    summary = ''
    if form.validate_on_submit():
        file = form.document.data
        text = docx_preprocess(file)
        percent = float(form.slider.data) / 100
        for para in text:
            max_length = len(para.split())
            min_length = math.ceil(percent * len(para.split()))
            summary = summary + Abstractive_summarizer(para, max_length=max_length, min_length=min_length)[0][
                "summary_text"]
        flash('your document has been summarized', 'success')
    return render_template('Docx.html', title='Extractive docx Summary',
                           form=form, legend='Document Summary', summary=summary, header=header)


@app.route('/abstractive/txt', methods=['GET', 'POST'])
def Abstractive_txt():
    header = "Abstractive text summarization"
    form = TxtForm()
    summary = ''
    if form.submit.data:
        text = form.content.data
        percent = float(form.slider.data) / 100
        max_length = len(text.split())
        min_length = math.ceil(percent * len(text.split()))
        summary = Abstractive_summarizer(text, max_length=max_length, min_length=min_length)[0]["summary_text"]
        flash('your document has been summarized', 'success')
    return render_template('txt.html', title='Abstractive text Summary',
                           form=form, legend='Text Summary', summary=summary, header=header)


@app.route('/extractive/txt', methods=['GET', 'POST'])
def Extractive_txt():
    header = "Extractive text summarization"
    form = TxtForm()
    summary = ''
    if form.submit.data:
        text = form.content.data
        percent = float(form.slider.data) / 100
        max_length = len(text.split())
        min_length = math.ceil(percent * len(text.split()))
        flash('your document has been summarized', 'success')
    return render_template('txt.html', title='Extractive text Summary',
                           form=form, legend='Text Summary', summary=summary, header=header)


@app.route('/abstractive/ocr', methods=['GET', 'POST'])
def Abstractive_ocr():
    header = "Abstractive image summarization"
    form = OcrForm()
    summary = ''
    if form.submit.data:
        img = form.img.data
        text = ocr_space_file(img)
        percent = float(form.slider.data) / 100
        max_length = len(text.split())
        min_length = math.ceil(percent * len(text.split()))
        summary = Abstractive_summarizer(text, max_length=max_length, min_length=min_length)[0]["summary_text"]
        flash('your image has been summarized', 'success')
    return render_template('ocr.html', title='Abstractive image Summary',
                           form=form, legend='Image Summary', summary=summary, header=header)


@app.route('/extractive/ocr', methods=['GET', 'POST'])
def Extractive_ocr():
    header = "Extractive image summarization"
    form = OcrForm()
    summary = ''
    if form.submit.data:
        img = form.img.data
        text = ocr_space_file(img)
        percent = float(form.slider.data) / 100
        max_length = len(text.split())
        min_length = math.ceil(percent * len(text.split()))
        summary = Abstractive_summarizer(text, max_length=max_length, min_length=min_length)[0]["summary_text"]
        flash('your image has been summarized', 'success')
    return render_template('ocr.html', title='Abstractive image Summary',
                           form=form, legend='Image Summary', summary=summary, header=header)



def voice_recognizer(record):
    with record as source:
        audio_data = Recognizer.record(source)

    text = Recognizer.recognize_google(audio_data, language='ar-Ar')
    return text


def docx_preprocess(doc):
    doc = docx.Document(doc)
    current_section = None
    current_text = ""
    chunks = []
    pre_text = ""
    for para in doc.paragraphs:
        # Check if the paragraph is a heading
        if para.style.name.startswith("Heading"):
            if current_section is not None:
                print(f"Section {current_section}: {current_text}\n")
            current_section += para.text
            current_text = ""
        else:
            # Check if the paragraph contains bold or underline text
            for run in para.runs:
                if run.bold or run.underline:
                    current_text += run.text

            # If the paragraph does not contain bold or underline text, append its text to the current section
            if current_text == "":
                current_text += para.text

            if len(current_text.split()) > 500:
                chunks.append(current_text)
                current_section = None
                current_text = ""

    chunks.append(current_text)
    return chunks


import requests
import json


def ocr_space_file(image_data, overlay=False, api_key='helloworld', language='ara'):
    """ OCR.space API request with image data.
        Python3.5 - not tested on 2.7
    :param image_data: The image data as bytes.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result as a dictionary.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    files = {'filename': ('image.jpg', image_data)}
    r = requests.post('https://api.ocr.space/parse/image',
                      files=files,
                      data=payload,
                      )
    result = json.loads(r.content)
    return result['ParsedResults'][0]['ParsedText']
