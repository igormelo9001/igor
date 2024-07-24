import os
import json

class IgorDB:
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def _get_collection_path(self, collection_name):
        return os.path.join(self.data_dir, f'{collection_name}.json')

    def create_collection(self, collection_name):
        path = self._get_collection_path(collection_name)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump([], f)
            return True
        return False

    def insert_document(self, collection_name, document):
        path = self._get_collection_path(collection_name)
        if os.path.exists(path):
            with open(path, 'r+') as f:
                data = json.load(f)
                data.append(document)
                f.seek(0)
                json.dump(data, f, indent=4)
            return True
        return False

    def find_documents(self, collection_name, query):
        path = self._get_collection_path(collection_name)
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = json.load(f)
                return [doc for doc in data if all(item in doc.items() for item in query.items())]
        return []

    def list_collections(self):
        return [f.replace('.json', '') for f in os.listdir(self.data_dir) if f.endswith('.json')]

def update_document(collection_name, query, update):
    db = IgorDB()
    path = db._get_collection_path(collection_name)
    with open(path, 'r') as f:
        data = json.load(f)
    for doc in data:
        if all(doc.get(k) == v for k, v in query.items()):
            doc.update(update)
    with open(path, 'w') as f:
        json.dump(data, f)
    return {"message": "Document updated successfully"}

def delete_document(collection_name, query):
    db = IgorDB()
    path = db._get_collection_path(collection_name)
    with open(path, 'r') as f:
        data = json.load(f)
    data = [doc for doc in data if not all(doc.get(k) == v for k, v in query.items())]
    with open(path, 'w') as f:
        json.dump(data, f)
    return {"message": "Document deleted successfully"}

def delete_all_documents(collection_name):
    db = IgorDB()
    path = db._get_collection_path(collection_name)
    with open(path, 'w') as f:
        json.dump([], f)