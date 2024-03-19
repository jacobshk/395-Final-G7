from pymongo import MongoClient
import certifi
ca = certifi.where()

# User {'email' : '', 'username' : '', 'classes' : []}
# Class {'bg_img' : '', 'class_id' : '', 'student_emails' : [], 'teacher_emails' : [], 'assignment_ids' : [], 'announcement_ids' : []}
# Assignments {id : '', 'file' : '', 'details' : '', 'submissions' : [], 'non_submissions' : [], 'grades' : {'student_emails' : 'val'}}, 'feedback' : {'student_emails' : 'val'}}}
# Announcements {'id' : '', 'text' : ''}
def main():
    uri = "mongodb+srv://enzo:poopybutthead@cluster0.5itsxbk.mongodb.net/"
    client = MongoClient(uri, tlsCAFile=ca)
    db = client['Cluster0']

#     # add classes into database
#     students = ['student1@gmu.edu', 'student2@gmu.edu']
#     teachers = ['teacher1@gmu.edu, teacher2@gmu.edu']
#     assignment_id = [123, 456, 789]
#     announcement_id = [123, 456, 789]

#     create(db, 'Classes', {
#         'bg_img': '',
#         'class_id': 12345,
#         'student_emails': students,
#         'teacher_emails': teachers,
#         'assignment_ids': assignment_id,
#         'announcement_ids': announcement_id
#     })
    
#     create(db, 'Classes', {
#         'bg_img': '',
#         'class_id': 67890,
#         'student_emails': students,
#         'teacher_emails': teachers,
#         'assignment_ids': assignment_id,
#         'announcement_ids': announcement_id
#     })

#    # Add users into the database
#     create(db, 'Users', {'email': 'student1@gmu.edu', 'username': 'student1', 'classes': [12345, 67890]})
#     create(db, 'Users', {'email': 'student2@gmu.edu', 'username': 'student2', 'classes': [12345, 67890]})

#     # Define submission and non-submission IDs
#     submissions = ['student1@gmu.edu']
#     non_submissions = ['student2@gmu.edu']

#     # Define grades and feedback dictionaries
#     grades = {'student1@gmu.edu': 90, 'student2@gmu.edu': 50}
#     feedback = {'student1@gmu.edu': 'Good work!', 'student2@gmu.edu': 'Needs improvement.'}

#     # Add assignments into the database
#     create(db, 'Assignments', {
#         'id': 123,
#         'file': '',
#         'details': '',
#         'submissions': submissions,
#         'non_submissions': non_submissions,
#         'grades': grades,
#         'feedback': feedback
#     })

#     create(db, 'Assignments', {
#         'id': 456,
#         'file': '',
#         'details': '',
#         'submissions': submissions,
#         'non_submissions': non_submissions,
#         'grades': grades,
#         'feedback': feedback
#     })

#     create(db, 'Assignments', {
#         'id': 789,
#         'file': '',
#         'details': '',
#         'submissions': submissions,
#         'non_submissions': non_submissions,
#         'grades': grades,
#         'feedback': feedback
#     })
    
#     # Add announcements into the database
    create(db, 'Announcements', {'id': 123, 'text': 'Welcome to the class!'})
    create(db, 'Announcements', {'id': 456, 'text': 'Assignment 1 is due next week!'})
    create(db, 'Announcements', {'id': 789, 'text': 'Remember to submit your assignments!'})
    
    

    print("Testing get_roster:\n")
    # Get roster of students for class 12345
    roster = get_roster(db, 12345)
    print('Class 12345: ', roster)

    # Get roster of students for class 67890
    roster = get_roster(db, 67890)
    print('Class 67890: ', roster)

    print("\nTesting get_grades:\n")
    # Get grades for student1@gmu for class 12345
    grades = get_grades(db, 'student1@gmu.edu', 12345)
    print('student1: ', grades)

    # Get grades for student2@gmu for class 67890
    grades = get_grades(db, 'student2@gmu.edu', 67890)
    print('student2: ', grades)

    print("\nTesting get_assignments:\n")
    #Get assignments for student1@gmu for class 12345
    assignments = get_assignments(db, 'student1@gmu.edu', 12345)
    print('student1: ', assignments)

    # Get assignments for student2@gmu for class 67890
    assignments = get_assignments(db, 'student2@gmu.edu', 67890)
    print('student2: ', assignments)

    print("\nTesting get_stream:\n")
    # Get stream for student1@gmu for class 12345
    stream = get_stream(db, 'student1@gmu.edu', 12345)
    print('student1: ', stream)

    # Get stream for student2@gmu for class 67890
    stream = get_stream(db, 'student2@gmu.edu', 67890)
    print('student2: ', stream)



