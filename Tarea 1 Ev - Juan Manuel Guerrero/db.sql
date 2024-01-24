CREATE TABLE client (
email VARCHAR(40) PRIMARY KEY,
password VARCHAR(32)
);
CREATE TABLE bike (
bike_id INT PRIMARY KEY AUTO_INCREMENT,
model VARCHAR(40),
color VARCHAR(40),
);
CREATE TABLE rental (
email VARCHAR(40),
bike_id INT,
ini_dt DATE,
end_dt DATE,
PRIMARY KEY (email, bike_id, ini_dt),
FOREIGN KEY (email) REFERENCES client(email),
FOREIGN KEY (bike_id) REFERENCES bike(bike_id)
);
