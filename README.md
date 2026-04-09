# Cloud Resume (AWS Project)

##  Live Demo

- Custom Domain: https://petkokolev-cloud.com
- CloudFront (HTTPS): https://d24i00e0pp817c.cloudfront.net  
- S3 Website Endpoint: http://petko-cloud-resume-1.s3-website.eu-west-2.amazonaws.com/

---

##  Overview

This project is a cloud-hosted personal resume website built using AWS services.

It demonstrates both frontend and backend cloud engineering concepts, including static website hosting, CDN distribution, serverless computing, API integration, and NoSQL database design, alongside CI/CD pipelines and observability.

It started as a static site and evolved into a full-stack serverless application with automated deployments through GitHub Actions, infrastructure as code using Terraform, and real-time monitoring using CloudWatch.

---

##  CI/CD Pipeline (Github Actions)

This project uses GitHub Actions to automate testing and deployment

Backend Pipeline:
- Runs Python tests using Pytest
- Packages Lambda function
- Deploys Infrastructure using Terraform
- Applies changes automatically on push to main branch

Frontend Pipeline
- Syncs frontend files to S3
- Invalidates CloudFront cache to ensure latest content is served

Key Features
- Automated depolyment on code changes
- Infrastructure as Code (Terraform)
- Secure AWS authentication using GitHub Secrets
- Separate frontend and backend workdlors

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
- Terraform (Infrastructure as Code)

Dev Tools
- GitHub (Version Control)
- GitHub Actions (CI/CD)
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
- IAM roles and secure credential management
- Infrastructure as Code using Terraform
- CI/CD automation using GitHub Actions
- Observability using CloudWatch metrics

---

##  Architecture Diagram

User (Browser) → CloudFront (CDN + HTTPS) →S3 (Static Website Hosting) → Browser (JavaScript) → API Gateway → Lambda Function (Python) → DynamoDB (Visitor Counter) → CloudWatch (Metrics & Logs)

CI/CD:
GitHub → GitHub Actions → AWS (Terraform + Deployment)

---

##  Features

- Static resume website hosted on AWS
- Global content delivery via CloudFront CDN
- Custom domain with HTTPS (Route 53 + ACM)
- Responsive and styled UI using CSS
- Dynamic visitor counter powered by serverless backend
- Real-time database updates using DynamoDB
- Fully integrated frontend and backend architecture
- Infrastructure managed using Terraform
- Automated CI/CD pipelines for deployment
- Real-time monitoring using CloudWatch metrics

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
- Using terminal and AWS CLI for development and debugging
- Managing infrastructure using Terraform
- Handling Git issues related to large files and repository management (Terraform files above 750mb limit, caused commit history to reset)
- Handling Git issues of logic (implementing try and catch to enable the code to still execute even if the lab environment have no credentials for AWS services to avoid hardcoded credentials which would reduce security)

---

##  How It Works (Visitor Counter)

1.	User visits the website
2.	JavaScript sends a request to API Gateway
3.	API Gateway triggers Lambda function
4.	Lambda increments the counter in DynamoDB
5.	Lambda publishes a metric to CloudWatch
6.	Updated count is returned to the frontend
7.	Visitor counter is displayed on the page

---

## Testing
Backend tests were implemented using purest to validate Lambda function

- Verified status codes and response structure
- Ensured visitor counter increments correctly 
- Tests executed automatically in CI pipeline
- Mockinh used to isolate AWS dependencies (DynamoDB and CloudWatch in lambda function)

---

## Local Setup
To run tests locally:

1. Clone GitHub repo if not done already
2. In terminal, write cd (file path/project name) and use ls to verify in correct folder (folder directory)
3. Write cd backend to access backend subfolder
4. Python command of: python3 -m pytest to run tests
Note: AWS credentials and region must be configured locally using the AWS CLI.

---

##  How to Deploy
OLD METHOD BEFORE CI/CD PIPELINE
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

NEW METHOD
Infrastructure and deployments are automated using Terraform and GitHub Actions

Backend:
- Terraform provisions Lambda, API Gateway, DynamoDB, IAM roles
- CI pipeline runs tests and deploys automatically

Frontend:
- Files uploaded to S3 via CI pipeline
- CloudFront cache invalidated after updates 

---

##  Challenges Faced

- Fixed HTML rendering issues caused by incorrect file encoding (TextEdit vs VS Code)
- Resolved S3 bucket policy errors (invalid resource) 
- Debugged CloudFront 403 errors caused by blocking public access
- Handled DynamoDB reserved keyword issue (views)
- Resolved data inconsistency caused by multiple counter records
- Debugged CloudFront caching issues causing stale frontend data
- Resolved AWS credential errors when running code locally (NoCredentialsError during unit testing through terminal) and in CI environments
- Debugged region misconfig between local environment and deployed AWS services
- Resolved GitHub push failures due to large Terraform provider files
- Fixed GitHub Actions pipeline failures (missing credentials, file paths)
- Resolved IAM permission issues for CloudWatch metrics (CloudWatch:PutMetricData) 

---

##  Future Improvements

- Improve API design (separate GET and POST reqeusts)
- Add CloudWatch alarms for traffic spikes 
- Expand Terraform configuration to fully modular infrastructure
- Migrate to private S3 bucket using CloudFront Origin Access Control (OAC)
- Expand unit and integration test coverage
- Enhance secuirty using leastpriviledge IAM policies instead of FullAccess during build process
- Create blog post documenting full build process

---

##  Why This Project

This project demonstrates practical cloud-engineering skills beyond theory, including the following:

- Building and deploying serverless applications
- Automateing infrastructure using Terraform
- Implementing CI/CD pipelines
- Applying monitoring and observability practices

It reflects on real-world workflows to simulate DevOps and cloud engineering roles to help with my own career progression
