-- Lists all bands with Glam rock as their main style, ranked by their longevity
SET @this_year := 2022;  -- Sets the current year for calculating ongoing band lifespans

SELECT band_name,
       IF(split IS NULL, @this_year - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'  -- Allows for partial matches on the style column
ORDER BY lifespan DESC;
