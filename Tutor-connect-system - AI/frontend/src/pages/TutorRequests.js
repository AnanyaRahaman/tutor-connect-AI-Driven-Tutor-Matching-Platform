import React,{useState,useEffect} from "react"
import API from "../api"

function TutorRequests(){

const [requests,setRequests]=useState([])

useEffect(()=>{

API.get("/tutoring/requests/")
.then(res=>setRequests(res.data))

},[])

return(

<div>

<h2>Available Tuition Requests</h2>

{requests.map(r=>(

<div key={r.id}>

<h3>{r.subject}</h3>

<p>{r.location}</p>

<p>{r.date}</p>

<p>{r.method}</p>

</div>

))}

</div>

)

}

export default TutorRequests