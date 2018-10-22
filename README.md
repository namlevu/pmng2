Product manager application

1.  System requirement
    Python 3.6.4
    Mongo DB 3.6

2.  How to run

-   install requirement python package by command
    `pip install -r requirements.txt`
-   run command
    `python server.py`

3.  API list

-   UserAPI

    [GET] api/users/
    [GET] api/users/(int:user_id)
    [POST] api/users
    [PUT] api/users
    [DELETE] api/users

99. Note
    _secret config in content_ `instance\config.py` is not controls by git.
    _start mongo in background_
    `sudo mongod --fork --logpath /var/log/mongod.log`
