
SELECT * FROM regions;
SELECT * FROM species;
SELECT * FROM climate;
SELECT * FROM observations;


-- Mission 1: Which regions have the most recorded species?
SELECT r.name AS region_name, COUNT(DISTINCT o.species_id) AS unique_species_count
FROM regions r
JOIN observations o ON r.id = o.region_id
GROUP BY r.name
ORDER BY unique_species_count DESC;

-- Mission 2: Which months have the highest observation activity?
SELECT strftime('%m', observation_date) AS month, COUNT(*) AS observation_count
FROM observations
GROUP BY month
ORDER BY observation_count DESC;

-- Mission 3: Detect species with few recorded individuals.
SELECT s.common_name, COUNT(*) AS observation_count
FROM species s
JOIN observations o ON s.id = o.species_id
GROUP BY s.common_name
ORDER BY observation_count ASC
LIMIT 10; -- Limit to the 10 least observed, adjust as needed

-- Mission 4: Which region has the highest number of distinct species observed?
SELECT r.name AS region_name, COUNT(DISTINCT o.species_id) AS unique_species_count
FROM regions r
JOIN observations o ON r.id = o.region_id
GROUP BY r.name
ORDER BY unique_species_count DESC
LIMIT 1;

-- Mission 5: Which species have been observed most frequently?
SELECT s.common_name, COUNT(*) AS observation_frequency
FROM species s
JOIN observations o ON s.id = o.species_id
GROUP BY s.common_name
ORDER BY observation_frequency DESC
LIMIT 10; -- Limit to the 10 most observed

-- Mission 6: Who are the people with the most observation records?
SELECT observer_name, COUNT(*) AS observation_count
FROM observations
GROUP BY observer_name
ORDER BY observation_count DESC
LIMIT 10; -- Limit to the top 10 observers

-- Mission 7: Which species have never been observed?
SELECT s.common_name
FROM species s
LEFT JOIN observations o ON s.id = o.species_id
WHERE o.id IS NULL;

-- Mission 8: On which dates were the most distinct species observed?
SELECT observation_date, COUNT(DISTINCT species_id) AS distinct_species_count
FROM observations
GROUP BY observation_date
ORDER BY distinct_species_count DESC
LIMIT 10;
