import React from "react"

function TutorCard({tutor}){

return(

<div>

<h3>{tutor.name}</h3>

<p>Subject: {tutor.subject}</p>

<p>Location: {tutor.location}</p>

<button>Request Tutor</button>

</div>

)

}

export default TutorCard