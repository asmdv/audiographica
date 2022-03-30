from flask import jsonify, request, Response, send_file
import os
import datetime as dt

from services.NoteExtractor import NoteExtractor
from services.converter import *
from services.print_sheet_music import print_sheet_music, extract_name

DIR_PATH = "./uploaded_files/"

def index():
  return jsonify(msg="Welcome to API page!")

def getDateTime():
  now = dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
  return jsonify(datetime=now)

def postAudio():
  if (request.files['file'].content_type[:5] != "audio"):
    return Response("Unsupported file type", status=400)
  file_path = os.path.join(DIR_PATH, request.files['file'].filename)
  request.files['file'].save(file_path)
  file_type = request.form['type']
  if file_type not in ['pdf', 'png']:
    return Response("Unsupported file type", status=400)
  ne = NoteExtractor(file_path)
  out = ne.get_all_estimated_freqs()
  print("Freq and length: ", out)
  freqs = [a[0] for a in out]
  ly_path = print_sheet_music(file_path, freqs)
  path = convert(ly_path, 'png')
  return send_file(path)

def get_pdf():
  filename = request.json['filename']
  file_path = os.path.join(DIR_PATH, filename)
  ly_path = extract_name(file_path) + ".ly"
  path = convert(ly_path, 'pdf')
  return send_file(path)