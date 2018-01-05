from . import session


class TV(object):
    def __init__(self, id_num):
        self.id = id_num

    def info(self):
        path = "https://api.themoviedb.org/3/tv/{}".format(self.id)
        res = session.get(path)
        print(res.json())
        return res.json()

    def credits(self):
        path = "https://api.themoviedb.org/3/tv/{}/credits".format(self.id)
        res = session.get(path)
        print(res.json())
        return res.json()