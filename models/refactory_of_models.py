from users import User
from users import Address
from users import Company
from todos import Todo
from posts import Post
from comments import Comment
from albums import Album
from photos import Photo
from json import dumps
from time import sleep
import mysql.connector as mc
import requests


"""
    les methodes de classe prepare_* font des insertions dans la base de donnees

"""

class Model:
    # mydb = mc.connect(option_files='my.ini')
    # mycursor = mydb.cursor()
    api_url    = 'https://jsonplaceholder.typicode.com/'
    # users      = requests.get(api_url + 'users')   .json()
    # todos      = requests.get(api_url + 'todos')   .json()
    # posts      = requests.get(api_url + 'posts')   .json()
    # comments   = requests.get(api_url + 'comments').json()
    # albums     = requests.get(api_url + 'albums')  .json()
    # photos     = requests.get(api_url + 'photos')  .json()

    @classmethod
    def init_db(cls):
        cls.mydb = mc.connect(option_files='my.ini')
        cls.mycursor = cls.mydb.cursor()

        return cls.mycursor

    @classmethod
    def close_db(cls):
        cls.mydb.commit()
        cls.mydb.close()

    # this insert the users data in the database
    @classmethod
    def prepare_users(cls):
        mycursor = cls.init_db()
        users = requests.get(cls.api_url + 'users').json()
        for user in users:
            id        = user.get('id')
            name      = user.get('name')
            username  = user.get('username')
            email     = user.get('email')
            phone     = user.get('phone')
            website   = user.get('website')

            #  hanling the address
            address = user.get('address')
            street  = address.get('street')
            suite   = address.get('suite')
            city    = address.get('city')
            zipcode = address.get('zipcode')
            geo     = dumps(address.get('geo'))

            # create an Address object
            address_instance = Address(street, suite, city, zipcode, geo)
            mycursor.execute(address_instance.insert())

            # retrieve address identificator
            addressId = f"SELECT id FROM address WHERE suite = '{suite}'"
            mycursor.execute(addressId)
            addressId = mycursor.fetchone()[0]

            # handling the company
            company      = user.get('company')
            company_name = company.get('name')
            catchPhrase  = company.get('catchPhrase')
            bs           = company.get('bs')
            company_instance = Company(company_name, catchPhrase, bs)
            mycursor.execute(company_instance.insert())

            # retrieve company identificator
            companyId = f"SELECT id FROM company WHERE name = '{company_name}'"
            mycursor.execute(companyId)
            companyId = mycursor.fetchone()[0]

            # create user object
            user_instance = User(id, name, username, email, addressId, phone, website, companyId)
            mycursor.execute(user_instance.insert())
        cls.close_db()




    @classmethod
    def prepare_todos(cls):
        mycursor = cls.init_db()
        todos = requests.get(cls.api_url + 'todos').json()
        for todo in todos:
            userId      = todo.get('userId')
            id          = todo.get('id')
            title       = todo.get('title')
            completed   = todo.get('completed')

            # create a todo object
            todo_instance = Todo(userId, id, title, completed)
            mycursor.execute(todo_instance.insert())


    @classmethod
    def prepare_posts(cls):
        mycursor = cls.init_db()
        posts = requests.get(cls.api_url + 'posts').json()
        for post in posts:
            userId  = post.get('userId')
            id      = post.get('id')
            title   = post.get('title')
            body    = post.get('body')

            # create a post object
            post_instance = Post(userId, id, title, body)
            mycursor.execute(post_instance.insert())
        cls.close_db()



    @classmethod
    def prepare_comments(cls):
        mycursor = cls.init_db()
        comments   = requests.get(cls.api_url + 'comments').json()
        for comment in comments:
            postId    = comment.get('postId')
            id        = comment.get('id')
            name      = comment.get('name')
            email     = comment.get('email')
            body      = comment.get('body')

            # create a comment object
            comment_instance = Comment(postId, id, name, email, body)
            mycursor.execute(comment_instance.insert())
        cls.close_db()



    @classmethod
    def prepare_albums(cls):
        mycursor = cls.init_db()
        albums = requests.get(cls.api_url + 'albums').json()
        for album in albums:
            userId    = album.get('userId')
            id        = album.get('id')
            title     = album.get('title')

            # create an instance of album
            album_instance = Album(userId, id, title)
            mycursor.execute(album_instance.insert())
        cls.close_db()




    @classmethod
    def prepare_photos(cls):
        mycursor = cls.init_db()
        photos = requests.get(cls.api_url + 'photos').json()
        for photo in photos:
            albumId         = photo.get('albumId')
            id              = photo.get('id')
            title           = photo.get('title')
            url             = photo.get('url')
            thumbnailUrl    = photo.get('thumbnailUrl')

            # create a photo object
            photo_instance = Photo(albumId, id, title, url, thumbnailUrl)
            mycursor.execute(photo_instance.insert())
        cls.close_db()












# insertion des users
Model.prepare_users()

sleep(5)
# insertion des todos
Model.prepare_todos()

# insertion des posts
Model.prepare_posts()

# insertion des comments
Model.prepare_comments()

# insertion des albums
Model.prepare_albums()

# insertion des photos
Model.prepare_photos()




