
CREATE DATABASE IF NOT EXISTS SQLDB;
use SQLDB;

CREATE TABLE SQLTABLE (
  name VARCHAR(20),
  color VARCHAR(max)
);

INSERT INTO SQLTABLE
  (name, color)
VALUES
  ('0', 'https://media4.giphy.com/media/QMHoU66sBXqqLqYvGO/giphy.gif');
