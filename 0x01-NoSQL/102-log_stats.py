#!/usr/bin/env python3
"""
Python script that provides enhanced stats
about Nginx logs stored in MongoDB, including top 10 IPs.
"""

import pymongo

def get_top_ips(collection, limit=10):
    """ Retrieve top IPs using aggregation. """
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": limit}
    ]
    return list(collection.aggregate(pipeline))

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    col = db.nginx

    print(f"{col.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: {col.count_documents({'method': method})}")

    status_checks = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")
    
    top_ips = get_top_ips(col)
    print("IPs:")
    for entry in top_ips:
        print(f"\t{entry['_id']}: {entry['count']}")
