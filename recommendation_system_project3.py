# Movie Recommendation System

# Movie database
movies = {
    "Inception": ["sci-fi", "thriller", "action"],
    "Titanic": ["romance", "drama"],
    "Avengers": ["action", "superhero", "sci-fi"],
    "The Hangover": ["comedy"],
    "Interstellar": ["sci-fi", "drama"],
    "John Wick": ["action", "thriller"],
    "Frozen": ["animation", "family"],
    "The Notebook": ["romance", "drama"]
}

# Take user input
user_input = input("Enter your interests separated by commas: ")

# Convert input into list
user_preferences = user_input.lower().split(",")

# Store recommendations
recommendations = []

# Recommendation Logic
for movie, genres in movies.items():

    match_score = 0

    for preference in user_preferences:

        if preference.strip() in genres:
            match_score += 1

    if match_score > 0:
        recommendations.append((movie, match_score))

# Sort recommendations by score
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display recommendations
print("\nRecommended Movies:\n")

for movie, score in recommendations:
    print(f"{movie}  ---> Match Score: {score}")