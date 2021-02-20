# Mentis-API

#### Problem Statement:

You are the ‘Natural Language processing’ expert and Python Engineer in ABC ltd. You are asked to write a simple python API to identify the Name, location, and product from the given text (Appendix A). The program has to handle multiple API requests concurrently and should leverage parallel processing capabilities of Python.



#### Technical Requirements 

1) API should be build using Python Flask
2) Use ‘Spacy’ for Named Entity Recognition (For identifying Name, Location, and Product in the text)
3) The API should handle any text and identify:
  - Name
  - City/Address
  - Product
The API should be able to handle multiple concurrent requests
The API should be able to parallel process requests

### Example Input
```
Dear team,
I ordered Excel Suite from ABC ltd on 10-02-2021. I am yet to receive the CD. Kindly do the needful.
Rajwat Singh,
Mumbai

```

### Expected Output
```
| Serial No |    Text      | Category |
---------------------------------------
|    1.     | Excel Suite  | PRODUCT  |
|    2.     | Rajwat Singh | PERSON   |
|    3.     | Mumbai       | CITY     |

```






