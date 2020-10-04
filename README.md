# Django_Framework
## Django web application concept
Django uses the concept of projects and apps to keep code clean and readable. A single Django project contains one or more apps within it that all work together to power a web application. This is why the command for a new Django project is startproject.
For example, a real-world Django e-commerce site might have one app for userauthentication, another app for payments, and a third app to power item listing details: each focuses on an isolated piece of functionality. That’s three distinct apps that all live within one top-level project.
## Introducing the Django Admin
### Philosophy 
Generating admin sites for your staff or clients to add, change, and delete content is tedious work that doesn’t require much creativity. For that reason, Django entirely automates creation of admin interfaces for models. 

Django was written in a newsroom environment, with a very clear separation between “content publishers” and the “public” site. Site managers use the system to add news stories, events, sports scores, etc., and that content is displayed on the public site. Django solves the problem of creating a unified interface for site administrators to edit content.

The admin isn’t intended to be used by site visitors. It’s for site managers.

## Local Path
`cd ~/Desktop/Django`
