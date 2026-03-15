import React,{useState} from "react"

function Chat(){

const [message,setMessage]=useState("")
const [messages,setMessages]=useState([])

const sendMessage = ()=>{

setMessages([...messages,message])
setMessage("")

}

return(

<div>

<h2>Chat</h2>

{messages.map((m,i)=>(

<p key={i}>{m}</p>

))}

<input
value={message}
onChange={(e)=>setMessage(e.target.value)}
/>

<button onClick={sendMessage}>Send</button>

</div>

)

}

export default Chat