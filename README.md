# Project Horror Movies Statistics

### Description:

Horror Movies Statistics is a mini app for horror movies information analysis. This app uses csv file to get information and uses Pandas library to manipulate data.

### How to install a project:

Clone the repository and go to it on the command line:

```
git clone git@github.com:Starkiller2000Turbo/horror_movies_statistics.git
cd horror_movies_statistics
```

Create and activate a virtual environment for Windows:

```
python -m venv venv
source venv/Scripts/activate
```

For Linux:

```
python3 -m venv venv
source venv/bin/activate
```

Update pip:

```
make pip
```

Dependency files are separated according to the following purposes:

```
requirements.txt - requirements for running the backend basics of the application
make req

requirements-style.txt - requirements for styling code during development
make style-req

```

### Preparing data file:

To fill the system with data, you need to use a file with the csv extension.
It must be placed in the data folder.

```
cd data
```

The required file name is specified in the scripts/config.py file.

#### Horror movies file horror_movies.csv:

| id | original_title | title | original_language | overview | tagline | release_date | poster_path | popularity | vote_count | vote_average | budget | revenue | runtime | status | adult | backdrop_path | genre_names | collection | collection_name |
|----|----------------|-------|-------------------|----------|---------|--------------|-------------|------------|------------|-------------|--------|---------|---------|--------|-------|---------------|-------------|------------|-----------------|
|Integer|String |String |String | String | String | Date | String | Float | Integer | Float | Float | Integer |Integer | String |Boolean |String | String | Integer | String |

### How to run application:

Launch the application:

```
make run
```

Resilt data files will be awailable at app/data directory.

### Technology stack used in the project:

- Python
- Pandas

### Authors:

- :white_check_mark: [Maksim Ermoshin](https://github.com/Starkiller2000Turbo)
