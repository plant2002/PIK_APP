from core import db_communication 
import difflib


class AuthLogic:
    def __init__(self):
        self.db = db_communication  

    # ---------------- LOGIN ----------------
    def login(self, email, password):
        """Check credentials from database."""
        query = "SELECT * FROM client WHERE email = %s AND pass = %s"
        client = self.db.fetch_one(query, (email, password))
        return bool(client)

    # ---------------- REGISTER ----------------
    def register(self, data):
        """Register new client if email not used yet."""
        check_query = "SELECT id FROM client WHERE email = %s"
        existing = self.db.fetch_one(check_query, (data["email"],))
        if existing:
            print("[AuthLogic] Email already registered.")
            return False

        insert_query = """
            INSERT INTO client (name, surname, email, pass, company_id)
            VALUES (%s, %s, %s, %s,
                (SELECT id FROM companies WHERE name = %s LIMIT 1)
            )
        """
        try:
            self.db.execute_query(insert_query, (
                data["name"], data["surname"], data["email"], data["password"], data["company"]
            ))
            print(f"[AuthLogic] Registered client {data['email']}")
            return True
        except Exception as e:
            print("[AuthLogic] Error registering:", e)
            return False

    # ---------------- COMPANY SUGGESTIONS ----------------
    def suggest_company(self, query):
        """Suggest companies based on fuzzy matching."""
        all_companies = self.db.fetch_all("SELECT name FROM companies")
        names = [c[0] for c in all_companies]
        matches = difflib.get_close_matches(query, names, n=5, cutoff=0.3)
        return matches

    # ---------------- CREATE NEW COMPANY ----------------
    def create_company(self, data):
        """Insert a new company into database."""
        check_query = "SELECT id FROM companies WHERE LOWER(name) = LOWER(%s)"
        exists = self.db.fetch_one(check_query, (data["name"],))
        if exists:
            print("[AuthLogic] Company already exists.")
            return False

        insert_query = "INSERT INTO companies (name, address, country) VALUES (%s, %s, %s)"
        try:
            self.db.execute_query(insert_query, (data["name"], data["address"], data["country"]))
            print(f"[AuthLogic] Created new company {data['name']}")
            return True
        except Exception as e:
            print("[AuthLogic] Error creating company:", e)
            return False
