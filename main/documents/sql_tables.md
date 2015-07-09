SQL Tables:
=================
	"following":

CREATE TABLE following
(
follower_id INT NOT NULL,
followed_id INT NOT NULL,
allowed CHAR(1) NOT NULL
);

-----------------
	"comments":

CREATE TABLE comments
(
comment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
commenter_id INT NOT NULL,
image_id INT NOT NULL,
comment VARCHAR(1000) NOT NULL,
deleted CHAR(1) NOT NULL
);

-----------------
	"likes":

CREATE TABLE likes
(
liker_id INT NOT NULL,
image_id INT NOT NULL
);
