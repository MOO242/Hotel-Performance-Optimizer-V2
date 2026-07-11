WITH source AS (
    SELECT * 
    FROM {{ source('HPO_V2', 'RAW_DIM_DATE') }}
)

SELECT *
FROM source