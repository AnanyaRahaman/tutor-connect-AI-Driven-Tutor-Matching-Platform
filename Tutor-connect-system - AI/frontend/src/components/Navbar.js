import React from "react"
import {Link} from "react-router-dom"

function Navbar(){

return(

<div>

<Link to="/dashboard">Dashboard</Link>

<Link to="/requests">Tutoring Jobs</Link>

<Link to="/calendar">Calendar</Link>

<Link to="/payments">Payments</Link>

</div>

)

}

export default Navbar