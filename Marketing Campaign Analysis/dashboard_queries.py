def get_country_kpi_query(country):

    if country == "All":
        return """
        SELECT
            COUNT(ID) AS total_customers,
            ROUND(AVG(Recency),2) AS avg_recency,
            ROUND((SUM(Response) * 100.0) / COUNT(ID),2) AS campaign_acceptance_rate,
            ROUND(AVG(Total_Spends),2) AS avg_spend_per_customer,
            ROUND(AVG(Total_Purchases), 2) AS avg_purchases_per_customer,
            SUM(AcceptedCmp1) AS accepted_cmp1,
            SUM(AcceptedCmp2) AS accepted_cmp2,
            SUM(AcceptedCmp3) AS accepted_cmp3,
            SUM(AcceptedCmp4) AS accepted_cmp4,
            SUM(AcceptedCmp5) AS accepted_cmp5,
            SUM(Response) AS response_count,
            SUM(Complain) AS complain_count
        FROM customers
        """, {}

    return """
    SELECT
        COUNT(ID) AS total_customers,
        ROUND(AVG(Recency),2) AS avg_recency,
        ROUND((SUM(Response) * 100.0) / COUNT(ID),2) AS campaign_acceptance_rate,
        ROUND(AVG(Total_Spends),2) AS avg_spend_per_customer,
        ROUND(AVG(Total_Purchases), 2) AS avg_purchases_per_customer,      
        SUM(AcceptedCmp1) AS accepted_cmp1,
        SUM(AcceptedCmp2) AS accepted_cmp2,
        SUM(AcceptedCmp3) AS accepted_cmp3,
        SUM(AcceptedCmp4) AS accepted_cmp4,
        SUM(AcceptedCmp5) AS accepted_cmp5,
        SUM(Response) AS response_count,
        SUM(Complain) AS complain_count
    FROM customers
    WHERE Country = %(country)s
    """, {"country": country}

def get_spend_query(country):

    if country == "All":
        return """
        SELECT
            SUM(MntWines) AS Wines,
            SUM(MntFruits) AS Fruits,
            SUM(MntMeatProducts) AS MeatProducts,
            SUM(MntFishProducts) AS FishProducts,
            SUM(MntSweetProducts) AS SweetProducts,
            SUM(MntGoldProds) AS GoldProducts
        FROM customers
        """, {}

    return """
    SELECT
        SUM(MntWines) AS Wines,
        SUM(MntFruits) AS Fruits,
        SUM(MntMeatProducts) AS MeatProducts,
        SUM(MntFishProducts) AS FishProducts,
        SUM(MntSweetProducts) AS SweetProducts,
        SUM(MntGoldProds) AS GoldProducts
    FROM customers
    WHERE Country = %(country)s
    """, {"country": country}

def get_purchase_query(country):

    if country == "All":
        return """
        SELECT
            COALESCE(SUM(NumDealsPurchases),0) AS DealPurchases,
            COALESCE(SUM(NumWebPurchases),0) AS WebPurchases,
            COALESCE(SUM(NumCatalogPurchases),0) AS CatalogPurchases,
            COALESCE(SUM(NumStorePurchases),0) AS StorePurchases
        FROM customers
        """, {}

    return """
    SELECT
        COALESCE(SUM(NumDealsPurchases),0) AS DealPurchases,
        COALESCE(SUM(NumWebPurchases),0) AS WebPurchases,
        COALESCE(SUM(NumCatalogPurchases),0) AS CatalogPurchases,
        COALESCE(SUM(NumStorePurchases),0) AS StorePurchases
    FROM customers
    WHERE Country = %(country)s
    """, {"country": country}

def get_age_vs_income_query():

    return """
    -- Individual Countries
    SELECT
        Country,
        CASE
            WHEN Income < 25000 THEN '0-25K'
            WHEN Income BETWEEN 25000 AND 49999 THEN '25K-50K'
            WHEN Income BETWEEN 50000 AND 74999 THEN '50K-75K'
            WHEN Income BETWEEN 75000 AND 99999 THEN '75K-100K'
            WHEN Income BETWEEN 100000 AND 124999 THEN '100K-125K'
            ELSE '125K+'
        END AS Income_Group,

        CASE
            WHEN (EXTRACT(YEAR FROM CURRENT_DATE) - Year_Birth) BETWEEN 30 AND 50 THEN '30 to 50'
            WHEN (EXTRACT(YEAR FROM CURRENT_DATE) - Year_Birth) BETWEEN 51 AND 60 THEN '51 to 60'
            WHEN (EXTRACT(YEAR FROM CURRENT_DATE) - Year_Birth) BETWEEN 61 AND 90 THEN '61 to 90'
            ELSE 'Other'
        END AS Age_Group,

        COUNT(*) AS Customer_Count
    FROM customers
    GROUP BY
        Country,
        Income_Group,
        Age_Group

    UNION ALL

    -- Combined Total Category
    SELECT
        'All Countries' AS Country,

        CASE
            WHEN Income < 25000 THEN '0-25K'
            WHEN Income BETWEEN 25000 AND 49999 THEN '25K-50K'
            WHEN Income BETWEEN 50000 AND 74999 THEN '50K-75K'
            WHEN Income BETWEEN 75000 AND 99999 THEN '75K-100K'
            WHEN Income BETWEEN 100000 AND 124999 THEN '100K-125K'
            ELSE '125K+'
        END AS Income_Group,

        CASE
            WHEN (EXTRACT(YEAR FROM CURRENT_DATE) - Year_Birth) BETWEEN 30 AND 50 THEN '30 to 50'
            WHEN (EXTRACT(YEAR FROM CURRENT_DATE) - Year_Birth) BETWEEN 51 AND 60 THEN '51 to 60'
            WHEN (EXTRACT(YEAR FROM CURRENT_DATE) - Year_Birth) BETWEEN 61 AND 90 THEN '61 to 90'
            ELSE 'Other'
        END AS Age_Group,

        COUNT(*) AS Customer_Count
    FROM customers
    GROUP BY
        Income_Group,
        Age_Group
    """, {}

