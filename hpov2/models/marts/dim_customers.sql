SELECT
{{dbt_utils.generate_surrogate_key(['customer_id'])}} as customer_key,
customer_id,
customer_name,
country,
nationality,
loyalty_member,
customer_segment,
loyalty_tier,
FROM {{ref('stg_customers')}}