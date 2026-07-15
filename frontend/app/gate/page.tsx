"use client";

import {useState} from "react";

export default function Page(){
 const [message,setMessage]=useState("");

 function enter(){
  setMessage("Premium gate access requested");
 }

 return (
  <main className="market-page">
   <section className="purchase-panel feature-glow">
    <h1>🚪 Bika Gate</h1>
    <p>Access premium marketplace features.</p>
    <button onClick={enter}>ENTER GATE</button>
    {message && <p>{message}</p>}
   </section>
  </main>
 );
}
