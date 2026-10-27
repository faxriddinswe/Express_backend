1. Insert qilishni har qil usuli bor 

1 Insert into table_name (column1, column2) values(value1, value2) deb yozish 

2 Insert into table_name VALUES (value1, value2) -> bunda coulumnlarni yozmasa hamma coumnlarni oladi ichiga faqat value yozishimiz kerak holos

3 Bazi bir column nomlarini tushushirib qoldirib yozish mumkin 

misol Insert into table_name (column1) values(value1)

column lar soni 4 ta deb lekin 1 tasini yozsak value ham bitta bolishi kerak aks holda error chiqadi 



----------------------------------------------------------------------------------


Null -- NOT null -- default 

Null - bu bosh qiymat degani 

not null bosh bolishi mumkin emas yani qimat kiritilishi kerak degani 

default esa avtomatik shu qiymatni oladi agarda qiymat kiritilmasa

Exxample:

CREATE TABLE contacts(
    ID int
    first_name VARCHAR(50) not null,
    last name VARCHAR(50) not null,
    Price numeric(3,2) default 1.00
    
)


--------------------------------------------------------------------------------