query_string = "office professor skalka"

valid_second_words = ["professor", "course"]
valid_professor_words = ["office", "position"]
valid_course_words = ["crn", "enrollment", "classroom", "professor"]



words = query_string.split()

if len(words) < 3:
    print("Invalid Input: Not enough query terms.")

if words[1] == "professor":
    if words[0] in valid_professor_words:
        # try doing the query
    else:
        print("Invalid Input: First query term must be either \"office\" or \"position\"")

elif words[1] == "courses":
    if words[0] in valid_course_words:
        # try doing the query
    else:
        print("Invalid Input: First query term must be either \"crn\" or \"enrollment\" or \"classroom\" or \"professor\"")
else:
    print("Invalid Input: Second query term must be either \"professor\" or \"courses\"")

