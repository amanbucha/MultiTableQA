SELECT river.river_name FROM river WHERE river.traverse IN (SELECT city.state_name FROM city WHERE city.population = (SELECT max(city.population) FROM city));;
SELECT city.city_name FROM city WHERE city.population=(SELECT min(city.population) FROM city WHERE city.state_name 
IN(SELECT state.state_name FROM state WHERE state.area=(SELECT max(state.area) FROM state)));
SELECT highlow.highest_point FROM highlow WHERE highlow.state_name IN(SELECT border_info.border FROM border_info WHERE border_info.state_name='mississippi');;
SELECT distinct river.river_name FROM river WHERE river.length IN ( SELECT max(mx) FROM (  SELECT river.traverse, max(river.length) AS mx FROM river WHERE river.traverse IN ( SELECT border_info.state_name FROM border_info WHERE border_info.border IN (SELECT border_info.border FROM border_info GROUP BY border_info.border having count(1) = (SELECT max(cnt1) FROM (SELECT border_info.border, count(1) AS cnt1 FROM border_info GROUP BY border_info.border) tmp1) ) ) GROUP BY river.traverse ) tmp2 );;
SELECT state.state_name FROM state WHERE state.state_name NOT IN (SELECT border_info.state_name FROM border_info);;
