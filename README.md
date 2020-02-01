# Recommendation_problem
Popularity based , Collaborative based, Content based recommendation system 

## Problem Statement: Recommend similar movies using the MongoDB database as a data source.

### Data Source-
MongoDB database

### Technologies Used- 
Python, MongoDB
	

### Metrics-
	Linear Kernel (sklearn library )
	Pearson Correlation


### Data Understanding- Data consists of movies name with the corresponding summary of the movie with genres. 

## Approach

### Popularity Based Recommendation System:<br>

- we get our hand dirty with the movie dataset. we look carefully at the user ratings and think what’s to be done?<br>
- The answer that strikes first is the most popular Item. This is exactly what we will be doing.<br>
- Technically this is super fast but id does come with a major drawback which is lack of personalization. The dataset that has many files but we will be looking at a few of these files mainly the ones which relate to movie ratings.<br>
- In this approach, we recommend items that are liked by most users. This is a blazing fast and dirty approach and thus has a major drawback. The things are, there is no personalization involved with this approach. Such methods are widely used in news portals and work effectively because of the following points<br>
- There is division by section so the user can look at the section of his interest.<br>
-  At a time there are only a few hot topics and there is a high chance that a user wants to read the news which is being read by most others
<br>
### Collaborative Based Recommendation System:
<br>
#### User-Based Collaborative Filtering 
<br>
- Here we find lookalike customers (based on similarity) and offer products which the first customer’s look-alike has chosen in the past. This algorithm is very effective but takes a lot of time and resources. It requires compute every customer pair information which takes time. Therefore, for big base platforms, this algorithm is hard to implement without a very strong parallelizable system.<br>
- Build a matrix of things each user bought viewed rated<br>
- compute similarity scores between users<br>
- find users similar to you<br>
- Recommend stuff they bought/viewed/rated that you haven’t yet<br>
#### Problems
<br>
- People taste change<br>
- They are usually many more people than things<br>
- People do bad things
<br>
#### Item Based Collaborative Filtering
<br>
- It is quite similar to the previous algorithm, but instead of finding customers look-alike, we try finding items look alike. Once we have items look-alike matrix, we can easily recommend alike items to customers who have purchased an item from the store. This algorithm is far less resource consuming than user-user collaborative filtering.<br>
- Find every pair of movies that were watched by the same person<br>
- Measure the similarity of rating across all the users who watched both<br>
- Sort movie then by similarity strength<br>
#### Interesting fact
<br>
Item- Item Collaboration is extensively used in amazon or most of the E-commerce companies and they came out with it in great detail.

### 3. Content-Based Recommendation System:
<br>
- In this, we mainly focus on features or content of movie features according to that we recommend similar movies. For eg. Whenever we visit movie platforms like Netflix or amazon prime as soon as you click on movie we get similar movies based on the similarity of the movie.<br>
- This is basic which has been used by almost every E-commerce platform company.<br>

