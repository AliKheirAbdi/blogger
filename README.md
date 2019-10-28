# Project
A personal blogging website where you can create and share your opinions and other users can read and comment on them. 

## Author
[Ali Kheir](https://github.com/AliKheirAbdi)

## Author Contact details
* Email: akheirali(@)gmail.com


## Project Description
A Flask application for a personal blogging website where you can create and share your opinions and other users can read and comment on them.
## Screenshot
![image](https://github.com/AliKheirAbdi/blogger/blob/master/screen.png)

## Set up instructions
1. You need to have python3.7 installed, venv and pip
2. Set up the virtual environment and activate it.

    
    $ python3.7 -m venv virtual


    $ source virtual/bin/activate


3. Install all modules required

    $ pip install flask


    $ pip install flask-bootstrap


    $ pip install flask-script

4. Create an instance folder ```mkdir instance``` in the root directory and navigate to it ```cd instance```
5. Create a config.py file in the instance folder ```touch config.py```
6.Run manage.py to Launch in the server to view the application

## Development
Want to contribute? Great!
* Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above)
```https://github.com/AliKheirAbdi/pitchit.git```
* Create a new branch ```git branch contributions```
* Edit your changes in your branch
* Run the application

### Known bugs
The comment box is not working.
User welcome email not set up

## Technologies used
Python3.7
Bootstrap

## BDD
| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Click Register      | Fill out the reg form | user is created |
| Click Login     | Enter username and pwd   | Application logs user in |
| Submit Article| User fills out the form and submits | The new blog post is posted|
| Delete Article| Modal popup with the delete button | The new post is deleted| Deleted from site
| Click Account| User bio is populated | User can edit their username, pwd and photo|




# License
MIT license
