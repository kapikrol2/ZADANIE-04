from flask import Flask

app = Flask(__name__)

# Zadanie 2 Strona główna
@app.route("/")
def index():
    return "Jan Kowalski - Strona główna Sklepu"

# Zadanie 3: Kolejne trasy
@app.route("/o-nas")
def o_nas():
    return "Nasze produkty wyróżniają się najwyższą jakością na rynku."

@app.route("/kontakt")
def kontakt():
    return "Napisz do nas: kontakt@mojsklep.pl"

@app.route("/regulamin")
def regulamin():
    return "1. Zakupy w naszym sklepie są proste i bezpieczne."

# Zadanie 4: Trasa ze zwracaniem statusu HTTP 403
@app.route("/admin")
def admin():
    return "Brak dostępu", 403

# Zadanie 5: Trasa zwracająca JSON
@app.route("/api/info")
def api_info():
    return {
        "nazwa": "Internetowy Sklep Komputerowy",
        "autor": "Jan Kowalski",
        "wersja": "1.0"
    }

if __name__ == "__main__":
    app.run(debug=True)
