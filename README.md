Insight Data Challenge
===========================================================

## Challenge Summary

This challenge is to implement two features:

1. Calculate the total number of times each word has been tweeted.
2. Calculate the median number of *unique* words per tweet, and update this median as tweets come in. 


## Getting Started

```
$ git clone git@github.com:jeanpan/insight_data_challenge.git
$ cd insight_data_challenge
$ ./run.sh
```


## Details of Implementation

* Calculate the total number of times each word has been tweeted : 

Use the concept of *MapReduce*, but run on single machine. 
*Mapper* counts every word as one, and then pipes data to *Reducer* which combines count by word. 

* Calculate the median number of *unique* words per tweet, and update this median as tweets come in : 

Use the concept of *Insertion Sort* to handle the streaming data. 
Whenever the num is coming, the list is sorted by *Insertion Sort*. Therefore, it's easy to get median for a sorted list. 
