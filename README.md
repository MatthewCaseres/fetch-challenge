# fetch-challenge
 
## Building

Go to the project directory containing the Dockerfile and the app folder and build the image.

```
docker build -t fetch .
```

You then run the container

```
docker run -d -p 80:80 fetch
```

## Using the API

The web server should start and be running and you can use the API that is appropriate for your docker host. I go to http://127.0.0.1/docs and use the swagger UI to test the API. The API is `POST` on `/calculate`.

## Testing

Testing is done in Pytest. When you are in the docker container run `pytest`.

## Development

I am using the `remote-containers` extension for Visual Studio Code.

## Notes

This was my first time *seriously* using Docker. I have it installed and have started it up before, but Poetry has always been how I manage dependencies for personal projects. I've built APIs in Node.js but Python was new, thankfully the fastAPI docs are great. Here are some resources I relied on:

* https://fastapi.tiangolo.com/tutorial/testing/
* https://fastapi.tiangolo.com/deployment/docker/