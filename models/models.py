from users import User
from users import Address
from users import Company
from todos import Todo
from posts import Post
from comments import Comment
from albums import Album
from photos import Photo
from json import dumps
import mysql.connector as mc
import requests

credentials = '/home/kaba/Bureau/projet-mvc/models/my.ini'

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
        cls.mydb = mc.connect(option_files=credentials)
        cls.mycursor = cls.mydb.cursor()

        return cls.mycursor

    @classmethod
    def close_db(cls):
        cls.mydb.commit()
        cls.mydb.close()

    @classmethod
    def retrieve_from(cls, my_class):
        mycursor = cls.init_db()
        mycursor.execute(my_class.select())
        result = mycursor.fetchall()
        for res in result:
            print(res)
        print()

    @classmethod
    def retrieve_users(cls):
        cls.retrieve_from(User)

    @classmethod
    def retrieve_todos(cls):
        cls.retrieve_from(Todo)


    @classmethod
    def retrieve_albums(cls):
        cls.retrieve_from(Album)

    @classmethod
    def retrieve_photos(cls):
        cls.retrieve_from(Photo)


    @classmethod
    def retrieve_posts(cls):
        cls.retrieve_from(Post)



    @classmethod
    def retrieve_comments(cls):
        cls.retrieve_from(Comment)


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










# # this has to move to the controller
# Model.retrieve_users()
