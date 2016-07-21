USE saiddit;

/* Both bob and jane's passwords are (the sha-256 digest of) their names. */
INSERT INTO Accounts
VALUES("bob", "81b637d8fcd2c6da6359e6963113a1170de795e4b725b84d1e0b4cfd9ec58ce9", 45);

INSERT INTO Accounts 
VALUES("jane", "81f8f6dde88365f3928796ec7aa53f72820b06db8664f5fe76a7eb13e24546a2", 0);

INSERT INTO Friends
VALUES("bob", "jane"); 

INSERT INTO Subsaiddits (title, description, default_or_not_default, creator)
VALUES("pokemon", "for discussion of all things pokemon", "default", "bob");  

INSERT INTO Posts (author, title, url, text, subsaiddit)
VALUES("bob", "Pokemon Go is cool", "http://www.pokemon.com", "For serious, guys.", "pokemon");

INSERT INTO Favourites (username, post_id)
VALUES("bob", 1); 

INSERT INTO Votes_on_posts (post_id, username, upvote_or_downvote)
VALUES(1, "bob", "upvote"); 

INSERT INTO Subscribers
VALUES("pokemon", "bob");

INSERT INTO Comments (username, text, parent_id)
VALUES("jane", "hahahahaha", 1); 	

INSERT INTO Votes_on_comments (username, comment_id, upvote_or_downvote)
VALUES("bob", 1, "upvote");

