import smtplib
from email.mime.text import MIMEText
import os



def send_email_mailtrap ( content ) :
    msg = MIMEText( content )
    msg['Subject'] = 'CHECK OUT FOLLOWING STOPPED RCGs'
    msg['From'] = 'server@ferro.com'
    msg['To'] = 'PDL@DXC.com'
    
    # The actual mail send
    server = smtplib.SMTP(os.environ['EMAIL_HOST'], os.environ['EMAIL_PORT'])
    server.starttls()
    server.login(os.environ['EMAIL_HOST_USER'], os.environ['EMAIL_HOST_PASSWORD'])
    server.sendmail('server@ferro.com', ['PDL@DXC.com'], msg.as_string())
    server.quit()


def check_stopped_rcgs ( sp_config_file ):
    
    fo = open (sp_config_file, "ro")
    stopped_rcgs = ""
    
    for line in fo:
        if "Stopped" in line:
            stopped_rcgs = stopped_rcgs + line
        
    fo.close()
    
    return stopped_rcgs
    

def init_mailtrap ( mailtrap_cfg_file ):
    
    fo = open ( mailtrap_cfg_file, "ro" )
    for line in fo:
        head, sep, tail = line.partition(" = ")
        if head == "EMAIL_HOST":
            os.environ['EMAIL_HOST'] = tail.strip().strip('\'"')
            continue
        if head == "EMAIL_HOST_USER":
            os.environ['EMAIL_HOST_USER'] = tail.strip().strip('\'"')
            continue
        if head == "EMAIL_HOST_PASSWORD":
            os.environ['EMAIL_HOST_PASSWORD'] = tail.strip().strip('\'"')
            continue
        if head == "EMAIL_PORT":
            os.environ['EMAIL_PORT'] = tail.strip().strip('\'"')
            continue
        

# Load Mailtrap config from file and set env variables
init_mailtrap("../../config/mailtrap.cfg")

srcgs = check_stopped_rcgs ("../../config/3par-config-files/170509.063412.0001")
#print ">>>>CHECK OUT FOLLOWING STOPPED RCGs<<<<\n" + srcgs

send_email_mailtrap( srcgs )
