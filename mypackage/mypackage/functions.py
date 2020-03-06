def dictionary_of_metrics(items):
    # your code here
    
    """Calculates the mean, median, variance, standard deviation, minimum and
    maximum of a list of entries.
    
    Parameter
    - - - - - 
    items: list
        Numerical entries.
    
    Returns
    - - - - 
    answer: dict
        The result of the calculations of the individual measures."""
    
    # sort the data in ascending order and finding the length (or size) of the list
    data = sorted(items)
    n = len(data)
    
    # calculate the mean
    def mean(data):
        return round(sum(data)/n,2)
    
    # calculate the median
    def median(data):
         # if the size of the data is even
        if n % 2 == 0:                   
            first_mid_point = int(n/2)
            second_mid_point = int(n/2) - 1
            median = (data[first_mid_point] + data[second_mid_point]) / 2
            return (median)
        # if the size of the data is odd
        else:                             
            mid_point = int(n/2) 
            median_2 = data[mid_point]
            return median_2
    
    # calculate the variance
    def variance(v):
        mean = round(sum(v)/len(v),2)
        return round(sum((i-mean)**2 for i in v)/(len(v)-1),2)
    
    # calculate the standard deviation
    def standard_dev(std):
        return round(variance(std)**0.5,2)
    
    # find the minimum value
    def minimum(data):
        return round(data[0],2)
    
    # find the maximum value
    def maximum(data):
        return round(data[-1],2)
    
    # create a dictionary of the entries
    answer = {'mean':mean(data), 'median': median(data),
            'var': variance(data),'std':standard_dev(data),
            'min':minimum(data),'max':maximum(data)}

    return answer

def five_num_summary(items):
    # your code here
    
    """ Calculate the five number summary (maximum, median, minimum, q1, q3).
    
    Parameter
    - - - - - 
    items: list
        Numerical entries.
    
    Returns
    - - - - 
    rs_dict: dict
        The result of the calculations of the measures."""
    
    # find the maximum value
    def my_max(lst):
        items_max = np.max(lst)
        return round(items_max, 2)
    
    # find the minimum value
    def my_min(lst):
        items_min = np.min(lst)
        return round(items_min, 2)
    
    # find the median
    def mid(lst):
        median = np.median(lst)
        return round(median, 2)
    
    # find the lower quartile, q1
    def my_q1(lst):
        q1 = np.percentile(lst, [25])
        return round(q1[0], 2)
    
    # find the upper quartile, q3
    def my_q3(lst):
        q3 = np.percentile(lst, [75])
        return round(q3[0], 2)
      
    # assing keys to variable 'name' and values to the variable 'values'
    names = ['max', 'median', 'min', 'q1', 'q3']
    values = [my_max(items), mid(items),my_min(items), my_q1(items), my_q3(items)]
    
    # zip the keys and values to create a dictionary
    zipped_list = zip(names, values)
    rs_dict = dict(zipped_list)
    
    return rs_dict 

def date_parser(dates):
    # your code here
    
    """Returns a date in the 'yyyy-mm-dd' format.
    
    Paramater
    - - - - - 
    dates: string
        An input of datetime strings.
        
    Returns
    - - - - 
    list comprehension: list of strings
        A result of a list comprehension and the split method returns the date."""
    
    listOne = []
    for x in dates:
        y = x.split(' ')[0]
        listOne.append(y)
     
    return listOne

def extract_municipality_hashtags(df):
    # your code here
    
    """Return a modified dataframe that includes two new columns with information
    about the municipality and hashtags of the tweet.
    
    Parameter
    - - - - -
    df: dataframe
        A pandas dataframe as the parameter.
        
    Returns
    - - - - 
    df: dataframe
        An updated dataframe with two new columns; municipality and hashtags."""
    
    
    # get the name of the municipality 
    def get_mun(a):
        for key in a.split():
            if key in  mun_dict.keys():
                return mun_dict[key]
        return np.nan
    
    # create a function that will extract the hashtags
    lst = []
    tweets = df['Tweets']
    for word in tweets:
        if '#' in word:
            lst.append(list(filter(lambda tweet:tweet.startswith('#'), word.lower().split())))
        else:
            lst.append('NaN')
        
    # apply the local function to the dataframe column containing the tweets
    df['municipality'] = df['Tweets'].apply(get_mun)
    df['hashtags'] = lst
    
    return df

def number_of_tweets_per_day(df):
    # your code here
    
    """Calculate the number of tweets posted per day.
    
    Paramter
    - - - - 
    df: datafame
        A pandas dataframe as the parameter.
    
    Returns
    - - - - 
    a: dataframe
        A new pandas dataframe with the date and number of tweets."""
    
    # create a variable 'dates' from a series 'Date' to cast a list
    dates = list(df['Date'])
    
    # assign dates to the series 'Date' in the format yyyy-mm-dd
    df['Date'] = [i.split(" ")[0] for i in dates]
    
    # create a dataframe to group the tweet date and count the number of tweets posted per day
    a = pd.DataFrame(df.groupby('Date')['Tweets'].count())
    
    return a

def word_splitter(df):
    # your code here
    
    """Tokenization - split sentences into a list of separate words.
    
    Paramter
    - - - - 
    df: datafame
        A pandas dataframe as the parameter.
    
    Returns
    - - - - 
    df: dataframe
        A pandas dataframe with a new column with split tweets."""
    
    # extract the 'Tweets' column from the data frame
    df_split = df['Tweets'][:]
    
    # split the tweets into a list of words
    df_list_split = [token.lower().split() for token in df_split]
    
    # add the column of split words to the data frame
    df['Split Tweets'] = df_list_split
    
    return df

def stop_words_remover(df):
    # your code here
    
    """A function that removes English stop words from a tweet.
    
    Paramter
    - - - - 
    df: datafame
        A pandas dataframe as the parameter.
    
    Returns
    - - - - 
    df: dataframe
        A pandas dataframe with a new column without stop words."""
    
    # extract the stop words from a dictionary
    stop_words = stop_words_dict.values()
    
    # create an empty list
    new_list = []
    
    # add the stop words to the empty list
    for lst in stop_words:
        new_list = new_list + lst
       
        
    # remove the stop words from the tweets
    def inner_fun(tweets):
        lst =  [word for word in tweets.lower().split() if word not in new_list]
        return lst
    
    # a new column to the dataframe
    df['Without Stop Words'] = df['Tweets'].apply(inner_fun)
    
    return df


