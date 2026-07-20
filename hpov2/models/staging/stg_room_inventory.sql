WITH source AS (
    select * 
    FROM {{source('HPO_V2', 'FACT_ROOM_INVENTORY')}}
)

SELECT *
FROM source
