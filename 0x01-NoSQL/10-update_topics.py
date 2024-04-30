#!/usr/bin/env python3
"""
Module to update topics in school documents.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the school name.

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics (list of str): list of topics approached in the school

    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
