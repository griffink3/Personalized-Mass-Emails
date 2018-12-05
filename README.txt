Mass Personalized Email Script
By: Griffin Kao

Instructions:
To use the script, you need the email provider host address and port (for gmail this will always be "smtp.gmail.com" and "465" respectively), as well as your email address and password.
So to send email from griffin_kao@brown.edu, I would run "python mass_personalized_email.py smtp.gmail.com 465 griffin_kao@brown.edu password" from terminal or the comand line.
By default, the script will try to read the personalized info from a file named email_list.csv, the email body from email_text.txt, and the email subject line from subject_text.txt.
If you want to read from different files, you can specify them: "python mass_personalized_email.py smtp.gmail.com 465 griffin_kao@brown.edu password another_email_list.csv another_email_text.txt another_subject_text.txt".
The info file must always be a csv and to be safe, you should have your email body text and subject text files be .txt files.
The csv file should always have a column with the email address with a column header of "email". Each additional column is a piece of personalized info.
For example, if I want to personalize  name and company name, I could have a csv file that looks like- 

"email,name,company
griffin_kao@brown.edu,Griffin,Brown University"

And then you would use the column headers surrounded by brackets as the markers in your email text to indicate where the personalized info goes. For example:

"Hi <name>,
You're company is <company>!
Bye!"

Note: If your email account is super secure you might get an "SMTPAuthenticationError(code, resp)" when you try running the script. If you're using gmail, you can fix this by going into the security settings of your gmail account (https://myaccount.google.com/u/4/security#signin) and turning on "Allow less secure apps".

Possible Uses: Nigerian Prince scam, sending all your ex's an email saying you have chlamydia, and thanking all the people who came to your barmitzvah so your mom gives you the gift money.
