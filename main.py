
import atm


def show_menu() -> None:
    print("\n┌─────────────────────────────┐")
    print("│         ATM MENU            │")
    print("├─────────────────────────────┤")
    print("│  1. Display Balance         │")
    print("│  2. Deposit Money           │")
    print("│  3. Withdraw Money          │")
    print("│  4. Bank Statement          │")
    print("│  5. Exit                    │")
    print("└─────────────────────────────┘")


def get_amount(prompt: str) -> float:
    """Prompt for a monetary amount; re-prompt on invalid input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  ⚠  Invalid input. Please enter a numeric amount.")


def main() -> None:
    print("\n" + "=" * 40)
    print("    Welcome to Python National Bank")
    print("=" * 40)

    name = input("\nEnter Account Holder's Name: ").strip()
    while not name:
        print("  Name cannot be empty.")
        name = input("Enter Account Holder's Name: ").strip()

    atm.set_account_name(name)
    print(f"\n  Hello, {name}!  Your account is ready.")

    while True:
        show_menu()
        choice = input("  Enter your choice (1-5): ").strip()

        if choice == "1":
            atm.display_balance()

        elif choice == "2":
            atm.display_balance()
            amount = get_amount("  Enter deposit amount (₹): ")
            print("  " + atm.deposit(amount))

        elif choice == "3":
            atm.display_balance()
            amount = get_amount("  Enter withdrawal amount (₹): ")
            print("  " + atm.withdraw(amount))

        elif choice == "4":
            atm.print_statement()

        elif choice == "5":
            print(f"\n  Thank you, {atm.account['name']}. Have a great day!\n")
            break

        else:
            print("  ⚠  Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()