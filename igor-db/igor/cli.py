import argparse
from database.py import IgorDB

def main():
    parser = argparse.ArgumentParser(description="IgorDB CLI")
    parser.add_argument('command', choices=['create_collection', 'insert_document', 'find_documents', 'list_collections'])
    parser.add_argument('--collection', help='Name of the collection')
    parser.add_argument('--document', help='Document to insert (as JSON string)')
    parser.add_argument('--query', help='Query to find documents (as JSON string)')

    args = parser.parse_args()

    db = IgorDB()

    if args.command == 'create_collection':
        if args.collection:
            success = db.create_collection(args.collection)
            if success:
                print(f'Collection {args.collection} created.')
            else:
                print(f'Collection {args.collection} already exists.')
        else:
            print('Please provide a collection name.')

    elif args.command == 'insert_document':
        if args.collection and args.document:
            document = json.loads(args.document)
            success = db.insert_document(args.collection, document)
            if success:
                print(f'Document inserted into {args.collection}.')
            else:
                print(f'Failed to insert document into {args.collection}.')
        else:
            print('Please provide a collection name and a document.')

    elif args.command == 'find_documents':
        if args.collection and args.query:
            query = json.loads(args.query)
            results = db.find_documents(args.collection, query)
            print(f'Found documents: {results}')
        else:
            print('Please provide a collection name and a query.')

    elif args.command == 'list_collections':
        collections = db.list_collections()
        print(f'Collections: {collections}')

if __name__ == '__main__':
    main()
