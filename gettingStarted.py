### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

#Questions:
def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"  
    elif question =="Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question =="Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question =="Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question =="What is the SHA256 hashing value of your NYU email and use the answer in your code":
        answer = "a6e90ac75f64f27949bb760b75bfa797e586c990c31905f5f23ae8ab904d0068"
    elif question =="Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question =="What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 3
    elif question =="What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    else:
        answer = "Question not recognized. Please check for typos."
    
    return answer


#Testing
if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))