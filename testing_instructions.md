## Basic testing instructions

#### dependencies
- `docker` for running and debugging an image of the server locally
- `docker-compose` to configure the image
- `python` and `pip` to interface with some of django's features
- (optional) `django-admin` to easially instantiate new apps if you'd like to implement anything else  

#### Running the server
First open up a terminal and run `dockerd` to start the daemon docker will connect to.
Then `cd` to the root directory, and run `docker-compose -f "docker/docker-compose.yml" up` to start a local version of the server. You can then connect to `localhost` and Mayan should be up and running. 

All the relevant info for docker-compose file should work fine, but feel free to email me (wrinkoff@andrew.cmu.edu) if you run into any difficult errors.

**NOTE: Keep an eye on the output of `docker-compose`**
If can't connect to localhost, chances are there's some compilation error that can't be resolved. The mayan server will either continuously try to reboot itself (failing each time), or it will simply shut down.
Either way, a backtrace is usually provided to fix the issue, or at least get it to compile.

#### Working with django locally
The `django` framework has a number of database management tools that require some local installations.
At the project's root directory, run `pip install -r requirements.txt` to install django and its dependencies. This allows you to run `python manage.py`, a small script built to manage/migrate databases django is using.

##### Running the documentation server
Mayan-EDMS has a documentation site, a local version of which can be compiled by running `make docs-html` from the root directory.

##### Testing site features
The page for managing reviewers and candidates is `http://localhost/#/home/candidates/candidates`.
If everything compiles, you should see a basic interface.
Otherwise, you'll see an ugly error message sprawled out on the screen. If a line number is referenced, it's an error with the python code. If there's no line number it's most likely a sql database issue.


