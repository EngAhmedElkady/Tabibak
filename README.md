# Tabibak
A medical application to predict heart disease, diabetes and kidney disease and contains some tips to maintain your health

## Overview
* Fully working API
* Well-structured and readable code
* Instructions in the README on how to run the project.

## Technologies
* asgiref==3.4.1
* cffi==1.14.6
* cryptography==35.0.0
* Django==3.2.7
* django-rest-knox==4.1.0
* djangorestframework==3.12.4
* gunicorn==20.1.0
* joblib==1.0.1
* numpy==1.21.2
* Pillow==8.3.2
* pycparser==2.20
* pytz==2021.1
* scikit-learn==1.0
* scipy==1.7.1
* sklearn==0.0
* sqlparse==0.4.2
* threadpoolctl==3.0.0
* whitenoise==5.3.0

## Database design
![image](https://user-images.githubusercontent.com/76946030/135693730-d1a8e33f-a550-4c72-911b-6e565ddc1f0f.png)


## Usage
server : [https://tabiba.herokuapp.com]( https://tabiba.herokuapp.com ) 

### account
* register
* login
* logout
* logoutall

* register :
That’s it. Now go to url ( https://tabiba.herokuapp.com/account/api/register/ ) in your browser or post and the following in content.
````
{
    "username": "admin",
    "email": "admin@bot.com",
    "password": "Password@123"
}

````
And in response, you will get similar data –

````
{
    "user": {
        "id": 2,
        "username": "admin1",
        "email": "admin1@bot.com"
    },
    "token": "790e890d571753148bbc9c4447f106e74ecf4d1404f080245f3e259703d58b09"
}
````

* login :
That’s it. Now go to url (https://tabiba.herokuapp.com/account/api/login/ ) in your browser or post and the following in content.

````
{
    "username": "admin",
    "password": "Password@123"
}
````

## profile :
[https://tabiba.herokuapp.com/account/api/profile/](https://tabiba.herokuapp.com/account/api/profile/)

* GIT
````
{
    "username": "Ahmed Elkady",
    "email": "ahmedabdalkaderma@gmail.com",
    "phone": "+201140369670",
    "photo": "uploads/52ac5893-b0f9-42d4-8575-e957bdcce8eb.jpeg"
}
````
* update :
You can update phone and photo
````
{
    "phone": "01140369670",
    "photo": "uploads/52ac5893-b0f9-42d4957bdcce8eb_7WWI03r.jpeg"
}

````

### Kidney
[https://tabiba.herokuapp.com//kidney/api/kidney_data/](https://tabiba.herokuapp.com/kidney/api/kidney_data/)

* POST
````
{
        "age": "50.00",
        "al": 20,
        "su": "20.00",
        "bgr": 10,
        "bu": 250,
        "sc": "20.00",
        "hemo": "50.02",
        "pcv": 28,
        "wc": 55,
        "htn": "yes"
}
````
and return 
````
{
    "result": [
        0
    ],
    "result2": [
        [
            0.8,
            0.2
        ]
    ]
}
````
* GET :
all kidney data for current user
````
[
    {
        "id": 1,
        "date": "2021-10-01T22:54:16.774322Z",
        "age": "50.00",
        "al": 20,
        "su": "20.00",
        "bgr": 10,
        "bu": 250,
        "sc": "20.00",
        "hemo": "50.02",
        "pcv": 28,
        "wc": 55,
        "htn": "yes",
        "result": 0,
        "result2": "0"
    },
    {
        "id": 2,
        "date": "2021-10-01T22:57:40.655739Z",
        "age": "50.00",
        "al": 20,
        "su": "20.00",
        "bgr": 10,
        "bu": 250,
        "sc": "20.00",
        "hemo": "50.02",
        "pcv": 28,
        "wc": 55,
        "htn": "yes",
        "result": 0,
        "result2": "0.8"
    }
]
````
## Heart
[https://tabiba.herokuapp.com//heart/api/heart_data/](https://tabiba.herokuapp.com/heart/api/heart_data/)

* POST
````
{

        "age": "50.00",
        "cp": "200.01",
        "trestbps": "350.00",
        "chol": "50.00",
        "thalach": "100.00",
        "exang": "360.00",
        "oldpeak": "140.00",
        "ca": "900.00"
}
````
and return 
````
{
    "result": [
        0
    ],
    "result2": [
        [
            1.0,
            0.0
        ]
    ]
}

````
* GET :
all heart data for current user
````
[
    {
        "id": 1,
        "date": "2021-10-01T23:00:05.784219Z",
        "age": "50.00",
        "cp": "200.01",
        "trestbps": "350.00",
        "chol": "50.00",
        "thalach": "100.00",
        "exang": "360.00",
        "oldpeak": "140.00",
        "ca": "900.00",
        "result": 0,
        "result2": 0
    },
    {
        "id": 2,
        "date": "2021-10-01T23:01:27.882909Z",
        "age": "50.00",
        "cp": "200.01",
        "trestbps": "350.00",
        "chol": "50.00",
        "thalach": "100.00",
        "exang": "360.00",
        "oldpeak": "140.00",
        "ca": "900.00",
        "result": 0,
        "result2": 1
    }
]
````
## Diabetes
[https://tabiba.herokuapp.com/Diabetes/api/Diabetes_data](https://tabiba.herokuapp.com/Diabetes/api/Diabetes_data)

* POST
````
{
        "age": "50.00",
        "Pregnancies": 120,
        "Glucose": 250,
        "SkinThickness": 360,
        "Insulin": 150
}
````
and retuen
````
{
    "result": [
        1.0
    ],
    "result2": [
        [
            0.2243900000442094,
            0.7756099999557908
        ]
    ]
}
````
* GET
all Diabetes data for current user
````

[
    {
        "id": 1,
        "age": "50.00",
        "date": "2021-10-01T23:00:26.475894Z",
        "Pregnancies": 120,
        "Glucose": 250,
        "SkinThickness": 360,
        "Insulin": 150,
        "result": 0,
        "result2": 0
    },
    {
        "id": 2,
        "age": "50.00",
        "date": "2021-10-01T23:05:06.228778Z",
        "Pregnancies": 120,
        "Glucose": 250,
        "SkinThickness": 360,
        "Insulin": 150,
        "result": 1,
        "result2": 0
    }
]
````

