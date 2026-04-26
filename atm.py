"""
atm.py  —  ATM logic module
All business logic lives here. main.py only calls these functions.
"""

from datetime import datetime


# ── Account State ────────────────────────────────────────────────────────────

account = {
    "name": "",
    "balance": 10000.0,
    "transactions": []          # list of dicts: {type, amount, balance, time}
}


# ── Internal Helper ───────────────────────────────────────────────────────────

def _record(transaction_type: str, amount: float) -> None:
    """Append a transaction to the statement log."""
    account["transactions"].append({
        "type": transaction_type,
        "amount": amount,
        "balance": account["balance"],
        "time": datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    })


# ── Public Functions ──────────────────────────────────────────────────────────

def set_account_name(name: str) -> None:
    account["name"] = name.strip()


def get_balance() -> float:
    return account["balance"]


def display_balance() -> None:
    print(f"\n  Current Balance : ₹ {account['balance']:,.2f}")


def deposit(amount: float) -> str:
    """
    Deposit money into the account.
    Returns a status message string.
    """
    if amount <= 0:
        return "❌  Deposit amount must be greater than ₹0."

    account["balance"] += amount
    _record("DEPOSIT", amount)
    return f"✅  Deposit of ₹{amount:,.2f} successful.  New Balance: ₹{account['balance']:,.2f}"


def withdraw(amount: float) -> str:
    """
    Withdraw money from the account.
    Returns a status message string.
    """
    if amount <= 0:
        return "❌  Withdrawal amount must be greater than ₹0."
    if amount > account["balance"]:
        return f"❌  Insufficient balance. Available: ₹{account['balance']:,.2f}"

    account["balance"] -= amount
    _record("WITHDRAWAL", amount)
    return f"✅  ₹{amount:,.2f} withdrawn successfully.  New Balance: ₹{account['balance']:,.2f}"


def print_statement() -> None:
    """Print a formatted transaction statement."""
    print("\n" + "=" * 58)
    print(f"  BANK STATEMENT")
    print(f"  Account Holder : {account['name']}")
    print(f"  Generated On   : {datetime.now().strftime('%d-%m-%Y  %H:%M:%S')}")
    print("=" * 58)

    if not account["transactions"]:
        print("  No transactions recorded yet.")
    else:
        print(f"  {'DATE & TIME':<22} {'TYPE':<12} {'AMOUNT':>10}  {'BALANCE':>12}")
        print("  " + "-" * 54)
        for t in account["transactions"]:
            print(
                f"  {t['time']:<22} {t['type']:<12} "
                f"₹{t['amount']:>9,.2f}  ₹{t['balance']:>11,.2f}"
            )

    print("=" * 58)
    print(f"  Closing Balance : ₹{account['balance']:,.2f}")
    print("=" * 58 + "\n")