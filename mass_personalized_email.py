#! /usr/bin/env python
"""
A python script that can be used to send mass emails that are personalized using
info read in from a csv file. THe SMTP host address, SMTP port, sender email, and 
sender password are required as command line arguments. Please read the README for
additional info and specifications.
"""
import argparse
import csv
import smtplib

def main():
    # Parsing for command line arguments 
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "host_address", nargs="?", default="address", type=str,
        help="host address for SMTP")
    parser.add_argument(
        "port", nargs="?", default="port", type=str,
        help="port number for SMTP")
    parser.add_argument(
        "sender_email", nargs="?", default="griffin_kao@brown.edu", type=str,
        help="email address of sender")
    parser.add_argument(
        "password", nargs="?", default="password", type=str,
        help="password")
    parser.add_argument(
        "info_file", nargs="?", default="email_list.csv", type=str,
        help="the csv file containing all the email list info")
    parser.add_argument(
        "email_text", nargs="?", default="email_text.txt", type=argparse.FileType("r"),
        help="text file containing the body of the email")
    parser.add_argument(
        "subject_text", nargs="?", default="subject.txt", type=argparse.FileType("r"),
        help="text file containing the subject of the email")
    args = parser.parse_args()

    # Reading in the raw email text
    original_text = args.email_text.read()
    args.email_text.close()
    # Reading in the email subject text
    subject = args.subject_text.read()
    args.subject_text.close()

    print("Email body: " + original_text)
    print("Email subject: " + subject)

    raw_input("Press Enter to continue...")

    # Setting up the SMTP server to be able to send emails
    s = smtplib.SMTP_SSL(host=args.host_address, port=args.port)
    s.login(args.sender_email, args.password)

    line = 0
    info = {}
    with open(args.info_file) as info_file:
        reader = csv.reader(info_file, delimiter=',')
        for row in reader:
            if line == 0:
                # Setting up the dictionary to store personalized info location from the csv header
                for i in range(len(row)):
                    token = "<" + row[i] + ">"
                    info[token] = i 
                if "<email>" not in info:
                    print("Error: Info csv must contain emails")
                    return
            else:
                new = original_text
                email = row[info["<email>"]] # Getting individual email
                # Replace tokens with personalized tokens
                for token in info:
                    new = new.replace(token, row[info[token]])
                msg = 'Subject: {}\n\n{}'.format(subject, new) # Creating a new message
                # Sending the email
                s.sendmail(args.sender_email, email, msg)
                print
                print("EMAIL " + str(line))
                print("Sent: " + new)
                print("To: " + email)
            line += 1
    s.quit # Quitting the SMTP server

if __name__ == "__main__":
    main()