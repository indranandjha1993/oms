# Dockerizing Django with Postgres, Gunicorn, and Nginx

## Manual
### Create a virtual environment to isolate our package dependencies locally

1. Create virtual environment
`$ python3 -m venv tutorial-env
`
2. Activate virtual environment
` $ source tutorial-env/bin/activate
`
3. Clone repo
`$ git clone git@github.com:indranandjha1993/oms.git
`
4. Install dependencies
`sh
$ pip install -r requirements.txt
`

Test it out at [http://localhost:8000](http://localhost:8000).

## Development

### Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

## Production

###Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
