# Simple Flask API Web Server
### *From Plain text to JSON*

### Info
This is a simple project from my Data Science course made by graduate students.

#### The Task
Create an API Web Server by using the Flask micro framework to display data from a Plain Text file in JSON format.
After receiving a request the server will respond with a JSON.

#### Routes (Endpoints)
These are the main Routes of the Web Server.

Index
	```https://127.0.0.1/```
	This shows the main page with an "Hello world!" text.

Name
	```https://127.0.0.1/name?name=Alessio&surname=Vaccaro```
	This shows a page with an your name and surname.

ReadFile
```https://127.0.0.1/readFile```
This shows a JSON obtained through the *"my_model.py"* and *"my_file.txt"* file and its functions.