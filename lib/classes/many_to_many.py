class Article:
    # Track all articles in a class variable
    all = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None

        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self) #It holds all created articles

    @property
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
        # Must be an Author
        if isinstance(value, Author):
            self._author = value
        else:
            # Invalid author, set a default only if none set
            if self._author is None:
                self._author = Author("Default Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Must be a Magazine
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            # Invalid magazine, set a default only if none set
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
        # Name: str, >0 chars, cannot change after set
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
        # If no topic areas, return None instead of empty list
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
        # Name: str, length 2-16, can change if valid
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            # Invalid name assignment
            if self._name is None:
                self._name = "DefaultName"
            # If not None, ignore invalid changes

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # Category: non-empty str, can change if valid
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value
        else:
            # Invalid category assignment
            if self._category is None:
                self._category = "DefaultCat"
            # If not None, ignore invalid changes

    def articles(self):
        arts = [article for article in Article.all if article.magazine == self]
        return arts

    def contributors(self):
        authors = {article.author for article in Article.all if article.magazine == self}
        return list(authors)

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        # Return None if no titles
        if len(titles) == 0:
            return None
        return titles

    def contributing_authors(self):
        articles_for_mag = [article for article in Article.all if article.magazine == self]
        author_count = {}
        for article in articles_for_mag:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        # More than 2 articles means count > 2
        result = [author for author, count in author_count.items() if count > 2]
        # If no contributing authors with more than 2 articles, return None
        if len(result) == 0:
            return None
        return result


# Create authors
author1 = Author("Bob Marley")
author2 = Author("Thomas Shelby")

# Create magazines
mag1 = Magazine("Tech Weekly", "Technology")
mag2 = Magazine("Health Today", "Health")

# Create articles
article1 = author1.add_article(mag1, "The Rise of Cats")
article2 = author1.add_article(mag2, "Healthy Living Tips")
article3 = author2.add_article(mag1, "Quantum Computing")
article4 = author2.add_article(mag1, "The Future of VR")

# Displaying the some information
print(f"Author1 articles: {[article.title for article in author1.articles()]}")
print(f"Mag1 contributors: {[author.name for author in mag1.contributors()]}")
print(f"Mag1 article titles: {mag1.article_titles()}")
print(f"Author1 magazines: {[mag.name for mag in author1.magazines()]}")
print(f"Author2 topic areas: {author2.topic_areas()}")
print(f"Mag1 contributing authors (more than 2 articles): {mag1.contributing_authors()}")
