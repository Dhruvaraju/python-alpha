- [Creating rest api with flask](#creating-rest-api-with-flask)
  - [Setting up environment](#setting-up-environment)
  - [Running code in docker without restarting](#running-code-in-docker-without-restarting)
  - [Initial endpoint](#initial-endpoint)


# Creating rest api with flask

## Setting up environment

- Create a folder and switch to it
- Create virtual environment with `python -m venv .venv`
- Add an interpreter from `ctrl+shift+p` or activate one with `.venv\Scripts\activate.bat`
- For windows `activate.bat`, for linux `activate.sh` or `activate`
- Add all required python packages in `requirements.txt` and install them with 

```sh
pip install -r requirements.txt
```
## Running code in docker without restarting

```sh
docker run -dp -w /app -v "location_of_current_code:/app" image_name
```

## Initial endpoint
- Create a method and return any value.
- `@app.get("/store")` add this to bind a uri to a method
- The return of the method will be sent as a response to this, endpoint.

