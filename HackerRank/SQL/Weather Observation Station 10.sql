SELECT DISTINCT city
FROM   station
WHERE  city not RLIKE '[aeiouAEIOU]$'