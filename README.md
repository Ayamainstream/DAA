# SQLAlchemy Authorization
This project is example of using authorization and verifying tokens.
If you authenticate correctly, you will get token. Provide this token to path in order to get access to restricted data.

### Group Aiya Zeinulla, Kaiyrkeldi Kabken, Nurtileu Shaizolla (WE ALL FROM SE-2008) 
## Installation
### Install Flask, SQLAlchemy, JWT 
```
pip install flask, pyjwt, Flask-SQLAlchemy
```
Change path in test.py file to path where project located on your system

```python
sys.path.insert(0,'YOUR_PATH')

```

Create table in PostgreSQL by using SQL dump file that locates in this repository
Change URI password, username and database name in code
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://YOUR_USERNAME:DATABSE_PASSWORD@localhost/DATABASE_NAME'
```
## Usage
```python
from src import db
db.start()
```
## Example
Input correct password and login
![image](https://user-images.githubusercontent.com/82699886/138740304-90c66916-276e-4003-a197-508780e85892.png)

After that you get token
![image](https://user-images.githubusercontent.com/82699886/138740143-52c0947c-4b60-4d53-9c35-015a1b9d22a7.png)

Provide token that you recieve after succesfull authentication to path like that: 
![image](https://user-images.githubusercontent.com/82699886/138740113-4bf35bf2-06ad-4bab-9d46-017a75cb9bc1.png)
```
http://127.0.0.1:5000/protected?token= YOUR TOKEN HERE
```
    
    
    
    
If you provide wrong password or login
![image](https://user-images.githubusercontent.com/82699886/138740591-7f08ef0d-7aee-4936-b983-d8d5c306c65b.png)

Then you get html text about it
![image](https://user-images.githubusercontent.com/82699886/138740631-32c662c6-4679-470d-b502-16b6e410c7b2.png)


## License

[MIT](https://choosealicense.com/licenses/mit/)
