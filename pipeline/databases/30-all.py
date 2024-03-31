#!/usr/bin/env python3
"""
module containing function list_all
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    Return:
        list of documents
    """
    documents = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
