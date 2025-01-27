from vault_manager import VaultManager

def main():
    vault = VaultManager()
    print("=== Lava Vault CLI ===")
    
    while True:
        action = input("\n[1] Add Password\n[2] Generate Random Password\n[3] Exit\n> ").strip()
        
        if action == "1":
            service = input("Service (e.g. Gmail): ").strip()
            if not service:
                print("⚠️ Service name required!")
                continue
                
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            vault.add_password(service, username, password)
            print("✅ Saved!")
        
        elif action == "2":
            try:
                length_input = input("Password length (default 12): ").strip()
                length = int(length_input) if length_input else 12
                password = vault.generate_password()
                print(f"🔑 Generated: {password}")
            except ValueError:
                print("⚠️ Please enter a valid number!")
        
        elif action == "3":
            print("Goodbye! 👋")
            break
        
        else:
            print("⚠️ Invalid choice! Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()