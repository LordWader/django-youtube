# django-youtube

This is a small django web-application that works with youtube api.

### Requirments
```
Python 3.7
django 2.2.3
djangorestframework 3.9.4
celery 4.3.0
redis server
```

### Server deployment
```
python manage.py runserver
```
### Redis + celery
```
$ redis-server
$ celery -A testapi worker
$ celery -A testapi beat
```

### Api documentation
1) method - POST
   endpoint - api/words
   body - {"key_word": string}
   response - {"id": integer, "key_word":string}
   
2) method - GET
   endpoint - api/words
   response - [{"key_word": string, "id": integer}, {"key_word": string, "id": integer}]
   
3) method - DELETE
   endpoint - api/words/<id:int>
   
4) method - GET
   endpoint - api/words/<id:int>/videos
   response - {"title": string, "id": integer, "url": [List<string>]}
 
5) method - POST
   endpoint - get-user-auth-token
   body - {"username": string, "password": string}
   response - {"token": string}
   
