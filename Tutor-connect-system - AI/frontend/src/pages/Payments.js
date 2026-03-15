import React from "react"
import axios from "axios"

function Payments(){

const pay = async ()=>{

const res = await axios.post(
"http://localhost:8000/api/payments/create-checkout/"
)

window.location.href =
`https://checkout.stripe.com/pay/${res.data.id}`

}

return(

<div>

<h2>Pay for Tutoring</h2>

<button onClick={pay}>Pay $50</button>

</div>

)

}

export default Payments