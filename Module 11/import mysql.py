import mysql.connector
from datetime import date, datetime, timedelta
tanggal = datetime.now().date()
cnx = mysql.connector.connect(user='root', 
database='perbankan')
cursor = cnx.cursor()
insert_transaksi = ("INSERT INTO transaksi (id_nasabahFK,
no_rekeningFK, jenis_transaksi, tanggal, jumlah) "
"VALUES (%s, %s, %s, %s, %s)")
data_transaksi = ('10', '100', 'kredit', 
tanggal.strftime('%Y-%m-%d'), '100000')
cursor.execute(insert_transaksi, data_transaksi)
cnx.commit()
cursor.close()
cnx.close()