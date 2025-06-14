#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB.
Database: logs
Collection: nginx
"""

from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total = collection.count_documents({})
    print(f"{total} logs")

    # HTTP methods counts
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Count of GET /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
