-- Lists all Glam rock bands by longevity, handling bands still active as of 2022
SELECT 
    band_name, 
    IF(split IS NOT NULL AND split != 0, split - formed, 2022 - formed) AS lifespan
FROM 
    metal_bands
WHERE 
    main_style = 'Glam rock' 
ORDER BY 
    lifespan DESC;
