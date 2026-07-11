WITH source AS (
    select * 
    FROM {{source('HPO_V2', 'RAW_FACT_BOOKINGS')}}
)

SELECT *
