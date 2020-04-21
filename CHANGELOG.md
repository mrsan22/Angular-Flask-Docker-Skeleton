## Angular-Flask-Docker v2.0.2 - 04/20/2020

### Improvements:
* Upgraded Python packages version.

### Bug Fix:
* Fixed typo in requirements.txt file


## Angular-Flask-Docker v2.0.1 - 06/15/2018
### New Features:
* Added `Service` based architecture that encapsulates common SQLAlchemy operations and exposes
API that interacts with the model. This way our `routes` functions becomes more concise and clear
with just a call to respective Service API. This can be found under `services` directory.

### Bug Fix:
* Added `as_dict` method under models BaseModel class to convert the Model object into dict.
Fixed `__repr__` for the same.

### Improvements:
* Created a new `user` blueprint with user related routes and a new user_service file.

## Angular-Flask-Docker v2.0.0 - 06/08/2018
### New Features:

* Added `Blueprint` support for handling api routes.
* Added `application factory` pattern to create Flask app.
* Added `UnitTests` support to the seed project with few sample tests.
* Usage of `.env` to set the environment variables.
* Added sample code on Client side (Angular) to get the data from Flask backend.

### Improvements:
* Improved server side application structure to support different environment configs and large
scale application structure.
* Complete `PostgreSQL` database support with sample table, db model and dummy data. An `init.sql`
script to create a db on container initialization.

## Angular-Flask-Docker v1.0.1 - 06/02/2018

### New Features:
* Added `PostgreSQL` database support to the seed project.

### Improvements:
* Updated Angular and RxJs to v6.

## Angular-Flask-Docker v1.0.0 - 09/07/2017

### New Features:
* Released Angular, Flask and Docker Skeleton project.
