#!/usr/bin/env python3
"""
Module to insert a document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs to insert as document fields

    Returns:
        The new document's _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