def get_education_vs_income_query():

    return """
    -- Individual Countries
    SELECT
        Country,
        CASE
            WHEN Income < 25000 THEN '0-25K'
            WHEN Income BETWEEN 25000 AND 49999 THEN '25K-50K'
            WHEN Income BETWEEN 50000 AND 74999 THEN '50K-75K'
            WHEN Income BETWEEN 75000 AND 99999 THEN '75K-100K'
            WHEN Income BETWEEN 100000 AND 124999 THEN '100K-125K'
            ELSE '125K+'
        END AS Income_Group,
        Education,
        COUNT(*) AS Customer_Count
    FROM customers
    GROUP BY
        Country,
        Income_Group,
        Education

    UNION ALL

    -- Combined Total Category
    SELECT
        'All Countries' AS Country,
        CASE
            WHEN Income < 25000 THEN '0-25K'
            WHEN Income BETWEEN 25000 AND 49999 THEN '25K-50K'
            WHEN Income BETWEEN 50000 AND 74999 THEN '50K-75K'
            WHEN Income BETWEEN 75000 AND 99999 THEN '75K-100K'
            WHEN Income BETWEEN 100000 AND 124999 THEN '100K-125K'
            ELSE '125K+'
        END AS Income_Group,
        Education,
        COUNT(*) AS Customer_Count
    FROM customers
    GROUP BY
        Income_Group,
        Education
    """, {}

def get_marital_vs_income_query():
    """
    Groups customers by both Income Bracket and Marital Status.
    Includes an 'All Countries' aggregate total alongside individual countries.
    """

    return """
    -- Individual Countries
    SELECT
        Country,
        CASE
            WHEN Income < 25000 THEN '0-25K'
            WHEN Income BETWEEN 25000 AND 49999 THEN '25K-50K'
            WHEN Income BETWEEN 50000 AND 74999 THEN '50K-75K'
            WHEN Income BETWEEN 75000 AND 99999 THEN '75K-100K'
            WHEN Income BETWEEN 100000 AND 124999 THEN '100K-125K'
            ELSE '125K+'
        END AS Income_Group,
        Marital_Status,
        COUNT(*) AS Customer_Count
    FROM customers
    GROUP BY
        Country,
        Income_Group,
        Marital_Status

    UNION ALL

    -- Combined Total Category
    SELECT
        'All Countries' AS Country,
        CASE
            WHEN Income < 25000 THEN '0-25K'
            WHEN Income BETWEEN 25000 AND 49999 THEN '25K-50K'
            WHEN Income BETWEEN 50000 AND 74999 THEN '50K-75K'
            WHEN Income BETWEEN 75000 AND 99999 THEN '75K-100K'
            WHEN Income BETWEEN 100000 AND 124999 THEN '100K-125K'
            ELSE '125K+'
        END AS Income_Group,
        Marital_Status,
        COUNT(*) AS Customer_Count
    FROM customers
    GROUP BY
        Income_Group,
        Marital_Status
    """, {}

def get_family_vs_income_query():

    return """
    -- Individual Countries
    SELECT
        Country,
        CASE
            WHEN Income < 25000 THEN '0-25K'
            WHEN Income BETWEEN 25000 AND 49999 THEN '25K-50K'
            WHEN Income BETWEEN 50000 AND 74999 THEN '50K-75K'
            WHEN Income BETWEEN 75000 AND 99999 THEN '75K-100K'
            WHEN Income BETWEEN 100000 AND 124999 THEN '100K-125K'
            ELSE '125K+'
        END AS Income_Group,
        CASE
            WHEN Family_Customer = 1 THEN 'Family Customer'
            ELSE 'Non-Family Customer'
        END AS Family_Status,
        COUNT(*) AS Customer_Count
    FROM customers
    GROUP BY
        Country,
        Income_Group,
        Family_Status

    UNION ALL

    -- Combined Total Category
    SELECT
        'All Countries' AS Country,
        CASE
            WHEN Income < 25000 THEN '0-25K'
            WHEN Income BETWEEN 25000 AND 49999 THEN '25K-50K'
            WHEN Income BETWEEN 50000 AND 74999 THEN '50K-75K'
            WHEN Income BETWEEN 75000 AND 99999 THEN '75K-100K'
            WHEN Income BETWEEN 100000 AND 124999 THEN '100K-125K'
            ELSE '125K+'
        END AS Income_Group,
        CASE
            WHEN Family_Customer = 1 THEN 'Family Customer'
            ELSE 'Non-Family Customer'
        END AS Family_Status,
        COUNT(*) AS Customer_Count
    FROM customers
    GROUP BY
        Income_Group,
        Family_Status
    """, {}