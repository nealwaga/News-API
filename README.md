# News-API
***
**Description**
---
This is a web application that displays a list of various news sources. On choosing a news source, it will preview the top news articles of the day. Clicking a news article will redirect the user to read it fully from the news source.
***
**User Stories**
---
These are the behaviours/features that the application implements for use by a user.
As a user I would like to:
* See various news sources.
* Select the ones they prefer.
* See the top news articles from that news source.
* See the image, description and time the news article was created.
* Click on an article and read it fully from the news source.
***
**Set-Up / Installation Requirements**
---
### Cloning
* In your terminal:
  `$ git clone https://github.com/nealwaga/News-API`
  `$ cd News-API`

---
### Running the Application
* Creating the virtual environment:
  `$ virtualenv virtual`
  `$ source virtual/bin/activate`
  `$ curl https://bootstrap.pypa.io/get-pip.py | python`

* Intsalling Flask and other Modules:
  `$ python3.6 -m pip install Flask`
  `$ python3.6 -m pip install Flask-Bootstrap`
  `$ python3.6 -m pip install Flask-Script`

* Setting up the API key:
  To be able to gather article info from the News API you will need an API Key.

  * Visit https://newsapi.org/ and register for an API key.
  * In the root directory of the project folder create a file: start.sh
  * Insert the following info into it:

          export NEWS_API_KEY='<Your-Api-Key>'
          python3 manage.py server

  * Insert the API Key you received from News Api where <Your-Api-Key> is.

* To run the application, in the terminal:
  `$ chmod +x start.sh`
  `$ ./start.sh`

---
**Technologies Used**
---
  * Python 3.8
  * Flask
  * HTML
  * CSS

---
**License**
---
This software is licensed under the MIT license. Copyright (c) 2022 Neal Waga