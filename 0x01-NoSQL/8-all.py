#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents found in the collection, or an empty list if no document.
    """
    return list(mongo_collection.find())
