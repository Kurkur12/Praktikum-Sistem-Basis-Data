import mysql.connector
cnx = mysql.connector.connect(user='root', 
database='perbankan')
cursor = cnx.cursor()
delete_transaksi = ("DELETE FROM transaksi "
                    "WHERE no_transaksi=%s")
data_transaksi = ('51',)
cursor.execute(delete_transaksi, data_transaksi)
cnx.commit()
cursor.close()
cnx.close()