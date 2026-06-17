from flask import Flask, render_template, request
app = Flask(__name__)

# TEMPAT SIMPAN DATA SEMENTARA
data_pesan = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kirim', methods=['POST'])
def kirim():
    nama = request.form['nama']
    email = request.form['email']
    pesan = request.form['pesan']
    tanggal = request.form['tanggal']

    # simpan ke list
    data_pesan.append({
        'nama': nama,
        'email': email,
        'pesan': pesan,
        'tanggal': tanggal
    })

    return render_template('sukses.html', nama=nama)
if __name__ == '__main__':
    app.run(debug=True)