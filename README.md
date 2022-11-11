# URL Shortner

## Features

*  FastAPI
*  Pydantic
*  SQLALCHEMY
*  Swagger

## Installation

1. Clone this repository
2. Create a virtual environment

    ```
    python -m venv env
    ```

3. Activate virtual environment in parent directory of your "env"

    For Linux and MAC

    ```
    source env/bin/activate
    ```

    For Windows

    ```
    env\Scripts\activate.bat
    ```

4. Install the requirements

    ```
    nstall -r requirements.txt
    ```

5. Create an environment variables. create a ***.env*** file. The File should have the following environment variables

    ```
    PROJECT_NAME=
    CONTACT_NAME=
    CONTACT_EMAIL=
    BASE_URL=
    DB_URL=sqlite:///./urlshortner.db
    ```

6. To run the code
    ```
    uvicorn main:app --reload
    ```

7. Open Browser and view the swagger docs

    ![alt text](shortner.png)

    To Create a url shortner, make a post request on ***/urls***