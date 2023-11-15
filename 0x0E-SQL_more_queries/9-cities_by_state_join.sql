-- list all cities contained in database
SELECT dities.id, cities.name, states.name FROM cities JOIN states
WHERE cities.state_id = states.id ORDER BY cities.id ASC;
