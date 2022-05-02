class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def __find_topic_by_id(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic

    def __find_category_by_id(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category

    def __find_document_by_id(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def edit_category(self, category_id, new_name):
        category = self.__find_category_by_id(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        category = self.__find_topic_by_id(topic_id)
        category.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_name):
        category = self.__find_document_by_id(document_id)
        category.edit(new_name)

    def delete_category(self, category_id):
        category = self.__find_category_by_id(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_topic_by_id(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_document_by_id(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__find_document_by_id(document_id)
        return document

    def __repr__(self):
        result = ''
        for doc in self.documents:
            result += str(doc) + '\n'
        return result
