# NoSQL Project: MongoDB Scripts

This repository contains a series of MongoDB and Python scripts designed to perform various operations on MongoDB databases. Each script has a specific function, ranging from listing databases to managing document data within collections.

## Repository Structure

- **GitHub Repository:** alx-backend-storage
- **Directory:** 0x01-NoSQL

## Scripts and Descriptions

### 0. List all databases
**File:** `0-list_databases`
- Lists all databases present in MongoDB.

### 1. Create a database
**File:** `1-use_or_create_database`
- Creates or switches to the database `my_db`.

### 2. Insert document
**File:** `2-insert`
- Inserts a document with the name "Holberton school" into the `school` collection.

### 3. All documents
**File:** `3-all`
- Lists all documents within the `school` collection.

### 4. All matches
**File:** `4-match`
- Lists all documents where name is "Holberton school" in the `school` collection.

### 5. Count
**File:** `5-count`
- Displays the number of documents in the `school` collection.

### 6. Update
**File:** `6-update`
- Updates documents, adding the address "972 Mission street" to those with the name "Holberton school".

### 7. Delete by match
**File:** `7-delete`
- Deletes all documents where the name is "Holberton school" from the `school` collection.

### 8. List all documents in Python
**File:** `8-all.py`
- A Python function that lists all documents in a specified collection.

### 9. Insert a document in Python
**File:** `9-insert_school.py`
- A Python function that inserts a new document into a collection based on given keyword arguments.

### 10. Change school topics
**File:** `10-update_topics.py`
- A Python function that updates the topics of a school document based on the school name.

### 11. Where can I learn Python?
**File:** `11-schools_by_topic.py`
- A Python function that returns a list of schools having a specific topic.

### 12. Log stats
**File:** `12-log_stats.py`
- A Python script that provides statistics about Nginx logs stored in MongoDB.

### 13. Regex filter
**File:** `100-find`
- Lists all documents with names starting with "Holberton" in the `school` collection.

### 14. Top students
**File:** `101-students.py`
- A Python function that returns all students sorted by average score.

### 15. Log stats - new version
**File:** `102-log_stats.py`
- Enhanced version of the log stats script that also lists the top 10 most present IPs.

## Usage

Each script can be run directly against a MongoDB database by following the instructions provided in the command line examples within this README. Python scripts require a running MongoDB instance and proper setup of the PyMongo library.

## Additional Information

For detailed usage of each script, refer to the specific MongoDB commands or Python functions defined within each file. Ensure MongoDB is installed and properly configured on your system to use these scripts.
