from flask import jsonify, request, Response, send_file
import os
import datetime as dt

from services.NoteExtractor import NoteExtractor
from services.converter import convert_to_pdf
from services.print_sheet_music2 import print_sheet_music

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
  ne = NoteExtractor(file_path)
  out = ne.get_all_estimated_freqs()
  freqs = [a[0] for a in out]
  print(file_path)
  print_sheet_music(file_path, freqs)
  pdf_path = convert_to_pdf(file_path)
  return send_file(pdf_path)