-- lists all the cities of california that can be found in the database hbtn_0d_usa
-- results must be in ascending order by cities .id
-- Not allowed to use JOIN  keyword

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
);
