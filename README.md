# chuck-norris-jokes
Chuck Norris Jokes server

### Endpoints
**GET /joke**</br>
Get Chuck Norris joke 

**Headers**
|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `Authorization` | required | string  | Your account authorization.                                                                     |
**Response**
```
{
    "id": "F6v0fEXeREek9FnF6_9k4A",
    "categories": ["some category"],
    "createdAt": "2020-01-05 13:42:25.352697",
    "joke": "Chuck Norris' first car was Optimus Prime."
}
```
First you will need to run the service locally.
In order to run a requst run one you can use the following request request
```bash
curl --location --request GET 'http://localhost:8000/joke' \
--header 'Authorization: 1111-2222-3333'
```
*******
The project is under the `joke-service` folder.
First create virtualenv and activate it

#### Installation
`pip install -r /path/to/requirements.txt`

#### Run tests
To run the service tests
`pytest`

#### Run the server
To run the service you can use this command
`uvicorn main:app`

#### Shira's logger infrastructure
For defining the logger attributes, change the variable in the setup_logger call in main.py
Additions and changes:
middleware.py:  activate the logger by middlware 
logger.py: define the logger attribute and sturcture
auth.py: added function which check if the request's user is autherized
main.py: added the definition of the global variables, the definition of the logger and creation of its instance
