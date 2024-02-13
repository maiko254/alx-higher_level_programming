-- lists all records of the table second_table except rows without name
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
