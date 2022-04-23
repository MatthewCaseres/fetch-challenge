# fetch-challenge
 
## Running the code

Go to the project directory containing the Dockerfile and the app folder and build the image.

```
docker build -t myimage .
```

You then run the container

```
docker run -d -p 80:80 myimage
```

The web server should start and be running and you can use the API that is appropriate for your docker host. For me I can go to http://127.0.0.1/docs and use the swagger UI to test the API. The API is `POST` on `/calculate`.

## Testing

Tests are in /app/test.py

## Notes

This was my first time using Docker or building an API in Python (I used to build APIs in Node.js). I hope I didn't do anything silly (naming convention wise).