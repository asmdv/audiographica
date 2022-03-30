from flask import jsonify, request, Response, send_file
import os
import shutil
import datetime as dt

from services.NoteExtractor import NoteExtractor
from services.converter import convert_to_pdf
from services.print_sheet_music import print_sheet_music

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
  print("Freq and length: ", out)
  freqs = [a[0] for a in out]
  print_sheet_music(file_path, freqs)
  pdf_path = convert_to_pdf(file_path)
  pdf_path = os.path.abspath(pdf_path)
  index = pdf_path.find('music-to-notes')
  project_path = pdf_path[0:index+len("music-to-notes")]
  file_path = project_path+"\\front-end\\music-to-notes\\public\\notes.png"
  shutil.copy(pdf_path,file_path)
  print("Generated notes at:",file_path)
  return jsonify(path=file_path)