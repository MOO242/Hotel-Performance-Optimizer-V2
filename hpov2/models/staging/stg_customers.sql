WITH source AS (
    select * 
    FROM {{source('HPO_V2', 'DIM_CUSTOMERS')}}
)

SELECT *
FROM source