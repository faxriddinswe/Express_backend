# PostgreSQL learning commands
1.	CREATE DATABASE -> creates a new database

2.	DROP DATABASE -> deletes an existing database

3.	CREATE TABLE -> creates a new table in the database

4.	DROP TABLE -> deletes an existing table

5.	INSERT INTO -> inserts new rows into a table

6.	SELECT -> retrieves data from a table

7.	WHERE -> filters records based on a specific condition

8.	UPDATE -> modifies existing data in a table

9.	DELETE -> removes records from a table

10.	ORDER BY -> sorts the result set in ascending or descending order

11.	GROUP BY -> groups rows that have the same values into summary rows

12.	HAVING -> filters groups based on a condition (used with GROUP BY)

13.	MIN / MAX -> returns the smallest or largest value in a column

14.	SUM / AVG -> calculates the total sum or average value of a numeric colum
n
15.	LIKE -> searches for a specified pattern in a column

16.	BETWEEN -> selects values within a given range

17.	IN -> allows you to specify multiple values in a WHERE clause

18.	AND / OR -> combines multiple conditions in a filter

19.	PRIMARY KEY -> uniquely identifies each record in a table

20.	FOREIGN KEY -> links two tables together and ensures data integrity

21.	ALTER TABLE -> adds, deletes, or modifies columns in an existing table

22.	JOIN (INNER, LEFT, RIGHT, FULL) -> combines rows from two or more tables based on a related column between them

23.	\l -> lists all databases on the server

24.	\c -> connects to a specific database

25.	\d -> lists all tables or describes the structure of a specific table

# Malumot turlari

## 1. Text - 3xil

Varchar - limit bolganda ishlatiladi varchar(10)

TEXT -> limit bo'lmaganda ishlatiladi - men 1994 yilda tug'ilganman limit yoq bolganmanda ishlatish kerak 

CHAR -> Varchar bilan bir xil lekin farqi berilgan uzunlikda joy oladi 
misol CHAR(10) 'kitob    ' -> kitob sozi 5 ta harfdan iborat lekin 10 deganimiz uchun qoshimcha space oladi 

## 2. Integer - 3 xil 

1 INT -> -2,147,483,648 dan 2,147,483,648 bolgan sonlarni saqlash uchun mlr

2 SMALLINT -> -32, 768 dana 32, 768 gacha sonlarni saqlash uchun 

3.BIGINT -9223372036854775808 dan 9223372036854775808 gacha saqlash mumkin

### Serial - > 

Int bilan bir xil lekin postgresql ning qiymatlarini avtomatik ravishda toldirib boradi 
MYSQL Da esa buni equvalenti AUTOINCREMENT

SMALLINT, SERIAL , BIGSERIAL

## Numeric

Misol uchun 123.45

Numeric(5,2): 123.45  -> qavs ichidagi 5 soni bu umuiy 5 ta raqamdan iborat va nuqtadan keyin 2 ta son borlihini bildiradi 

Numeric(5): 12345 - birinchi argument berilgan bunda nuqtani 0 deb qabul qiladi postgresql

Numeric: 1234

## Floating Numbers

Hisob kitob qilish shart bolmasa 

REAL (4 bytes)
DOUBLE PRECISION (8 )

ishlatish mumkin 

Agar hisob kitob qilsih shart bolsa Numeric ishlatish kerak boladi 

## Boolean TRUE or FALSE

is_married BOOLEAN

## Vaqt malumot turlari 

DATE -sanalar uchun 2021-10-12

TIME - vaqt uchun 10:25:19

TIMESTAMP - ham sana ham vaqt ishlatish uchun 2021-10-12 10:25:19




