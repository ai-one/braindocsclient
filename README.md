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

## Scripts

### `braindocs2database`

__Core Features:__
* Get Analysis Results from BrainDocs (via API) and insert into MySQL Database
* Upon initial setup, creates tables in MySQL Database to store BrainDocs results

__Usage__:

After installation the command can be run in a terminal window:

```
$ braindocs2database
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

It displays the current settings and asks the user if he wants to update the configuration. 

__Local Export__

Per default `braindocs2database` exports the data into a local [SQLite](https://www.sqlite.org/) database.

__MySQL Export__

To export into a [MySQL](https://www.mysql.com/), the `DATABASE -> url` option needs to be changed from `sqlite:///braindocs_export.db` to e.g.:

```
mysql://root@localhost/braindocs
```

Make sure that the appropriate Python extension for MySQL is installed. This can be done via:

```
pip install mysql-python
```

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
