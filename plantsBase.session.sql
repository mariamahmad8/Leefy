CREATE DATABASE plant_db;

DROP TABLE IF EXISTS plant_information;
DROP TABLE IF EXISTS USER;


-- @block
 TABLE USER (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password TEXT NOT NULL
);

-- @block
CREATE TABLE plant_information (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  type VARCHAR(255) NOT NULL,
  soil VARCHAR(255),
  location TEXT,
  water_freq VARCHAR(255),
  light_needs VARCHAR(255),
  extra_info TEXT,
  owner_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (owner_id) REFERENCES USER(id)
);



-- @block
INSERT INTO USER (name, email, password) VALUES
  ('Mariam', 'm.ahmad0826@gmail.com', 'enterpass]'); 

-- @block
INSERT INTO plant_information (owner_id, name, soil, type, location) VALUES
  (1, 'tomato', 'dry', 'vegetable', 'bedroom'),
  (1, 'carrot', 'wet', 'vegetable', 'kitchen'),
  (1, 'lily', 'dry', 'flower', 'garage');

-- @block
SELECT * FROM plant_information
WHERE type = 'vegetable'
AND name LIKE 't%';

-- @block
CREATE INDEX name_index ON plant_information(name);


-- @block
SELECT * FROM USER
INNER JOIN plant_information
ON plant_information.owner_id = USER.id;