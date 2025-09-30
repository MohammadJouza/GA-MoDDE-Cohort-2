v02: 25-09-30 | 11:55:44 - 
v02: 25-09-30 | 12:57:44 - 
25-09-30 | 14:25:11 - 
v03: 25-09-30 | 15:31:47 - 

--  !- Start 1-1
-- 1
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


-- 3

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
-- 
-- 25-09-30 | 12:06:03 - 

CREATE TABLE courses (
	course_id SERIAL PRIMARY KEY,
	course_code VARCHAR(10),
	course_name VARCHAR(100)
);

-- Example data
INSERT INTO courses (course_code, course_name) VALUES
('SE', 'Software Engineering'),
('DSI', 'Data Science Immersive'),
('UXD', 'User Experience Design'),
('WD',  'Web Development'),
('PM',  'Product Management');

CREATE TABLE instructors (
	instructor_id SERIAL PRIMARY KEY, 
	name VARCHAR(255) NOT NULL, 
	email VARCHAR(200) NOT NULL, 
	course_id INT REFERENCES courses(course_id)
);

-- SEI instructors (course_id = 1)
INSERT INTO instructors (name, email, course_id) VALUES
('Alice Johnson', 'alice@generalassembly.com', 1),
('Bob Smith', 'bob@generalassembly.com', 1),
('Jouza', 'jouza@generalassembly.com', 1),
('Purvi', 'purvi@generalassembly.com', 1),
('Israa', 'israa@generalassembly.com', 1);

-- DSI instructors (course_id = 2)
INSERT INTO instructors (name, email, course_id) VALUES
('Carol Lee', 'carol@generalassembly.com', 2),
('David Kim', 'david@generalassembly.com', 2);

-- UXD instructors (course_id = 3)
INSERT INTO instructors (name, email, course_id) VALUES
('Emma Brown', 'emma@generalassembly.com', 3);

-- WD instructors (course_id = 4)
INSERT INTO instructors (name, email, course_id) VALUES
('Frank Wilson', 'frank@generalassembly.com', 4),
('Grace Hall', 'grace@generalassembly.com', 4);

-- PM instructors (course_id = 5)
INSERT INTO instructors (name, email, course_id) VALUES
('Henry Clark', 'henry@generalassembly.com', 5);

-- !- END  1-M

-- !- Extra how to get all the Data
-- !- HW: read about JOIN & Left Join

SELECT c.course_code, c.course_name, i.name AS instructor_name
FROM courses c
LEFT JOIN instructors i
  ON c.course_id = i.course_id
ORDER BY c.course_code;


-- !- start  M-M
CREATE TABLE student_course_enrollment (
	enrollment_id SERIAL PRIMARY KEY,
	student_id INT REFERENCES students(student_id) NOT NULL,
	course_id INT REFERENCES courses(course_id) NOT NULL,
	UNIQUE (student_id, course_id)
);

-- Jack enrolls in SEI and PM
INSERT INTO student_course_enrollment (student_id, course_id) VALUES (1, 1);
INSERT INTO student_course_enrollment (student_id, course_id) VALUES (1, 5);

-- Jill enrolls in SEI and DSI
INSERT INTO student_course_enrollment (student_id, course_id) VALUES (2, 1);
INSERT INTO student_course_enrollment (student_id, course_id) VALUES (2, 2);

-- John enrolls in WD
INSERT INTO student_course_enrollment (student_id, course_id) VALUES (3, 4);

-- Jackie enrolls in UXD and SEI
INSERT INTO student_course_enrollment (student_id, course_id) VALUES (4, 3);
INSERT INTO student_course_enrollment (student_id, course_id) VALUES (4, 1);

-- Captain Barbossa teaches SEI but also "enrolls" in it (for peace on campus 😉)
INSERT INTO student_course_enrollment (student_id, course_id) VALUES (5, 1);

-- Slagathorn enrolls in nothing (mysterious one)

-- !- END  M-M
-- !- Read About JOIN
SELECT c.course_code, c.course_name, s.name AS student_name
FROM student_course_enrollment e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
ORDER BY c.course_code, s.name;

-- !- HW what happen if we delete the course which inside the join table