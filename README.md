# KSI dashboard

<https://ksi.fi.muni.cz/monitor>

## Software needed

 * Python 3.5
 * virtualenv
 * packages from `requirements.txt`

## Installation

 1. Clone this repository.
 2. Install virtualenv & packages into `ksi-py3-venv` directory.
    ```
    virtualenv -p python3 ksi-py3-venv
    source ksi-py3-venv/bin/activate
    pip3 install -r requirements.txt
    ```
 3. Enter db url into `config.py` file. Format:
    ```
    SQL_ALCHEMY_URI = 'mysql://username:password@server/db_name?charset=utf8mb4'
    ```

## Serve static files

You can make static html files and then serve them via web server:
```
$ make all
```

## Edit files

You can run jupyter notebook and edit all the files:
```
$ jupyter notebook
```
