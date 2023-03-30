use homescope;
SELECT * FROM users;
INSERT INTO users (first_name, last_name, email, password)
VALUES ("Tony",	"Stark",	"tony@email.com",	"$2b$12$PqkyxDhC5.4.4/Ie.Pi7Fej0i3mwXd31C3vU5JlvuiQkZBD2QpMcO"),
("Jacob",	"Yang",	"jacob@email.com",	"$2b$12$WyGgd/zvFAcRNaiIXWKmXeqwIxPvKFIuuqE0zOJem5y7HJD.GGN.K");


INSERT INTO homes (name, street_address, city, state, zipcode, description, bed, bath, sq_ft, price, image, type, user_id) 
VALUES 
("Jacob",	"1223 Street",	"Ocean",	"HA",	"14540",	"adsofiaowejn"	"2"	"2",	"1234",	"123450",	"Single Family Homes",	"http://res.cloudinary.com/dggzaweqo/image/upload/v1680162800/eee24y1mlvmmjjyykmfr.jpg", "2"),
("Jacob",	"12313 Road",	"Wawa",	"Wawa",	"45641",	"adsofiaowejn"	"2"	"3",	"1234",	"123450",	"Multi Family Homes",	"http://res.cloudinary.com/dggzaweqo/image/upload/v1680162852/nxgl4cbgoaymyuroyndc.jpg", "2"),
("Jacob",	"Red Street",	"Red City",	"RC",	"41540",	"adsofiaowejn"	"2"	"2",	"54125",	"1231123",	"Single Family Homes",	"http://res.cloudinary.com/dggzaweqo/image/upload/v1680162737/vfthei5vbntn5djtrt3b.jpg", "2"),
("Jacob",	"148 Blue Street",	"New York",	"NY",	"1230",	"adsofiaowejn"	"2"	"2",	"3300",	"125000",	"Single Family Homes",	"http://res.cloudinary.com/dggzaweqo/image/upload/v1680162447/jagkqgbbqx6exz5px3zd.jpg", "2"),
("Tony",	"148 Blue Street",	"Ocean",	"MA",	"1325",	"adsofiaowejn"	"2"	"2",	"3000",	"685140",	"Townhouse",	"http://res.cloudinary.com/dggzaweqo/image/upload/v1680163525/hlos3ftg0vfoawa02pbm.jpg", "1"),
("Tony",	"120 Sky Road",	"New York",	"NY",	"21540",	"adsofiaowejn"	"3"	"2",	"3548",	"758420",	"Townhouse",	"http://res.cloudinary.com/dggzaweqo/image/upload/v1680163595/rwkn2zlx5qvpcyevk7d3.jpg", "1");