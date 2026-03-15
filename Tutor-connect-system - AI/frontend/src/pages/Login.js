import React,{useState} from "react"
import API from "../api"

function Login(){

const [username,setUsername]=useState("")
const [password,setPassword]=useState("")

const login = async ()=>{

try{

const res = await API.post("/users/login/",{

username,
password

})

localStorage.setItem("token",res.data.access)

alert("Login successful")

}catch(error){

alert("Login failed")

}

}

return(

<div>

<h2>Login</h2>

<input
placeholder="Username"
onChange={(e)=>setUsername(e.target.value)}
/>

<input
type="password"
placeholder="Password"
onChange={(e)=>setPassword(e.target.value)}
/>

<button onClick={login}>
Login
</button>

</div>

)

}

export default Login