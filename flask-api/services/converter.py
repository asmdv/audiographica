import os
import shutil

def convert_to_pdf(file_path:str):
  stream = os.system("lilypond" + " --png " + file_path)
  filename = file_path.split("/")[-1].strip()
  path = file_path[:-len(filename)]
  filename = filename.split(".")[0] + ".png"
  shutil.move(filename, path + filename)
  return path + filename