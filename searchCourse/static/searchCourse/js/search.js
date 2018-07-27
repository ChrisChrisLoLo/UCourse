//Code to change the URL to /COURSE/101 
//or whatever is inputted into the form for searching for a single element.

function searchSingle() {
    console.log("DSFS");
    subjectCode = document.getElementById("singleSubject").value.toUpperCase();
    courseCode = document.getElementById("singleCourse").value;
    window.location.href = `/search/${subjectCode}/${courseCode}`;
    return;
}

//Code below suppresses typical form behavior for seaching for a single course, and makes the form
//only run searchSingle() on submit. Did this so I can still use form validation.
(function() {
    "use strict";
 
    window.addEventListener("load", function() {
      document.getElementById("singleSearchForm").addEventListener("submit", function(event) {
        event.target.checkValidity();
        event.preventDefault(); // Prevent form submission and contact with server
        event.stopPropagation();
      }, false);
    }, false);
  }()
);