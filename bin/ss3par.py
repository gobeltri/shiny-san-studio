

def check_stopped_rcgs ( sp_config_file ):
    
    fo = open (sp_config_file, "ro")
    stopped_rcgs = ""
    
    for line in fo:
        if "Stopped" in line:
            stopped_rcgs = stopped_rcgs + line
        
    fo.close()
    
    return stopped_rcgs
    
    
srcgs = check_stopped_rcgs ("public/3par-config-files/170509.063412.0001")
print ">>>>CHECK OUT FOLLOWING STOPPED RCGs<<<<\n" + srcgs