# copado-sample-test-class
## what is this repository for?
This repository has a sample apex class and test class which are written to work on top of the Copado data model.
Those who have tried to build apex on top of copado might have noticed that writing the test class is difficult.
1. Licenses are checked during test runs
2. SOQL limits can be reached in the test setup.
3. creating artifacts which match copado input/output can be difficult (e.g. commit attachment jsons)

The content in this repo is aimed at helping clients to overcome those issues without days or even weeks of complex reverse engineering.
Also, for those who have AI, the idea is that you should be able to reference the test data factory and sample test class in your prompt to get better results faster.

Highlights:
- CopadoTestDataFactory, a class with helper methods that can be used to create copado records such as user stories and promotions
- CopadoTestUtility, a class with methods to work around copado permissions & licenses
- CopadoSampleTestClass, a sample test class which can be used as inspiration and starting point
- Expression_FlowsInPromotion & Test: A logic to get the list of flows in a promotion and parse them as JSON & the respective test class
- copado_object_schema.json: use this as context in your AI workspace to reduce schema related issues or hallucinations

## How to use it?
- read and understand
- Use Copado AI (Build Agent), gemini, cursor, ... to reference the sample and build your logic on top of it.
- Deploy those classes to your org via SF CLI and build on top of it.

## What if it stops working?
This repo IS NOT owned by Copado, so it WILL NOT BE MAINTAINED by Copado.
So if at some point it's not working any longer, pls suggest an improvement and we can keep it going as a small community of Copado nerds who help each other.

## Will there be more automation use cases in the future?
Maybe. Depends on the workload I have and I'm happy to include good examples.

## Was this written by AI?
Partially.
