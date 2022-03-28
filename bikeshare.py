import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    month = 0
    day = 0
    # Getting city name from user
    while True:
        city = input("What city you want to analyze(chicago, new york city, washington):").lower()
        if CITY_DATA.get(city, False):
            break
        else:
            print("That is not a city, Make sure you entered valid city")

    # Getting Type of filter to apply on data from user and storing them
    while True:
        filter_answer = input("Do you want to filter by month, day, both or no filter? ").lower()
        if filter_answer == 'month':
            while True:
                month = input("Enter the month number (1 >> 6) 1 for Jan, 2 for Feb ... etc ")
                if int(month) < 7 and int(month) > 0:
                    break
                else:
                    print("please enter a valid month number")
            break
        elif filter_answer == 'day':
            while True:
                day = input("enter a day ok week number (1 >> 7), 1 for Sat, 2 for Sun ... etc ")
                if int(day) < 8 and int(day) > 0:
                    
                    break
                else:
                    print("please enter a valid day number")
            break

        elif filter_answer == 'both':
            while True:
                month = input("Enter the month number (1 >> 6) 1 for Jan, 2 for Feb ... etc ")
                if int(month) < 7 and int(month) > 0:
                    break
                else:
                    print("please enter a valid month number")
            while True:
                day = input("enter a day ok week number (1 >> 7), 1 for Sat, 2 for Sun ... etc ")
                if int(day) < 8 and int(day) > 0:
                    
                    break
                else:
                    print("please enter a valid day number")

            break
        elif filter_answer == 'no filter':
            break
    print('-'*40)
    # Returning fitlers the user want to apply
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Reading the file witch the user seleted
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Creatin new columns containing every raw's month, weekday and hour
    df['month count'] = df['Start Time'].dt.month
    df['week day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    # Filtering the database by the filters whitch user selected
    if month:
        if day:
            df = df.loc[df['month count'] == int(month)]
            df = df.loc[df['week day'] == int(day)- 1]
        else:
            df = df.loc[df['month count'] == int(month)]
    elif day:
            df = df.loc[df['week day'] == int(day) - 1]
    
   
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # Making two dicts containg weekdays and months
    days = {0 : 'Saturday', 
            1 : 'Sunday',
            2 : 'Monday',
            3 : 'Tuesday',
            4 : 'Wednesday',
            5 : 'Thursday',
            6 : 'Friday'}
    months = {1 : 'January',
              2 : 'February',
              3 : 'March',
              4 : 'April',
              5 : 'May',
              6 : 'June',
              7 : 'July',
              8 : 'August',
              9 : 'September',
              10 : 'October',
              11 : 'November',
              12 : 'December'}
             
              

    # Display the most common month and day of week depent on the filter that user selected
    if not month and not day:
        
        most_common_day = df['week day'].mode()[0]
        print('Most common day for travel is ' + days[most_common_day])
        most_common_month = df['month count'].mode()[0]
        print('Most common month for travel is ' + months[most_common_month])

    elif not day:
        most_common_day = df['week day'].mode()[0]
        print('Most common day for travel is ' + days[most_common_day])

    # Display the most common start hour
    most_common_hour = df['hour'].mode()[0]
 
    print('Most common hour for travel is ' + str(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # Display the most common start station
    most_common_start = df['Start Station'].mode()[0]
    print('Most common start station is "' + most_common_start + '"')
    # Display the most common end station
    most_common_end = df['End Station'].mode()[0]
    print('Most common end station is "' + most_common_end + '"')
    # Display the most common trip from start a station to an end station
    df['Combine start and end'] ='from "' + df['Start Station'] + '" to "' +  df['End Station'] + '"'
    print('Most common trip is ' + df['Combine start and end'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
   
    # Display total travel time
    total_hours = int(df['Trip Duration'].sum() / 3600)
    total_minutes = int((df['Trip Duration'].sum() % 3600) / 60)
    total_seconds = (df['Trip Duration'].sum()) - (60 * total_minutes) - (3600 * total_hours)
    total_time = "total time travel is {} hours {} minutes {} seconds".format(total_hours, total_minutes, int(total_seconds))
    print(total_time)
    
    # Display mean travel time
    mean_hours = int(df['Trip Duration'].mean() / 3600)
    mean_minutes = int((df['Trip Duration'].mean() % 3600) / 60)
    mean_seconds = (df['Trip Duration'].mean()) - (60 * mean_minutes) - (3600 * mean_hours)
    mean_time = "mean time travel is {} hours {} minutes {} seconds".format(mean_hours, mean_minutes, int(mean_seconds))

    print(mean_time)


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('-' * 10)
    print("Types of users")
    
    for i in range(0, len(df['User Type'].value_counts().index.tolist())):
        user_type_name = df['User Type'].value_counts().index.tolist()[i]
        user_type_count = df['User Type'].value_counts()[i]
        print(user_type_name, user_type_count)

    # Display counts of gender
    try:
        print('-' * 10)
        print("Gender of users")
        
        for i in range(0, len(df['Gender'].value_counts().index.tolist())):
            user_gender_name = df['Gender'].value_counts().index.tolist()[i]
            user_gender_count = df['Gender'].value_counts()[i]
            print(user_gender_name, user_gender_count)

    except:
        print('No gender Date provided')

    # Display earliest, most recent, and most common year of birth
    try:
        print('-' * 10)
        print("Range of birth years for users")
        min_year = df['Birth Year'].min()
        max_year = df['Birth Year'].max()
        mc_year = df['Birth Year'].mode()[0]

        print("Earliest year of birth is {}".format(int(min_year)))
        print("Most recent year of birth is {}".format(int(max_year)))
        print("Most common year of birth is {}".format(int(mc_year)))
    except:
        print("No birth year data provided")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    
    
    
    df = df.drop(columns=['month count', 'week day', 'hour'])
    df = df.fillna("Data is not avaibalbe")
    j = 5
    while True: 
        
        answer = input("Do you want to see individual data ? (yes or no): ")
        if answer.lower() == "no":
            break
        elif answer.lower() == "yes":
            for i in range(j):
                print ("{")
                print(df.iloc[i])
                print ("}")
            j += 5

        else:
            print("Please enter a valid answer('yes' or 'no')")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
