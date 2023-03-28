<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Vandit Tejas Popat (vp645)</td></tr>
<tr><td> <em>Generated: </em> 3/27/2023 11:24:04 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/vp645" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228113218-0683db70-992d-44a4-9157-c5edd35adcf8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I am trying to calculate cost by adding another list where on the<br>go I will be adding the cost to it, just like the inprogress<br>burger this cost list would store the cost in each screenshot I am<br>trying to show that I append cost in each method and in the<br>end I return the sum of that list from calculate cost.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228113773-68b0bf59-9691-4c8a-aeaa-9987dc503b3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I am trying to show that I append cost in each method<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228113856-d583560a-70a7-4f7d-95cd-386d79fe0795.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I am trying to show that I append cost in each method<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228114031-e517db1b-0a47-458a-b87a-1791cb55f662.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I show the total burgers we create with the total cost upto<br>now <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228114216-60b0a827-f29f-4177-9de3-336288d986ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>returning the sum of the list of inprogress cost<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228114328-12789ab5-cf86-468f-aa35-926206d0237c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Formatting with .2f and , as in currency<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>I am trying to calculate cost by adding another list where on the<br>go I will be adding the cost to it, just like the inprogress<br>burger this cost list would store the cost in each screenshot I am<br>trying to show that I append cost in each method and in the<br>end I return the sum of that list from calculate cost. And for<br>currency formatter I used .2f like in the first assignment to display it<br>in 2 decimal places all the time<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228114504-2e02d8cc-9263-4327-b6a8-006f59354f32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot we raise out of stock exception when the quantity defined in<br>the list is less than 0 that is I have no more stock<br>of that patty or topping present, i print out this message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228114961-0e496e61-5b44-4d79-9a11-cb67ac720f7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I am checking if the machine is clean or not by checking<br>the remaining_uses if that is less than 0 the machine is not clean<br>and I ask for an input clean once i write clean the machine<br>cleans itself and we continue from where we left off<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228115194-3631ff5f-a9d0-49f6-b88f-394b2e12e789.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I am checking if what i entered is present in the list<br>of available options or no, if it is not I print out this<br>message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228115416-00437bb9-57da-422a-9f96-3409636c4a67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Moreover we have defined 3 as the limit for any topping or patty<br>so if that limit is exceeded we print out this exception with the<br>name of the stage<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228115624-c096ed74-fc9d-4150-9266-caa9a77dca2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here we check if the user entered the right amount as the bill<br>if not we throw this exception and print the following <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>OutOfStockException:&nbsp; We raise out of stock exception when the quantity defined in the<br>list is less than 0 that is I have no more stock of<br>that patty or topping present, i print out this message<div>NeedsCleaningException : Here I<br>am checking if the machine is clean or not by checking the remaining_uses<br>if that is less than 0 the machine is not clean and I<br>ask for an input clean once i write clean the machine cleans itself<br>and we continue from where we left off<br></div><div>InvalidChoice : Here I am checking<br>if what i entered is present in the list of available options or<br>no, if it is not I print out this message<br></div><div>ExceededRemaining: Moreover we have<br>defined 3 as the limit for any topping or patty so if that<br>limit is exceeded we print out this exception with the name of the<br>stage<br></div><div>InvalidPayment: Here we check if the user entered the right amount as the<br>bill if not we throw this exception and print the following&nbsp;<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228116751-03b1e339-c593-45b3-9996-6f49dffca6d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This image shows all passed test cases using pytest-rA what we are trying<br>to do in these test cases is that we are creating inputs which<br>would create exceptions and if we create exceptions the test case is passed.<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228117039-289e6a99-7f5a-4b09-bd16-d6b082ce3142.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the first test case where we have to check that the<br>first thing selected is bun and not anything else so we selected patty<br>here and assert check for false thus passed the test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228117356-c4fdeec0-38d9-49c6-aaae-7cf116917378.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the second test case where we check to add patty only<br>if it is in stock so we create veggies for more than 10<br>times thus checking if it throws exception when the quantity is greater than<br>available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228117649-f1634093-b224-48bb-af31-e6f63409379d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the third test case where we check to add toppings only<br>if it is in stock so we create bbq for more than 10<br>times thus checking if it throws exception when the quantity is greater than<br>available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228118372-e8d7c903-f806-4a73-9e7b-cb262d5f3b94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the 4th test case where we can only add patty for<br>3 combinations only so here i tried for more than three which would<br>throw an exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228118420-a9b207af-acb0-4e8a-9d25-d8101ac16c3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the 5th test case where we can only add toppings for<br>3 combinations only so here i tried for more than three which would<br>throw an exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228118460-921052b8-ff61-4e3a-a2b9-c8e7c0d385c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the 6th test case where I check for the cost of<br>random burgers and check it with my calculate function and get the right<br>answer<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228118526-1f9022ff-3ee7-42f7-8ff0-ac38821858e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is test case 7 and here i calculate the cost for all<br>3 burgers together and check it with our calculate function <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228118697-1f0b210d-5b49-40d9-b641-97aa5365fc49.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the 8th test case where i check for how many burgers<br>in total i have made purchase of in total created 3 burgers<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>what we are trying to do in these test cases is that we<br>are creating inputs which would create exceptions and if we create exceptions the<br>test case is passed.&nbsp;<br></div>This is the first test case where we have to<br>check that the first thing selected is bun and not anything else so<br>we selected patty here and assert check for false thus passed the test<br>case<div>This is the second test case where we check to add patty only<br>if it is in stock so we create veggies for more than 10<br>times thus checking if it throws exception when the quantity is greater than<br>available<br>This is the third test case where we check to add toppings only<br>if it is in stock so we create bbq for more than 10<br>times thus checking if it throws exception when the quantity is greater than<br>available<br></div><div>This is the 4th test case where we can only add patty for<br>3 combinations only so here i tried for more than three which would<br>throw an exception<br></div><div>This is the 5th test case where we can only add<br>toppings for 3 combinations only so here i tried for more than three<br>which would throw an exception<br></div><div>This is the 6th test case where I check<br>for the cost of random burgers and check it with my calculate function<br>and get the right answer<br></div><div>This is test case 7 and here i calculate<br>the cost for all 3 burgers together and check it with our calculate<br>function&nbsp;<br></div><div>This is the 8th test case where i check for how many burgers<br>in total i have made purchase of in total created 3 burgers<br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/15">https://github.com/vanditpopat/IS601-004/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>The issues I faced was in writing test cases, the logic for calculation<br>came to me easily but to test based on exceptions was not clear<br>and I had no idea for to check for exceptions in test cases<br>took a little research to do that<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/228119592-8e7f05ae-b9f4-4951-af90-0bf333de6492.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is examples where i order 2 burgers i can clearly see the<br>burger selected the price and in the end the total price with 2<br>burgers that is the total burgers created <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/vp645" target="_blank">Grading</a></td></tr></table>