from flask import Flask, request, jsonify
from igor.database import IgorDB

app = Flask(__name__)
db = IgorDB()

@app.route('/create_collection', methods=['POST'])
def create_collection():
    data = request.json
    collection_name = data.get('collection_name')
    if collection_name:
        success = db.create_collection(collection_name)
        return jsonify({'success': success}), 201 if success else 400
    return jsonify({'error': 'Collection name required'}), 400

@app.route('/insert_document', methods=['POST'])
def insert_document():
    data = request.json
    collection_name = data.get('collection_name')
    document = data.get('document')
    if collection_name and document:
        success = db.insert_document(collection_name, document)
        return jsonify({'success': success}), 201 if success else 400
    return jsonify({'error': 'Collection name and document required'}), 400

@app.route('/find_documents', methods=['POST'])
def find_documents():
    data = request.json
    collection_name = data.get('collection_name')
    query = data.get('query')
    if collection_name and query:
        results = db.find_documents(collection_name, query)
        return jsonify({'results': results}), 200
    return jsonify({'error': 'Collection name and query required'}), 400

@app.route('/list_collections', methods=['GET'])
def list_collections():
    collections = db.list_collections()
    return jsonify({'collections': collections}), 200

@app.route('/update_document', methods=['POST'])
def update_document():
    collection_name = request.json.get('collection_name')
    query = request.json.get('query')
    update = request.json.get('update')
    path = get_collection_path(collection_name)
    with open(path, 'r') as f:
        data = json.load(f)
    for doc in data:
        if all(doc.get(k) == v for k, v in query.items()):
            doc.update(update)
    with open(path, 'w') as f:
        json.dump(data, f)
    return jsonify({"message": "Document updated successfully"})

@app.route('/delete_document', methods=['POST'])
def delete_document():
    collection_name = request.json.get('collection_name')
    query = request.json.get('query')
    path = get_collection_path(collection_name)
    with open(path, 'r') as f:
        data = json.load(f)
    data = [doc for doc in data if not all(doc.get(k) == v for k, v in query.items())]
    with open(path, 'w') as f:
        json.dump(data, f)
    return jsonify({"message": "Document deleted successfully"})

@app.route('/delete_all_documents', methods=['POST'])
def delete_all_documents():
    collection_name = request.json.get('collection_name')
    path = get_collection_path(collection_name)
    with open(path, 'w') as f:
        f.write('[]')
    return jsonify({"message": "All documents deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
