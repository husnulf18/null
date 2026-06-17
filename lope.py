from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Membuat database
def init_db():

    conn = sqlite3.connect("data.db")

    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS surat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        email TEXT,
        alamat TEXT,
        tanggal TEXT,
        isi TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/simpan", methods=["POST"])
def simpan():

    nama = request.form["nama"]
    email = request.form["email"]
    alamat = request.form["alamat"]
    tanggal = request.form["tanggal"]
    isi = request.form["isi"]

    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("""
    INSERT INTO surat
    (nama,email,alamat,tanggal,isi)
    VALUES (?,?,?,?,?)
    """,(nama,email,alamat,tanggal,isi))

    conn.commit()
    conn.close()

    return render_template("success.html")


@app.route("/surat")
def surat():

    conn = sqlite3.connect("data.db")

    c = conn.cursor()

    c.execute("SELECT * FROM surat")

    data = c.fetchall()

    conn.close()

    return render_template(
        "letters.html",
        data=data
    )


if __name__ == "__main__":
    app.run(debug=True)