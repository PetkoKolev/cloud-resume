# Cloud Resume (AWS Project)

##  Live Demo

- Custom Domain: https://petkokolev-cloud.com
- CloudFront (HTTPS): https://d24i00e0pp817c.cloudfront.net  
- S3 Website Endpoint: http://petko-cloud-resume-1.s3-website.eu-west-2.amazonaws.com/

---

##  Overview

This project is a cloud-hosted personal resume website built using AWS services. 

It demonstrates both frontend and backend cloud engineering concepts, including static website hosting, CDN distribution, serverless computing, NoSQL database integration, API integration and real-world debugging of cloud systems.

The application evolved from a simple static site into a full-stack serverless application with a live visitor counter powered by AWS Lambda and DynamoDB.

---

##  Technologies Used

Frontend
- HTML
- CSS
- JavaScript (Fetch API)

Backend (Serverless)
- AWS Lambda (Python)
- Amazon DynamoDB
- AWS SDK (boto3)
- AWS API Gateway (HTTP API)

Cloud & Infrastructure
- AWS S3 (Static Website Hosting)
- AWS CloudFront (CDN + HTTPS)
- AWS Route 53 (DNS & Domain Management)
- AWS Certificate Manager (SSL/TLS)

Dev Tools
- GitHub (Version Control)
- VS Code
- Pytest (Backend testing)
- AWS CLI (Local development & Authentication)
- Terminal (CLI testing & debugging)

---

##  Key AWS Concepts

- Static website hosting using S3
- CDN (Content Delivery Network) using CloudFront
- HTTPS & SSL certificate management with ACM
- DNS routing using Route 53 (A records & alias records)
- Serverless architecture with Lambda
- API design using API Gateway (HTTP API)
- NoSQL database design with DynamoDB
- Cache invalidation and CDN behaviour
- Public vs private bucket access control

---

##  Architecture Diagram

User (Browser) → CloudFront (CDN + HTTPS) →S3 (Static Website Hosting) → Browser (JavaScript) → API Gateway → Lambda Function (Python) → DynamoDB (Visitor Counter)
---

##  Features

- Static resume website hosted on AWS
- Global content delivery via CloudFront CDN
- Custom domain with HTTPS (Route 53 + ACM)
- Responsive and styled UI using CSS
- Dynamic visitor counter powered by serverless backend
- Real-time database updates using DynamoDB
- Fully integrated frontend and backend architecture

---

##  What I Learned

- How to host static websites using AWS S3
- Difference between S3 website endpoint vs S3 API endpoint
- How CloudFront integrates with S3 origins
- Debugging 403 Access Denied errors in AWS
- Designing and integrating serverless backends
- Importance of correct content types and file encoding
- Managing public vs private access in cloud environments
- Handling DynamoDB data modelling and reserved keywords
- How to config IAM users and access keys for secure local AWS access
- Differences between AWS-managed credentials (Lambda) vs local environments 
- Debugging AWS SDK issues such as missing region and credentials
- Running and validating backend logic logically using Pytest
- Using terminal to interact with cloud services and run automated tests

---

##  How It Works (Visitor Counter)

1.	User visits the website
2.	JavaScript sends a request to API Gateway
3.	API Gateway triggers Lambda function
4.	Lambda increments the counter in DynamoDB
5.	Updated count is returned to the frontend
6.	Visitor counter is displayed on the page

---

## Testing
Backend tests were implemented using purest to validate Lambda function

- Verified status codes and response structure
- Ensured visitor counter increments correctly 
- Tests executed locally using Python and terminal CLI
- Integrated AWS SDK (boto3) for real DynamoDB interaction

---

## Local Setup
To run tests locally:

1. Clone GitHub repo if not done already
2. In terminal, write cd (file path/project name) and use ls to verify in correct folder
3. Write cd backend to access backend subfolder
4. Python command of: python3 -m pytest 

---

##  How to Deploy

1. Create an S3 bucket and enable static website hosting  
2. Upload HTML, CSS and JavaScript files  
3. Configure bucket policy for public access  
4. Create CloudFront distribution pointing to S3 website endpoint  
5. Request SSL certificate via AWS Certificate Manager  
6. Add custom domain using Route 53 and alias records  
7. Attach certificate to CloudFront distribution
8. Create DynamoDB table
9. Deploy Lambda function (Python)
10. Create API Gateway (HTTP API) and connect to Lambda
11. Connect frontend JavaScript to API endpoint
12. Invalidate CloudFront cache after updates (may load previous versions containing old JavaScript if not done) 

---

##  Challenges Faced

- Fixed HTML rendering issues caused by incorrect file encoding (TextEdit vs VS Code)
- Resolved S3 bucket policy errors (invalid resource) 
- Debugged CloudFront 403 errors caused by blocking public access
- Handled DynamoDB reserved keyword issue (views)
- Resolved data inconsistency caused by multiple counter records
- Debugged CloudFront caching issues causing stale frontend data
- Resolved AWS credential errors when running code locally (NoCredentialsError during unit testing through terminal)
- Debugged region misconfig between local environment and deployed AWS services

---

##  Future Improvements

- Improve API design (separate GET and POST reqeusts)
- Implement Infrastructure as Code using Terraform or AWS SAM
- Set up CI/CD pipeline for automated deployments using GitHub Actions
- Migrate to private S3 bucket using CloudFront Origin Access Control (OAC)
- Add unit tests for Lambda functions
- Add caching strategy optimisation in CloudFront
- Create blog post documenting full build process
