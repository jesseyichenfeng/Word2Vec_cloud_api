

# Koho Takehome Test
A simple case of using **Flask** and **Docker** to build an ML powered API server, running on **AWS EB**,  and meantime, using **AWS Kinesis** to continuously recording incoming requests. 

The function is: When you request a few words, the server will respond top 10 similarity single words according to your input, and also come with similarity values from 0 to 1.  
  

### Tools:
- Gensim
- Docker
- AWS Elastic Beanstalk (m5a.large, 2 vCPU, 8G memory, $0.086 per Hour)
- AWS Kinesis Fireholes
### Model:
English Wikipedia 2015 +  [NewsCrawl](http://www.statmt.org/wmt14/translation-task.html)  - 7B tokens - 368,999 words - 300 dimensions
Download the model into `/app` directory for testing.

-   [Word Vectors (398MB)](https://www.dropbox.com/s/kguufyc2xcdi8yk/lexvec.enwiki%2Bnewscrawl.300d.W.pos.vectors.gz?dl=1)


### Use case:

Sample API requests(cURL might not be working on newest WIN10 Commend Prompt):

    $ curl -X GET "kohotext.us-east-1.elasticbeanstalk.com/api"  -H "Content-Type: application/json" --data '{"text":"I want cashback debit card!!"}'

Sample respons:

    {"cardholder":0.5077738761901855,"cardholders":0.6193097233772278,"cards":0.6568129658699036,"cheque":0.5149604082107544,"contactless":0.5407369136810303,"customers":0.5053408741950989,"if":0.5097475051879883,"ll":0.5397184491157532,"overdraft":0.527230441570282,"you":0.6080142855644226}

[Use case using  python script](https://github.com/jesseyichenfeng/koho_takehome_test/blob/master/api_requests_example.ipynb)

[Sample data collected by AWS Kinesis](https://github.com/jesseyichenfeng/koho_takehome_test/blob/master/kohotext-1-2019-12-18-04-23-05-32fc0319-19ad-4d19-b004-65c460c1c6fe)



### Resource:
The simple version of this docker image (without kinesis collecting incoming requests) :
[koho_text_api Docker Image](https://hub.docker.com/r/fengyic1/koho_text_api)

### reference:
[https://github.com/alexandres/lexvec](https://github.com/alexandres/lexvec)

