#!/usr/bin/env python3
"""
Python function for sorting students by average score.
"""

def top_students(mongo_collection):
    """
    Sorts students by average score in descending order.

    Args:
        mongo_collection: The collection object.

    Returns:
        List of sorted students with their average scores.
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
