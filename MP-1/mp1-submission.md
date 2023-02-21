<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Vandit Tejas Popat (vp645)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2023 11:21:40 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/vp645" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220244884-9f2798ff-41f3-4a3b-a62b-23c69cfde217.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this add task method I use the if conditions to check if<br>the input is provided correctly update the last Activity to the current datetime<br>and add all this to the global variable tasks Print a message to<br>say the task is successful and save it.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220244991-aa3b94ac-59b7-4908-be78-b5b04a2af7e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This tell us that we have not added any input properly and thus<br>try again<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">update lastActivity with the current datetime value</span><div><span style="font-size: 13px;">set the name,<br>description, and due date (all must be provided)</span><br></div><div><span style="font-size: 13px;">add the new task<br>to the tasks list</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">Message confirming or denying it.</span></div><div><span style="font-size:<br>13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245102-83cf4b7a-b799-4e57-90e4-c5f099e7e290.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I am getting the task by Id and then trying to update<br>the task, firstly I check if the input i provided or not Then<br>I also check whether the input provided is different to the initial value<br>and update the last Activity accordingly, I also check for index out of<br>bound exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>I replaced todo with the following property in that index provided<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245102-83cf4b7a-b799-4e57-90e4-c5f099e7e290.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I am getting the task by Id and then trying to update<br>the task, firstly I check if the input i provided or not Then<br>I also check whether the input provided is different to the initial value<br>and update the last Activity accordingly, I also check for index out of<br>bound exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245243-7cd19f30-0849-4763-9b4f-1766658f2e3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I have shown for success above and showing for index out of bound<br>here<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">find the task by index</span><div><span style="font-size: 13px;">consider index out of bounds<br>scenarios and include appropriate message(s) for invalid index</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">update incoming<br>task data if it&#39;s provided (if it&#39;s not provided use the original task<br>property value)</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">update lastActivity with the current datetime value</span><span style="font-size:<br>13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245352-715ce0c4-4370-4075-92da-b991b06ae529.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I basically find the task by index if not present send a<br>message and if present change the done to present time<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245482-2ff0dd6b-f30a-44e1-812e-5e9b2e50e363.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I have shown success in the above image and if task is already<br>done I return that as well<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">find the task by index</span><div><span style="font-size: 13px;">consider index out of bounds<br>scenarios and include appropriate message(s) for invalid index</span></div><div><span style="font-size: 13px;">If not done update<br>done with present time</span></div><div><span style="font-size: 13px;">If done display message</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245609-b1b3b550-0ff4-4e5d-b472-4e22949cdb23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I check for the index first if present I just take that<br>dictionary and print it out using print statement<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245697-3c275da5-a657-4127-b579-8df0159db78d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success is shown above out of bound shown in this ss<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245769-bbac0a34-8a48-4213-8d41-e7bde4bcb4aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I present 2 task with different data and one out of bound<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245861-2ce67f14-fe46-4194-83f1-2b3835dd2337.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete/remove task from list by index and consider out of bound using del<br>function call<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220245918-255455af-4a47-4635-a4ba-7c5266b15193.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shown deleted above and out of bound here<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">delete/remove task from list by index</span><div><span style="font-size: 13px;">message should show if<br>it was successful or not</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">consider index out of bounds<br>scenarios and include appropriate message(s) for invalid index</span><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220246012-c483600b-e16e-41bf-82b6-5401565136c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I iterate through the list and check if done is still false<br>if yes Append that task to a different list and then print that<br>list out if not then print that message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220246096-bfd758bd-8ddf-4b2a-b3fa-1b02ac2e0224.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success shown above after done with that task failure shown here<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">generate a list of tasks where the task is not done</span><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;pass that list into list_tasks()</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">Failure shows some message<br>about no tasks</span><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220246179-8f1dfd8c-84dd-4a87-8e1e-22c75af7f359.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the overdue task by checking if the done attribute is false<br>and the due date is before today If so show the task or<br>else the message of no such tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220246258-02bf234a-f155-4616-9bf1-50e1d2313cf6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success above failure here<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">generate a list of tasks where the due date is older<br>than now and that are not complete</span><div><span style="font-size: 13px;">pass that list into list_tasks()</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<br></span></div><div><span style="font-size: 13px;">Success and failure message</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220246417-048c11a4-6b6c-48af-84d4-962442f7bf94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Get task by id and when present convert the now to the format<br>and then subtract that from due Get the days using .days and seconds<br>using .second and then find hours minutes left to that day and display<br>it Also check for overdue assignment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220246465-c93fe183-8fe0-435e-88d2-52abfd674022.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success above failure here<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">get the task by index</span><div><span style="font-size: 13px;">consider index out of bounds<br>scenarios and include appropriate message(s) for invalid index</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">get the<br>days, hours, minutes, seconds between the due date and now</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size:<br>13px;">display the remaining time via print in a clear format showing days, hours,<br>minutes, seconds</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">if the due date is in the past<br>print out how many days, hours, minutes, seconds the task is over due<br>(clearly note that it&#39;s over due, values should be positive)</span><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220246541-50f05f7f-72b5-4c7f-ac7c-5a344fc2106a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Testing and wrong outputs<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/220246575-410de821-9371-4d23-8f5b-d4e180479fc3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>JSON File<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>I took this project as a complete newbie in python and learnt a<br>lot about how method works how can we call methods and function, use<br>of dict inside list and a few datetime functions that might come handy<br>to me in the future, I faced a few errors while accessing dictionary<br>inside list wrong index wrong datetime format etc but I tried and solved<br>almost all problems.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/7">https://github.com/vanditpopat/IS601-004/pull/7</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/vp645" target="_blank">Grading</a></td></tr></table>