# old version of models.py
#
# from users import User
# from users import Address
# from users import Company
# from todos import Todo
# from posts import Post
# from comments import Comment
# from albums import Album
# from photos import Photo
# from json import dumps
# from time import sleep
# import mysql.connector as mc
# import requests
#
#
# """
#     les methodes de classe prepare_* font des insertions dans la base de donnees
#
# """
#
# class Model:
#     api_url    = 'https://jsonplaceholder.typicode.com/'
#     # users      = requests.get(api_url + 'users')   .json()
#     # todos      = requests.get(api_url + 'todos')   .json()
#     # posts      = requests.get(api_url + 'posts')   .json()
#     # comments   = requests.get(api_url + 'comments').json()
#     # albums     = requests.get(api_url + 'albums')  .json()
#     # photos     = requests.get(api_url + 'photos')  .json()
#
#
#     # this insert the users data in the database
#     @classmethod
#     def prepare_users(cls):
#         users = requests.get(cls.api_url + 'users').json()
#         with mc.connect(option_files='my.ini') as mydb:
#             mycursor = mydb.cursor()
#             for user in users:
#                 id        = user.get('id')
#                 name      = user.get('name')
#                 username  = user.get('username')
#                 email     = user.get('email')
#                 phone     = user.get('phone')
#                 website   = user.get('website')
#
#                 #  hanling the address
#                 address = user.get('address')
#                 street  = address.get('street')
#                 suite   = address.get('suite')
#                 city    = address.get('city')
#                 zipcode = address.get('zipcode')
#                 geo     = dumps(address.get('geo'))
#
#                 # create an Address object
#                 address_instance = Address(street, suite, city, zipcode, geo)
#                 mycursor.execute(address_instance.insert())
#
#                 # retrieve address identificator
#                 addressId = f"SELECT id FROM address WHERE suite = '{suite}'"
#                 mycursor.execute(addressId)
#                 addressId = mycursor.fetchone()[0]
#
#                 # handling the company
#                 company      = user.get('company')
#                 company_name = company.get('name')
#                 catchPhrase  = company.get('catchPhrase')
#                 bs           = company.get('bs')
#                 company_instance = Company(company_name, catchPhrase, bs)
#                 mycursor.execute(company_instance.insert())
#
#                 # retrieve company identificator
#                 companyId = f"SELECT id FROM company WHERE name = '{company_name}'"
#                 mycursor.execute(companyId)
#                 companyId = mycursor.fetchone()[0]
#
#                 # create user object
#                 user_instance = User(id, name, username, email, addressId, phone, website, companyId)
#                 mycursor.execute(user_instance.insert())
#
#             mydb.commit()
#
#
#
#     @classmethod
#     def prepare_todos(cls):
#         todos = requests.get(cls.api_url + 'todos').json()
#         with mc.connect(option_files='my.ini') as mydb:
#             mycursor = mydb.cursor()
#             for todo in todos:
#                 userId      = todo.get('userId')
#                 id          = todo.get('id')
#                 title       = todo.get('title')
#                 completed   = todo.get('completed')
#
#                 # create a todo object
#                 todo_instance = Todo(userId, id, title, completed)
#                 mycursor.execute(todo_instance.insert())
#             mydb.commit()
#
#     @classmethod
#     def prepare_posts(cls):
#         posts = requests.get(cls.api_url + 'posts').json()
#         with mc.connect(option_files='my.ini') as mydb:
#             mycursor = mydb.cursor()
#             for post in posts:
#                 userId  = post.get('userId')
#                 id      = post.get('id')
#                 title   = post.get('title')
#                 body    = post.get('body')
#
#                 # create a post object
#                 post_instance = Post(userId, id, title, body)
#                 mycursor.execute(post_instance.insert())
#             mydb.commit()
#
#     @classmethod
#     def prepare_comments(cls):
#         comments   = requests.get(cls.api_url + 'comments').json()
#         with mc.connect(option_files='my.ini') as mydb:
#             mycursor = mydb.cursor()
#             for comment in comments:
#                 postId    = comment.get('postId')
#                 id        = comment.get('id')
#                 name      = comment.get('name')
#                 email     = comment.get('email')
#                 body      = comment.get('body')
#
#                 # create a comment object
#                 comment_instance = Comment(postId, id, name, email, body)
#                 mycursor.execute(comment_instance.insert())
#             mydb.commit()
#
#     @classmethod
#     def prepare_albums(cls):
#         albums = requests.get(cls.api_url + 'albums').json()
#         with mc.connect(option_files='my.ini') as mydb:
#             mycursor = mydb.cursor()
#             for album in albums:
#                 userId    = album.get('userId')
#                 id        = album.get('id')
#                 title     = album.get('title')
#
#                 # create an instance of album
#                 album_instance = Album(userId, id, title)
#                 mycursor.execute(album_instance.insert())
#             mydb.commit()
#
#
#     @classmethod
#     def prepare_photos(cls):
#         photos = requests.get(cls.api_url + 'photos').json()
#         with mc.connect(option_files='my.ini') as mydb:
#             mycursor = mydb.cursor()
#             for photo in photos:
#                 albumId         = photo.get('albumId')
#                 id              = photo.get('id')
#                 title           = photo.get('title')
#                 url             = photo.get('url')
#                 thumbnailUrl    = photo.get('thumbnailUrl')
#
#                 # create a photo object
#                 photo_instance = Photo(albumId, id, title, url, thumbnailUrl)
#                 mycursor.execute(photo_instance.insert())
#                 # print(photo_instance.insert())
#             mydb.commit()
#
#
#
#
#
#
#
#
#
# #
# # # insertion des users
# # Model.prepare_users()
# #
# # # insertion des todos
# # Model.prepare_todos()
# #
# # # insertion des posts
# # Model.prepare_posts()
# #
# # # insertion des comments
# # Model.prepare_comments()
# #
# # # insertion des albums
# # Model.prepare_albums()
# #
# # # insertion des photos
# # Model.prepare_photos()
