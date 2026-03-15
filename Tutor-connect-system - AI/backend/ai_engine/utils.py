def subject_match(student_subject, tutor_subject):
    return 1 if student_subject.lower() == tutor_subject.lower() else 0


def price_difference(student_budget, tutor_price):
    return abs(student_budget - tutor_price)


def availability_score(available):
    return 1 if available else 0