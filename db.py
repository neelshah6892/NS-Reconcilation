import psycopg2
import mysql-connector

conn = psycopg2.connect(user = "postgres",password = "rocker12", host = "127.0.0.1", port = "5433", database = "nova")
cursor = conn.cursor()
query = """SELECT DISTINCT "Invoice Date"
FROM
    "TWOA"
    INNER JOIN "INWARD"
        ON "Invoice Date" = "DOCUMENTDATE" AND "Supplier GSTIN" = "Supplier GSTIN"
WHERE
    "Invoice Date" <> "DOCUMENTDATE"
"""
cursor.execute(query)
print(cursor)
cursor.close()
conn.commit()
conn.close()

SELECT DISTINCT "Invoice Date", "DOCUMENTDATE", "Supplier GSTIN","SUPPLIERGSTIN","Invoice Number","DOCUMENTNUMBER"
FROM
    "TWOA"
    INNER JOIN "INWARD"
        ON "Invoice Date" = "DOCUMENTDATE" AND "Supplier GSTIN" = "SUPPLIERGSTIN" AND "Invoice Number" = "DOCUMENTNUMBER"
WHERE
    "Invoice Date" <> "DOCUMENTDATE" AND "Supplier GSTIN" <> "SUPPLIERGSTIN" AND "Invoice Number" <> "DOCUMENTNUMBER"





CASE
      WHEN "TWOA.Supplier GSTIN" == "INWARD.SUPPLIERGSTIN" && "TWOA.Invoice Date" == "INWARD.DOCUMENTDATE" && "TWOA.My GSTIN" == "INWARD.RECIPIENTGSTIN" && "TWOA.Total Transaction Value" == "INWARD.INVOICEVALUE"
	  THEN "EXISTS IN BOTH 2A AND INWARD"
	  ELSE WHEN ""
END

