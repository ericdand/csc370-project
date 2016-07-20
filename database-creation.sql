DROP DATABASE IF EXISTS saiddit;
CREATE DATABASE saiddit;

USE saiddit;

CREATE TABLE Accounts(
username VARCHAR(20) PRIMARY KEY,
password VARCHAR(64) NOT NULL,
reputation INT DEFAULT 0
); 

CREATE TABLE Subsaiddits(
title VARCHAR(40) PRIMARY KEY,
description VARCHAR(255) NOT NULL DEFAULT "",
default_or_not_default VARCHAR(20) NOT NULL,
creator VARCHAR(20),
created_time DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (creator) REFERENCES Accounts(username) ON DELETE SET NULL
);

CREATE TABLE Friends(
first  VARCHAR(20),
second VARCHAR(20),
PRIMARY KEY (first, second),
FOREIGN KEY (first) REFERENCES Accounts(username) ON DELETE CASCADE,
FOREIGN KEY (second) REFERENCES Accounts(username) ON DELETE CASCADE
); 
				
CREATE TABLE Posts(      
id INT AUTO_INCREMENT PRIMARY KEY,
author VARCHAR(20) NOT NULL,
title VARCHAR(80) NOT NULL,
url VARCHAR(256),
text VARCHAR(10000) NOT NULL DEFAULT "",
subsaiddit VARCHAR(40) NOT NULL,
upvotes INT NOT NULL DEFAULT 0,
downvotes INT NOT NULL DEFAULT 0,
created DATETIME DEFAULT CURRENT_TIMESTAMP,
last_edited DATETIME,
FOREIGN KEY (author) REFERENCES Accounts(username) ON DELETE CASCADE,
FOREIGN KEY (subsaiddit) REFERENCES Subsaiddits(title) ON DELETE CASCADE
);

CREATE TABLE Favourites(
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL, 
post_id INT NOT NULL,
FOREIGN KEY (post_id) REFERENCES Posts(id) ON DELETE CASCADE,
FOREIGN KEY (username) REFERENCES Accounts(username) /* No "on delete cascade here", since Posts already cascades when the user is deleted. */
);

CREATE TABLE Votes_on_posts(
id INT NOT NULL AUTO_INCREMENT,
username VARCHAR(20) NOT NULL, 
post_id INT NOT NULL,
upvote_or_downvote VARCHAR(8) NOT NULL,
PRIMARY KEY (id, username),
FOREIGN KEY (username) REFERENCES Accounts(username) ON DELETE CASCADE,
FOREIGN KEY (post_id) REFERENCES Posts(id) ON DELETE CASCADE
);

CREATE TABLE Subscribers(
subsaiddit VARCHAR(40) NOT NULL REFERENCES Subsaiddits(title) ON DELETE CASCADE,
username VARCHAR(20) NOT NULL REFERENCES Accounts(username) ON DELETE CASCADE,
PRIMARY KEY (subsaiddit, username)
);

CREATE TABLE Comments(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(20) NOT NULL, 
text VARCHAR(255) NOT NULL,
parent_id INT NOT NULL,
upvotes INT DEFAULT 0, /* We track up/downvotes directly here so that we don’t have to query the Votes_on_comments table so much. */
downvotes INT DEFAULT 0, /* Note to implementers: keep these counts accurate! */
published_time DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (parent_id) REFERENCES Posts(id) ON DELETE CASCADE	
);

CREATE TABLE Votes_on_comments( 
	username VARCHAR(20),
	comment_id INT,
upvote_or_downvote VARCHAR(8) NOT NULL, 
created DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (username, comment_id),	
FOREIGN KEY (username) REFERENCES Accounts(username) ON DELETE CASCADE,
FOREIGN KEY (comment_id) REFERENCES Comments(id) ON DELETE CASCADE	
);
