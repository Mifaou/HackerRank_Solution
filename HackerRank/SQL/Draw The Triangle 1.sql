SET @NUMBER = 21;
SELECT REPEAT('* ', @NUMBER := @NUMBER - 1)
    FROM information_schema.tables WHERE @NUMBER > 1;