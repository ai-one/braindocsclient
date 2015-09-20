# BraindocsClient

The goal of the BraindocsClient is to provide a utility for BrainDocs users to interact with the [BrainDocs API](https://ai-one.box.com/s/73fku761ffnekcwvb1pkl7rznqic0y6k).

Currently it contains `braindocsclient` library for talking to the BrainDocs API and the script `braindocs2database` that helps the user to export analysis results from BrainDocs into a database of their choice.

## Installation

The current version of BraindocsClient can be installed by issuing the following command:

```
$ pip install git+https://github.com/ai-one/braindocsclient.git
````

To install a specific release or experimental branch, run:

```
$ pip install git+https://github.com/ai-one/braindocsclient.git@v1.0.1
```

## Installation on Windows

__Requirements__

Before installing and running this utility, the user must have the following:

1. BrainDocs account, URL, Username and Password.
2. Install Python 2.7 – this can be found at www.python.org
3. Install DB Browser for SQLite – this can be found at www.sqlitebrowser.org
4. Setup a folder for the database files – for example on your Desktop C:\Users\[yourname]\Desktop\BD SQL Data

__Installation__

The current version of BraindocsClient can be found at https://github.com/ai-one/braindocsclient/releases

1. Download the Source code (zip) of the latest version.
2. Open the Command Prompt window.
3. Install the program, at the Command Prompt type:

```
C:\> pip install [location and name of the downloaded zip file]
```

For example: `C:\> pip install C:\Users\[yourname]\Downloads\braindocsclient-1.0.2.zip`.

## Scripts

### `braindocs2database`

__Core Features:__
* Get Analysis Results from BrainDocs (via API) and insert into MySQL Database
* Upon initial setup, creates tables in MySQL Database to store BrainDocs results

__Usage__:

After installation the command can be run in a terminal window.

Since all files (export data, settings, etc.) are stored in the current working directory, make sure to change directory to the location of your choice, e.g.:

```
$ cd C:\Users\[yourname]\Desktop\BD SQL Data
```

Then run `braindocs2database`:

```
$ braindocs2database
```

The response then should be:

```
braindocs2database
Copyright (c) 2015 ai-one inc. All rights reserved.

>>> Current settings:

BRAINDOCS
   username: bd_user
   password: bd_password
   url: https://nathandev2.cloudapp.net/at
DATABASE
   url: sqlite:///braindocs_export.db


Update settings? [no]?
```

It displays the current settings and asks the user if he wants to update the configuration. `no` is the default response as no settings will be changed.

* __First time__: User should enter [yes] and complete prompts for user’s BrainDocs Account including the username, password and url.
* __Warning__: User should note that the program will download all Analyses in the user account every time and overwrite the file. If the user wishes to preserve the previous version, the file name for the download should be changed here.
* __Additional BrainDocs account(s)__: If the user has additional accounts, the data can be downloaded by changing the username and password but we recommend changing the file name for each download here to avoid overwriting the db file from the other account(s). Alternatively the program could be executed from a different folder setup for that data.
* __Optionally - change target database:__
   * _Local Export_: Per default `braindocs2database` exports the data into a local [SQLite](https://www.sqlite.org/) database.
   * _MySQL Export_: To export into a [MySQL](https://www.mysql.com/), the `DATABASE -> url` option needs to be changed from `sqlite:///braindocs_export.db` to e.g. `mysql://root@localhost/braindocs`. Make sure that the appropriate Python extension for MySQL is installed. This can be done via: `$ pip install mysql-python`.

Once the user has completed any changes to the settings and verified the changes, [enter] at the Update settings? Prompt will run the program as in the example below.


If `no` (default option when hitting `Enter`), the program runs the export/import with the given settings:

```
Starting import...
importing analysis results: processed 1 of 11 ...
importing analysis results: processed 2 of 11 ...
importing analysis results: processed 3 of 11 ...
importing analysis results: processed 4 of 11 ...
importing analysis results: processed 5 of 11 ...
importing analysis results: processed 6 of 11 ...
importing analysis results: processed 7 of 11 ...
importing analysis results: processed 8 of 11 ...
importing analysis results: processed 9 of 11 ...
importing analysis results: processed 10 of 11 ...
importing analysis results: processed 11 of 11 ...
importing analysis results: done
```

__Additional Suggested Requirements:__
* Packaged as an EXE (py2exe for Windows, py2app for Mac) so users do not need to install Python on their machine

### `database2braindocs` (not yet implemented)

__Core Features:__
* Select TextUnits from MySQL Database and push to BrainDocs (via API)

## Library

The `braindocsclient.BraindocsApi` class facilitates the communication between a client and the analyst-toolbox's BrainDocs:

### `braindocsclient.BraindocsApi`

__`getAnalysisResults()`__

Retrieve JSON with all available analysis results.

__`getAnalysisDetailsTextUnits(analysisId)`__

Retrieve JSON with textunit scores for a specific analysis result.
