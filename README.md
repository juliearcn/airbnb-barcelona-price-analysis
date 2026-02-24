# Airbnb Barcelona Price Analysis

## Project Overview
This project aims to identify the main factors influencing Airbnb listing prices in Barcelona.
The objective is to identify the most significant variables affecting pricing in order to better understand the structure and dynamics of the local short-term rental market.

## Data Source
The dataset comes from [**Inside Airbnb – Barcelona (Summary Listings)**](https://insideairbnb.com/fr/get-the-data/).

After cleaning missing values and removing outliers, the final dataset contains **14,513 listings**.

## Key Questions
The analysis is structured around the following key questions:
1. What is the impact of room type on price?
2. How do prices vary across neighborhoods?
3. Does the number of reviews influence pricing?

## Data Cleaning
### Missing Values 
Since **price** is the target variable, all listings with missing price values were removed.
The dataset was reduced from 19,410 to **15,276 listings**.

### Outlier Treatment
The price distribution was highly right-skewed, with extreme values reaching up to €10,000.
To prevent these outliers from biasing the analysis, listings above the **95th percentile (€425)** were excluded.
The final working dataset includes **14,513 listings**.

### Methodological Rationale
These steps ensure a more representative sample of the “standard” market and improve the robustness of statistical comparisons.

## Analysis 1 - Room Type 

### Objective
To evaluate whether **room type** significantly influences pricing.

### Main Findings
The analysis highlights a clear market segmentation.

**Hotels** and **entire homes/apartments** exhibit the highest median prices.
Entire homes/apartments show significantly greater price dispersion, indicating strong heterogeneity within this segment (from budget studios to high-end properties).
In contrast, hotels display a more concentrated price distribution, suggesting a more standardized pricing strategy.

**Private** and **shared rooms** represent the most affordable segments, although some private rooms are positioned within the premium range.

### Key Insight
Room type is a strong determinant factor of Airbnb pricing in Barcelona, creating a clear segmentation between premium and budget markets.

## Analysis 2 - Neighborhood

### Objective
To assess the impact of **location** on pricing. 

### Main Findings
Significant median price differences are observed across neighborhoods.
Eixample shows the highest median price (€165), while Nou Barris displays the lowest (€64), representing a gap of over €100.

### Cross-Analysis (Neighborhood x Room Type)
Even when controlling for room type, substantial differences remain.
For example, entire homes reach a median of €198 in Eixample compared to €100.5 in Ciutat Vella. This confirms Eixample's premium position within the market.

Interestingly, Ciutat Vella (historically a highly touristic and central district) does not display the highest prices.
This suggests that centrality and tourism alone do not fully explain pricing differences.

Several hypotheses may account for this:

- Smaller average property sizes in the historic center.
- High competition leading to price pressure.
- Dense supply creating competitive dynamics.

Unobserved variables such as property size, quality, or amenities likely contribute to these differences.

### Key Insight
Location is a major pricing determinant, though its impact varies depending on specific neighborhood characteristics not fully captured in the dataset.

## Analysis 3 - Number of Reviews 

### Objective 
To determine whether listing popularity (measured by **total reviews**) influence pricing. 

### Descriptive Observation
The number of reviews is highly right-skewed. 
Most listings have fewer than 10 reviews, while a small minority accumulate very high counts (up to 1,820).

### Main Result 
Listings without reviews show a significantly lower median price (€91) compared to those with at least one review (€140).

### Interpretation
This suggest that newer or less active listings may adopt more aggressive pricing strategies to attract their firts bookings.
However, beyond the distinction between zero and non-zero reviews, the total number of reviews does not appear to be a primary pricing determinant compared to room type and location.

### Key Insight
The number of reviews reflects listing maturity and activity more than premium positioning.

# Conclusion
The analysis reveals a clearly structured Airbnb market in Barcelona.
- **Room type** is the most determinant factor in pricing segmentation.
- **Location** plays a major role, with significant differences across neighborhoods, even when controlling for room type.
- **Number of reviews** has a more limited impact, mainly reflecting entry-stage pricing strategies.

Overall, Airbnb pricing in Barcelona appears to be primarily driven by the nature of the property and its location rather than its popularity level.