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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    
    city = ''
    while city not in cities:
        city = input('Please choose a city from either Chicago, New York City, or Washington: ')
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    month = ''
    while month not in months:
        month = input('Please choose a month between January and June, or choose all for all of the months: ')
        month = month.lower()
              
     

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
      
    day = ''
    while day not in days:
        day = input('Please choose a day of the week, or choose all for all of the days: ')
        day = day.lower()

    print('-'*40)
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
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['DOW'] = df['Start Time'].dt.day_name()
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour
    
    
    if month != 'all':
        df = df[df['Month']==month.title()]
        
                                         
    if day != 'all':
        df = df[df['DOW']==day.title()]                                     
    
    return df

def view_sample(df):
    """Displays the dataframe in batches of 5 if it is requested"""
    
    show_data = input('Do you want to see raw data (y or n)?: ')
    data_index = 0
    
    while show_data.lower() == 'y':
        print(df.iloc[data_index: data_index + 5])
        data_index += 5
        
        show_data = input("Do you want to see more rows (y or n)?: ")


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print('The most common month to travel is {}.'.format(common_month))

    # TO DO: display the most common day of week
    common_day = df['DOW'].mode()[0]
    print('The most common day to travel is {}.'.format(common_day))

    # TO DO: display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print('The most common start hour is {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common starting station is {}.'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common ending station traveling to is {}.'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combo'] = df['Start Station'] + ' to ' + df['End Station']
    common_station_combo = df['Combo'].mode()[0]
    print('The most frequent combination of stations is {}.'.format(common_station_combo))

    print("\nThis took %s seconds to compile." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {}.'.format(total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {}.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # TO DO: Display counts of user types
    type_df = df['User Type'].value_counts()
    print('The number of users by type is:')
    for index, value in type_df.items():
        print(index, value)

    # TO DO: Display counts of gender
   
    try:
        gender_df = df['Gender'].value_counts()
        print('\nThe number of users by gender is: ')
        for index, value in gender_df.items():
            print(index, value)
    except:
        print('\nThis dataset does not include gender data')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('\nThe earliest year is {}, the most recent year is {}, and the most common year is {}.'.format(int(earliest_year), int(most_recent_year), int(common_year)))
    except:
        print('\nThis dataset does not include user birth year')

    print("\nThis took %s seconds to compile." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_sample(df)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
