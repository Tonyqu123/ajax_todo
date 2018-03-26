from pymongo import MongoClient


Client = MongoClient()
db = Client.test


class Model(object):

    @classmethod
    def find(cls, **kwargs):
        d_list = []
        cls_name = cls.__name__
        result = db[cls_name].find(dict(kwargs))
        for o in result:
            o.pop('_id')
            d_list.append(o)
        return d_list

    def save(self):
        cls_name = self.__class__.__name__
        db[cls_name].insert_one(self.__dict__)

    def __repr__(self):
        cls_name = self.__class__.__name__
        info = self.__dict__
        return cls_name+'<'+str(info)+'>'

    def update(self, **kwargs):
        '''
        :param kwargs: {'x', 1} 把self.x 改为 1
        '''
        cls_name = self.__class__.__name__
        d = dict(kwargs)
        k, v = d.items()
        attr, value = k[0], v[0]
        v = getattr(self, attr)
        print(v)
        db[cls_name].update_one(
            {attr: v},
            {'$set': {attr: value}}
        )

    def to_json(self):
        j = self.__dict__.copy()
        return j

    @classmethod
    def all(cls):
        return cls.find()




class User(Model):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.password = kwargs.get('password')


class Todo(Model):

    def __init__(self, title):
        self.title = title

    def to_json(self):
        return self.__dict__.copy()


# print(list(db.User.find()))