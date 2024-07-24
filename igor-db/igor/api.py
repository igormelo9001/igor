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
    data = request.json
    collection_name = data.get('collection_name')
    query = data.get('query')
    update = data.get('update')
    if collection_name and query and update:
        success = db.update_document(collection_name, query, update)
        return jsonify({'success': success}), 200 if success else 400
    return jsonify({'error': 'Collection name, query, and update required'}), 400

@app.route('/delete_document', methods=['POST'])
def delete_document():
    data = request.json
    collection_name = data.get('collection_name')
    query = data.get('query')
    if collection_name and query:
        success = db.delete_document(collection_name, query)
        return jsonify({'success': success}), 200 if success else 400
    return jsonify({'error': 'Collection name and query required'}), 400

@app.route('/delete_all_documents', methods=['POST'])
def delete_all_documents():
    data = request.json
    collection_name = data.get('collection_name')
    if collection_name:
        success = db.delete_all_documents(collection_name)
        return jsonify({'success': success}), 200 if success else 400
    return jsonify({'error': 'Collection name required'}), 400

@app.route('/delete_collection', methods=['POST'])
def delete_collection():
    data = request.json
    collection_name = data.get('collection_name')
    if collection_name:
        success = db.delete_collection(collection_name)
        return jsonify({'success': success}), 200 if success else 400
    return jsonify({'error': 'Collection name required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
