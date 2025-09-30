--  !- Start 1-1

CREATE TABLE students (
  student_id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  mobile VARCHAR(50)
);


INSERT INTO students VALUES (DEFAULT, 'Jack Sparrow', 28, '999-999-9999');
INSERT INTO students VALUES (DEFAULT, 'Jilly Cakes', 30, '910-111-1111');
INSERT INTO students VALUES (DEFAULT, 'Johnny Bananas', 25, '678-111-1234');
INSERT INTO students VALUES (DEFAULT, 'Jackie Lackie', 101, '910-456-7890');
INSERT INTO students VALUES (DEFAULT, 'Slaggy McRaggy', 28);

SELECT * FROM students;

-- 2
CREATE TABLE address (
	address_id SERIAL PRIMARY Key,
	street VARCHAR(150),
	city VARCHAR(50),
	state VARCHAR(10)
);

ALTER TABLE students ADD COLUMN student_address_id INT;

ALTER TABLE students 
ADD CONSTRAINT fk_student_address 
FOREIGN KEY (student_address_id) 
REFERENCES address (address_id);


-- Step-3

INSERT INTO address VALUES (DEFAULT, '200 Horton Ave', 'Lynbrook', 'NY');
INSERT INTO address VALUES (DEFAULT, '123 Webdev Dr', 'Boston', 'MA');
INSERT INTO address VALUES (DEFAULT, '555 Five St', 'Fivetowns', 'NY');
INSERT INTO address VALUES (DEFAULT, '2 OldForThis Ct', 'Fivetowns', 'NY');

update students set student_address_id = 1 where name = 'Jack Sparrow';
update students set student_address_id = 2 where student_id = 3;
update students set student_address_id = 3 where student_id = 4;
update students set student_address_id = 4 where student_id = 5;



--  !- END 1-1

-- !- Start 1-M
-- Step-4 





-- !- END  1-M
