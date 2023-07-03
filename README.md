# 𝐒𝐞𝐧𝐭𝐢𝐦𝐞𝐧𝐭 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬 𝐨𝐧 𝐄-𝐂𝐨𝐦𝐦𝐞𝐫𝐜𝐞 𝐬𝐢𝐭𝐞 𝐮𝐬𝐢𝐧𝐠 𝐇𝐚𝐝𝐨𝐨𝐩

<b>⋆ Tool used :</b>
Instant Data Scraper <br>
<b>⋆ Python library :</b>
BeautifulSoup <br>
<b>⋆ Sites :</b>
Flipkart and Amazon <br>

<b>About :</b>
<p>Sentiment analysis is a natural language processing (NLP) technique used to determine whether data is positive, negative or neutral.It is performed to help businesses monitor brand and product sentiment in customer feedback and understand customer needs. I have used Instant Data Scrapper Tool for extracting data for analysis using Hadoop and BeautifulSoup Library.<br></p>
<p> My extracted data consists of information regarding Product name, Product ratings, Total product reviews, stars, current price and discount offered on product.
Here, BeautifulSoup library is used to pull the data out of HTML and XML files. It creates a parce tree from page source code that can be used to extract data in readable manner. </p>
<p> Further, Hadoop is used for our data analysis as it is an open-source framework, and it works efficiently on large datasets ranging from size gigabytes to petabytes. Also, Hadoop allows clustering multiple computers to analyse massive datasets in parallel.
The main objective to use sentimental analysis is to analyse people’s perspective regarding purchase of the product which can result in business strategies in a way. Moreover, business analysts can gain useful insights over different products.</p>

<b> Queries : </b><br>
-	Find the Lenovo products that get a rating of above 3, whose MRP is less than 60,000 and get a discount of 25%.<br>
-	Find the products named Lenovo and hp and get more than a 20% discount.<br>
-	Laptops that receive negative statement.<br>
-	HP laptops get more than 2 stars with flat discounts.<br>
-	Lenovo laptops with more than 3 stars, a current price of less than 50,000, and positive statements.<br>
-	Find the product that gets stars above 4 and gives a discount of more than 30% and gives any additional discounts.<br>
-	Find the name products with no rating or stars.<br>
-	List the product names that have a discount of more than 50%, offer any additional discounts, and receive a positive response.<br>
-	List down the names of those products that have negative reviews.<br>
-	List down the names of the products whose current price is less than their MRP.<br>
-	List out all the product from Flipkart having less price than 30,000 and having stars above 4.5.<br>
-	List out all the products that have no stars, no ratings, and no reviews.

<b> For output :</b><br>
<h5> hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -files mapper.py,reducer.py -mapper "python3 mapper.py 1" -reducer "python3 reducer.py" -input <your_input_csv_file_path> -output <your_output_directory_path></h5>

