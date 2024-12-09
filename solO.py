#DISCLAIMER: I DO NOT WARRANTY THIS CODE TO BE BUG FREE OR TO BE FIT FOR PURPOSE, RUNNING solO AGAINST A PROJECT DOES NOT GUARANTEE THAT THE PROJECT IS SECURE AND/OR BUG FREE
from subprocess import PIPE,Popen
import random
import os
import glob
import json
import re

def runSolO(project_dir,rules_dir):
    # Used for progress output
    print("---START--------------------------------------------------------------------\n")
    # Used for report output
    MarkdownString = "# solO Report\n"
    print("[+] Running solO against directory: ",project_dir)
    MarkdownString = MarkdownString + "- Running solO against directory: " + project_dir + "\n"
    print("\n")
    print("[+] Rules templates directory set as : ",rules_dir)
    MarkdownString = MarkdownString + "- Rules templates directory set as : " + rules_dir + "\n"
    print("\n")
    try:
        # First import all templates to minimise IO
        # Rules are stored in the rules array
        rules = []
        rulecheckfinds = ""
        for jsonfile in os.listdir(rules_dir):
            with open(rules_dir + "/" + jsonfile, 'r', encoding="utf-8") as rulefile:
                ruleEntry = rulefile.read()
                rule = json.loads(ruleEntry)
                rules.append(rule)
                
        # Now check for files that implement the Circuit trait    
        accountsList = "## Rust files found:\n"
        # Walk all directories and subdirectories from the main folder which was set in project_dir
        for root,dirs, files in os.walk(project_dir):
            for file in files:
                # Only read files ending in ".rs"
                if file.endswith(".rs"):
                    hasAccounts = False
                    foundObj = True
                    with open(os.path.join(root,file), 'r', encoding="utf-8") as rustfile:
                        rustcode = rustfile.read()
                        # For now just check for text as below which should find "#[derive(Accounts)]"
                        if rustcode.find("#[derive(Accounts)]") > 0:
                            accountsList = accountsList + "   [^] " + file + "\n"
                            hasAccounts = True
                        rustfile.close()

                        if hasAccounts:
                            accountsList = accountsList + "### File: " + os.path.join(root,file) + "\n "
                            strObj = ""
                            strAddInstr = ""
                            strAttributes = ""
                            with open(os.path.join(root,file), 'r', encoding="utf-8") as rustfile:
                                foundObj = False
                                attributesfound = False
                                openAttrib = 0
                                
                                for rustLine in rustfile:
                                    isInstruction = False
                                    if rustLine.find("[derive(Accounts)]") > 0:
                                        foundObj = True
                                    if foundObj:
                                        if rustLine.find("}") > 0:
                                            foundObj = False
                                        if rustLine.find("[instruction(") > 0:
                                            strAddInstr = "Struct has instuction inputs of : " + rustLine.replace("#","").replace("\n","")
                                            isInstruction = True
                                        if re.search(r'\b{}\b'.format("pub struct"),rustLine):
                                            strObj = strObj + "---\n #: Account Object found: " + rustLine.split("struct",1)[1].split("<",1)[0].strip() + "\n\n"
                                            if len(strAddInstr) > 0:
                                                strObj = strObj + "*" + strAddInstr + "* \n\n"
                                                strAddInstr = "" 
                                        if rustLine.find("[") > 0 and rustLine.find("]") < 0 and attributesfound == True:
                                            openAttrib = openAttrib + 1  
                                        if attributesfound:
                                            if openAttrib > 0:
                                                strTmp = rustLine.replace("]","").replace(")","").strip()
                                            else:
                                                if rustLine.find("]") > 0:
                                                    if rustLine.find("[") > 0 and rustLine.find("]") > 0:
                                                        strTmp = rustLine.strip()
                                                    else:
                                                        strTmp = rustLine.replace("]","").replace(")","").strip()
                                                else:
                                                    strTmp = rustLine.strip()
                                            if len(strTmp)> 0:
                                                strAttributes = strAttributes +  "- " + strTmp  + "\n"
                                        if rustLine.find("#[account(") > 0:
                                            strObj = strObj + "Anchor account member below has attributes: \n"
                                            attributesfound = True
                                            strTmp = rustLine.replace("#[account(","").replace(")","").replace("]","").strip()
                                            if len(strTmp)> 0:
                                                strAttributes = strAttributes+ "- " + strTmp + "\n"  
                                            if rustLine.find("]") > 0:
                                                attributesfound = False 
                                                strObj = strObj + strAttributes + "\n"
                                        if rustLine.find("]") > 0 and rustLine.find("[") < 0 and attributesfound == True:
                                            if openAttrib > 0:
                                                openAttrib = openAttrib - 1
                                            else:
                                                attributesfound = False
                                                strTmp = rustLine.replace(")]","").strip()
                                                if len(strTmp)> 0:
                                                    strAttributes = strAttributes+ "- " + strTmp + "\n"
                                                strObj = strObj + strAttributes + "\n"
                                                strAttributes = ""                                   
                                            
                                        if rustLine.find(":") > 0 and attributesfound == False and isInstruction == False:
                                            strObj = strObj + "**" + rustLine.split(":",1)[0].replace("pub ", "").strip() + " of type " + rustLine.split(":",1)[1].replace("\n","").strip() + "**\n\n"

                            accountsList = accountsList + strObj
                            strObj = ""
                            strAddInstr = ""
                            
                                    
                    #First list and describe the accounts
                    # Now loop through the rules array and check the "match" value against the code 
                    # retrieved from reading the source file
                    for rule in rules:
                        intfound = 0
                        for strmatch in rule["match"]:
                            if rustcode.find(strmatch) > 0:
                                # The counter makes sure it only lists the file once 
                                # and not for each match in a file
                                if intfound == 0:
                                    intfound = 1
                                    rulecheckfinds = rulecheckfinds + "### File: " + os.path.join(root,file) + "\n   #: Match found on : " + strmatch + "\n   #: " + rule["description"] + "\n\n"
                                    # setup the file path
                                    filepath = os.path.join(root,file)
                                    # Use Popen to open grep the "match" value in the file
                                    # and capture the output
                                    with Popen("grep -n -C 1 '" + strmatch + "' " + filepath + " -rIs",shell=True,stdout=PIPE) as proc:
                                        try:
                                            out, errs = proc.communicate(timeout=15)
                                        except TimeoutExpired:
                                            proc.kill()
                                            out, errs = proc.communicate()
                                        bashOutput = out.decode()
                                    # String to concatenate all match finds
                                    rulecheckfinds = rulecheckfinds + "```\n" + bashOutput + "\n```\n"
                
                        
                            
        print(accountsList)
        print("## Rule checks returned the list of code to check below:\n") 
        rulecheckfinds = "## Rule checks returned the list of code to check below:\n" + rulecheckfinds
        print(rulecheckfinds)
        print("---END----------------------------------------------------------------------")
        # Setup final string to write out to report
        MarkdownString = MarkdownString + accountsList + rulecheckfinds
        
        #Write out the markdown into the report file
        f = open("solOReport.md", "w")
        f.write(MarkdownString)
        f.close()
    except Exception as e:
        print("[#### ] solO ran into an exception : ",e)

def main():
    #Setup python argument parsing    
    import argparse
    parser = argparse.ArgumentParser()
    # 2 arguments used
    # project_dir ---> is the fully qualified path to the Solana project folder
    # rules_dir   ---> is the fully qualified path to the templates directory in 
    #                   most cases will be one level down for here
    parser.add_argument("project_dir", help="The project directory")
    parser.add_argument("rules_dir", help="The directory which has the JSON rules templates to check against")
    args = parser.parse_args()
    # Parse the arguments and call the runSolO function
    runSolO(args.project_dir, args.rules_dir)

main()
