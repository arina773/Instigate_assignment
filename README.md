# Table of contents

- Requirements <br>
      <pre>
      Receives two folders <folder1> and <folder2> as cormand line argunents  <br>
      Receives two folders <folder1> and <folder2> as cormand line argunents <br>
      Traverses <folder1>, finds all files in it, compares (with same file with the same folder hierarchy) in <folder2><br>
      Creates html report file.<br>
          If file1 in <folder1> is the same as file1 in <folder2> add line in html: <folder1/file1> is the same as <folder2/file2><br>
          If file1 in <folder1> differs from file2 in <folder2> add line in html: <folderl/ftle1> differs <folder2/ftle2> "link_to_diff_ftles"<br>
      If some file exists in <folder1> but is absent in folder then add line in html: <folder1/file3> is missing in <folder2><br>
      </pre>
- Modules <br>
  <pre>
   difflib <br>
   filecmp <br>
   os <br>
   path <br>
   sys <br>
   </pre>
 - Installation<br>
  <pre>
  None
  </pre>
- Configuration<br>
  <pre>
  None
  </pre>
