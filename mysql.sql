-- -- CRUD -- --

-- CREATE

INSERT INTO cats_table (name) VALUES ("Mrs Kitty");
-- also adds the id aka the primary key
-- each cat needs a primary key - they are unique - no two cats get the same id

-- READ

SELECT * FROM cats_table; -- all cats
SELECT * FROM cats_table WHERE id = 1; -- specific cat with id = 1
SELECT * FROM cats_table WHERE name = "Mrs Kitty"; -- specific cat with id = 1
SELECT * FROM cats_table LIMIT 1; -- returns only 1 cat
SELECT * FROM cats_table ORDER BY name DESC; -- returns cats in reverse alphabetical order (z-a)

-- UPDATE

UPDATE cats_table SET name = "Ms Kitty"; -- sets all names to Ms Kitty
UPDATE cats_table SET name = "Ms Kitty" WHERE id = 1; -- set name for cat with id = 1
UPDATE cats_table SET name = "Ms Kitty" WHERE name = "Mrs Kitty"; -- set name for cat with name = Mrs Kitty

-- DELETE

DELETE FROM cats_table; -- delete all the cats in the table
DROP TABLE cats_table;
DELETE FROM cats_table WHERE id = 1; -- delete specific cat

-- -- FOREIGN KEYS -- -- 

CREATE TABLE cats_table (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE cat_toys_table (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
cat_id INTEGER -- foreign key - connects the two tables
);

-- one to many relationship - cat toy belongs to a cat
-- one cat has many toys
-- foreign key always goes into the table with the many in a one to many