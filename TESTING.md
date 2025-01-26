## Code Validation

### HTML

[HTML W3C Validator](https://validator.w3.org)

I checked every page on the website and every single page displays these errors due to django templating.

![Image](https://github.com/user-attachments/assets/24f17332-10d4-45d1-9f3e-4f329aa893da)


### CSS

[CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator)


![Image](https://github.com/user-attachments/assets/2ec173f5-2707-4477-af1b-ad3858ed4ec7)

### JavaScript

[JShint Validator](https://jshint.com)

All errors are due to the need to use 'esversion 6' with JSHINT.

![Image](https://github.com/user-attachments/assets/345def97-3a47-4557-97ae-cd81d8ebacc2)


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Booking 

Views.py

![Image](https://github.com/user-attachments/assets/284088ef-ac49-4042-8238-25d735c4d76b)

Models.py

![Image](https://github.com/user-attachments/assets/c12967fb-6fe5-4575-94a8-d07eb1e9cdaf)

#### Users

Models.py

![Image](https://github.com/user-attachments/assets/6314f3c9-c16c-48c7-b79b-976346ce4c46)

Views.py

![Image](https://github.com/user-attachments/assets/523f0cd8-931e-47a4-af3b-e79d552e9d57)

Signals.py

![Image](https://github.com/user-attachments/assets/f7e3bcd3-e2c8-4574-9acd-b2156b9114db)



#### Website

Views.py

![Image](https://github.com/user-attachments/assets/9e1b95de-671d-4a8e-bbc8-99213f69c3ae)

Models.py

![Image](https://github.com/user-attachments/assets/bbae0753-5c9d-4d67-b582-0199f97ea249)


## Browser Compatibility


The website was tested for compatibility issues accross many different browsers

| Browser | Issues | Notes |
| --- | --- | --- |
| Chrome | None | Works as expected |
| Firefox | None | Works as expected |
| IE | None | Multiple broken elements |
| Safari | None | Works as expected |
| Opera | None | No smooth-scrolling |
| Edge | None | No smooth-scrolling |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Issues | Notes |
| --- | --- | --- |
| Mobile (DevTools) | None | Works as expected |
| Tablet (DevTools) | None | Works as expected |
| Desktop 1920x1080 | None | Works as expected |
| Desktop 25600x1440 | None | Minor scaling issues |
| Samsung S20 | None | Works as expected |

## Lighthouse Audit

I've tested my deployed website using the DevTools Lighthouse Audit

Desktop

![Image](https://github.com/user-attachments/assets/47404353-442d-4c5e-8fb3-4df0125b7759)

Mobile

![Image](https://github.com/user-attachments/assets/5330bd62-92ea-4d9e-a4de-aa61b032aa0c)

## Defensive Programming

Manual testing

| Page                       | User Action                               | Expected Result                                | Pass/Fail | Comments        |
|----------------------------|-------------------------------------------|-----------------------------------------------|-----------|-----------------|
| **Nav Links**              |                                           |                                               |           |                 |
|                            | Click on Logo                             | Redirects to Home page                        | Pass      |                 |
|                            | Click on Home link                        | Redirects to Home page                        | Pass      |                 |
|                            | Click on About link                       | Redirects to About page                       | Pass      |                 |
|                            | Click on News link                        | Redirects to News page                        | Pass      |                 |
|                            | Click on Contact link                     | Redirects to Contact page                     | Pass      |                 |
|                            | Click on Register link                    | Redirects to Register page                    | Pass      |                 |
|                            | Click on Login link                       | Redirects to Login page                       | Pass      |                 |
|                            | Click on Profile link     | Redirects to User Profile page               | Pass      |                 |
|                            | Click on Booking| Redirects to Booking page           | Pass      |                 |
| **Navigation - Logged Out**|                                           |                                               |           |                 |
|                            | Navigate to restricted URLs               | Redirects to Login page                       | Pass      |                 |
| **Home Page**              |                                           |                                               |           |                 |
|                            | Click on "Continue Reading" button               | Redirects to news page                | Pass      |                 |
|                            | Click on news title                       | Redirects to news details page                | Pass      |                 |
| **Register**               |                                           |                                               |           |                 |
|                            | Enter valid email                        | Accepts only valid email format               | Pass      |                 |
|                            | Enter valid password (twice)              | Accepts only valid password format            | Pass      |                 |
|                            | Click on "Sign Up" button                 | Redirects to Login page                       | Pass      |                 |
| **Log In**                 |                                           |                                               |           |                 |
|                            | Enter valid password                      | Accepts only valid password format            | Pass      |                 |
|                            | Click Login button                        | Redirects to Home page                        | Pass      |                 |
| **Log Out**                |                                           |                                               |           |                 |
|                            | Click Logout button                       | Logs out user, redirects to Logout page       | Pass      |                 |
| **Profile**                |                                           |                                               |           |                 |
|                            | Click on "Update" button            | Saves new user information to the profile                     | Pass      |                 |
|                            | Click on "Delete" booking button     | Deletes the booking           | Pass      |                 |
| **Booking**  |                                           |                                               |           |                 |
|                            | Click on "Game Type" input         | Displays available game types                 | Pass      |                 |
|                            | Click on "Select Court"           | Displays available courts              | Pass      |                 |
|                            | Click on "Select Date"           | Displays calendar              | Pass      |                 |
|                            | Click on "Check Availability"           | Checks availability and returns times              | Pass      |                 |
|                            | Click on available timeslot           | Selects a timeslot              | Pass      |                 |
|                            | Click on "Book Now"           | Saves the booking information              | Pass      |                 |
| **Admin Page** |                                      |                                               |           |                 |
|                            | Click "Add User" button         | Adds User      | Pass      |                 |
|                            | Click "Edit User" button         | Edits User      | Pass      |                 |
|                            | Click "Delete User" button         | Deletes User      | Pass      |                 |
|                            | Click "Add News" button                       | Adds a new News post            | Pass      |                 |
|                            | Click "Edit News" button                       | Edits a News post            | Pass      |                 |
|                            | Click "Delete News" button                       | Deletes a News post            | Pass      |                 |
|                            | Click "Add Booking" button                       | Adds a new booking            | Pass      |                 |
|                            | Click "Edit Booking" button                       | Edits a booking            | Pass      |                 |
|                            | Click "Delete Booking" button                       | Deletes a booking            | Pass      |                 |
|                            | Click "Add GameType" button                       | Adds a new GameType            | Pass      |                 |
|                            | Click "Edit GameType" button                       | Edits GameType            | Pass      |                 |
|                            | Click "Delete GameType" button                       | Deletes GameType            | Pass      |                 |
|                            | Click "Add Court" button                       | Adds a new Court            | Pass      |                 |
|                            | Click "Edit Court" button                       | Edits Court           | Pass      |                 |
|                            | Click "Delete Court" button                       | Deletes Court           | Pass      |                 |




## User Stories / Epics Testing

| User Story | Pass / Fail | Comments |
| --- | --- | --- |
| As a customer, I can sign out of the page, so that I don't compromise the security of my account. | Pass |  |
| As a customer, I can click on the relevant links at the top of the page, so that navigate the page effectively. | Pass |  |
| As an administrator, I can create automated emails for confirmations, news and other relevant information, so that they don't need to be sent manually to each user. | Pass |  |
| As an administrator, I can create, edit or delete posts on the front-end of the page, so that I don't need to access the page files to make changes to content. | Pass |  |
| As an administrator, I can change the account privileges, so that I can grant access to restricted features. | Pass |  |
| As an administrator, I can create, view, edit or delete all the current bookings, so that I can manage the booking system in case of errors or changes. | Pass |  |
| As a customer, I can reset my password, so that I am able to log in. | Pass |  |
| As a customer, I can enter my profile, so that I can edit my information. | Pass |  |
| As a customer, I can log in to the members area, so that I can use the websites features and change my profile information. | Pass |  |
| As a customer, I can create an account, so that I can become a member and use the features of the website. | Pass |  |
| As a customer, I can enter the contact page, so that I can find information about the way to contact the page support. | Pass |  |
| As a customer, I can enter the about page, so that I can find more information about the basketball stadium. | Pass |  |
| As a customer, I can enter the booking page, so that I can reserve a time in the available court. | Pass |  |
| As a customer, I can view the page, so that I can learn about the basketball stadium. | Pass |  |
