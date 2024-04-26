# 0x00-MySQL_Advanced

This repository contains SQL scripts for various advanced MySQL operations, including creating tables, triggers, indexes, functions, and stored procedures. Each script is designed to operate on a MySQL database configured for educational purposes.

## Tasks Overview

### 0. We are all unique!
- **File:** `0-uniq_users.sql`
- **Description:** Creates a `users` table with unique email addresses, preventing duplication and enforcing business rules.

### 1. In and not out
- **File:** `1-country_users.sql`
- **Description:** Extends the `users` table with a `country` attribute, using an ENUM type for specific country codes (US, CO, TN).

### 2. Best band ever!
- **File:** `2-fans.sql`
- **Description:** Calculates and lists the origin countries of bands ordered by the number of fans, using data imported from `metal_bands.sql.zip`.

### 3. Old school band
- **File:** `3-glam_rock.sql`
- **Description:** Lists all bands classified as "Glam rock" by their longevity using data from `metal_bands.sql.zip`.

### 4. Buy buy buy
- **File:** `4-store.sql`
- **Description:** Implements a trigger that automatically adjusts the item quantity in the `items` table upon adding a new order in the `orders` table.

### 5. Email validation to sent
- **File:** `5-valid_email.sql`
- **Description:** Creates a trigger that ensures the `valid_email` attribute in the `users` table is reset only when the email address is changed.

### 6. Add bonus
- **File:** `6-bonus.sql`
- **Description:** Introduces a stored procedure `AddBonus` to add or update project scores for students, including automatic project creation if not existing.

### 7. Average score
- **File:** `7-average_score.sql`
- **Description:** Defines a stored procedure `ComputeAverageScoreForUser` that calculates and updates the average score for a specified student.

### 8. Optimize simple search
- **File:** `8-index_my_names.sql`
- **Description:** Creates an index `idx_name_first` on the `names` table to improve search performance for queries based on the first letter of names.

### 9. Optimize search and score
- **File:** `9-index_name_score.sql`
- **Description:** Establishes a composite index `idx_name_first_score` on the `names` table to enhance query efficiency involving both the first letter of names and scores.

### 10. Safe divide
- **File:** `10-div.sql`
- **Description:** Provides a function `SafeDiv` that safely divides two numbers, returning 0 when the divisor is zero to prevent errors.

### 11. No table for a meeting
- **File:** `11-need_meeting.sql`
- **Description:** Creates a view `need_meeting` that lists students requiring meetings based on their scores and the last meeting date.

### 12. Average weighted score
- **File:** `100-average_weighted_score.sql`
- **Description:** Develops a stored procedure `ComputeAverageWeightedScoreForUser` that computes and stores a weighted average score for a student.

### 13. Average weighted score for all!
- **File:** `101-average_weighted_score.sql`
- **Description:** Introduces a stored procedure `ComputeAverageWeightedScoreForUsers` to calculate and update the weighted average scores for all students in the database.

## Usage

Each script is designed to be executed on a MySQL server. Ensure you have the correct permissions and the database is set up according to the initialization scripts provided with each task.

