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


# GET Request

1 Search by Title :
[http://127.0.0.1:5000/posts/searchbytitle/jaack](http://127.0.0.1:5000/posts/searchbytitle/jack)

2 Search by Author:
[http://127.0.0.1:5000/posts/Searchbyauthor/Joe](http://127.0.0.1:5000/posts/Searchbyauthor/Joe)

3 Search By Tags:
[http://127.0.0.1:5000/posts/searchbyTags/Test](http://127.0.0.1:5000/posts/searchbyTags/Test)

4 Search By Tags:
[http://127.0.0.1:5000/posts/searchbybody/Its a movie show](http://127.0.0.1:5000/posts/searchbybody/Its%20a%20movie%20show)

5 Get all Posts at :
[http://127.0.0.1:5000/post/all](http://127.0.0.1:5000/post/all)


# Post Request

1 Register a user:
[http://127.0.0.1:5000/Registeruser](http://127.0.0.1:5000/Registeruser)

2 Adding a Post use Authorization:
[http://127.0.0.1:5000/user/post/addpost](http://127.0.0.1:5000/user/post/addpost)


# Update Request

1 Update a Post using post id use Authorization:
[http://127.0.0.1:5000/user/post/6](http://127.0.0.1:5000/user/post/6)

2 Upload a file to a Post using id  use Authorization:
[http://127.0.0.1:5000/post/upload/document/2](http://127.0.0.1:5000/post/upload/document/2)

# Download a Pdf file that was in the post
1 Download a file :
[http://localhost:5000/user/post/download/web_scrap_1624708822.pdf](http://localhost:5000/user/post/download/web_scrap_1624708822.pdf)



# Delete Request

1 Delete a Post use Authorization
[http://127.0.0.1:5000/post/delete/2](http://127.0.0.1:5000/post/delete/2)

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


