import React, { useState } from "react";
import API from "../api";

function Register(){

const [username,setUsername]=useState("")
const [email,setEmail]=useState("")
const [password,setPassword]=useState("")

const register = async () =>{

await API.post("/users/register/",{

username,
email,
password

})

alert("Registration successful")

}

return(

<div>

<h2>Register</h2>

<input
placeholder="username"
onChange={(e)=>setUsername(e.target.value)}
/>

<input
placeholder="email"
onChange={(e)=>setEmail(e.target.value)}
/>

<input
type="password"
placeholder="password"
onChange={(e)=>setPassword(e.target.value)}
/>

<button onClick={register}>Register</button>

</div>

)

}

export default Register