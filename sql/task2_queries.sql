-- 1. Display all records
SELECT *
FROM superstore_cleaned;

-- 2. Filter records using WHERE
SELECT *
FROM superstore_cleaned
WHERE Category = 'Furniture';

-- 3. Sort records using ORDER BY
SELECT *
FROM superstore_cleaned
ORDER BY Sales DESC;

-- 4. Display Top 10 records using LIMIT
SELECT *
FROM superstore_cleaned
ORDER BY Sales DESC
LIMIT 10;

-- 5. Group records by Category
SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM superstore_cleaned
GROUP BY Category;

-- 6. Filter grouped data using HAVING
SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM superstore_cleaned
GROUP BY Category
HAVING SUM(Sales) > 100000;