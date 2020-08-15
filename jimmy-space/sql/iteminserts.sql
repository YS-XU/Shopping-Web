insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Dress 1","12.24","S",4,"clothing","dresses","dress1.jpeg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Dress 2","42.24","S",4,"clothing","dresses","dress2.jpeg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Dress 3","67.24","S",4,"clothing","dresses","dress3.jpeg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Dress 4","45.24","S",4,"clothing","dresses","dress4.jpeg");

insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Shirt 1","56.24","S",4,"clothing","top","shirt1.png");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Shirt 2","56.24","S",4,"clothing","top","shirt2.jpg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Shirt 3","56.24","S",4,"clothing","top","shirt3.jpeg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Shirt 4","56.24","S",4,"clothing","top","shirt4.jpeg");

insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Suit 1","11.24","S",4,"clothing","suits","suits1.jpeg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Suit 2","80.00","S",6,"clothing","suits","suits2.png");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Suit 3","32.21","S",12,"clothing","suits","suits5.jpeg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Suit 4","99.99","S",5,"clothing","suits","suits4.jpg");

insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Bottom 1","89.24","S",4,"clothing","bottom","bottom.jpg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Bottom 2","23.24","S",4,"clothing","bottom","bottom2.jpg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Bottom 3","56.34","S",4,"clothing","bottom","bottom3.jpg");
insert into Item(Item,Price,Size,Quentity,Categories,Subcategories,Image) values("Bottom 4","79.24","S",4,"clothing","bottom","bottom4.jpg");


CREATE TABLE Cart(UserID bigint(20) unsigned, ItemID bigint(20) unsigned, Quantity INTEGER NOT NULL, FOREIGN KEY (UserID) REFERENCES USER(UserID) , FOREIGN KEY (ItemID) REFERENCES Item(ItemID)); 
