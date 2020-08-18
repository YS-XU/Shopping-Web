-- CREATE TABLES
CREATE TABLE USER(UserID SERIAL PRIMARY KEY, Firstname VARCHAR(100) NOT NULL, Lastname VARCHAR(100) NOT NULL, Email VARCHAR(100) NOT NULL, Passwords VARCHAR(100) NOT NULL);
CREATE TABLE Invoice(UserID SERIAL, FOREIGN KEY (UserID) REFERENCES USER(UserID), OrderNumber VARCHAR(10) PRIMARY KEY, Dates VARCHAR(10) NOT NULL, Buyer VARCHAR(20) NOT NULL, Street VARCHAR(50) NOT NULL, City VARCHAR(20) NOT NULL, State VARCHAR(20) NOT NULL,
Zipcode VARCHAR(5) NOT NULL, Country VARCHAR(2) NOT NULL, Price VARCHAR(8));
CREATE TABLE Creditcard(UserID SERIAL, FOREIGN KEY (UserID) REFERENCES USER(UserID), Card INTEGER NOT NULL, Fullname VARCHAR(50), Dates VARCHAR(5), Csc INTEGER NOT NULL);
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
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 1","12.24","clothing","dresses","dress1.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 2","42.24","clothing","dresses","dress2.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 3","67.24","clothing","dresses","dress3.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 4","45.24","clothing","dresses","dress4.jpeg");
-- Footwear -- Sandles
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 1","12.24","clothing","dresses","dress1.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 2","42.24","clothing","dresses","dress2.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 3","67.24","clothing","dresses","dress3.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 4","45.24","clothing","dresses","dress4.jpeg");
-- Footwear -- Slippers
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 1","12.24","clothing","dresses","dress1.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 2","42.24","clothing","dresses","dress2.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 3","67.24","clothing","dresses","dress3.jpeg");
insert into Item(Item,Price,Categories,Subcategories,Image) values("Dress 4","45.24","clothing","dresses","dress4.jpeg");

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
