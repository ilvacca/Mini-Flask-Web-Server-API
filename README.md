# Mini Flask API Web Server Example

### *From Plain text to JSON*

---

## 1. Info
This is a sample project to learn the basics of a Web Server using Flask and Python.

## 2. The Task
Create an **API Web Server** by using the **Flask** micro framework to *expose* data extracted from a *plain text file* in *JSON*.
After receiving a request **the server will respond with a JSON**.

## 3. Routes (Endpoints)
These are the main routes of the Web Server.

### 3.1. Index
```
https://127.0.0.1/
```
This shows the main page with an "Hello world!" text.

### 3.2. Name
```
https://127.0.0.1/name?name=YOURNAME&surname=YOURSURNAME
```
This shows a page with an your name and surname.

### 3.3. ReadFile
```
https://127.0.0.1/readFile
```
This shows a JSON obtained through the *"modules.py"* and its functions and the *"my_file.txt"* file.


## 3.4. Endpoint: "ReadFile"
The output of the **ReadFile endpoint** will be:
```
[
	{
		"id":"1",
		"temperature":"12"
	},{
		"id":"2",
		"temperature":"42"
	},{
		"id":"3",
		"temperature":"15"
	},{
		"id":"4",
		"temperature":"23"
	}
	...
]
```

## Credits

*These resources were created with* ❤ *by Alessio Vaccaro*.
[Website](https://www.alessiovaccaro.com) | [LinkedIn](https://www.linkedin.com/in/alessio-vaccaro/) 