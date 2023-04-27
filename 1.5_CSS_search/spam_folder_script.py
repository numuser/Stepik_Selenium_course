import os

count, path = 1, os.getcwd()
htmlContent = """<!DOCTYPE html>
<html>
<body>
  <h1>Look at my favorite cat memes:</h1>
  <p>If there's one thing that the internet was made for, it's funny cat memes.</p>
  <div class = "column">
      <div class="card-body">
          <img class="picture" src="https://www.dailydot.com/wp-content/uploads/2018/10/olli-the-polite-cat.jpg">
          <h3 id="polite"> Polite cat </h3>
          <p data-type="description"> Nice cat </p>
      	  <div class="btn-group">
	          <button type="button" class="btn btn-sm">View</button>
	          <button type="button" class="btn btn-sm">Edit</button>
	      </div>
      </div>
      <div class="card-body">
          <img class="picture" src="https://i.kym-cdn.com/photos/images/newsfeed/001/328/469/2a0.jpg">
          <h3 id="banana"> Banana cat </h3>
          <div class="btn-group">
	          <button type="button" class="btn btn-sm">View</button>
	          <button type="button" class="btn btn-sm">Edit</button>
          </div>
      </div>
   <div class="card-body">
      <img class="picture" src="https://thumbs.dreamstime.com/z/cat-colored-pool-watermelon-ring-slice-lying-swimming-resort-215604928.jpg">
      <h3 id="melon"> Watermelon cat </h3>
      <div class="btn-group">
	      <button type="button" class="btn btn-sm">View</button>
	      <button type="button" class="btn btn-sm">Edit</button>
	  </div>
   </div>
</div>
</body>
</html>
"""

cssContent = """/* */
{
    color:blue;
}



img {
	height: 100px;
}
.card-body {
    width: 200px;
    border: 1px;
    border: 1px solid rgba(0,0,0,.125);
    padding-right: 15px;
    padding-left: 15px;
    box-shadow: 0 0.25rem 0.75rem rgba(0, 0, 0, .05);
    border-top-left-radius: calc(.25rem - 1px);
    border-top-right-radius: calc(.25rem - 1px);
    margin-right: 15px;
    margin-left: 15px;
}

.btn-group {
    margin-bottom: 10px;
}


.column {
	display: flex;
}
body {
    color: black;
}
"""
print("Current working dir %s" % path)
for _ in range(int(input())):
    try:
        os.mkdir(path + "\\" + str(count))
    except FileExistsError:
        print(f"File {count} already exist!")
        count += 1
        continue
    with open(path + "\\" + str(count) + "\\" + "page.html", 'w') as html_page, open(path + "\\" + str(count) + "\\" + "page.css",
                                                                        'w') as css_page:
        html_page.write(htmlContent)
        css_page.write(cssContent)
    count += 1
