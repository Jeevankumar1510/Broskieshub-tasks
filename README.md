Command-Line Calculator (Python)

This is a simple yet powerful command-line calculator written in Python that supports multiple operations like Addition, Subtraction, Multiplication, and Division on multiple numbers. It also gracefully handles invalid input, invalid choices, and division by zero errors.

---

 File Structure

calculator.py README.md

---

## 🚀 Features

- ➕ Add multiple numbers
- ➖ Subtract multiple numbers
- ✖️ Multiply multiple numbers
- ➗ Divide multiple numbers
- 🔁 Repeats until user exits manually
- ❌ Handles:
  - Non-numeric input
  - Invalid menu choices
  - Division by zero
  - Less than two numbers

---

## 🧠 How It Works

### ✅ Menu

When you run the script, it will repeatedly show the following menu:

Choose operation:

1. Add


2. Subtract


3. Multiply


4. Divide


5. Exit



---

## 🔢 Input Format

After selecting an operation (1–4), the program will ask:

Enter numbers separated by space:

You must enter at least **two numbers**, like:

5 10 15

---

## ⚙️ Operation Examples

### 1️⃣ Addition

**Input:**

Enter choice (1-5): 1 Enter numbers separated by space: 5 10 15

**Output:**

Result: 30.0

---

### 2️⃣ Subtraction

**Input:**

Enter choice (1-5): 2 Enter numbers separated by space: 20 5 3

**Output:**

Result: 12.0

---

### 3️⃣ Multiplication

**Input:**

Enter choice (1-5): 3 Enter numbers separated by space: 2 4 5

**Output:**

Result: 40.0

---

### 4️⃣ Division

**Input:**

Enter choice (1-5): 4 Enter numbers separated by space: 100 5 2

**Output:**

Result: 10.0

---

## ❗ Error Handling

### 🚫 Invalid Input (non-numeric)

**Input:**

Enter numbers separated by space: 5 a 10

**Output:**

Invalid input. Please enter only numbers.

---

### 🛑 Division by Zero

**Input:**

Enter choice (1-5): 4 Enter numbers separated by space: 50 0

**Output:**

Result: Error: Division by zero

---

### ⛔ Invalid Choice

**Input:**

Enter choice (1-5): 8

**Output:**

Invalid choice. Try again.

---

### ⚠️ Less than Two Numbers

**Input:**

Enter numbers separated by space: 5

**Output:**

Please enter at least two numbers.

---

## 🛠️ How to Run

### 📌 Prerequisites

- Python 3.x installed

### ▶️ Run the Program

Open terminal and run:

```bash
python calculator.py


---

💻 Screenshot (Example)

Choose operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Enter choice (1-5): 1
Enter numbers separated by space: 2 3 4
Result: 9.0
