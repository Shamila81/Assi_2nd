from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/prime_number/<int:number>")
def check_prime_number(number):
    if number <= 1:
        return jsonify({"Number": number, "isPrime": False})

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return jsonify({"Number": number, "isPrime": False})

    return jsonify({"Number": number, "isPrime": True})

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)

#task 02"""

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_airport_info(icao_code):
    # Connect to the airport database
    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()

    # Query the database for the airport information
    cursor.execute("SELECT name, location FROM airports WHERE icao_code = ?", (icao_code,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    if result is None:
        return None
    else:
        return {"ICAO": icao_code, "Name": result[0], "Location": result[1]}

@app.route('/airport/<icao_code>')
def get_airport_by_icao(icao_code):
    airport_info = get_airport_info(icao_code)

    if airport_info is None:
        return jsonify({"error": "Airport not found"}), 404
    else:
        return jsonify(airport_info)

if __name__ == '__main__':
    app.run(debug=True)


