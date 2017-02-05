# Forex Predictor

Forex Predictor is a web application which helps to predict whether particular company/business would be in need of foreign exchange services and estimate their propensity score, determining their probability of using forex services.

You can find web application here - [Forex Predictor](https://shielded-thicket-76813.herokuapp.com/solo/)
## Documentation

The documentation available as of the date of this release is included in the docs/ directory.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Before starting make sure you have python installed on your linux operation system

Start virtual environment by going to Forex/ directory where virEnv folder is located and type the following command on terminal

```
source virEnv/bin/activate
```

Make sure you have pip installed. If not then, 
to install pip, securely download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) . 

Then run the following:

```
python get-pip.py
```

The requirements.txt file in Forex directory contains all prerequisites required to run the application.

If you don't have them, you can install them by typing following command

```
pip freeze
```

### Running the Application

In Forex/ directory where manage.py file is located, type following command on 
terminal

```
python manage.py runserver
```

If everything goes fine, you will see following address by default on terminal to run server

```
http://127.0.0.1:8000/
```
Open this link in your favourite browser and start using the application


To quit server, type the following shortcut on command line

```
CONTROL-C
```

## Built With

* [Django](https://docs.djangoproject.com/en/1.10/) - The web framework used
* [Microsoft Cognitive Services](https://www.microsoft.com/cognitive-services/en-us/bing-web-search-api/documentation) - APIs to interact with Bing search engine
* [Natural Language Toolkit (NLTK)](http://www.nltk.org/) - For natural language processing, particularly entity recognition
* [Xgboost](https://xgboost.readthedocs.io/en/latest/) - Machine learning library
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web scrapper to get information from web pages
* [Postgres SQL](https://www.postgresql.org/docs/) - Database for the system

## Authors

* [Ashish Kulkarni](https://github.com/coolashish/) 
* [Saket Komavar](https://github.com/Saket-Komawar/) 
* [Shubham Shah](https://github.com/SHUB1SHAH/) 

## License

This project is licensed under the --- License - see the [LICENSE.md](LICENSE.md) file

## Acknowledgments

* Hat tip to anyone who's code was used
