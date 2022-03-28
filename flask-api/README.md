### To install
Run `pip install -r requirements.txt`

### To run the app
`python app.py`

### API endpoints

`POST` `localhost:5000/api/audio` : To upload audio file. In body use `form-data` with key name "file" and value your file.

`GET` `localhost:5000/api/` : Welcome page

`GET` `localhost:5000/api/datetime` : Prints current time. Just for fun :D