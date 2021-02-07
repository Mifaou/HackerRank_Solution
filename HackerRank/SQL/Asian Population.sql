Select SUM(City.Population)
From City, Country
Where Code = CountryCode And Continent = 'Asia';