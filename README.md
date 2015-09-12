# braindocsClient

The goal of the braindocsClient is to provide a utility for BrainDocs users to interact with the [BrainDocs API](https://ai-one.box.com/s/73fku761ffnekcwvb1pkl7rznqic0y6k).

Currently it contains one script `braindocs2datbase` that helps the user to export analysis results from BrainDocs into a datbase of their choice.

## Installation

The current version of braindocsClient can be installed by issuing the following command:

```bash
pip install git+https://github.com/ai-one/braindocsClient.git
````

To install a specific release or experimental branch, run:

```bash
pip install git+https://github.com/ai-one/braindocsClient-py.git@v1.0.0
```

## Scripts

### `braindocs2database`

__Core Features:__
* Get Analysis Results from BrainDocs (via API) and insert into MySQL Database
* Upon initial setup, creates tables in MySQL Database to store BrainDocs results

__ Additional Suggested Requirements__
* Packaged as an EXE (py2exe for Windows, py2app for Mac) so users do not need to install Python on their machine

### `database2braindocs` (not yet implemented)

__Core Features:__
* Select TextUnits from MySQL Database and push to BrainDocs (via API)
