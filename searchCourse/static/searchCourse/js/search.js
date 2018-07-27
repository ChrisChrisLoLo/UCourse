//Code to change the URL to /COURSE/101 
//or whatever is inputted into the form for searching for a single element.

function searchSingle() {
    console.log("DSFS");
    subjectCode = document.getElementById("singleSubject").value.toUpperCase();
    courseCode = document.getElementById("singleCourse").value;
    window.location.href = `/search/${subjectCode}/${courseCode}`;
    return;
}