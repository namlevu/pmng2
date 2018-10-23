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
    ```
    # instance/config.py
    SECRET_KEY = 'your_secret_key_string'    
    # local mongodb
    #MONGODB_SETTINGS_DB = 'localhost:27017'
    # mongodb driver 3.4
    # remote mongodb
    MONGODB_SETTINGS = {
        'db': 'test',
        'host': 'mongodb://<username>:<password>@clusterx-shard-00-00-gpfx1.mongodb.net:27017,clusterx-shard-00-01-gpfx1.mongodb.net:27017,clusterx-shard-00-02-gpfx1.mongodb.net:27017/test?ssl=true&replicaSet=ClusterX-shard-0&authSource=xxx&retryWrites=true'
    }
    ```
    _start mongo in background_
    `sudo mongod --fork --logpath /var/log/mongod.log`
