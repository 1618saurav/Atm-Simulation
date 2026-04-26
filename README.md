# ATM Simulation — Python Project 1

A menu-driven ATM simulation built in Python. Supports balance display, deposits, withdrawals, and a live transaction statement with timestamps.

---

## Project Structure

```
atm_project/
├── atm.py        # Business logic — balance, deposit, withdraw, statement
├── main.py       # Entry point — menu loop and user interaction
└── README.md
```

> Follows **package architecture**: all logic lives in `atm.py`, all input/output lives in `main.py`.

---

## How to Run

Make sure Python 3 is installed, then run:

```bash
python main.py
```

No external libraries required. Only the built-in `datetime` module is used.

---

## Features

| Feature | Description |
|---|---|
| Display Balance | Shows current account balance |
| Deposit Money | Adds amount to balance and logs the transaction |
| Withdraw Money | Deducts amount with insufficient balance check |
| Bank Statement | Prints full transaction history with timestamps and running balance |

---

## How It Works

### Data Storage
Account state is held in a single dictionary in `atm.py`:

```python
account = {
    "name": "",
    "balance": 10000.0,
    "transactions": []   # list of dicts: {type, amount, balance, time}
}
```

### Deposit Logic
- Validates that amount is greater than ₹0
- Adds to balance
- Records transaction via `_record()`

### Withdrawal Logic
- Validates amount is greater than ₹0
- Checks against current balance before deducting
- Records transaction via `_record()`

### Statement Logic
- Iterates over `account["transactions"]`
- Displays type, amount, running balance, and timestamp for every entry
- Shows closing balance at the bottom

---

## Package Architecture

| File | Responsibility |
|---|---|
| `atm.py` | All business logic — no `input()` calls |
| `main.py` | All user interaction — no business logic |

This separation means `atm.py` can be tested independently without running the menu.

---

## Concepts Used

| Concept | Where |
|---|---|
| `datetime` module | Transaction timestamps |
| Dictionary | Account state and transaction records |
| Functions | Each feature is a separate function |
| `while True` loop | Keeps the menu running until user exits |
| `try/except` | Handles non-numeric amount input |
| f-strings | All formatted output |
| Module import | `main.py` imports and calls `atm.py` |

---

## Sample Output

```
========================================
    Welcome to Python National Bank
========================================

Enter Account Holder's Name: Saurav

  Hello, Saurav!  Your account is ready.

┌─────────────────────────────┐
│         ATM MENU            │
├─────────────────────────────┤
│  1. Display Balance         │
│  2. Deposit Money           │
│  3. Withdraw Money          │
│  4. Bank Statement          │
│  5. Exit                    │
└─────────────────────────────┘
  Enter your choice (1-5): 2

  Current Balance : ₹ 10,000.00
  Enter deposit amount (₹): 5000
  ✅  Deposit of ₹5,000.00 successful.  New Balance: ₹15,000.00

  Enter your choice (1-5): 4

==========================================================
  BANK STATEMENT
  Account Holder : Saurav
  Generated On   : 26-04-2026  11:21:12
==========================================================
  DATE & TIME            TYPE         AMOUNT       BALANCE
  --------------------------------------------------------
  26-04-2026  11:21:12   DEPOSIT    ₹5,000.00  ₹15,000.00
==========================================================
  Closing Balance : ₹15,000.00
==========================================================
```

---

## Known Limitations

- Data is not saved to a file — balance and history reset when the program exits
- Single account only — no multi-user or PIN authentication
- No daily withdrawal limit enforced

---

## Author

**Saurav**
B.Tech CSE — Chandigarh Engineering College (CGC)
Semester 2 — Python Programming Lab
