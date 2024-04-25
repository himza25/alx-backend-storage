-- Lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name,
       IF(split IS NOT NULL, split - formed, 2022 - formed) AS lifespan
FROM bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
