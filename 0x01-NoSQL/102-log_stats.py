#!/usr/bin/env python3
"""
Advanced logging stats script for nginx logs.
"""

from pymongo import MongoClient

def log_stats():
    """ Function to print logs statistics including top 10 IPs. """
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client.logs
    nginx_collection = db.nginx
    
    # Total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # HTTP methods
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"    method {method}: {count}")
    
    # Status checks
    status_check = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check} status check")
    
    # Top 10 IPs
    top_ips = nginx_collection.aggregate([
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ])
    
    print("IPs:")
    for ip in top_ips:
        print(f"    {ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
