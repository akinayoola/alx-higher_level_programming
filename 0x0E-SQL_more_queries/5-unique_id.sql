-- a script that creates the table unique_id
CREATE TABLE IF NOT EXISTS (id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
);
