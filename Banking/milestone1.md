<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Vandit Tejas Popat (vp645)</td></tr>
<tr><td> <em>Generated: </em> 5/1/2023 12:49:05 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/vp645" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235378836-b2d3e919-ab4a-4b85-bfef-59f9c031f579.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above ss shows I cannot move ahead without valid email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235378867-a2d5f838-3495-4c62-9ada-1f3b491a3651.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above ss shows I cannot move ahead without a 8 character password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235378900-777bb938-7370-4c20-a967-b1c35b0f36f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above ss shows I cannot move ahead if the password doesnt match<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235378955-c658adf8-a748-4fac-8916-f2decbf77bdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above ss shows if I try to use the same email it<br>gives me an error for the same <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235379025-0cbac90a-e134-4e3c-8b04-f12585ae3bc3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above ss shows if I try to use the same username it<br>gives me an error for the same<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235379097-76057bd8-1b4a-4fe1-ad32-b4462d80f816.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above ss shows the user registered successfully<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235380600-3221f762-630d-439a-bac7-dc5d5f6655eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We can see the user added in the last row <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/27">https://github.com/vanditpopat/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>The form is handles using wtf flask form</div><div>We have used wtf form validators<br>like validators = [DataRequired(), Email() ] this means this is required</div><div>The password is<br>handled by bycrypt algorithm hashes and salt password securely</div><div>The db is utilized by<br>only basic operation of create update delete</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235393543-625f1219-cd7e-4142-9e91-2cad276290ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The user exist in database but i entered wrong password and got this<br>error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235393639-6a19b8d4-f34b-4f95-8053-4ca04e480b15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above user does not exist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235393864-7da8cbf3-038c-473f-99f9-43851ff2da0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This Shows a flash message for successful login as well as the landing<br>screen<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/27">https://github.com/vanditpopat/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>The form is handles using wtf flask form</div><div>We have used wtf form validators<br>like validators = [DataRequired(), Email() ] this means this is required</div><div>The password is<br>handled by bycrypt algorithm hashes and salt password securely</div><div>The db is utilized by<br>only basic operation of create update delete</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235394689-45972ef1-1fb7-4f36-84eb-2bad9f2cfde7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash message showing the logout successful message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235396063-17cb0feb-4876-410c-b29d-920b924927c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tried going to the landing page without login so got unauthorized error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/27">https://github.com/vanditpopat/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">The session logic is used from<br>flask login.<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">We will store the users<br>id<br><br>in the active session so he can access the login protected pages.<o:p></o:p></span></p><br><br><p class="MsoNormal"><span<br>style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;;mso-font-kerning:<br>0pt;mso-ligatures:none;mso-fareast-language:EN-IN">When the user logged out the users id is<br>removed from the session.</span><o:p></o:p></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235396063-17cb0feb-4876-410c-b29d-920b924927c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tried going to the landing page without login so got unauthorized error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235406525-c96eb391-3dd3-441d-b4a4-51d5e3d1c5a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tried accessing add roles page but cannot as not logged in as an<br>admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235407413-e76a60ca-e674-4f4c-92d0-6de2bb8ecb46.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The snapshot shows admin as role<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235408140-3ff362ab-244c-4fb6-a35f-325b9553a905.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the Userrole table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235408229-c16e4d86-1fca-4631-8075-b88d277b85f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the user table where user with id 1 is admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/27">https://github.com/vanditpopat/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp;roles are assigned to the user<o:p></o:p></span></p><br><br><p>&lt;p<br>class=&quot;MsoNormal&quot; style=&quot;margin-bottom:0cm;line-height:normal&quot;&gt;<span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp;when the assigned role user<br>login, he will<br><br>only<br>be able to see limited part which is set by the admin&lt;o:p&gt;</o:p></span></p></p><br><p class="MsoNormal"><span<br>style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;;mso-font-kerning:<br>0pt;mso-ligatures:none;mso-fareast-language:EN-IN">We are using flask principle<br>for the roles part<o:p></o:p></span></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">In the application i have defined<br>one admin permission object with the<br>help<br><br>of flask principle package<o:p></o:p></span></p><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New<br>Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">The session will check for the active roles assigned to<br><br>the user.<o:p></o:p></span></p><p<br>class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><br><br><br><br></p><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;;mso-font-kerning:<br>0pt;mso-ligatures:none;mso-fareast-language:EN-IN">&nbsp;For example if the user has<br>the admin role<br>assigned then he<br><br>will able to perform all the admin stuff such<br>as create role and<br><br>assign role to users<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235484493-d86bf89b-8b81-4d7f-bf32-0c01a86ee1dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation is styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235484594-7985b464-a498-4be3-a30c-ab431a309369.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data Output is in a clean way <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235484948-daee0377-d080-4150-8124-b713e1296df3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Forms are styled properly as well<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/27">https://github.com/vanditpopat/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>I have used bootstrap for the styling of forms and nav bars<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235396063-17cb0feb-4876-410c-b29d-920b924927c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the unauthorized access error if not logged in <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235393543-625f1219-cd7e-4142-9e91-2cad276290ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I entered the wrong password for an existing user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235406525-c96eb391-3dd3-441d-b4a4-51d5e3d1c5a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Persmission denied as not the right role was logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/27">https://github.com/vanditpopat/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>We are using flask flash messages function to show user friendly message witht<br>the help of exception handling when a error occur a custom message id<br>displayed in the web application&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235487165-c985b6f5-9d5f-4563-b98d-6af61d057ef3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Snapshot of the profile with prefilled username and email<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/27">https://github.com/vanditpopat/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">It is happening with the help<br>of current user flask login object values<br><br>and we are pulling the data from<br>the database of the particular user login.&nbsp;<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;;mso-font-kerning:<br>0pt;mso-ligatures:none;mso-fareast-language:EN-IN">The<br>flask login will retrive<br>the data into the form.<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235488387-ac349db8-a5ff-413c-aac5-0156a6b6fffe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235488483-400063e5-f944-4c3e-a644-37f9e789727f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper Email is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235488806-748ef71b-0199-4f0a-a9a8-0dc58bf06c73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Password error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235488947-766ac108-4aa9-4753-9b57-9de54b8696be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Mismatch error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235489119-fd037a11-53e1-4bfe-bb43-d191a26ad331.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username exist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235489239-acc963c1-c2bf-44e2-9cf4-8b354f7cb644.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before the change<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235489351-2f69020e-b52f-4169-9faf-4ab925b5d761.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After username update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/235489590-c75e5930-4ece-491b-b2a2-ea1b2f8c6ee4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database updated user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/27">https://github.com/vanditpopat/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp;for the validation we are using<br>the<br>wtf form validators<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp;we will get the<br>user from the flask login object<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">after<br>editing the data the session will be<br><br>refreshed with the updated record<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Times<br>New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;;mso-font-kerning:<br>0pt;mso-ligatures:none;mso-fareast-language:EN-IN">It works similar as the<br>register route.&nbsp;<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp;In these milestone I learned the<br>user<br>authentication using the wtf forms, validators<br><br>and flask login<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:Symbol;mso-ascii-font-family:&quot;Times New Roman&quot;;<br>mso-fareast-font-family:&quot;Times<br>New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">·</span><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp; I also learned about<br>registering<br>the user<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:Symbol;mso-ascii-font-family:&quot;Times New Roman&quot;;<br>mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">·</span><span style="font-size:12.0pt;font-family:&quot;Times New<br>Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp; I learned that the user<br><br>can login with the username and<br>email, for these we are using the rex functions<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:Symbol;mso-ascii-font-family:&quot;Times New<br>Roman&quot;;<br>mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">·</span><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp; I learned about<br>the user roles<br>using flask principles.<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:Symbol;mso-ascii-font-family:&quot;Times New Roman&quot;;<br>mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New<br>Roman&quot;;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">·</span><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp; I learned about the sessions<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span<br>style="font-size:12.0pt;font-family:Symbol;mso-ascii-font-family:&quot;Times New Roman&quot;;<br>mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">·</span><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp; I<br>learned about how to show<br>error friendly messages to the user<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:Symbol;mso-ascii-font-family:&quot;Times<br>New Roman&quot;;<br>mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">·</span><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp; I learned<br>about the database operation performed to store user details, assign role to<br>user.<o:p></o:p></span></p><br><br><p class="MsoNormal"<br>style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:Symbol;mso-ascii-font-family:&quot;Times New Roman&quot;;<br>mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">·</span><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">&nbsp;<br>I learned about how a user can not access the roles restricted parts<br>inthe website.<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>Symbol;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-fareast-font-family:&quot;Times New Roman&quot;;<br>mso-bidi-font-family:&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;<br>mso-fareast-language:EN-IN">·</span><span style="font-size:12.0pt;line-height:<br>107%;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times<br>New Roman&quot;;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">&nbsp; I learned about how to check the username and<br>email are already<br>a part of the database so if new user try to use the<br>same it will give a user friendly error message.<o:p></o:p></span></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vp645-prod.herokuapp.com/">https://is601-vp645-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/vp645" target="_blank">Grading</a></td></tr></table>