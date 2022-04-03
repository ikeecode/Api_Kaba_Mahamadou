import sys
sys.path.insert(0, '../models/')


from models import Model



class Controller:
    preparer = {
        'users': Model.prepare_users,
        'todos': Model.prepare_todos,
        'posts': Model.prepare_posts,
        'comments': Model.prepare_comments,
        'albums': Model.prepare_albums,
        'photos': Model.prepare_photos,
        'all': [Model.prepare_users, Model.prepare_todos,
                Model.prepare_posts, Model.prepare_comments,
                Model.prepare_albums, Model.prepare_photos]
    }
    retriever = {
        'users': Model.retrieve_users,
        'todos': Model.retrieve_todos,
        'posts': Model.retrieve_posts,
        'comments': Model.retrieve_comments,
        'albums': Model.retrieve_albums,
        'photos': Model.retrieve_photos,
        'all': [Model.retrieve_users, Model.retrieve_todos,
                Model.retrieve_posts, Model.retrieve_comments,
                Model.retrieve_albums, Model.retrieve_photos]
    }

    @classmethod
    def prepare_model(cls, class_):
        if class_ == 'all':
            for prep in cls.preparer.get(class_):
                prep()
        else:
            cls.preparer.get(class_)()


    @classmethod
    def retrieve_model(cls, class_):
        if class_ == 'all':
            for ret in cls.retriever.get(class_):
                ret()
        else:
            cls.retriever.get(class_)()
