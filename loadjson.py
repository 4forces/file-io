import json

# working with json files
with open('example_2.json') as filepointer:
    data = json.load(filepointer)
    print(data)

# working with direct copy paste json files
# json_string = """
# {
#     "quiz": {
#         "sport": {
#             "q1": {
#                 "question": "Which one is correct team name in NBA?",
#                 "options": [
#                     "New York Bulls",
#                     "Los Angeles Kings",
#                     "Golden State Warriros",
#                     "Huston Rocket"
#                 ],
#                 "answer": "Huston Rocket"
#             }
#         },
#         "maths": {
#             "q1": {
#                 "question": "5 + 7 = ?",
#                 "options": [
#                     "10",
#                     "11",
#                     "12",
#                     "13"
#                 ],
#                 "answer": "12"
#             },
#             "q2": {
#                 "question": "12 - 8 = ?",
#                 "options": [
#                     "1",
#                     "2",
#                     "3",
#                     "4"
#                 ],
#                 "answer": "4"
#             }
#         }
#     }
# }
# """
# d = json.loads(json_string) #json
# print(d) #python dictionrary