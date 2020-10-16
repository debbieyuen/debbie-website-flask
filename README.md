# debbie-website-flask


```
python app.py
```

Requires gsheets and flask. 

```
pip install Flask
pip install gsheets
```

In order to setup the Google Sheets, go to https://developers.google.com/sheets/api/quickstart/python and click on "Enable the Google Sheets API".

Move credentials.json to the same directory as the GitHub repository. 

Next, replace the variable, `sheets` with your own Google Drive excel sheet URL. 

```
sheets = Sheets.from_files('credentials.json', 'storage.json')
url = "INSERT URL HERE"
```

The excel document should look like this!

| Project Name  | Image URL     | Description   | Category Tag  |
| ------------- | ------------- | ------------- | ------------- |
| Project 1     | Link to image URL  | This is my Project! | Photography |
| Project 2     | Link to image URL | This is my 2nd Project! | UI/UX |
