# 📊 Social Media Analytics Tool

A Python-based console application that manages and analyzes social media profiles using a **Binary Search Tree (BST)**.  
This project demonstrates object-oriented programming, data structures, and test-driven development using **PyTest**.

---

## 🚀 Overview

The **Social Media Analytics Tool** allows users to:

- Store and manage social media profiles efficiently using a BST
- Perform analytics on different platforms (Instagram, TikTok, LinkedIn)
- Interact with the system through a menu-driven CLI
- Validate functionality through a comprehensive PyTest suite

---

## 🧠 Key Concepts

- **Binary Search Trees (BST)** for efficient data storage and retrieval
- **Object-Oriented Programming (OOP)** with inheritance and polymorphism
- **Data Validation & Error Handling**
- **Unit Testing with PyTest**
- **Encapsulation and Operator Overloading**

---

## 🏗️ Project Structure

```
.
├── main.py
├── bst.py
├── social_media.py
├── instagram.py
├── linkedin.py
├── tiktok.py
│
├── bst_test.py
├── social_media_test.py
├── instagram_test.py
├── linkedin_test.py
├── tiktok_test.py
```

---

## ⚙️ Features

### 🌳 Binary Search Tree
- Insert social media profiles
- Retrieve profiles by username
- Remove profiles (handles all BST cases)
- In-order traversal display (sorted output)

### 📱 Platform-Specific Analytics

#### Instagram
- Engagement score calculation
- Story activity classification
- Average likes per post
- Engagement ratio tracking

#### TikTok
- Repost rate calculation
- Viral video detection
- Engagement score (likes + comments + shares)

#### LinkedIn
- Connection acceptance rate
- Profile view rate (daily average)
- Network activity level classification

---

## 🖥️ How to Run

### 1. Clone the Repository
```
git clone https://github.com/msalvad2/social-media-analytics-system.git
```

### 2. Install Dependencies
```
pip install numpy pytest
```

### 3. Run the Application
```
python main.py
```

---

## 🧪 Running Tests

Run all tests:
```
pytest
```

Run a specific test file:
```
pytest bst_test.py
```

---

## 🧾 Example Usage

```
WELCOME to the Social Media Analytics Tool!
--------------------------------------------
Main Menu:
1. Add Instagram Profile
2. Add TikTok Profile
3. Add LinkedIn Profile
4. Search for Profile
5. Display All Profiles
6. Update Profile Stats
7. Remove Profile
8. View Profile Analytics
9. Exit
```

---

## 🛡️ Error Handling

The application includes validation for:
- Invalid data types
- Negative values
- Duplicate usernames
- Division-by-zero scenarios

---

## 📈 Design Highlights

- **BST ensures O(log n)** average performance
- **Polymorphism** across platforms (Instagram, TikTok, LinkedIn)
- **Encapsulation** for data safety
- **Operator Overloading** (`+`, `<`, `==`)

---

## 👨‍💻 Author

**Miguel Salvador**

---

## 📌 Future Improvements

- Add GUI (Tkinter or Web UI)
- Persist data (database or file storage)
- Add more platforms
- Add data visualization

---

## 📄 License

This project is for educational purposes.
