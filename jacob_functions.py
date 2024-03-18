def set_background(img):
    """
    Teachers can upload new image	
    Called: When user selects "Customize" button	
    img: jpg file	
    If valid file uploaded, sets new background image in SQL .
    Else throws error
    """
    #Note: to work with files, must do in django
    pass

def get_grades(user_email: str, class_id: str):
    """
    Overview: Retrieves all grades for all students for all assignments and displays graded/ungraded assignments	
    Called: When user "Classroom Layout / Grades (Teachers) loads	
    "User email: string
    class id: string"	"If user does not exist in class, displays error message
    Returns all assignments + grades. If user has submitted assignment + does not have grade, returns appropriate message
    If no assignments exist, displays appropriate message"	
    GET info from assignments collection																			
    """
    pass

def update_grades(class_id: str, student_email: str):
    """
    Overview: Allows teachers to input new grades for a specific student for a specific assignment	
    Called: When user selects "add grade" on assignment	"User email: string
    class id: string
    student email: string"	
    Creates new grade for assignment for student in DB	
    PUT info to assignments collection																		
    """
    pass


def create_assignment(class_id: str, file, details: str):
    """
    Overview: Allows teachers to create new assignment	
    Called: When user selects "plus button" on page	"User email: string
    class id: string
    file: file
    details: string"	
    Creates new assignment in DB if all fields are valid	
    POST info to assignments collection																			
    """
    pass

def modify_assignment(user_email: str, class_id: str, details: str, file):
    """
    Overview: Allows teachers to remove assignment	
    Called: When user selects edit assignment	
    "User email: string
    class id: string
    file: file
    details: string"	
    Modifies assignemnt as appropriate	
    PUT info to assignments collection																		
    """
    pass