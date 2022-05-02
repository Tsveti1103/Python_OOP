from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(pages)

    def __init_photos(self, pages):
        return [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE))

    def add_photo(self, label):
        for i, pgs in enumerate(self.photos):
            if len(pgs) < PhotoAlbum.PHOTOS_PER_PAGE:
                pgs.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(pgs)}"
        return "No more free slots"

    def display(self):
        row = '-' * 11
        result = row + '\n'
        for page in self.photos:
            result += ' '.join(['[]' for _ in page]) + '\n' + row + '\n'
        return result

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
