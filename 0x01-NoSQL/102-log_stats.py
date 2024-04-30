#!/usr/bin/env python3
"""
Python script for logging statistics with IP count.
"""

import pymongo

def log_stats():
    """
    Prints log stats and top 10 most present IPs.
    """
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print(f"    method {method}: {collection.count_documents({'method': method})}")

    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})} status check")

    # Top 10 IPs
    ip_counts = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in ip_counts:
        print(f"    {ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
