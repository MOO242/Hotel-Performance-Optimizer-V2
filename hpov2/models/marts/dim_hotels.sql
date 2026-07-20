SELECT
{{dbt_utils.generate_surrogate_key(['property_id'])}} as hotel_key,
property_id,
property_name,
brand,
region,
country,
hotel_category,
city,
room_capacity,
opening_date,

FROM {{ref('stg_hotels')}}

