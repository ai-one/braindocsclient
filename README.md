# braindocsClient

The goal of the braindocsClient is to provide a utility for BrainDocs users to interact with the BrainDocs API.

## Core Features:
* Get Analysis Results from BrainDocs (via API) and insert into MySQL Database
* Select TextUnits from MySQL Database and push to BrainDocs (via API)

## Additional Suggested Requirements
* Upon initial setup, offers to create tables in MySQL Database to store BrainDocs results
* Stores login information so users do not need to re-insert upon every launch of application
* Packaged as an EXE (py2exe for Windows, py2app for Mac) so users do not need to install Python on their machine