import mysql.connector
cnx = mysql.connector.connect(user='root',
database='perbankan')
cursor = cnx.cursor()
update_transaksi = ("UPDATE transaksi SET jumlah=%s "
                    "WHERE no_transaksi=%s")
data_transaksi = ('200000', '51')
cursor.execute(update_transaksi, data_transaksi)
cnx.commit()
cursor.close()
cnx.close()