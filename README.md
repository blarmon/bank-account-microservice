# bank-account-microservice

A microservice used to perform crud operations on (fake) customer bank accounts through an API

This site is essentially just an API connected to a postgres backend hosted on Heroku.

[Hosted on Heroku](https://bank-account-microservice.herokuapp.com/api/)

### The API can be explored using the Django Rest Framework built in tools linked above, using a tool like [Postman](https://www.getpostman.com/) to make calls to the endpoints listed below, or by utilizing a python library I have created, the repo and documentation for which lives [here](https://github.com/blarmon/bamLib) 

## Important note: The free heroku service I'm using shuts the server down after 30 minutes of inactivity. Your first call to the server will likely be slow due to this. If you click the heroku link above you can start the server up before you utilize the microservice.

API endpoints:

note: please attach {'Content-Type': 'application/json'} as a header for all calls (this is already taken care of if using the bam library I created.)

* accounts: https://bank-account-microservice.herokuapp.com/api/accounts/  

  * "GET" - https://bank-account-microservice.herokuapp.com/api/accounts/
    * returns a json object containing info about all accounts
  * "GET" - https://bank-account-microservice.herokuapp.com/api/accounts/ **_\<account id\>_**
    * returns a json object containing info about the account with the given id
  * "POST" - https://bank-account-microservice.herokuapp.com/api/accounts/
    * given the required data (outlined below), will create a new account associated with the given customer (user) id and return a json object with the new account's data. (note: account_opened will default to datetime.now() if no datetime is supplied)
      * data = {customer_id: *number*,
                account_type: *string*,
                balance: *number*, 
                interest_rate: *number*,
                account_opened: *datetime*}
  * "PATCH" - https://bank-account-microservice.herokuapp.com/api/accounts/ **_\<account id\>_**
    * given one or more fields from the required data (outlined below), will update those fields for the account with the given id, and return a 20X status if successful.
      * data = {account_id: *number*,
                customer_id: *number*,
                account_type: *string*,
                balance: *number*, 
                interest_rate: *number*,
                account_opened: *datetime*}
  * "DELETE" - https://bank-account-microservice.herokuapp.com/api/accounts/ **_\<account id\>_**
    * will delete the account with the given account id and return a 20X http status if successful.

* users: https://bank-account-microservice.herokuapp.com/api/users/  

  * "GET" - https://bank-account-microservice.herokuapp.com/api/users/
    * returns a json object containing info about all users
  * "GET" - https://bank-account-microservice.herokuapp.com/api/users/ **_\<user id\>_**
    * returns a json object containing info about the user with the given id
  * "POST" - https://bank-account-microservice.herokuapp.com/api/users/
    * given the required data (outlined below), will create a new user and return a json object with the new user's data.
      * data = {username: *string*,
                email: *string*,}
  * "PATCH" - https://bank-account-microservice.herokuapp.com/api/users/ **_\<user id\>_**
    * given one or more fields from the required data (outlined below), will update those fields for the user with the given id, and return a 20X status if successful.
      * data = {user: *string*,
                email: *string*}
  * "DELETE" - https://bank-account-microservice.herokuapp.com/api/users/ **_\<user id\>_**
    * will delete the user with the given id and return a 20X http status if successful.
