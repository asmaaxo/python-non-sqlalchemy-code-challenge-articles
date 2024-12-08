class Article:
    # Empty array stores all articles in a class variable
    all = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None

        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    @property #Decorator- A function that modifies 
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Title: str, length 5-50, immutable once set
        if self._title is not None:
            # Title already set, do not change
            return
        # First time setting title
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            # Invalid initial title, set a default
            self._title = "Default Title"

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            if self._author is None:
                self._author = Author("Default Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            if self._magazine is None:
                self._magazine = Magazine("DefaultMag", "DefaultCat")


class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name is not None:
            return
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value
        else:
            self._name = "Default Author"

    def articles(self):
        result = [article for article in Article.all if article.author == self]
        return result

    def magazines(self):
        mags = {article.magazine for article in Article.all if article.author == self}
        mags_list = list(mags)
        return mags_list

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        mags = {article.magazine for article in Article.all if article.author == self}
        cats = {m.category for m in mags}
        cats_list = list(cats)
        if len(cats_list) == 0:
            return None
        return cats_list


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            if self._name is None:
                self._name = "DefaultName"

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value
        else:
            if self._category is None:
                self._category = "DefaultCat"

    def articles(self):
        arts = [article for article in Article.all if article.magazine == self]
        return arts

    def contributors(self):
        authors = {article.author for article in Article.all if article.magazine == self}
        return list(authors)

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        if len(titles) == 0:
            return None
        return titles

    def contributing_authors(self):
        articles_for_mag = [article for article in Article.all if article.magazine == self]
        author_count = {}
        for article in articles_for_mag:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        result = [author for author, count in author_count.items() if count > 2]
        if len(result) == 0:
            return None
        return result
