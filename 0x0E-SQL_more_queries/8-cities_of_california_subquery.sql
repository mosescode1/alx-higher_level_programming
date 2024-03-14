-- Write a script that lists all cities contained in the database hbtn_0d_usa.
USE hbtn_0d_usa;

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM state
                    WHERE name='California'
                )
ORDER BY id;