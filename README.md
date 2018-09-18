# UCourse
An unofficial University of Alberta web app that both contains course listings offered by the UofA, and also allows users to rate courses based on a set of criteria.
http://www.picopigeon.com

# Features
Search - Search for any classes offered by the UofA based on a set of criteria. Filter courses based on your preferences or directly search for a course.

Rate - Rate a course based on a set of criteria, and leave the course a comment for other user's to view.

Easy Login - Not willing to make an account to post a review? That's okay! Google+ sign in is supported, allowing for a quick and secure method of logging in.

Mobile Friendly - Whether at home or on to go, UCourse is mobile friendly, and easily accesible from all devices.

# Technical Aspects
This application uses Django, Bootstrap, as well as SQLite for its tech stack. Course information was retrieved from a csv, which was scraped from the university course directory, and put into a relational database. Techniques such as pagination was used to display the courses nicely in the search view. The Rating form has integrated cross-site forgery attack prevention.

# Current Limitations
This web application is mostly limited by the resources it has to work with. While a UofA API exists (UODA), which offers a plethora of information, including academic programs, course units, as well as terms the course is offered, access to this API was denied, as it's intended for commercial use. This limits the scope of what information can be used, and hence what the app can do. A possible (yet messy) workaround with this might be to build a scraper for beartracks itself. The two biggest issues is that 1.The information scraped must be manually updated and 2.The scraper will need to be sufficienty complex, since beartracks requires a sign in and is a bit "unconventional" in comparison to other web sites.
