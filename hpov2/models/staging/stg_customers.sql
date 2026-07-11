WITH source AS (
    select * 
    FROM {{source('HPO_V2', 'RAW_DIM_CUSTOMERS')}}
)

SELECT *
FROM source