CREATE TABLE authors (
    id       INTEGER      PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR (50) NOT NULL,
    email    VARCHAR (50) UNIQUE
                          NOT NULL,
    mobile   VARCHAR (25)
);