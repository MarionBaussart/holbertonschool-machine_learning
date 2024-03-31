#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    nb_documents = collection.estimated_document_count()
    print("{} logs".format(nb_documents))

    nb_docs_get = collection.count_documents({"method": "GET"})
    nb_docs_post = collection.count_documents({"method": "POST"})
    nb_docs_put = collection.count_documents({"method": "PUT"})
    nb_docs_patch = collection.count_documents({"method": "PATCH"})
    nb_docs_delete = collection.count_documents({"method": "DELETE"})
    print("Methods:")
    print("\tmethod GET: {}".format(nb_docs_get))
    print("\tmethod POST: {}".format(nb_docs_post))
    print("\tmethod PUT: {}".format(nb_docs_put))
    print("\tmethod PATCH: {}".format(nb_docs_patch))
    print("\tmethod DELETE: {}".format(nb_docs_delete))

    nb_docs_get_status = collection.count_documents(
        {"method": "GET",
         "path": "/status"})
    print("{} status check".format(nb_docs_get_status))
