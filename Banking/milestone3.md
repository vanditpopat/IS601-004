<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Bank Project</td></tr>
<tr><td> <em>Student: </em> Vandit Tejas Popat (vp645)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 2:09:29 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/vp645" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> User will be able to transfer between their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transfer page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236067179-0cefec4f-2127-4d46-a681-48acae9d10d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the page for internal transfer within different accounts<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing dropdown values</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236067703-7096e0aa-c4ee-4e2f-81d4-09df08102bcc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This would show us the account type, number and the price of two<br>different account type<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing user can't transfer more funds than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236068392-32da369a-7d17-4809-8124-024c40766569.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the message we when we try to transfer the money more<br>that the amount present<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot showing user can't transfer to the same account</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236096966-2ca82019-16f5-4000-bb0d-a4b9aae1698c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the snippet of the website where it is not allowed to<br>transfer between the two accounts<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236097122-9df4c57e-49e2-4fbb-b010-4ce2ca50dfc5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code snippet from the line 226 to 232 shows the code for<br>this where I check whether the source and the destination is same, if<br>yes this error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot showing you can't transfer an negative balance</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236097367-14390bd8-d70e-4c7a-9ded-33d50d86ac9d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We can see the application side throwing error on negative funds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236100048-42994741-9613-4653-bd5a-4f11b20a7b66.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the code snippet to check that the minimum number is 1<br>so that we cannot transfer 0 or negative in the application<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot of the generated transaction history from the db</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236105892-6b065251-9e18-4a86-b253-fefda0a43d1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>see the record with internal memo that is a successful transaction<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a screenshot of the Accounts table showing both affected accounts</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236107662-dbcf86cc-5002-4466-a344-341a3b8cfdfd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the snapshot of all accounts in the system<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Briefly explain the code process/flow of a transfer including how the accounts are fetched for the dropdowns</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Segoe UI&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;color:#1F2328;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">Initial<br>balance is fetched by using the accounts id<br>from all the<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Segoe UI&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;color:#1F2328;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">number of<br>accounts and their expected values<br>or total balance is displayed<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Segoe UI&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;color:#1F2328;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">- two<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Segoe<br>UI&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;color:#1F2328;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">transaction<br>are calculated by when a user transfer the money from source<br>to<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Segoe UI&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;color:#1F2328;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">destination account the money will be deducted from<br>the src account and it<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Segoe UI&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;color:#1F2328;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">will be<br>credited in the<br>destination account, this all process will be done<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Segoe UI&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;color:#1F2328;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">after<br>the<br>final commit.<o:p></o:p></span></p><br><br><p class="MsoNormal"><span style="font-size:12.0pt;line-height:107%;font-family:<br>&quot;Segoe UI&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;color:#1F2328;<br>mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-IN">- source account is deducted and destination<br>account is credited</span><o:p></o:p></p><br></td></tr>
<tr><td> <em>Sub-Task 9: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/36">https://github.com/vanditpopat/IS601-004/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 10: </em> Add link to transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vp645-prod.herokuapp.com/">https://is601-vp645-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Transaction History Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transaction history page showing the new transfer transaction</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236109590-3c96e553-c161-41a5-9b5c-74aba5000e6e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Look at the first record that is the internal transfer record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots demonstrating the filters and pagination</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236109730-80bef3bc-b65b-4b0a-a130-c85b717f3dec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Applied the transaction type as transfer filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236109969-000cabef-1e1a-45be-b330-195fe885af4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Applied date filter for 2023-05-03 day <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236528006-91c707f4-1151-4f79-867b-2030940b5420.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pagination done, was not able to do it before so that is why<br>cannot see it in the previous screenshots but was able to do it<br>later therefore the ss from now on will contain pagination<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the filters/pagination work</td></tr>
<tr><td> <em>Response:</em> <p>So the logic for pagination is that I have added a limit per<br>page that is 2&nbsp;<div>since i dont have a lot of transactions and once<br>the result of transaction goes above the page limit</div><div>&nbsp;I create a new page<br>and that is shown by page variable in the url</div><div>I just divide the<br>result count by two so as many results I get i creat divide<br>by 2 pages</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/41">https://github.com/vanditpopat/IS601-004/pull/41</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add link to Transaction History page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vp645-prod.herokuapp.com/">https://is601-vp645-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User's profile First name and Last name </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's profile with the new fields</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236529002-4ac822c9-2ec3-4b84-a22a-ba4486b04c90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We can now see the first and last name on the profile page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/41">https://github.com/vanditpopat/IS601-004/pull/41</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Add link to profile page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vp645-prod.herokuapp.com/">https://is601-vp645-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to transfer funds to another user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the external transfer page with filled in data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236531364-443cad9c-c9f1-4df7-a434-97d4bee279cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sending money to someone&#39;s account through external transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing user can't send more than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236531902-5fc1cb2a-d679-4677-811f-e17e525b57ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cannot exceed the amount of more than present<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236532470-9450c226-7ea4-47d3-bd2a-2b135510ee1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet where I check the expected balance and see that the amount<br>is less than the expected balance<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing they can't send a negative amount</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236532683-5cec328d-1918-4d8c-940b-e4ce9489de90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Application side ss for not able to transfer negative amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236532919-85aa20fc-4056-4df6-9d38-2ad20e57b635.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Validation to funds so that minimum is 1 and not negative<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot(s) showing message if a user doesn't exist and/or a destination account wasn't found</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236533285-c7fdb17d-4c45-4ee0-b1cc-1af5536c778e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The message when I cannot find the user account as I have entered<br>the wrong information<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236533563-1d4ddb2b-e4a0-4cc1-acee-e0ba0a3e5b9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Script for user not found<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot of the transactions table showing the recorded transfer</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236533776-f92257b0-e436-4cb2-a285-cb8ae7e4bcf5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Application ss for successful transfer<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236533990-6b864e3d-a2e5-4b23-b657-78af00bea0e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>See the last two records with memo ext transfer ss<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot(s) showing the updated account balances</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/51928264/236534213-175cc719-21a9-4c72-b669-b3a87279dd36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check row 3 and 4 the balance changed from 4650 to 3650 for<br>3 and 600 to 1600 for 4<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain the process of looking up the target user's account and the validation logic</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">Account is fetched using the account<br>id plus the user id<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">- The<br>destination account is fetched using the input given by user as a last<br><br>name<br>and the account number ending 4 digits.<o:p></o:p></span></p><br><br><p class="MsoNormal" style="margin-bottom:0cm;line-height:normal"><span style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:<br>&quot;Times New<br>Roman&quot;;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:<br>EN-IN">- Then it will perform the two transaction one will be deduction of<br>amount from src account and the<br><br>same amount will be transferred to the src<br>account</span></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vanditpopat/IS601-004/pull/41">https://github.com/vanditpopat/IS601-004/pull/41</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add link to external transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vp645-prod.herokuapp.com/">https://is601-vp645-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learning for how transfer between two account and the logic behind it, learnt<br>the most in pagination on how to add it and how to add<br>it in the UI as well.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/vp645" target="_blank">Grading</a></td></tr></table>