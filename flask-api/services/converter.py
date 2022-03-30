import os
import shutil

def convert(file_path:str, file_type:str):
  stream = os.system("lilypond" + " --" + file_type + " " + file_path)
  filename = file_path.split("/")[-1].strip()
  path = file_path[:-len(filename)]
  filename = filename.split(".")[0] + "." + file_type
  shutil.move(filename, path + filename)
  return path + filename