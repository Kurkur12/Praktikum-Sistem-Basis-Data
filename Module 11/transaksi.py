import mysql.connector

cnx = mysql.connector.connect(user='root', 
database='perbankan')
cursor = cnx.cursor()

query = ("SELECT DISTINCT nasabah.nama_nasabah", 
DATE_FORMAT (transaksi.tanggal, '&M') AS nama_bulan "
        "FROM transaksi"
        "LEFT JOIN nasabah ON nasabah.id_nasabah = transaks.id_nasabahFK"
        "WHERE MONTH (transaksi.tanggal) BETWEEN 10 AND 12"
cursor.execute(query)

print("Nasabah yang melakukan transaksi pada bulan 
Oktober sampai Desember:")
for (nama_nasabah, nama_bulan) in cursor:
    print("{} melakukan transaksi pada bulan {}".format(
        nama_nasabah, nama_bulan
 ))
 
cursor.close()
cnx.close()