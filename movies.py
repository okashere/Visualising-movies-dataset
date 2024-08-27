import pandas as pd

# Sample data
data = {
    'budget': [
        1000000, 5000000, 2000000, 3000000, 1500000,
        2500000, 4500000, 1200000, 3500000, 800000,
        6000000, 2200000, 3300000, 1400000, 750000,
        1300000, 5200000, 2700000, 3100000, 4200000,
        1800000, 2500000, 3500000, 2900000, 4000000
    ],
    'genres': [
        'Action|Adventure', 'Comedy|Drama', 'Action|Sci-Fi', 'Drama|Romance', 'Adventure|Comedy',
        'Horror|Thriller', 'Documentary|Biography', 'Fantasy|Adventure', 'Mystery|Crime', 'Animation|Family',
        'Comedy|Romance', 'Drama|War', 'Sci-Fi|Thriller', 'Action|Comedy', 'Fantasy|Drama',
        'Horror|Sci-Fi', 'Adventure|Drama', 'Romance|Comedy', 'Drama|Thriller', 'Mystery|Drama',
        'Action|Horror', 'Adventure|Family', 'Comedy|Fantasy', 'Drama|Mystery', 'Thriller|Sci-Fi'
    ],
    'homepage': ['', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', ''],
    'id': list(range(1, 26)),
    'keywords': [
        'hero|battle', 'funny|friends', 'aliens|space', 'love|drama', 'explore|journey',
        'fear|chase', 'life|story', 'magic|quest', 'detective|mystery', 'kids|fun',
        'romance|laughter', 'war|struggle', 'future|tech', 'fight|humor', 'myth|legend',
        'monster|fear', 'adventure|challenge', 'love|comedy', 'secrets|danger', 'crime|drama',
        'battle|darkness', 'family|journey', 'fantasy|dreams', 'secrets|history', 'future|unknown'
    ],
    'original_language': ['en'] * 25,
    'original_title': [
        'Hero Quest', 'Funny Friends', 'Alien Invasion', 'Love Story', 'Adventure Awaits',
        'Night Fear', 'Life Chronicles', 'Mystic Lands', 'Dark Detective', 'Cartoon Fun',
        'Love & Laughs', 'Battlefield', 'Tech Future', 'Action Laughs', 'Legend of Myths',
        'Alien Monster', 'Great Expedition', 'Romantic Comedy', 'Thrilling Secrets', 'Hidden Truths',
        'War of Shadows', 'Family Bond', 'Dream World', 'Mystery Unveiled', 'Sci-Fi Thrills'
    ],
    'overview': [
        'A hero embarks on a quest.', 'A group of friends have fun.', 'Aliens invade Earth.', 'A touching love story.', 'An adventure awaits.',
        'A night of fear.', 'A story of life.', 'A journey through mystical lands.', 'A detective solves crimes.', 'Fun for the whole family.',
        'A romance full of laughs.', 'A war drama.', 'A futuristic thriller.', 'Action and comedy combined.', 'A tale of legends and myths.',
        'A battle with a monster.', 'An epic expedition.', 'A lighthearted romantic comedy.', 'A thriller full of secrets.', 'A drama uncovering truths.',
        'A war in the shadows.', 'A family journey.', 'A world of dreams.', 'A mystery that is revealed.', 'A thrilling sci-fi adventure.'
    ],
    'popularity': [
        7.8, 6.5, 8.2, 7.0, 7.5,
        6.9, 7.3, 7.8, 8.1, 6.2,
        7.4, 6.8, 8.0, 7.2, 6.7,
        7.9, 7.1, 6.6, 7.7, 7.3,
        6.8, 7.0, 6.9, 7.6, 7.8
    ],
    'production_companies': [
        'Company A', 'Company B', 'Company C', 'Company D', 'Company E',
        'Company F', 'Company G', 'Company H', 'Company I', 'Company J',
        'Company K', 'Company L', 'Company M', 'Company N', 'Company O',
        'Company P', 'Company Q', 'Company R', 'Company S', 'Company T',
        'Company U', 'Company V', 'Company W', 'Company X', 'Company Y'
    ],
    'production_countries': ['US'] * 25,
    'release_date': [
        '2024-01-01', '2024-02-15', '2024-03-20', '2024-04-10', '2024-05-25',
        '2024-06-30', '2024-07-18', '2024-08-22', '2024-09-15', '2024-10-05',
        '2024-11-11', '2024-12-20', '2024-01-30', '2024-02-25', '2024-03-12',
        '2024-04-18', '2024-05-06', '2024-06-21', '2024-07-14', '2024-08-29',
        '2024-09-18', '2024-10-28', '2024-11-15', '2024-12-01', '2024-12-24'
    ],
    'revenue': [
        10000000, 20000000, 15000000, 12000000, 18000000,
        8000000, 14000000, 9500000, 22000000, 6000000,
        16000000, 13000000, 21000000, 17000000, 11000000,
        19000000, 9000000, 8500000, 15000000, 14000000,
        13000000, 14500000, 16000000, 18000000, 20000000
    ],
    'runtime': [
        120, 95, 110, 130, 105,
        90, 85, 100, 125, 80,
        115, 98, 123, 132, 140,
        108, 117, 121, 134, 90,
        99, 127, 101, 113, 124
    ],
    'spoken_languages': ['English'] * 25,
    'status': ['Released'] * 25,
    'tagline': [
        'Epic Adventure', 'Laugh Out Loud', 'Space War', 'Love Conquers All', 'Journey Begins',
        'Fear the Night', 'Life Unfolds', 'Magic Awaits', 'Mystery Solved', 'Fun for Everyone',
        'Romantic Comedy', 'War and Peace', 'Futuristic Thriller', 'Action & Humor', 'Legend Lives On',
        'Monster Battle', 'Journey Beyond', 'Love & Laughs', 'Secret Uncovered', 'Truth Revealed',
        'Shadows of War', 'Family First', 'Dream Big', 'Mystery Solved', 'Thrills Ahead'
    ],
    'title': [
        'Hero Quest', 'Funny Friends', 'Alien Invasion', 'Love Story', 'Adventure Awaits',
        'Night Fear', 'Life Chronicles', 'Mystic Lands', 'Dark Detective', 'Cartoon Fun',
        'Love & Laughs', 'Battlefield', 'Tech Future', 'Action Laughs', 'Legend of Myths',
        'Alien Monster', 'Great Expedition', 'Romantic Comedy', 'Thrilling Secrets', 'Hidden Truths',
        'War of Shadows', 'Family Bond', 'Dream World', 'Mystery Unveiled', 'Sci-Fi Thrills'
    ],
    'vote_average': [
        7.5, 6.8, 8.1, 7.3, 7.6,
        7.0, 7.2, 8.0, 7.9, 6.4,
        7.1, 6.6, 7.8, 7.2, 6.7,
        8.0, 7.1, 6.9, 7.4, 7.3,
        7.0, 7.2, 6.8, 7.7, 7.5
    ],
    'vote_count': [
        1400, 1100, 2200, 1000, 1900,
        1200, 2100, 1700, 1400, 2000,
        900, 800, 1800, 1700, 1300,
        1450, 1600, 1800, 1900, 2100,
        1200, 1500, 1600, 1900, 2000
    ],
    'cast': [
        'Actor A|Actor B', 'Actor C|Actor D', 'Actor E|Actor F', 'Actor G|Actor H', 'Actor I|Actor J',
        'Actor K|Actor L', 'Actor M|Actor N', 'Actor O|Actor P', 'Actor Q|Actor R', 'Actor S|Actor T',
        'Actor U|Actor V', 'Actor W|Actor X', 'Actor Y|Actor Z', 'Actor AA|Actor BB', 'Actor CC|Actor DD',
        'Actor EE|Actor FF', 'Actor GG|Actor HH', 'Actor II|Actor JJ', 'Actor KK|Actor LL', 'Actor MM|Actor NN',
        'Actor OO|Actor PP', 'Actor QQ|Actor RR', 'Actor SS|Actor TT', 'Actor UU|Actor VV', 'Actor WW|Actor XX'
    ],
    'crew': [
        'Director A|Writer B', 'Director C|Writer D', 'Director E|Writer F', 'Director G|Writer H', 'Director I|Writer J',
        'Director K|Writer L', 'Director M|Writer N', 'Director O|Writer P', 'Director Q|Writer R', 'Director S|Writer T',
        'Director U|Writer V', 'Director W|Writer X', 'Director Y|Writer Z', 'Director AA|Writer BB', 'Director CC|Writer DD',
        'Director EE|Writer FF', 'Director GG|Writer HH', 'Director II|Writer JJ', 'Director KK|Writer LL', 'Director MM|Writer NN',
        'Director OO|Writer PP', 'Director QQ|Writer RR', 'Director SS|Writer TT', 'Director UU|Writer VV', 'Director WW|Writer XX'
    ],
    'director': [
        'Director A', 'Director C', 'Director E', 'Director G', 'Director I',
        'Director K', 'Director M', 'Director O', 'Director Q', 'Director S',
        'Director U', 'Director W', 'Director Y', 'Director AA', 'Director CC',
        'Director EE', 'Director GG', 'Director II', 'Director KK', 'Director MM',
        'Director OO', 'Director QQ', 'Director SS', 'Director UU', 'Director WW'
    ]
}

# Create DataFrame
df_movies = pd.DataFrame(data)

# Save to CSV
df_movies.to_csv('movies_dataset.csv', index=False)
