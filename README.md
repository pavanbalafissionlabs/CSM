# Content Management System(CSM)

Content Management System is similar to Blog Application but only with Backend.

#### Create vertiual Environoment

```python
python -m venv csm_env
```

#### Activate vertiual Environoment

```bash
csm_env\scripts\activate
```
### install  required modules  

```bash
pip install -r requirements.txt
```

### Change to Directory

```bash
cd Context_system_Manager Api
```
### Execute in Terminal 
```bash
python
```
# Creating DataBase
```bash
from API import db
```

```bash
db.create_all()
```
### Run Application
```bash
python run.py
```

# Search  
[http://localhost:5000/search](http://localhost:5000/search)


# Get all content 
[http://localhost:5000/content](http://localhost:5000/content)



# Register a user
[http://localhost:5000/Register](http://localhost:5000/Register)

# Add a Post use Authorization
[http://localhost:5000/addcontent](http://localhost:5000/addcontent)




#  Update a Post using post id use Authorization
[http://localhost:5000/content/8](http://localhost:5000/content/8)

# Upload a file to a Post using id  use Authorization
[http://localhost:5000/uploadDocument/7](http://localhost:5000/uploadDocument/7)


# Download a file 
[localhost:5000/user/post/download/Vue.js-Assignment_1.pdf](localhost:5000/user/post/download/Vue.js-Assignment_1.pdf)





# Delete a Post use Authorization
[http://localhost:5000/delete/2](http://localhost:5000/delete/2)

# Register Schema 

```Json
{
"email":"email",
"password":"password",
"Fullname":"Fullname",
"Address":"Address",
"city":"city",
"State":"State",
"Country":"Country",
"Phone":Phone,
"Pincode":Pincode
}
```



# Post Schema 

```Json
{
"Title":"Title",
"Body":"Body",
"Summary":"Summary",
"PostTags":"PostTags",
"Filename":"Filename"

}
```
# File schema


```Json
 {
'File':'type pdf'
}
```

