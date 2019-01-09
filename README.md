# Finance Manager API

It's a basic example of the REST application that's using a django rest framework. App uses DefaultRouter with viewsets, generics and api decorators.

## How to run app
Download the next [script](./runserver.sh) and run its.

```bash
wget https://raw.githubusercontent.com/rostIvan/financemanager/master/runserver.sh && bash runserver.sh
```

And then open localhost:8000/api/ on your browser to view the app.

## Available routes

django admin page
* admin/     

django login page   
* auth/login/ 

getting token on user
* auth-token/

all api methods 
* api/
    * create-user/
    * users/
    * categories/
    * transactions/
    * pretty/
        * usernames/
        * categories/
        * transactions/

`Note:` All the routes under api/pretty/* are **read only** 
## Login as admin
You're be able to auth using via next page: http://localhost:8000/admin/

`login:` admin

`password:` admin
 
 Or create a new superuser:
```bash
./manage.py createsuperuser
```
Admin has all privileges and has access to any data
## Base RESTful model
|  Method |  Path | Info     |
|---|---|---|
| GET | /users           |           Returns a list of users|
| GET | /users/\<id>     |      Returns information for a specific user|
| POST | /users          |          Create a new user|
| PUT |   /users/\<id>   |      Completely modifies a specific user|
| PATCH | /users/\<id>   |    Partially updates a specific user|
| DELETE |/users/\<id>   |   Remove a specific user|

## Examples of API calls
If you want to test api calls, probably you need to install some tools like a "Postman" or simple terminal "cURL"

### Create user
If you wanna create a new account(without any superuser privileges) just execute the next command:
```bash
curl -w "\nhttp_code:  %{http_code}\n" \
-X POST \
-H 'Accept: application/json; indent=4' \
-d 'username=luke&password=qwerty' \                      
http://localhost:8000/api/create-user/ 
```
Output:
```json
{
    "id": 15,
    "username": "luke",
    "email": "",
    "date_joined": "2019-01-09T00:37:16.143572Z"
}
```
That command will produce a User(username: 'luke', password: 'qwerty')

For every user application automatically generates token
### Obtain user auth token
```bash
curl -L \
-X POST \
-H 'Accept: application/json; indent=4' \   
-d 'username=luke&password=qwerty' \                       
http://localhost:8000/auth-token/
```

 The output will be something like that:
 ```json
{ "token": "03f4f2417065a1e4cbea0071de46c40d7f41c044" }
```
Now you can to use auth token instead of your login and password.

### GET
#### Users
* Retrieve all users(it's possible if you have permissions)
```bash
curl -L \
-X GET \ 
-H 'Authorization: Token fc1f652a93c2d972c108a32eeaea87f2d99a94d7' \
-H 'Accept: application/json; indent=4' \   
http://localhost:8000/api/users/ 
```
```json
[
    {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "date_joined": "2019-01-02T01:38:57Z"
    },
    {
        "id": 8,
        "username": "john",
        "email": "",
        "date_joined": "2019-01-04T02:42:09.509637Z"
    },
    {
            "id": 15,
            "username": "luke",
            "email": "",
            "date_joined": "2019-01-09T00:37:16.143572Z"
    }
]
```
* Retrieve user with id=1
```bash
curl -L \
-X GET \
-H 'Authorization: Token fc1f652a93c2d972c108a32eeaea87f2d99a94d7' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/users/1/ 
```
```json
{
    "id": 1,
    "username": "admin",
    "email": "admin@example.com",
    "date_joined": "2019-01-02T01:38:57Z"
}
```
* Get users with username 'luke'
```bash
curl -L \
-X GET \
-H 'Authorization: Token fc1f652a93c2d972c108a32eeaea87f2d99a94d7' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/users\?username=luke 
```
```json
[
    {
        "id": 15,
        "username": "luke",
        "email": "",
        "date_joined": "2019-01-09T00:37:16.143572Z"
    }
]
```
#### Categories
* Get all user categories with auth token "0a0032ed3f38d95dcfe498e703d68264138c60cf"
```bash
curl -L \
-X GET \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/categories/
```
```json
[
    {
        "id": 34,
        "name": "Car"
    },
    {
        "id": 15,
        "name": "Rent"
    },
    {
        "id": 9,
        "name": "Pizza"
    },
    {
        "id": 2,
        "name": "Beer"
    }
]
```
* Get user category with id=15
```bash
curl -L \
-X GET \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/categories/15/
```
```json
{
    "id": 15,
    "name": "Rent"
}
```
#### Transactions
* Get all user transactions with token: '0a0032ed3f38d95dcfe498e703d68264138c60cf'
```bash
curl -L \
-X GET \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/transactions/
```
```json
[
    {
        "id": 13,
        "category_name": "Pizza",
        "title": "Pizza Party #2",
        "description": "",
        "amount": "-250.00",
        "datetime": "2019-01-06T13:41:28.444667Z"
    },
    {
        "id": 33,
        "category_name": "Pizza",
        "title": "Pizza Party",
        "description": "",
        "amount": "-150.00",
        "datetime": "2019-01-08T16:35:11.785720Z"
    },
    {
        "id": 3,
        "category_name": "Pizza",
        "title": "Pizza \"Carbonara\"",
        "description": "Pizza on my home party",
        "amount": "-30.00",
        "datetime": "2019-01-06T09:53:55.826219Z"
    },
    {
        "id": 22,
        "category_name": "Beer",
        "title": "Cup of beer",
        "description": "",
        "amount": "-20.00",
        "datetime": "2019-01-08T13:03:18.557498Z"
    },
    {
        "id": 51,
        "category_name": "Rent",
        "title": "Cup of beer",
        "description": "",
        "amount": "-20.00",
        "datetime": "2019-01-08T13:03:18.557498Z"
    }
]
```
* Get user transaction with id=51
```bash
curl -L \
-X GET \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/transactions/34
```
```json
{
    "id": 34,
    "category_name": "Car",
    "title": "Repair",
    "description": "",
    "amount": "-150.00",
    "datetime": "2019-01-09T22:56:41.346738Z"
}
```
#### Pretty
* Get all the registered usernames (only superuser has permission)
```bash
curl -L \
-X GET \
-H 'Authorization: Token fc1f652a93c2d972c108a32eeaea87f2d99a94d7' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/pretty/usernames/
```
```json
[
    "admin",
    "vasya",
    "petya",
    "kolya",
    "alex",
    "john",
    "nick",
    "andrew",
    "david",
    "luke"
]
```
* Get all user categories as list names
```bash
curl -L \
-X GET \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/pretty/categories/
```
```json
[
    "Car",
    "Rent",
    "Pizza",
    "Beer"
]
```
* Get all transactions grouped by category
```bash
curl -L \
-X GET \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/pretty/transactions/
```
```json
[
    {
        "category": "Car",
        "transactions": []
    },
    {
        "category": "Rent",
        "transactions": []
    },
    {
        "category": "Pizza",
        "transactions": [
            {
                "id": 13,
                "title": "Pizza Party #2",
                "description": "",
                "amount": "-250.00",
                "datetime": "2019-01-06T13:41:28.444667Z"
            },
            {
                "id": 33,
                "title": "Pizza Party",
                "description": "",
                "amount": "-150.00",
                "datetime": "2019-01-08T16:35:11.785720Z"
            },
            {
                "id": 3,
                "title": "Pizza \"Carbonara\"",
                "description": "Pizza on my home party",
                "amount": "-30.00",
                "datetime": "2019-01-06T09:53:55.826219Z"
            }
        ]
    },
    {
        "category": "Beer",
        "transactions": [
            {
                "id": 22,
                "title": "Cup of beer",
                "description": "",
                "amount": "-20.00",
                "datetime": "2019-01-08T13:03:18.557498Z"
            }
        ]
    }
]
```
### POST
#### Users
* [Create new user](#create-user)
* [Obtain user token](#obtain-user-auth-token)
#### Categories
* Create new category and attach to user with token: '0a0032ed3f38d95dcfe498e703d68264138c60cf'
```bash
curl -L \
-X POST \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
-d 'name=Car' \
http://localhost:8000/api/categories/
```
```json
{
    "id": 42,
    "name": "Car"
}
```
#### Transactions
* Create new transaction for user

```bash
curl -L \
-X POST \  
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
-d 'category_name=Car&title=Repair&amount=-150' \ 
http://localhost:8000/api/transactions/
```
```json
{
    "id": 34,
    "category_name": "Car",
    "title": "Repair",
    "description": "",
    "amount": "-150.00",
    "datetime": "2019-01-09T22:56:41.346738Z"
}
```
### PUT
#### Users
* Put into transaction model with id=8 data:
      
      username: 'kevin'
      email: 'kevin@gmail.com'
      password: 'jgSLd7GYX5jNUKRux4TLNOlyHE4moRGKWHvmMh'
```bash
curl -L \                             
-X PUT \
-H 'Authorization: Token fc1f652a93c2d972c108a32eeaea87f2d99a94d7' \
-H 'Accept: application/json; indent=4' \
-d 'username=kevin&password=jgSLd7GYX5jNUKRux4TLNOlyHE4moRGKWHvmMh&email=kevin@gmail.com' \ 
http://localhost:8000/api/users/11/
```
```json
{
    "id": 11,
    "username": "kevin",
    "email": "kevin@gmail.com",
    "date_joined": "2019-01-04T21:41:51.382797Z"
}
```
#### Categories
* Replace category model with id=20 on:
      
      name: 'Rest'
```bash
curl -L \
-X PUT \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
-d 'name=Rest' \ 
http://localhost:8000/api/categories/20/
```
```json
{
    "id": 20,
    "name": "Rest"
}
```
#### Transactions
* Put into transaction model with id=8 data:
      
      category_name: 'Sport'
      title: 'Gym'
      amount: -190 
      description: 'Now I do sports'

```bash
curl -L \
-X PUT \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
-d 'category_name=Sport&title=Gym&amount=-190&description=Now I do sports' \
http://localhost:8000/api/transactions/8/
```
```json
{
    "id": 8,
    "category_name": "Sport",
    "title": "Gym",
    "description": "Now I do sports",
    "amount": "-190.00",
    "datetime": "2019-01-06T13:09:21.068322Z"
}
```
### PATCH
#### Users
* Set new username ('jack') for user with id=11
```bash
curl -L \
-X PATCH \
-H 'Authorization: Token fc1f652a93c2d972c108a32eeaea87f2d99a94d7' \
-H 'Accept: application/json; indent=4' \
-d 'username=jack' \                     
http://localhost:8000/api/users/11/
```
```json
{
    "id": 11,
    "username": "jack",
    "email": "jack@gmail.com",
    "date_joined": "2019-01-04T21:41:51.382797Z"
}
```

#### Categories
* Update category name to 'Food' with id=32
```bash
curl -L \
-X PATCH \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
-d 'name=Food' \
http://localhost:8000/api/categories/32/ 
```
```json
{
    "id": 32,
    "name": "Food"
}
```
#### Transactions
* Change category name and title to ('Sport', 'Gym') for transaction with id=8 
```bash
curl -L \
-X PATCH \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
-H 'Accept: application/json; indent=4' \
-d 'category_name=Sport&title=Gym' \             
http://localhost:8000/api/transactions/8/
```
```json
{
    "id": 8,
    "category_name": "Sport",
    "title": "Gym",
    "description": "",
    "amount": "-190.00",
    "datetime": "2019-01-06T13:09:21.068322Z"
}
```

### DELETE
* Delete user with id=15 (only superuser has permission)
```bash
curl -L \
-X DELETE \
-H 'Authorization: Token fc1f652a93c2d972c108a32eeaea87f2d99a94d7' \
-H 'Accept: application/json; indent=4' \
http://localhost:8000/api/users/15/
```
* Delete category with id=40
```bash
curl -L \
-X DELETE \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
http://localhost:8000/api/categories/40/
```
* Delete transaction with id=7
```bash
curl -L \
-X DELETE \
-H 'Authorization: Token 0a0032ed3f38d95dcfe498e703d68264138c60cf' \
http://localhost:8000/api/transactions/7/
```
## Tools
* python 3.7.1
* pip 18.1 
* django 2.1.4
* DRF 3.9.0
* postgres 11.1
* curl 7.63.0 