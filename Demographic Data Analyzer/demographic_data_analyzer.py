import pandas as pd

def analyze_demographic_data(display_output=True):
    # Load the dataset
    data_frame = pd.read_csv("adult.data.csv")

    # Count the number of occurrences for each race in the dataset
    race_distribution = data_frame['race'].value_counts()

    # Compute the average age of male participants
    male_participants = data_frame[data_frame['sex'] == "Male"]
    avg_age_males = round(male_participants['age'].mean(), 1)

    # Calculate the percentage of individuals holding a Bachelor's degree
    bachelors_degree = data_frame[data_frame['education'] == "Bachelors"]
    bachelors_percentage = round(bachelors_degree.shape[0] / data_frame.shape[0] * 100, 1)

    # Determine the percentage of people with higher education (Bachelors, Masters, Doctorate) earning more than 50K
    higher_education = data_frame[data_frame['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = data_frame[~data_frame['education'].isin(["Bachelors", "Masters", "Doctorate"])]

    higher_education_earning_50k = round(higher_education[higher_education['salary'] == ">50K"].shape[0] / higher_education.shape[0] * 100, 1)
    lower_education_earning_50k = round(lower_education[lower_education['salary'] == ">50K"].shape[0] / lower_education.shape[0] * 100, 1)

    # Find the minimum hours per week worked
    minimum_working_hours = data_frame['hours-per-week'].min()

    # Calculate the percentage of people working the minimum number of hours per week and earning more than 50K
    min_hours_workers = data_frame[data_frame['hours-per-week'] == minimum_working_hours]
    rich_min_hour_workers = round(min_hours_workers[min_hours_workers['salary'] == ">50K"].shape[0] / min_hours_workers.shape[0] * 100, 1)

    # Identify the country with the highest percentage of people earning more than 50K
    high_income_by_country = data_frame[data_frame['salary'] == ">50K"]['native-country'].value_counts()
    total_by_country = data_frame['native-country'].value_counts()
    country_earning_percentage = high_income_by_country / total_by_country * 100

    top_earning_country = country_earning_percentage.idxmax()
    top_country_percentage = round(country_earning_percentage.max(), 1)

    # Determine the most common occupation for people earning more than 50K in India
    top_occupation_india = data_frame[(data_frame['salary'] == ">50K") & (data_frame['native-country'] == "India")]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if display_output:
        print("Race count:\n", race_distribution)
        print("Average age of males:", avg_age_males)
        print(f"Percentage with Bachelor's degrees: {bachelors_percentage}%")
        print(f"Percentage of higher education earning >50K: {higher_education_earning_50k}%")
        print(f"Percentage of lower education earning >50K: {lower_education_earning_50k}%")
        print(f"Minimum work hours: {minimum_working_hours} hours/week")
        print(f"Percentage of high earners among those who work the least: {rich_min_hour_workers}%")
        print("Country with highest percentage of high earners:", top_earning_country)
        print(f"Highest percentage of high earners in a country: {top_country_percentage}%")
        print("Top occupation in India:", top_occupation_india)

    return {
        'race_distribution': race_distribution,
        'avg_age_males': avg_age_males,
        'bachelors_percentage': bachelors_percentage,
        'higher_education_earning_50k': higher_education_earning_50k,
        'lower_education_earning_50k': lower_education_earning_50k,
        'minimum_working_hours': minimum_working_hours,
        'rich_min_hour_workers': rich_min_hour_workers,
        'top_earning_country': top_earning_country,
        'top_country_percentage': top_country_percentage,
        'top_occupation_india': top_occupation_india
    }

analyze_demographic_data()
