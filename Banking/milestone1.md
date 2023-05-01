<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Joy Prakashchandra Patel (jp2267)</td></tr>
<tr><td> <em>Generated: </em> 11/12/2022 16:05:25</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/jp2267" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206923047-914cbc35-ddff-4454-9b9e-83e83735e7c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206923105-313f06b2-a1d4-45e9-83b8-40e6646beadd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206923142-8c1172a1-ec68-4a4e-b72d-5d945722cf32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206923202-b4b93c63-1b4e-4775-81ed-4ade6c474172.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206923221-a45039bb-3dde-4bcf-b4ec-7b4cc3378744.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206923244-5a9f14f7-2bb5-4ee6-b05f-5be5632d2436.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the form with valid data filled in before the form is submitted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206923272-3a60029a-62b6-446a-94bb-bc3c1c561461.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully added record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206923334-bf5fd3a1-5ae7-412a-8c18-711fce927fbd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/24">https://github.com/jp2267/is-601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ul><li>The form is handle using the wtf flask forms.</li><li>The validation are used by<br>wtf forms validators functions.</li><li>The password is handle by bcrypt algorithm which hases the<br>password in a plain text.</li><li>The db is utilized for basic database operation such<br>as create, read ,update and delete.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206923142-8c1172a1-ec68-4a4e-b72d-5d945722cf32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206924075-ceb0e53a-0d0a-4388-9be8-125846b30892.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entered the login credentials<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206924088-dd92fb3e-c465-4799-a0e2-9567171a107f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/24">https://github.com/jp2267/is-601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ul><li>The form is handle using the wtf flask forms.</li><li>The validation are used by<br>wtf forms validators functions.</li><li>The password is handle by bcrypt algorithm which hases the<br>password in a plain text.</li><li>The db is utilized for basic database operation such<br>as creat, read ,update and delete.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206924203-5d89574e-b83a-43de-a390-8ccda7768bb1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the user is logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206924245-6dbe4e2b-b6e1-4566-9536-ce4c0b3337c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/24">https://github.com/jp2267/is-601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ul><li>The session logic is used from flask login.</li><li>We will store the users id<br>in the active session so he can access the login protected pages.</li><li>When the<br>user logged out the users id is removed from the session.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206924245-6dbe4e2b-b6e1-4566-9536-ce4c0b3337c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206924674-3c710698-75fe-4995-b4b8-2cc092b1cc9e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing a user without an appropriate role can&#39;t access the role-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206924856-6e709a0f-1236-472a-a582-2fe3c3dd3e3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles Table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206924902-80823af5-6681-4b17-84fa-67e56d69349c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first user is the admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/24">https://github.com/jp2267/is-601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <ul><li>roles are assigned to the user</li><li>when the assigned role user login, he will<br>only be able to see limited part which is set by the admin</li><li>We<br>are using flask principle for the roles part</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <ul><li>In the application i have defined one admin permission object with the help<br>of flask principle package</li><li>The session will check for the active roles assigned to<br>the user.</li><li>For example if the user has the admin role assigned then he<br>will able to perform all the admin stuff such as create role and<br>assign role to users.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206925020-bdd522bb-64f0-4547-a89c-8a9cbfaae884.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows basic style is given<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206925064-4fb0ed89-3030-4f15-beee-586db853fb5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows basic style is given<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206925091-9e6d43ce-5ebd-44ab-b124-77abb3b9639a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>form is proper formated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/24">https://github.com/jp2267/is-601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <ul><li>I have used bootstrap classes for styling the navigation bar, the form fields<br>and the body content of the web application.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206925194-016363a2-dc1a-47fc-aa71-72e3893b59f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>permission denied message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206925617-fbb2bc99-5ccf-4e0a-9670-f9a8d06f259d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username already exist message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206925657-7f088b20-bbd0-4abb-9a94-d01821bc6dbb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email already exist message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/24">https://github.com/jp2267/is-601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <ul><li>We are using flask flash messages function to show user user friendly message<br>with the help of exception handling when a error occur a custom message<br>id displayed in the web application.&nbsp; &nbsp;&nbsp;</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206925876-ab1977c9-f040-43aa-a6a5-f986429c87b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the users profile with pre-filled data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/24">https://github.com/jp2267/is-601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <ul><li>It is happening with the help of current user flask login object values<br>and we are pulling the data from the database of the particular user<br>login.&nbsp;</li><li>The flask login will retrive the data into the form.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926111-2d70f41b-84f6-4f27-8ff2-0f6508adadca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926197-a570acc6-fe5c-4e1f-a550-8468996f46f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926301-7538b5e5-4ea9-44d1-8eae-b5115be3625f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926240-f229e8e4-68a7-4cbe-821d-18278a9bf07a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926368-6b8a8739-6ec8-4fd4-9f4e-9f5f32346476.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username already in use message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926443-3374d298-d0dd-483d-9e4d-4a1a98d5d0c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926557-3cf0a216-e95c-4dfb-9d88-5c3eb4430450.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before editing see the second record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926583-d57834ee-ecff-4c53-8842-0a4416cb3a76.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after editing see the second record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926601-0a87c02d-4543-4419-bff1-4ee59928ac1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>editing record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206926637-52493147-f9d3-495d-b28a-873febc39ff7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>record edited <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/24">https://github.com/jp2267/is-601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <ul><li>for the validation we are using the wtf form validators</li><li>we will get the<br>user from the flask login object</li><li>after editing the data the session will be<br>refreshed with the updated record</li><li>It works similar as the register route.&nbsp;</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <ul><li>In these milestone I learned the user authentication using the wtf forms, validators<br>and flask login</li><li>I also learned about registering the user</li><li>I learned that the user<br>can login with the username and email, for these we are using the<br>rex functions</li><li>I learned about the user roles using flask principles.</li><li>I learned about the<br>sessions</li><li>I learned about how to show error friendly messages to the user</li><li>I learned<br>about the database operation performed to store user details, assign role to user.</li><li>I<br>learned about how a user can not access the roles restricted parts in<br>the website.</li><li>I learned about how to check the username and email are already<br>a part of the database so if new user try to use the<br>same it will give a user friendly error message.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is-601-jp2267-fp-prod.herokuapp.com/">https://is-601-jp2267-fp-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/jp2267" target="_blank">Grading</a></td></tr></table>