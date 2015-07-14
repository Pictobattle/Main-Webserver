#SQL Tables:

##	"following":

```sql
CREATE TABLE following
(
	follower_id INT NOT NULL,
	followed_id INT NOT NULL,
	allowed CHAR(1) NOT NULL
	UNIQUE (follower_id,followed_id)
);
```

---
##	"comments":

```sql
CREATE TABLE comments
(
	comment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	commenter_id INT NOT NULL,
	image_id INT NOT NULL,
	comment VARCHAR(1000) NOT NULL,
	deleted CHAR(1) NOT NULL
);
```

---
##	"likes":

```sql
CREATE TABLE likes
(
	liker_id INT NOT NULL,
	image_id INT NOT NULL,
	UNIQUE (liker_id,image_id)
);
```

---
##	"logins":

```sql
CREATE TABLE logins
(
	user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(100) NOT NULL,
	password VARCHAR(100) NOT NULL,
	UNIQUE (email)
);
```

---
##	"profiles":

```sql
CREATE TABLE profiles
(
	profile_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(100) NOT NULL,
	website VARCHAR(100) NOT NULL,
	firstname VARCHAR(100) NOT NULL,
	lastname VARCHAR(100) NOT NULL,
	mood_message VARCHAR(200) NOT NULL,
	owner_id INT NOT NULL
);
```

---
##	"profile_sharing"

```sql
CREATE TABLE profile_sharing
(
	profile_id INT NOT NULL,
	user_id INT NOT NULL,
	accepted CHAR(1) NOT NULL,
	UNIQUE (profile_id,user_id)
);
```

---
## "blocks":

```sql
CREATE TABLE blocks
(
	blocker_id INT NOT NULL,
	blocked_id INT NOT NULL,
	UNIQUE (blocker_id, blocked_id)
);
```

---
## "posts":

```sql
CREATE TABLE posts
(
	post_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	post_text VARCHAR(1000) NOT NULL,
	repost CHAR(1) NOT NULL,
	private CHAR(1) NOT NULL
);
```

---
## "friends":

```sql
CREATE TABLE friends
(
	friender_id INT NOT NULL,
	friend_id INT NOT NULL,
	accepted CHAR(1) NOT NULL
	UNIQUE (friender_id,friend_id)
);
```

===
# SQL Users

## Local User
```sql
CREATE USER 'pictobattle'@'localhost';
GRANT ALTER, INSERT, SELECT ON pictobattle.* TO 'pictobattle'@'localhost';
```
The user can access and alter all of the tables in the database "pictobattle"
---

## External User
```sql
CREATE USER 'pictoext'@'lucieng.ddns.net';
GRANT ALTER, INSERT, SELECT ON pictobattle.* TO 'pictoext'@'%' IDENTIFIED BY 'picto1Battle';
```
