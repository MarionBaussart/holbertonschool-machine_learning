#!/usr/bin/env python3
"""
module containing function insert_school
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a collection based on kwargs
    Return:
        the new _id
    """
    new_id = mongo_collection.insert_one(kwargs).inserted_id
    
    # for key, value in kwargs:
    #     value = kwargs[key]
    #     new_id = mongo_collection.insert_one({key:value}).inserted_id

    return new_id
