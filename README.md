# Cloud Resume (AWS Project)

## Live Demo

- Custom Domain: https://petkokolev-cloud.com  
- CloudFront (HTTPS): https://d24i00e0pp817c.cloudfront.net  
- S3 Website Endpoint: http://petko-cloud-resume-1.s3-website.eu-west-2.amazonaws.com/

---

## Overview

This project is a full-stack serverless cloud application that hosts my personal resume using AWS.

It demonstrates real-world cloud engineering and DevOps practices, including infrastructure as code, CI/CD automation, API security, rate limiting, and observability.

Originally built as a static site, it evolved into a production-style system with a secure backend, automated deployments, and resilience testing under load.

---

## CI/CD Pipeline (GitHub Actions)

### Backend Pipeline
- Runs Python tests using Pytest
- Packages Lambda function
- Deploys infrastructure using Terraform
- Applies changes automatically on push to main branch

### Frontend Pipeline
- Syncs frontend files to S3
- Invalidates CloudFront cache to ensure latest content is served

### Key Features
- Automated deployment on code changes  
- Infrastructure as Code (Terraform)  
- Secure AWS authentication using GitHub Secrets  
- Separate frontend and backend workflows  

---

## Technologies Used

### Frontend
- HTML, CSS, JavaScript (Fetch API)

### Backend (Serverless)
- AWS Lambda (Python)
- Amazon DynamoDB
- AWS API Gateway (HTTP API)
- Lambda Authorizer (custom authentication)

### Cloud & Infrastructure
- AWS S3 (Static Website Hosting)
- AWS CloudFront (CDN + HTTPS)
- AWS Route 53 (DNS)
- AWS Certificate Manager (SSL)
- Terraform (Infrastructure as Code)

### Dev Tools
- GitHub (Version Control)
- GitHub Actions (CI/CD)
- Pytest (Backend testing)
- AWS CLI
- VS Code / Terminal

---

## Key AWS Concepts

- Static website hosting using S3  
- CDN distribution using CloudFront  
- HTTPS with ACM certificates  
- DNS routing using Route 53  
- Serverless architecture with Lambda  
- API design using API Gateway (HTTP API)  
- NoSQL data modelling with DynamoDB  
- IAM roles and secure access control  
- Infrastructure as Code (Terraform)  
- CI/CD automation with GitHub Actions  
- Observability using CloudWatch  
- API security using Lambda Authorizers  
- Rate limiting and throttling  

---

## Architecture

User (Browser)  
→ CloudFront (CDN + HTTPS)  
→ S3 (Static Website Hosting)  
→ JavaScript (Frontend)  
→ API Gateway  
→ Lambda Authorizer (Authentication)  
→ Lambda Function  
→ DynamoDB (Visitor Counter)  
→ CloudWatch (Metrics & Logs)

CI/CD:  
GitHub → GitHub Actions → AWS

---

## Features

- Static resume website hosted on AWS  
- Global content delivery via CloudFront  
- Custom domain with HTTPS  
- Dynamic visitor counter (serverless backend)  
- Infrastructure managed with Terraform  
- Automated CI/CD pipelines  
- CloudWatch metrics and logging  

### 🔐 Security
- Custom Lambda Authorizer for API protection  
- Token-based authentication via HTTP headers  
- Restricted CORS to specific domain  

### 🚦 API Protection
- Rate limiting using API Gateway throttling  
- Burst and steady-state traffic control  
- Protection against abuse and excessive requests  

### 🔥 Resilience Testing
- Load tested API using parallel requests (curl)  
- Observed system behaviour under high traffic  
- Identified failure responses (503 Service Unavailable)  
- Validated throttling effectiveness  

---

## How It Works (Visitor Counter)

1. User visits the website  
2. Frontend sends authenticated request to API Gateway  
3. Lambda Authorizer validates request  
4. Lambda function updates counter in DynamoDB  
5. Metric sent to CloudWatch  
6. Updated count returned to frontend  
7. Displayed on UI  

---

## Testing

Backend tests implemented using Pytest:

- Validates status codes and response structure  
- Ensures counter logic works correctly  
- Uses mocking to isolate AWS dependencies  
- Runs automatically in CI pipeline  

---

## Challenges Faced

- Debugging CloudFront caching issues  
- Resolving IAM permission errors  
- Handling DynamoDB reserved keywords  
- Fixing CI/CD pipeline failures  
- Managing Terraform state and large files  
- Implementing secure CORS policies  
- Debugging API authentication failures  
- Handling rate limiting and backend saturation under load  

---

## What I Learned

- Building full-stack serverless applications  
- Designing secure APIs with authentication  
- Implementing rate limiting and traffic control  
- Debugging real-world cloud issues  
- Writing testable backend code  
- Automating deployments with CI/CD  
- Using Terraform for infrastructure management  
- Observing system behaviour under load  

---

## Future Improvements

- Add CloudWatch alarms and alerting  
- Introduce SQS for async processing  
- Improve IAM policies (least privilege)  
- Expand test coverage (integration tests)  
- Modularise Terraform configuration  
- Add dashboard for usage analytics  

---

## Why This Project

This project demonstrates practical cloud engineering skills including:

- Serverless architecture design  
- Infrastructure automation  
- CI/CD implementation  
- API security and protection  
- Observability and monitoring  
- Real-world debugging and problem solving  

It reflects production-style workflows and showcases readiness for cloud and DevOps engineering roles.
