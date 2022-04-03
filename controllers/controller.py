import sys
sys.path.insert(0, '../models/')


from models import Model



class Controller:
    preparer = {
        'users': Model.prepare_users,
        'todos': Model.prepare_todos,
        'posts': Model.prepare_posts,
        'comments': Model.prepare_comments,
        'album': Model.prepare_albums,
        'photos': Model.prepare_photos
    }
    retriever = {
        'users': Model.retrieve_users,
        'todos': Model.retrieve_todos,
        'posts': Model.retrieve_posts,
        'comments': Model.retrieve_comments,
        'album': Model.retrieve_albums,
        'photos': Model.retrieve_photos
    }

    @classmethod
    def prepare_model(cls, class_):
        cls.preparer.get(class_)()


    @classmethod
    def retrieve_model(cls, class_):
        cls.retriever.get(class_)()
