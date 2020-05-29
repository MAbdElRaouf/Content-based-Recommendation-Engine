# Simple Content-based Recommendation Engine API With Flask [Heroku Deployed]

> A simple content-based Netflix shows recommendation engine run as an API with Flask and deployed to Heroku.
> Medium article: https://medium.com/@MAbdElRaouf/simple-content-based-recommendation-engine-flask-api-heroku-dd27760dfe8e
# Installation
1. Create new folder named "Netflix Shows Recommendation API"
2. Open a new command (or Anaconda) prompt inside the folder, or point terminal directory to its path:

    ```sh
    cd /d <parent directory path>\Netflix Shows Recommendation API
    ```
3. Create a new Python virtual environment:

    ```sh
    virtualenv recommendation_api_env
    ```
4. Activate recommendation_api_env:
    ```sh
    recommendation_api_env\Scripts\activate
    ```
5. The packages required for this project are pandas, scikit-learn, flask and gunicorn. Run the following command to batch install them:
    ```sh
    pip install pandas sklearn flask gunicorn
    ```
6. After it has finished installing, save the project's list of packages to a text file with this command. Heroku uses this file as reference to what packages to install:
    ```sh
    pip freeze > requirements.txt
    ```
7. Install Heroku CLI:
    https://devcenter.heroku.com/articles/heroku-cli

8. Create Procfile for Heroku declaring gunicorn as the process type:
    ```sh
    echo web: gunicorn recommendation_api:app > Procfile
    ```



# Usage

- Run `shows_vectorizer.py` to generate a pickle file of TF-IDF vectorizer.

- Start the recommendation engine API locally by running `recommendation_api.py`.

- To run it on Heroku's cloud, see the setup instructions [here](https://medium.com/@MAbdElRaouf/simple-content-based-recommendation-engine-flask-api-heroku-dd27760dfe8e).

- Communicating with the API can be either through sending JSON POST requests to endpoint /api/ or interacting with the Swagger UI at endpoint /apidocs/
    - Example 1: POST request to https://netflix-recommendation-api.herokuapp.com/api with payload:
        ```
        {
        "title": "The Matrix"
        }
        ```
         is responded to with
         ```
         {
          "result": [
            {
              "title": "The Matrix Reloaded",
              "confidence": 0.4
            },
            {
              "title": "The Matrix Revolutions",
              "confidence": 0.3
            },
            {
              "title": "Jupiter Ascending",
              "confidence": 0.1
            },
            {
              "title": "Terminator 3: Rise of the Machines",
              "confidence": 0.1
            },
            {
              "title": "Sense8",
              "confidence": 0.1
            }
          ]
        }
         ```
     
     - Example 2: Using the user interface at https://netflix-recommendation-api.herokuapp.com/apidocs
         
# Built With
- Scikit-Learn
- Flask
- Flasgger