def create(db, collection, data):
    try:
        obj = db[collection].insert_one(data)
        # print("Data inserted successfully:", obj.inserted_id)
        return obj
    except Exception as e:
        print("Error:", e)
    # obj = db[collection].insert_one(data)
    # return obj


def get_roster(db, class_id):
    class_document = db['Classes'].find_one({'class_id': class_id})
    if class_document:
        student_emails = class_document.get('student_emails', [])
        if student_emails:
            # Fetch user details for the student emails
            users_cursor = db['Users'].find({'email': {'$in': student_emails}})
            users = list(users_cursor)
            if users:
                # Construct a dictionary mapping email to username
                email_to_username = {user['email']: user['username'] for user in users}
                # Construct a list of dictionaries containing email and username
                roster = [{'email': email, 'username': email_to_username[email]} for email in student_emails]
                return roster
            else:
                return [{'message': 'No Users Exist in Database'}]
        else:
            return [{'message': 'No Users Enrolled in Class'}]
    else:
        raise ValueError("Class not found.")

def get_grades(db, user_email, class_id):
    user_document = db['Users'].find_one({'email': user_email, 'classes': class_id})
    if user_document:
        assignment_ids = db['Classes'].find_one({'class_id': class_id}).get('assignment_ids', [])
        if assignment_ids:
            # Fetch assignment details for the assignment IDs
            assignments_cursor = db['Assignments'].find({'id': {'$in': assignment_ids}})
            assignments = list(assignments_cursor)
            if assignments:
                grades = []
                for assignment in assignments:
                    if user_email in assignment['submissions']:
                        grade = assignment['grades'].get(user_email)
                        feedback = assignment['feedback'].get(user_email, "No feedback provided.")
                        grades.append({'id': assignment['id'], 'grade': grade, 'feedback': feedback})
                    else:
                        grades.append({'id': assignment['id'], 'message': 'User has not submitted this assignment'})
                return grades
            else:
                return [{'message': 'No Assignments Exist in Database'}]
        return []
    else:
        raise ValueError("User does not exist in class.")


def get_assignments(db, user_email, class_id):
    user_document = db['Users'].find_one({'email': user_email, 'classes': class_id})
    if user_document:
        assignment_ids = db['Classes'].find_one({'class_id': class_id}).get('assignment_ids', [])
        if assignment_ids:
            # Fetch assignment details for the assignment IDs
            assignments_cursor = db['Assignments'].find({'id': {'$in': assignment_ids}})
            assignments = list(assignments_cursor)
            if assignments:
                assignment_id_list = [assignment['id'] for assignment in assignments]
                return {'assignments' : assignment_id_list }          
            else:
                return [{'message': 'No Assignments Exist in Database'}]
        return []
    else:
        raise ValueError("User does not exist in class.")

def get_stream(db, user_email, class_id):
    user_document = db['Users'].find_one({'email': user_email, 'classes': class_id})
    if user_document:
        # Fetch assignment IDs for the class
        assignment_ids = db['Classes'].find_one({'class_id': class_id}).get('assignment_ids', [])
        if assignment_ids:
            # Fetch assignment details for the assignment IDs
            assignments_cursor = db['Assignments'].find({'id': {'$in': assignment_ids}})
            assignments = list(assignments_cursor)
            if assignments:
                # Extract assignment IDs from the assignment details
                assignment_id_list = [assignment['id'] for assignment in assignments]
            else:
                assignment_id_list = []

        else:
            assignment_id_list = []

        # Fetch announcement IDs for the class
        announcement_ids = db['Classes'].find_one({'class_id': class_id}).get('announcement_ids', [])
        if announcement_ids:
            # Initialize a set to store unique announcement texts
            unique_announcements = set()

            # Fetch announcement details for the announcement IDs
            for announcement_id in announcement_ids:
                announcement = db['Announcements'].find_one({'id': announcement_id})
                if announcement:
                    # Add the announcement text to the set
                    unique_announcements.add(announcement['text'])

            # Convert the set to a list
            announcement_text_list = list(unique_announcements)
        else:
            announcement_text_list = []

        return {'assignments': assignment_id_list, 'announcements': announcement_text_list}

    else:
        raise ValueError("User does not exist in class.")




if __name__ == "__main__":
    main()
