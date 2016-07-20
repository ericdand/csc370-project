USE saiddit;

INSERT INTO Accounts
VALUES("bob", "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362931b9824", 45);

INSERT INTO Accounts 
VALUES("jane", "2ce24dba5fb0a30e26e83b2ac5b2229e1b161e5c1fa7425e73043362931b9824", 0);

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

