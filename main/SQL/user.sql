-- CREATE TABLES
CREATE TABLE USER(UserID SERIAL PRIMARY KEY, Firstname VARCHAR(100) NOT NULL, Lastname VARCHAR(100) NOT NULL, Email VARCHAR(100) NOT NULL, Passwords VARCHAR(100) NOT NULL);
CREATE TABLE Invoice(UserID bigint(20) unsigned, FOREIGN KEY (UserID) REFERENCES USER(UserID), OrderNumber VARCHAR(10) PRIMARY KEY, Dates VARCHAR(10) NOT NULL, Buyer VARCHAR(20) NOT NULL, Street VARCHAR(50) NOT NULL, City VARCHAR(20) NOT NULL, State VARCHAR(20) NOT NULL,
Zipcode VARCHAR(5) NOT NULL, Country VARCHAR(2) NOT NULL, Price VARCHAR(8));
CREATE TABLE Creditcard(UserID SERIAL, FOREIGN KEY (UserID) REFERENCES USER(UserID), Card VARCHAR(16), Fullname VARCHAR(50), Dates VARCHAR(8), Csc varchar(3));
CREATE TABLE Item(ItemID SERIAL PRIMARY KEY, Item VARCHAR(50) NOT NULL, Price VARCHAR(6) NOT NULL, Categories VARCHAR(15) NOT NULL, Subcategories VARCHAR(15) NOT NULL, Image varchar(20));
CREATE TABLE Cart(UserID bigint(20) unsigned, ItemID bigint(20) unsigned, Quantity INTEGER NOT NULL, FOREIGN KEY (UserID) REFERENCES USER(UserID) , FOREIGN KEY (ItemID) REFERENCES Item(ItemID));
CREATE TABLE Inventory(ItemID SERIAL, UNIQUE(ItemID), FOREIGN KEY (ItemID) REFERENCES Item(ItemID), Small INTEGER NOT NULL, Med INTEGER NOT NULL, Large INTEGER NOT NULL, Xlarge INTEGER NOT NULL);
CREATE TABLE Wishlist(UserID bigint(20) unsigned, ItemID bigint(20) unsigned, FOREIGN KEY(ItemID) REFERENCES Item(ItemID),FOREIGN KEY(UserID) REFERENCES USER(UserID));

-- INSERT ITEMS INTO DATABASE

-- Clothing -- Dress
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 1","12.24","clothing","dresses","dress1.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 2","42.24","clothing","dresses","dress2.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 3","67.24","clothing","dresses","dress3.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 4","45.24","clothing","dresses","dress4.jpeg");
-- Clothing -- Top
insert into Item(Item,Price,Categories,Subcategories,Image) values("Shirt 1","56.24","clothing","top","shirt1.png");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Shirt 2","56.24","clothing","top","shirt2.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Shirt 3","56.24","clothing","top","shirt3.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Shirt 4","56.24","clothing","top","shirt4.jpeg");
-- Clothing -- Suits
insert into Item(Item,Price,Categories,Subcategories,Image) values("Suit 1","11.24","clothing","suits","suits1.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Suit 2","80.00","clothing","suits","suits2.png");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Suit 3","32.21","clothing","suits","suits5.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Suit 4","99.99","clothing","suits","suits4.jpg");
-- Clothing -- Bottom
insert into Item(Item,Price,Categories,Subcategories,Image) values("Bottom 1","89.24","clothing","bottom","bottom.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Bottom 2","23.24","clothing","bottom","bottom2.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Bottom 3","56.34","clothing","bottom","bottom3.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Bottom 4","79.24","clothing","bottom","bottom4.jpg");


-- Footwear -- Sneakers
insert into Item(Item,Price,Categories,Subcategories,Image) values("sneakers 1","12.24","footwear","sneakers","sneaker1.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("sneakers 2","42.24","footwear","sneakers","sneaker2.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("sneakers 3","67.24","footwear","sneakers","sneaker3.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("sneakers 4","45.24","footwear","sneakers","sneaker4.jpg");
-- Footwear -- Sandles
insert into Item(Item,Price,Categories,Subcategories,Image) values("sandles 1","34.24","footwear","sandles","sandle1.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("sandles 3","12.24","footwear","sandles","sandle3.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("sandles 2","67.24","footwear","sandles","sandle2.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("sandles 4","43.24","footwear","sandles","sandle4.jpeg");
-- Footwear -- Slippers
insert into Item(Item,Price,Categories,Subcategories,Image) values("slippers 1","12.24","footwear","slippers","slipper1.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("slippers 2","42.24","footwear","slippers","slipper2.png");
insert into Item(Item,Price,Categories,Subcategories,Image) values("slippers 3","67.24","footwear","slippers","slipper3.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("slippers 4","45.24","footwear","slippers","slipper4.jpeg");


-- Accessories --Sunglasses
insert into Item(Item,Price,Categories,Subcategories,Image) values("sunglass 1","12.24","accessories","sunglasses","sunglass1.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("sunglass 2","43.24","accessories","sunglasses","sunglass2.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("sunglass 3","12.24","accessories","sunglasses","sunglass3.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("sunglass 4","87.24","accessories","sunglasses","sunglass4.jpeg");

-- Accessories --Watches
insert into Item(Item,Price,Categories,Subcategories,Image) values("watch 1","122.24","accessories","watches","watch1.webp");
insert into Item(Item,Price,Categories,Subcategories,Image) values("watch 2","99.24","accessories","watches","watch2.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("watch 3","1000.24","accessories","watches","watch3.jpg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("watch 4","99.24","accessories","watches","watch4.jpg");

-- END INSERT

-- INSERT SIZE QUANTITIES INTO THE INVENTORY
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(1,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(2,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(3,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(4,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(5,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(6,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(7,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(8,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(9,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(10,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(11,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(12,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(13,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(14,10,10,10,10);
INSERT INTO Inventory(ItemID,Small,Med,Large,Xlarge) values(15,10,10,10,10);
