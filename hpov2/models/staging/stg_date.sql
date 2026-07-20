WITH source AS (
    SELECT * 
    FROM {{ source('HPO_V2', 'DIM_DATE') }}
)

SELECT *
FROM source