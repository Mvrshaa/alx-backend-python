# 🌀 Python Generators Project

This project demonstrates advanced usage of Python generators to process large datasets efficiently, integrate with SQL, and simulate real-world streaming scenarios.

---

## ✅ Features and Learning Objectives

* Use `yield` for memory-efficient streaming
* Process data in batches using generators
* Lazy load paginated records
* Aggregate SQL data with minimal memory use

---

## 📁 Project Structure

```
python-generators-0x00/
├── seed.py              # Setup MySQL DB + load CSV
├── 0-stream_users.py    # Task 1: Yield rows one-by-one
├── 1-batch_processing.py# Task 2: Batch fetch + filter age > 25
├── 2-lazy_paginate.py   # Task 3: Lazy pagination with offset
├── 4-stream_ages.py     # Task 4: Average age calculation
├── 0-main.py            # Runs DB seed & sanity check
├── 1-main.py            # Test stream_users
├── 2-main.py            # Test batch_processing
├── 3-main.py            # Test lazy_pagination
├── 4-main.py            # Test average age
├── user_data.csv        # Provided seed data
```

---

## ⚙️ Setup

1. Ensure MySQL is running locally
2. Set root user + password in `seed.py` (default: `root`/`root`)
3. Install MySQL connector:

   ```bash
   pip install mysql-connector-python
   ```
4. Run seed script:

   ```bash
   python 0-main.py
   ```

---

## 🚀 Task Usage

### Task 1: Stream Users

```bash
python 1-main.py
```

### Task 2: Batch Processing

```bash
python 2-main.py | head -n 5
```

### Task 3: Lazy Paginate

```bash
python 3-main.py | head -n 10
```

### Task 4: Stream + Aggregate

```bash
python 4-main.py
```

---

## ✅ Notes

* All generators use `yield` to avoid memory bloat
* Queries are optimized to handle large datasets
* Filtering and aggregation is done in Python, not SQL

---

## 🔗 Repo

**GitHub:** [alx-backend-python](https://github.com/mvrshaa/alx-backend-python)

---

## 🧪 Example Output

```
Average age of users: 68.23
{'user_id': 'abc123', 'age': 78, ...}
...
```

---
