# 📚 Python Generators - ALX Project Overview

This project is part of the **ALX Software Engineering** curriculum and focuses on using **Python Generators** to handle real-world, data-intensive problems. It simulates how to work with large datasets from SQL databases using memory-efficient generator functions.

---

## 🎯 Project Objectives

* Implement **Python generator functions** using `yield`
* Stream and process data from **MySQL** databases efficiently
* Simulate **batch processing**, **lazy pagination**, and **streamed aggregations**
* Integrate Python with SQL using **MySQL Connector**

---

## 🧠 Key Skills Acquired

* Writing and consuming Python generators
* Connecting Python scripts to SQL databases
* Performing SQL operations (SELECT, LIMIT, OFFSET)
* Efficient memory handling with large datasets
* Structuring clean, modular Python scripts for database operations

---

## 🗂️ Core Components

| File                    | Description                                   |
| ----------------------- | --------------------------------------------- |
| `seed.py`               | Sets up DB and loads CSV data                 |
| `0-stream_users.py`     | Streams users one at a time with a generator  |
| `1-batch_processing.py` | Batches users and filters based on age        |
| `2-lazy_paginate.py`    | Simulates pagination with offsets and yields  |
| `4-stream_ages.py`      | Calculates average user age using a generator |

---

## 🔁 Generator Patterns Used

* One-by-one row streaming
* Batched fetching
* Lazy pagination with LIMIT/OFFSET
* Memory-efficient reduction (average)

---

## ⚙️ Technologies

* Python 3.x
* MySQL / MariaDB
* MySQL Connector Python
* CSV file parsing
* Git/GitHub for version control

---

## 🧪 Testing and Output

Each file has a corresponding `*-main.py` that can be run to validate the logic.

Example:

```bash
python 4-main.py
# ➜ Average age of users: 67.45
```

---

## 🧩 Why Generators?

Generators are essential in scalable systems to reduce memory consumption by yielding data only when needed — this is ideal when working with **streams, APIs, or massive datasets**.

---

## 📎 Submission Checklist

* [x] MySQL schema created
* [x] Data inserted from `user_data.csv`
* [x] Generators implemented in all tasks
* [x] Scripts tested with provided main files
* [x] README documentation completed

---

