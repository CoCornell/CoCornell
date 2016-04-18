
API Prefix: /api/

In following samples, the authentication will be omitted. But you need to make authentications if needed.

status: ok / error

error code


# GET /token/  
Returns a unique token for authorized user, which expires in 6000 seconds. You need to use this token for every subsequent requests to authenticate. Just specify authentication data like this: `-u <your_token>:unused`.


### Requires Authentication
Yes

### Parameters
None

### Sample Request
```
curl -u hy456:123 -X GET http://localhost:5000/api/token/
```

### Sample Result
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ0OTEyMDE5MSwiaWF0IjoxNDQ5MTE5NTkxfQ.eyJuZXRpZCI6Imh5NDU2In0.zQMTo0VfXuyjq8T2ut-pP_-vxuq-m1_e214Gkg2M6Vk"
}
```




# POST /signup/
Sign up a new user specified by netid, password and name. Returns user's info if sign up successfully.

### Requires Authentication
No

### Parameters
Parameter | Required / Optional    | Value
----------|------------------------|---------
`netid`   |  Required              | string
`password`|  Required              | string
`name`    |  Required              | string

### Sample Request
```
curl -d "netid=abc123&name=Jack&password=123" -X POST http://localhost:5000/api/signup/
```

### Sample Result
```json
{
  "status": "OK",
  "user": {
    "name": "Jack",
    "netid": "abc123",
    "reg_time": "2015-12-03 00:40:38"
  }
}
```



# GET /board/
Returns all the boards the user has access to.

### Requires Authentication
Yes

### Parameters
None

### Sample Request
```
curl http://localhost:5000/api/board/
```

### Sample Result
```json
{
  "boards": [
    {
      "id": 1,
      "name": "project1"
    },
    {
      "id": 2,
      "name": "project2"
    }
  ],
  "status": "OK"
}
```



# GET /board/count/
Returns number of boards the user has access to.

### Requires Authentication
Yes

### Parameters
None

### Sample Request
```
curl http://localhost:5000/api/board/count/
```

### Sample Result
```json
{
  "count": 8,
  "status": "OK"
}
```


# GET /list/\<int:list_id\>/
Returns the list, including all the cards in it specified by list id.

### Requires Authentication
Yes

### Parameters
None

### Sample Request
```
curl http://localhost:5000/api/list/1/
```


### Sample Result
```json
{
  "list": {
    "board_id": 1,
    "cards": [
      {
        "content": "content",
        "id": 22,
        "is_image": false,
        "list_id": 6
      },
      {
        "content": "test.png",
        "id": 31,
        "is_image": true,
        "list_id": 6
      }
    ],
    "id": 6,
    "name": "new_list"
  },
  "status": "OK"
}
```





# DELETE /list/\<int:list_id\>/
Delete the list specified by list id.

### Requires Authentication
Yes

### Parameters
None

### Sample Request
```
curl -X DELETE http://localhost:5000/api/list/1/
```

### Sample Result
```json
{
  "deleted": true,
  "status": "OK"
}
```



# POST /list/
Add a list.

### Requires Authentication
Yes

### Parameters
Parameter | Required / Optional    | Value
----------|------------------------|---------
`board_id`|  Required              | Integer
`name`    |  Required              | string

### Sample Request
```
curl -X POST -d "board_id=1&name=new_list" http://localhost:5000/api/list/
```

### Sample Result
```json
{
  "created": true,
  "list": {
    "board_id": 1,
    "id": 6,
    "name": "new_list"
  },
  "status": "OK"
}
```




# DELETE /card/\<int:card_id\>/
Delete the card specified by card id.

### Requires Authentication
Yes

### Parameters
None

### Sample Request
```
curl -X DELETE http://localhost:5000/api/card/1/
```

### Sample Result
```json
{
  "deleted": true,
  "status": "OK"
}
```





# POST /card/
Add a text card.

### Requires Authentication
Yes

### Parameters
Parameter | Required / Optional    | Value
----------|------------------------|---------
`list_id` |  Required              | Integer
`content` |  Required              | string

### Sample Request
```
curl -X POST -d "list_id=6&content=content" http://localhost:5000/api/card/
```

### Sample Result
```json
{
  "created": true,
  "list": {
    "content": "content",
    "id": 22,
    "is_image": false,
    "list_id": 6
  },
  "status": "OK"
}
```


# POST /upload/
Add an image card.

### Requires Authentication
Yes

### Parameters
Parameter | Required / Optional    | Value
----------|------------------------|---------
`list_id` |  Required              | Integer
`file`    |  Required              | File

### Sample Request
```
curl -X POST http://localhost:5000/api/upload/ -d "list_id=6&file=@/Users/yhf/Desktop/test.png"
```

### Sample Result
```json
{
  "card": {
    "content": "test.png",
    "id": 30,
    "is_image": true,
    "list_id": 6
  },
  "created": true,
  "status": "OK"
}
```