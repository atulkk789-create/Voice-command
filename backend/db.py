import sqlite3

con = sqlite3.connect("python.db")
cursor = con.cursor()


# create table
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)
# insert int able

query = "INSERT INTO web_COMMAND VALUES(null,'amazon','https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=2256745889688718944&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9153786&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1')"
cursor.execute(query)
con.commit()
