# pyCDG

Coding Data Gatherer (CDG) aims to **store data** regarding the effort of a developers team when 
working on softwares projects to **generate views** to make easy to follow-up the progress.

# Requirements
* [Pipenv](https://pipenv.kennethreitz.org/en/latest/)
* [Yarn](https://classic.yarnpkg.com/en/docs/install)

# Environment Setup

```shell script
# Install dependencies
pipenv install

cd frontend
yarn install
```

# Run with hot-reloads for development
```shell script
# Run Django back-end
pipenv shell
python manage.py runserver 8080

# Run Vue front-end
cd frontend
./node_modules/.bin/vue serve src/main.js
```