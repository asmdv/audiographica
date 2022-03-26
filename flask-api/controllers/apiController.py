from flask import jsonify, request, Response
import os
import datetime as dt

from services.NoteExtractor import NoteExtractor

DIR_PATH = "./uploaded_files/"

def index():
  return jsonify(msg="Welcome to API page!")

def getDateTime():
  now = dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
  return jsonify(datetime=now)

def postAudio():
  file_path = os.path.join(DIR_PATH, request.files['file'].filename)
  if (request.files['file'].content_type[:5] != "audio"):
    return Response("Unsupported file type", status=400)
  ne = NoteExtractor(file_path)
  out = ne.get_all_estimated_freqs()
  return jsonify(msg=out)