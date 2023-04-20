<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Vandit Tejas Popat (vp645)</td></tr>
<tr><td> <em>Generated: </em> 4/20/2023 12:56:56 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/vp645" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232894875-ce6fd4bd-2332-441d-a03f-9d539e437fec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Display shows the url from heroku dev and change in nav bar with<br>my ucid and the brough to you by is also changed to my<br>name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232896290-e44235b7-7785-4850-b559-9d8ec445a461.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Display the change in url_for() in the code to company search and add<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232896559-4976b966-61e3-4874-b648-36d87d3a2199.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Display the change in url_for() in the code to employee search and add<br>and also for the import_csv which is in admin.py <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232897227-1056c981-1ba8-47a0-b6e9-01b2380527d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This displays the database of Companies and you see my ucid on the<br>left and the company data is populated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232897894-de641503-6472-455e-adbe-e8bd46a4351e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This displays the database of employee and you see my ucid on the<br>left and the employee data is populated<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232898317-5408a366-6256-4bd4-ad5b-da2419a9b39c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I added a word file instead of csv and therefor I got<br>a warning flash message saying it is not csv<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232898780-223402fb-a095-491b-8182-d0d0fe04b67b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the code I used for that and here in allowed extension<br>i only allow csv and check the extension by splitting at a .<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232899145-430c505e-3e86-4809-acd9-9502f4caf860.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I am reading the csv as a dict from the stream provided<br>by using csv.DictReader after importing the csv library in python at the start.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232899145-430c505e-3e86-4809-acd9-9502f4caf860.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I also show that I am first checking if all the columns<br>in csv are present and not empty for the company and then creating<br>a dict for storing all values from a particular row and append it<br>to the company list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232901891-1115d230-110f-4bc3-88ee-4430f9f558ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I also show that I am first checking if all the columns<br>in csv are present and not empty for the employee and then creating<br>a dict for storing all values from a particular row and append it<br>to the employee list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233141607-e73421f4-27ac-4af7-80c1-a6de16f15ce5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Displaying the number of companies and empolyees added and a message if nothing<br>is added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233141977-e10a587b-a128-4ec7-a6c3-abe266e4c5fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>A flash message showing no file was selected in importing the csv<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/232898317-5408a366-6256-4bd4-ad5b-da2419a9b39c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I added a word file instead of csv and therefor I got<br>a warning flash message saying it is not csv<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233142607-10bc41af-2227-4436-ae0f-4536ec2b8477.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the message that data is added and also how much data<br>is added for each table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233144719-5d188b71-ac47-45f7-ae2e-040b09a9115a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data in companies table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233146334-973d09b4-8236-4939-8ea7-60bc16d8bc62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data in Employees Table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233148508-80542477-324c-4c76-9247-8f6e6d78bda5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code will retrieve all the required employee information from the form.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233149049-320b517e-b1e6-4950-9354-fb32cc3bf0ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code checks if we have all the field present to add for<br>the employee if not we would flash an appropriate message, in this ss<br>we also check the regex for the email, to check of it is<br>appropriate<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233150045-ad4f908a-5873-45cd-99ee-0659823f343c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code has the appropriate insert query if the company is not provided<br>and also if it is provided and in this screenshot we also have<br>an exception block if we have some issue to tell us something went<br>wrong<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233153226-950216a0-0571-4b58-a487-addd06c85f90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Already filled in data for employee from importcsv<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233153463-830ff70f-0271-4879-806d-a7f00bf7ae72.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The details of Employee i want to create<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233153528-df8dfd12-022a-4f58-a9ff-2a27ba4871e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message when created the user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233153967-145c6052-1e76-4255-822b-a50ce0fa31b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Since the field is required in the form I have created I wont<br>be able to submit without the first name and therefore I see the<br>message please fill out these field<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233154468-4d9bfbcc-c1a8-4aee-842b-0c590a976838.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Since the field is required in the form I have created I wont<br>be able to submit without the first name and therefore I see the<br>message please fill out these field<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233155375-af78781c-575e-4f6a-8a6b-7c81a9ad0114.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Since the field is required in the form I have created I wont<br>be able to submit without the first name and therefore I see the<br>message please fill out these field<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233155508-526ddd90-cf81-4bfa-81b2-1b7bc66753ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash message for a valid email address required<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233156245-f390a467-b1be-4d98-957c-1d7459bb100b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB result check the first employee I have sorted the employee with created<br>timestamp it is same as the ss above the employee i added<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233157150-361ce172-c770-4033-b56c-3a42ace4c0fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The select query with left join in the above ss<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233157566-885935ff-6bd6-4a64-8345-c464562916fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Request args for the required fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233157566-885935ff-6bd6-4a64-8345-c464562916fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This also shows the append for all the field required and also the<br>limit between 1 and 100 logic is shown in the ss and the<br>error message for out of bound limit as well<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233158877-61807655-f9d2-4402-8ed3-0cafafe03ac9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Append sorting is shown in the above ss<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233159165-eddedf97-1d63-4c2c-a6ff-a9f6a73570e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception error message printed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233159599-0ca2f56b-569a-420e-aa7b-231a20e33e6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First Name filter asc applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233159742-837e8bcb-9216-4fab-bf55-cd6830d4da88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last Name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233159939-bcbfe2c0-86eb-4698-9f05-d232ee6e8067.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Filter Applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233160083-ba19cdcf-b6fb-4f5f-8631-2bb9a4bda871.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Filter App<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233159599-0ca2f56b-569a-420e-aa7b-231a20e33e6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Asc filter on first name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233160291-3e4b5930-91ca-43c9-bf08-4d914fec0afb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Desc filter on company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233171116-dfc9d17e-6fe1-42d5-86b7-7ea6f0059d7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code shows the id extracted of the company and a flash message if<br>not found the id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233172003-ad9f1aba-1a49-4936-a19c-4b086b1cd3b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for retrieving the firstname last name and the fields and also the<br>flash message if not present.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233172406-fc8b612e-6680-4c15-b8eb-14628052f2f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the update query with a company present or absent and<br>the message for an exception <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233173622-5463cf6a-39b0-4464-bdcd-8433c42ef189.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet with the select query and also the render template code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233173912-cb34991a-b84a-4a2a-bf77-8212c709e837.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before the edit was made<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233174131-75d7e376-770e-4c25-a658-a1a0433e3d62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data changed for last name and email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233174316-ff636f84-b77c-4338-bd20-3164414a734b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message after update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233174623-ad5f1e42-df84-442d-8200-beeb0aa4a5b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Record after update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233174923-544d3e2a-04b1-4c14-b4c2-7d75f10caec2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The first data row is the updated value <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233175941-e9e59258-c102-4606-be34-9484163a2646.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet to retrieve the following field<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233176972-ccc34626-0600-4649-9827-22069e76dbcc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet to check and show appropriate flash messages for all required fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233177447-e205e8cb-d923-4f04-8b7f-1dd085c4d5d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insert query and except block codes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233177827-8138bd69-9d9a-48dc-bd39-b609970d40ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First search screen where we could see the data added by csv import<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233178657-273f1a3a-8e2b-4268-9101-209afb873419.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data to input <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233178781-0372d6d3-b605-469b-ab04-46cf15881b39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233179404-a6d502ac-21a9-4a0d-88e3-ca5ba267a70d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name Error flash message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233179967-bc5f7a1b-1599-4571-a36c-cea9e6566450.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Address flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233180731-663f811d-477d-4ca2-beea-51de43a1bb57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>City flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233223817-2acb3a2e-3b7a-4672-9f3d-d643bd5fdfce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Zip flash message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233224256-4b7f6e95-961b-463f-8438-cb3af49a4897.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country and state are required so i cannot move ahead therefore this message<br><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233225196-d3f56434-ff92-4050-ac04-69bed9b29e59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first record is the added record<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233225772-e492fdaf-3a70-4749-b355-c8084c910d54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Select query to fetch  id, name, address, city, country, state, zip, website,<br>employee count (as employee) for the company <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233226251-bfb30f72-56e1-4b9b-8056-8b275b109879.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Append like for name, and equality filter for  country and state if<br>present as well as sorting and limit between 1 to 100, <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233226753-a14831e9-4e51-4d6f-9108-24667725c3a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception message if something went wrong<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233226894-b82c27f5-d458-4171-95bb-d74135eb4be4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name filter applied in asc order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233226970-dc032285-36ec-41e3-909f-48efeb7faf98.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>City filter applied in asc order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233227022-ca39aa85-b097-4a14-93cb-643587b30057.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country filter applied in asc ord<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233227124-11b3e593-2aaa-4cea-be21-2ee5f2f5129f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State filter applied in asc order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233226894-b82c27f5-d458-4171-95bb-d74135eb4be4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name filter applied in asc order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233227231-a0da46ba-e9a2-467a-a7c4-104f7313bc3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State filter applied desc order<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233227407-2449fd71-8b6d-4dd5-aa11-68cad6521ca7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search for id of the company and error message for the same<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233227495-226dcc66-48a7-49d1-bf89-2123d981e3be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Retrieve all the value from form like name, country etc <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233227717-48f61618-b643-4221-8242-1767e07e0bdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash message for every field if not present in the form <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233227889-3bee542a-ec7e-4f8c-a380-0332de91ba6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update query with a flash message if it doesnt work<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233228098-067ae019-2a60-4124-9345-6fa09e064445.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper select query and render template <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233228208-0aa61d8e-beac-4473-ad6f-9c98cb6ad21f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Will edit the first one <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233229364-ecddbd29-ec1e-473b-b307-4a5aeadc6058.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233229418-76e4bea7-c7e8-4a04-b6b7-214a705ed9f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The first value is updated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233229819-08fdb0de-f851-4d98-9570-f761f66172a5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check the first record it is updated<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233241536-b612d6ed-c7c1-4e32-a50c-1e3f37f73c1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This ss shows the entire working of delete employee along with flash messages<br>for succes and failut<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233242077-13512a44-9103-45f3-a7cd-0503e29fe08b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>records before deletion will delete the 1st employee record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233242199-ef22e30a-781b-493c-a279-d6f770544e72.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message as deleted the 1st row.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233243291-05d115f2-ec3e-49c6-8a24-94b144e40be0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The entire code snippet shows deleting company by id, redirecting to search page<br>and with flash messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233245445-797b85d7-23e7-408e-812c-c6dc6f6f97e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Initial search page will delete the first record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233246047-ef113ac4-30b1-48bd-bfbf-448e6ab15b98.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deleted the first row and also the success message<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233247510-1cdf8439-0fab-4ae1-b413-051256fa274b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case test_add_company successful <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233248412-9c423c97-594d-44d2-b9b1-1e0b52e80712.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case test_add_employee successful<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233248617-d223ddc4-97df-4bcd-9706-a8e87852bdac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case test_edit_company successful<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233248840-d63d89fe-ee47-4686-b5fd-75dee8831986.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case test_edit_employee successful<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233249041-37616abc-3fbd-41a0-abd2-4142f579320c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case test_employee_count successful<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233249528-13dca3f0-0be3-449f-b9e7-eca783c179ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case test_search_employee successful<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/233249696-85355a8e-3450-4e6d-a9c2-459acf162557.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case for import csv successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>This assignment has taught me almost everything new, how to import csv how<br>to read a file in using TextIOWrapper and read as a dict. How<br>to render pages and connect html pages to py files.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/vp645" target="_blank">Grading</a></td></tr></table>